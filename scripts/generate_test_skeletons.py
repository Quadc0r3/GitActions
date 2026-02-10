import os
import ast
import google.generativeai as genai

# Setup Gemini API
API_KEY = os.environ.get("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

def get_ai_test_code(module_name, function_name, source_code):
    if not API_KEY:
        return f"def test_{function_name}():\n    # TODO: Implement test for {function_name}\n    pass\n\n"

    prompt = f"""
    Schreibe einen professionellen Pytest-Testfall für die Funktion '{function_name}' im Modul '{module_name}'.
    Hier ist der Quellcode des Moduls:
    ```python
    {source_code}
    ```
    Antworte NUR mit dem Python-Code für die Testfunktion. Keine Erklärungen, kein Markdown-Codeblock.
    Verwende 'from src import {module_name}' für den Import, falls nötig, aber gehe davon aus, dass der Import bereits am Dateianfang steht.
    """
    
    try:
        response = model.generate_content(prompt)
        test_code = response.text.strip()
        # Remove markdown code blocks if AI included them despite instructions
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
                    if test_func_name not in existing_tests:
                        print(f"Generating AI test for {node.name} in {module_name}...")
                        new_tests += get_ai_test_code(module_name, node.name, source_code)
            
            if new_tests:
                with open(test_path, "a" if existing_tests else "w") as f:
                    f.write(new_tests)
                print(f"Updated {test_path}" if existing_tests else f"Generated {test_path}")

if __name__ == "__main__":
    generate_skeletons()
