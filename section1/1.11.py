
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            with open(destination_file, 'w') as dest:
                for line in src:
                    dest.write(line)
        print("File Copied Successfully!")            
        print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"The file '{source_file}' does not exist.")
    except IOError as e:
        print(f"An error occurred while accessing the file: {e}")

source_file = 'C:\\Users\\RAHUL\\Desktop\\vscode_python\\section1\\source.txt'
destination_file = 'C:\\Users\\RAHUL\\Desktop\\vscode_python\\section1\\destination.txt'
copy_file(source_file, destination_file)
