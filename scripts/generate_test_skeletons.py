import os
import ast

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
                tree = ast.parse(f.read())
            
            new_tests = ""
            if not existing_tests:
                new_tests += f"from src import {module_name}\n\n"
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    test_func_name = f"def test_{node.name}():"
                    if test_func_name not in existing_tests:
                        print(f"Adding test skeleton for {node.name} in {module_name}...")
                        new_tests += f"{test_func_name}\n"
                        new_tests += f"    # TODO: Implement test for {node.name}\n"
                        new_tests += f"    pass\n\n"
            
            if new_tests:
                with open(test_path, "a" if existing_tests else "w") as f:
                    f.write(new_tests)
                print(f"Updated {test_path}" if existing_tests else f"Generated {test_path}")

if __name__ == "__main__":
    generate_skeletons()
