# Categorizing Files by Extension

import os, shutil

# Setting working directory to Chapter 05 folder (inside Excel_Python)

chapter_directory = os.path.join(os.getcwd(), 'Chapter 05')
os.chdir(chapter_directory)
folder_path = os.path.join(os.getcwd(), 'testfiles')

# Categorizing files by extension
file_extensions = {
    '.docx': 'WordFiles',
    '.jpg': 'Images',
    '.py': 'CodeFiles',
    '.ipynb': 'CodeFiles' # Notebooks
}

for entry in os.scandir(folder_path):
    if entry.is_file():
        file_ext = os.path.splitext(entry.name)[1]
        if file_ext in file_extensions:
            sub_folder_name = file_extensions[file_ext] # Creating sub-folders with names by file types
            sub_folder = os.path.join(folder_path, sub_folder_name)
            os.makedirs(sub_folder, exist_ok=True)
            # Moving files to respective folder
            source = entry.path
            destination = os.path.join(sub_folder, entry.name)
            shutil.move(source, destination)
            print(f"Moved {entry.name} → {sub_folder_name}")


# You can also acheive the same using os.listdir()
for filename in os.listdir(folder_path):
    if os.path.isfile(filename):
        file_ext = os.path.splitext(filename)[1]
        if file_ext in file_extensions:
            # Creating sub-folders
            sub_folder_name = file_extensions[file_ext]
            sub_folder = os.path.join(folder_path, sub_folder_name)
            os.makedirs(sub_folder, exist_ok=True)
            # Moving files to respective folder
            source = os.path.join(folder_path, filename)
            destination = os.path.join(sub_folder, filename)
            shutil.move(source, destination)
