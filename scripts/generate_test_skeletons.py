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
            
            if not os.path.exists(test_path):
                print(f"Creating test skeleton for {filename}...")
                with open(os.path.join(src_dir, filename), "r") as f:
                    tree = ast.parse(f.read())
                
                with open(test_path, "w") as f:
                    f.write(f"from src import {module_name}\n\n")
                    for node in ast.walk(tree):
                        if isinstance(node, ast.FunctionDef):
                            f.write(f"def test_{node.name}():\n")
                            f.write(f"    # TODO: Implement test for {node.name}\n")
                            f.write(f"    pass\n\n")
                print(f"Generated {test_path}")

if __name__ == "__main__":
    generate_skeletons()
