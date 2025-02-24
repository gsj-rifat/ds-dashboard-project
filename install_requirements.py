import subprocess

def install_requirements(interpreter_path):
    try:
        # Run the pip install command
        subprocess.run(
            ['C:/Users/nn/PycharmProjects/DS_Employee_Dashboard/venv/Scripts/python.exe', '-m', 'pip', 'install', '-r', interpreter_path],
            check=True
        )
        print(f"Packages from {interpreter_path} installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install packages: {e}")

# Specify the path to the requirements.txt file
interpreter_path = 'C:/Users/nn/PycharmProjects/DS_Employee_Dashboard/path/requirements.txt'

# Install packages
install_requirements(interpreter_path)
