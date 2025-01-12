import os

def generate_mock_modules(imports, base_dir):
    """
    Generates Python module files with multiple mock classes grouped together in the same file.
    
    Args:
        parsed_imports (list): A list of tuples (module_name, class_name, alias).
        base_dir (str): The base directory where modules will be generated.
    """
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Dictionary to store classes by module
    module_classes = {}

    # Group classes by their module name
    for imp in imports:
        imp = imp.strip()
        parts = imp.split('.')
        class_name = parts[-1]
        print(f"Class name: {class_name}")

        module_path = parts[:-1]
        module_file = module_path[-1] + ".py"
        module_path_minus_file = module_path[:-1]
        print(f"Module file: {module_file}")
        # TODO: Build the path from module_path (if len > 1) and module_file

        directory_path = os.path.join(base_dir, *module_path_minus_file)
        print(f"Directory path: {directory_path}")

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"Created directory: {directory_path}")  # Debugging

        full_path = os.path.join(directory_path, module_file)
        print(f"Full path: {full_path}")

        if full_path not in module_classes:
            module_classes[full_path] = [class_name]
        else:
            module_classes[full_path].append(class_name) 
    print(module_classes)

    # Write the generated content into the module files
    for file_path, items in module_classes.items():
        with open(file_path, "w") as f:
            for class_name in items:
                if class_name.startswith('VTK_'):
                    # If it's a constant, set it to 1
                    f.write(f"{class_name} = 1\n")
                else:
                    # If it's a class, define it with NotImplementedError
                    f.write(f"""class {class_name}:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError(f"'{class_name}' is not implemented yet")
\n""")

        print(f"Generated {file_path}")


with open('vtkimports.txt', 'r') as file:
    lines = file.readlines()

lines = [x for x in lines if x.startswith('vtk')]

# Base directory where the modules will be created
base_dir = "vtkmodules"

# Call the function to generate the actual Python modules and classes
generate_mock_modules(lines, base_dir)

