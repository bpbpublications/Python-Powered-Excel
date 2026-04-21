# Renaming all files from a folder with a prefix 
# Using scandir(), creating log file for updo renaming

import os, json

# Setting working directory to Chapter 05 folder (inside Excel_Python)

chapter_directory = os.path.join(os.getcwd(), 'Chapter 05')
os.chdir(chapter_directory)
folder_path = os.path.join(os.getcwd(), 'testfiles')

prefix = "Jan_" # Prefix to add to filenames
log_file = os.path.join(folder_path, "rename_log.json")  # Log file to store original names

# Task 1: To save original filenames before renaming
rename_log = {}

for entry in os.scandir(folder_path):    
    if entry.is_file() and not entry.name.startswith(prefix):  # Avoid re-renaming
        old_path = entry.path    
        new_filename = prefix + entry.name  
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
        rename_log[new_filename] = entry.name  # Store mapping in dictionary
        print(f"Renamed: {entry.name} ➝ {new_filename}")

# Save the mapping to a JSON log file
with open(log_file, "w") as f:
    json.dump(rename_log, f)

print("✅ Batch renaming complete! Original names saved in rename_log.json")


# Task 2: To load the log file and revert names
    
# import os, json

# current_dir = os.getcwd() # Change this to your directory containing 'testfiles' folder
# folder_path = os.path.normpath(os.path.join(current_dir, 'testfiles'))

# prefix = "Jan_" # Prefix to add to filenames
log_file = os.path.join(folder_path, "rename_log.json")  # Log file to store original names

with open(log_file, "r") as f:
    rename_log = json.load(f)

current_files = [entry.name for entry in os.scandir(folder_path)]# Get current files in directory
print(current_files)

for new_name, old_name in rename_log.items():
    old_path = os.path.join(folder_path, new_name)
    new_path = os.path.join(folder_path, old_name)
    if new_name in current_files:
        os.rename(old_path, new_path)
        print(f"Reverted: {new_name} ➝ {old_name}")
   
    # os.remove(log_file) # Remove log file after reverting

print("✅ Undo complete! All files restored to original names.") 
    
