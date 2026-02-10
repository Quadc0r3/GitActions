import os
import ast

def generate_doku():
    src_dir = "src"
    doku_file = "DOKU.md"
    
    content = "# Projekt Dokumentation\n\n"
    content += "Dieses Dokument wurde automatisch erstellt.\n\n"
    
    for filename in os.listdir(src_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            content += f"## Modul: `{filename}`\n"
            with open(os.path.join(src_dir, filename), "r") as f:
                tree = ast.parse(f.read())
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    docstring = ast.get_docstring(node) or "Keine Dokumentation vorhanden."
                    content += f"### Funktion: `{node.name}`\n"
                    content += f"{docstring}\n\n"
    
    with open(doku_file, "w") as f:
        f.write(content)
    print(f"Update {doku_file} erfolgreich.")

if __name__ == "__main__":
    generate_doku()
