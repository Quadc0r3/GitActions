import os
import ast
from google import genai

# Setup Gemini API using the new google-genai SDK
API_KEY = os.environ.get("GOOGLE_API_KEY")
client = None
if API_KEY:
    try:
        client = genai.Client(api_key=API_KEY)
    except Exception as e:
        print(f"Failed to initialize Gemini Client: {e}")

def get_ai_test_code(module_name, function_name, source_code):
    if not client:
        return f"def test_{function_name}():\n    # TODO: Implement test for {function_name}\n    pass\n\n"

    prompt = f"""
    Schreibe einen professionellen Pytest-Testfall für die Funktion '{function_name}' im Modul '{module_name}'.
    Hier ist der Quellcode des Moduls:
    ```python
    {source_code}
    ```
    Antworte NUR mit dem Python-Code für die Testfunktion. Keine Erklärungen, kein Markdown-Codeblock.
    Verwende 'from src import {module_name}' für den Import.
    Gehe davon aus, dass der Import 'from src import {module_name}' bereits am Dateianfang steht, falls du ihn nicht explizit mitschreibst.
    Antworte wirklich NUR mit der Funktionsdefinition.
    """
    
    try:
        # Im neuen SDK ist 'gemini-1.5-flash' der korrekte String (ohne models/)
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=prompt
        )
        test_code = response.text.strip()
        # Clean up potential markdown formatting if AI ignores instructions
        if "```" in test_code:
            test_code = test_code.split("```python")[-1].split("```")[0].strip()
        return test_code + "\n\n"
    except Exception as e:
        print(f"AI Generation failed for {function_name}: {e}")
        return f"def test_{function_name}():\n    # AI failed: {e}\n    pass\n\n"

def generate_skeletons():
    src_dir = "src"
    test_dir = "tests"
    
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    for filename in os.listdir(src_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            test_filename = f"test_{module_name}.py"
            test_path = os.path.join(test_dir, test_filename)
            
            existing_tests = ""
            if os.path.exists(test_path):
                with open(test_path, "r") as f:
                    existing_tests = f.read()
            
            with open(os.path.join(src_dir, filename), "r") as f:
                source_code = f.read()
                tree = ast.parse(source_code)
            
            new_tests = ""
            if not existing_tests:
                new_tests += f"from src import {module_name}\n\n"
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    test_func_name = f"def test_{node.name}():"
                    todo_marker = f"# TODO: Implement test for {node.name}"
                    # Also check for AI failure messages to retry them
                    error_marker = "# AI failed:"
                    
                    if test_func_name not in existing_tests or todo_marker in existing_tests or error_marker in existing_tests:
                        print(f"Generating AI test for {node.name} in {module_name}...")
                        generated_code = get_ai_test_code(module_name, node.name, source_code)
                        
                        # Logic to replace old TODOs or failed tests
                        if todo_marker in existing_tests or error_marker in existing_tests:
                            # This is a bit simplified; for a robust tool we'd use a better parser
                            # But for this demo, we'll try to find and replace the block
                            lines = existing_tests.splitlines()
                            start_line = -1
                            for i, line in enumerate(lines):
                                if line.strip() == test_func_name:
                                    start_line = i
                                    break
                            
                            if start_line != -1:
                                # Find the end of this function (next def or empty line or end of file)
                                end_line = start_line + 1
                                while end_line < len(lines) and not lines[end_line].startswith("def") and not lines[end_line].startswith("from") and not lines[end_line].startswith("import"):
                                    end_line += 1
                                
                                # Replace the lines from start_line to end_line
                                lines[start_line:end_line] = [generated_code.strip()]
                                existing_tests = "\n".join(lines) + "\n"
                            else:
                                new_tests += generated_code
                        else:
                            new_tests += generated_code
            
            if new_tests or "AI failed" in existing_tests: # Check if we still have failures or new ones
                with open(test_path, "w") as f:
                    f.write(existing_tests.strip() + "\n\n" + new_tests.strip() + "\n")
                print(f"Updated {test_path}")

if __name__ == "__main__":
    generate_skeletons()
