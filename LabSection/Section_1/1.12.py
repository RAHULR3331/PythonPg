import os

def create_directory(directory_name):
    try:
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except OSError as e:
        print(f"Error: {e}")

def list_directory_contents(directory_name):
    try:
        contents = os.listdir(directory_name)
        print(f"Contents of '{directory_name}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: Directory '{directory_name}' does not exist.")
    except OSError as e:
        print(f"Error: {e}")

def search_py_files(directory_name):
    try:
        py_files = [f for f in os.listdir(directory_name) if f.endswith('.py')]
        print(f"'.py' files in '{directory_name}':")
        for file in py_files:
            print(file)
    except FileNotFoundError:
        print(f"Error: Directory '{directory_name}' does not exist.")
    except OSError as e:
        print(f"Error: {e}")

def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' does not exist.")
    except OSError as e:
        print(f"Error: {e}")

directory_name = 'test_directory'
file_name_to_remove = 'test_directory/random.txt'

# Create a directory
create_directory(directory_name)

# List directory contents
list_directory_contents(directory_name)

# Search for .py files in the directory
search_py_files(directory_name)

# Remove a particular file
remove_file(file_name_to_remove)