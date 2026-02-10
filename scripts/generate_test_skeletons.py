import os
import ast
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file for local testing
load_dotenv()

# Setup Gemini API
API_KEY = os.environ.get("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    print("Warnung: Kein GOOGLE_API_KEY in der Umgebung oder .env gefunden!")

def get_ai_test_code(module_name, function_name, source_code):
    if not API_KEY:
        return f"def test_{function_name}():\n    # TODO: Implement test for {function_name}\n    pass\n\n"

    try:
        # We try to use gemini-1.5-flash which is the most common one
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = f"Schreibe einen Pytest-Testfall für die Funktion '{function_name}' im Modul '{module_name}'. Code:\n{source_code}\nAntworte NUR mit dem reinen Python-Code der Testfunktion."
        
        response = model.generate_content(prompt)
        test_code = response.text.strip()
        
        # Clean up code blocks
        if "```" in test_code:
            test_code = test_code.split("```")
            for part in test_code:
                if part.strip().startswith("python"):
                    test_code = part.replace("python", "", 1).strip()
                    break
            else:
                test_code = test_code[1].strip() if len(test_code) > 1 else test_code[0].strip()
        
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
            
            if not existing_tests:
                existing_tests = f"from src import {module_name}\n\n"
            
            new_tests_found = False
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    test_func_name = f"def test_{node.name}():"
                    
                    # We generate if it's missing OR if it's just a dummy/failed test
                    should_generate = (test_func_name not in existing_tests) or \
                                      ("# TODO" in existing_tests and test_func_name in existing_tests) or \
                                      ("# AI failed" in existing_tests and test_func_name in existing_tests)
                    
                    if should_generate:
                        print(f"Generiere Test für {node.name}...")
                        generated_code = get_ai_test_code(module_name, node.name, source_code)
                        
                        if test_func_name in existing_tests:
                            # Replace the old block
                            lines = existing_tests.splitlines()
                            start_idx = -1
                            for i, line in enumerate(lines):
                                if test_func_name in line:
                                    start_idx = i
                                    break
                            
                            if start_idx != -1:
                                end_idx = start_idx + 1
                                # Look for end of function (next def or next test start)
                                while end_idx < len(lines) and not lines[end_idx].strip().startswith("def "):
                                    end_idx += 1
                                
                                lines[start_idx:end_idx] = [generated_code.strip()]
                                existing_tests = "\n".join(lines)
                                new_tests_found = True
                        else:
                            existing_tests += "\n" + generated_code
                            new_tests_found = True
            
            if new_tests_found:
                with open(test_path, "w") as f:
                    f.write(existing_tests.strip() + "\n")
                print(f"Datei aktualisiert: {test_path}")

if __name__ == "__main__":
    generate_skeletons()
