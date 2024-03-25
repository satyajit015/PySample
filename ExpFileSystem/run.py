import os
import shutil

# get current directory 
current_dir = os.getcwd()
print("Current Directory: ", current_dir)

# get root directory 
root_dir = os.path.abspath(os.sep)
print("Root Directory: ", root_dir)


def list_files_and_folders(directory):
    
    mypath = os.path.abspath(directory)

    # Iterate over the items in the directory
    for item in os.listdir(directory):
        # Get the full path of the item
        full_path = os.path.join(directory, item)
        # Check if it's a file or directory
        if os.path.isfile(full_path):
            print("File:", item)
        elif os.path.isdir(full_path):
            print("Folder:", item)


dir_path = './'
list_files_and_folders(dir_path)