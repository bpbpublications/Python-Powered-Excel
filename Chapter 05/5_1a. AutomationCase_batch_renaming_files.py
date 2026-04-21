# Renaming all files from a folder with a prefix 
# Using scandir(), no logs maintained

import os

# Setting working directory to Chapter 05 folder (inside Excel_Python)

chapter_directory = os.path.join(os.getcwd(), 'Chapter 05')
os.chdir(chapter_directory)
folder_path = os.path.join(os.getcwd(), 'testfiles')

# Prefix to remove from filenames
prefix = "Jan_"

# Loop through all files in the directory
for entry in os.scandir(folder_path):
    if entry.is_file():  # Skip directories, process only files
        old_path = entry.path  # Directly get full path
        new_filename = prefix + entry.name  # Add prefix
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)  # Rename file
        print(f"Renamed: {entry.name} ➝ {new_filename}")

print("✅ Batch renaming complete!")

# To remove prefix again:
for entry in os.scandir(folder_path):
    # print(entry.name)

    if entry.name.startswith(prefix):
        # print(entry.name)
        without_prefix_name = entry.name[len(prefix):]
        # print(without_prefix_name)
        # Remove prefix
        old_path = os.path.join(folder_path, entry.name)
        # print(old_path)
        new_path = os.path.join(folder_path,  without_prefix_name)
        # print(new_path)
        os.rename(old_path, new_path)
        print(f"Reverted: {entry.name} ➝ {without_prefix_name}")

print("✅ Undo complete! Files restored to original names.")
