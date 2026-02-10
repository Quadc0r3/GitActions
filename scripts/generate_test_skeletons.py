import os
import ast
from google import genai
from dotenv import load_dotenv

# Robust loading of .env from the project root
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
env_path = os.path.join(project_root, ".env")
load_dotenv(dotenv_path=env_path)

# Setup Gemini API using the NEW SDK (google-genai)
API_KEY = os.environ.get("GOOGLE_API_KEY")
client = None

if API_KEY:
    try:
        client = genai.Client(api_key=API_KEY)
        print(f"DEBUG: Gemini Client initialisiert (Key-Endung: {API_KEY[-4:]})")
    except Exception as e:
        print(f"Fehler bei der Initialisierung: {e}")
else:
    print("Warnung: Kein GOOGLE_API_KEY gefunden!")

def get_ai_test_code(module_name, function_name, source_code):
    if not client:
        return f"def test_{function_name}():\n    # TODO: Implement test (Client/API Key missing)\n    pass\n\n"

    try:
        # We'll use 2.0-flash as it's state-of-the-art and was in your debug list
        # Fallback to 1.5-flash if needed
        model_name = 'gemini-2.5-flash'
        
        prompt = f"""
        Schreibe einen professionellen Pytest-Testfall für die Funktion '{function_name}' im Modul '{module_name}'.
        Hier ist der Quellcode des Moduls:
        ```python
        {source_code}
        ```
        Regeln:
        1. Antworte NUR mit dem reinen Python-Code der Testfunktion. Keine Erklärungen.
        2. Verwende 'from src import {module_name}' am Anfang oder gehe davon aus, dass der Import bereits existiert.
        3. Nutze aussagekräftige 'assert' Statements.
        """
        
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        test_code = response.text.strip()
        
        # Clean up markdown if AI includes it
        if "```" in test_code:
            test_code = test_code.split("```python")[-1].split("```")[0].strip()
        return test_code + "\n\n"
    except Exception as e:
        print(f"AI Generation failed for {function_name}: {e}")
        return f"def test_{function_name}():\n    # AI failed: {str(e)}\n    pass\n\n"

def generate_skeletons():
    src_dir = os.path.join(project_root, "src")
    test_dir = os.path.join(project_root, "tests")
    
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    for filename in os.listdir(src_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            test_path = os.path.join(test_dir, f"test_{module_name}.py")
            
            existing_content = ""
            if os.path.exists(test_path):
                try:
                    with open(test_path, "r", encoding="utf-8") as f:
                        existing_content = f.read()
                except UnicodeDecodeError:
                    with open(test_path, "r", encoding="cp1252") as f:
                        existing_content = f.read()
            
            try:
                with open(os.path.join(src_dir, filename), "r", encoding="utf-8") as f:
                    source_code = f.read()
            except UnicodeDecodeError:
                with open(os.path.join(src_dir, filename), "r", encoding="cp1252") as f:
                    source_code = f.read()
            
            tree = ast.parse(source_code)
            
            updated_content = existing_content
            if not updated_content.strip():
                updated_content = f"from src import {module_name}\n\n"
            
            has_changes = False
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    test_func_name = f"def test_{node.name}():"
                    # Check if test for this function is missing, a TODO, or a previous failure
                    is_missing = test_func_name not in updated_content
                    is_dummy = ("# TODO" in updated_content or "# AI failed" in updated_content) and test_func_name in updated_content
                    
                    if is_missing or is_dummy:
                        print(f"Generiere Test für {node.name}...")
                        new_test = get_ai_test_code(module_name, node.name, source_code)
                        
                        if is_dummy:
                            lines = updated_content.splitlines()
                            for i, line in enumerate(lines):
                                if test_func_name in line:
                                    end_idx = i + 1
                                    while end_idx < len(lines) and not lines[end_idx].strip().startswith("def "):
                                        end_idx += 1
                                    lines[i:end_idx] = [new_test.strip()]
                                    updated_content = "\n".join(lines)
                                    break
                        else:
                            updated_content += "\n" + new_test
                        has_changes = True
            
            if has_changes:
                with open(test_path, "w", encoding="utf-8") as f:
                    f.write(updated_content.strip() + "\n")
                print(f"Datei aktualisiert: {test_path}")

if __name__ == "__main__":
    generate_skeletons()
