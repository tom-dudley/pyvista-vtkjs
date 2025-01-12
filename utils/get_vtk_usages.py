import re
import sys
import types
import requests
import ast
import os

def extract_imports_from_ast(content):
    """
    Extracts VTK import statements from the given Python source content.

    Args:
        content (str): The Python source code as a string.

    Returns:
        list of tuple: A list of (module_name, class_name, alias) tuples.
    """
    results = []
    tree = ast.parse(content)

    for node in ast.walk(tree):
        # Handle standard imports: from vtkmodules.<module> import <class> as <alias>
        if isinstance(node, ast.ImportFrom) and node.module and node.module.startswith("vtkmodules."):
            module_name = node.module[len("vtkmodules."):]  # Strip the "vtkmodules." prefix
            for alias in node.names:
                class_name = alias.name
                as_name = alias.asname if alias.asname else alias.name
                results.append((module_name, class_name, as_name))

    return results

def create_mock_modules(parsed_imports):
    """
    Dynamically creates mock modules and injects them into sys.modules.

    Args:
        parsed_imports (list): A list of tuples (module_name, class_name, alias).
    """
    # Root vtkmodules package
    vtkmodules = types.ModuleType("vtkmodules")

    for module_name, class_name, alias in parsed_imports:
        # Split module_name into parts for nested modules
        parts = module_name.split(".")
        parent = vtkmodules

        # Create nested modules
        for part in parts:
            full_name = f"{parent.__name__}.{part}"
            if not hasattr(parent, part):
                submodule = types.ModuleType(full_name)
                setattr(parent, part, submodule)
                sys.modules[full_name] = submodule
            parent = getattr(parent, part)

        # Create mock class
        mock_class = type(class_name, (), {})
        setattr(parent, alias, mock_class)

    # Inject the root vtkmodules into sys.modules
    sys.modules["vtkmodules"] = vtkmodules

# URL of the source file
# url = "https://raw.githubusercontent.com/pyvista/pyvista/refs/heads/main/pyvista/core/_vtk_core.py"
# url = "https://raw.githubusercontent.com/pyvista/pyvista/refs/tags/v0.44.2/pyvista/plotting/_vtk.py"
url = "https://raw.githubusercontent.com/pyvista/pyvista/refs/tags/v0.44.2/pyvista/plotting/_vtk_gl.py"

# Fetch the content from the URL
response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Failed to fetch content from URL: {url}")

content = response.text

# Parse imports
parsed_imports = extract_imports_from_ast(content)

# Create mock modules
create_mock_modules(parsed_imports)

imports = [f"{x}.{y}" for (x,y,_) in parsed_imports] 
imports = sorted(imports)

script_dir = os.path.dirname(os.path.realpath(__file__))

with open('vtkimports-gl.txt', 'w') as f:
    for i in imports:
        f.write(i + "\n")

print(f"{len(imports)} imports written to vtkimports-gl.txt")
    
