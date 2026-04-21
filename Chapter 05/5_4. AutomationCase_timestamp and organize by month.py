# This script renames files by appending a timestamp (from their last modified date) 
# and moves them into folders based on the year and month.

import os, shutil, time

chapter_directory = os.path.join(os.getcwd(), 'Chapter 05')
os.chdir(chapter_directory)
 

source_folder =  os.path.join(os.getcwd(), "organizeByTimeStamp_Case") # Change to your folder path
destination_root = os.path.join(os.getcwd(), "organizeByTimeStamp_Case", "Organized_Reports")  # Where to organize files

# os.mkdir(destination_root) # Gives error if folder already exists, alternatetly we can use 
os.makedirs(destination_root, exist_ok=True)

# # Understand timestamp for file modification

file_path = "Attendance Records.xlsx"  # Replace with an actual file path

# Get last modified timestamp
mod_time = os.path.getmtime(file_path)
print("Modified Timestamp:", mod_time)

# Convert timestamp to readable format
readable_time = time.localtime(mod_time)
print('Readble Timestamp for file modification')
print("Last Modified:", time.strftime("%Y-%m-%d %H:%M:%S", readable_time))



# Timestamping and organizing files Use case:

for entry in os.scandir(source_folder):

    if entry.is_file():  # Ensure it's a file
        mod_time = os.path.getmtime(entry.path) # Get file's last modified timestamp
        formatted_time = time.strftime("%Y-%m-%d", time.localtime(mod_time))  # YYYY-MM-DD
        
        # Extract year and month for folder organization
        year_month = time.strftime("%Y-%m", time.localtime(mod_time))  # YYYY-MM
        
        # Create destination folder for that year and month
        destination_folder = os.path.join(destination_root, year_month)
        os.makedirs(destination_folder, exist_ok=True)

        # New file name with timestamp
        name, ext = os.path.splitext(entry.name)
        new_filename = f"{name}_{formatted_time}{ext}"
        new_path = os.path.join(destination_folder, new_filename)
        # shutil.move(entry.path, new_path) # Move and rename file
        shutil.copy(entry.path, new_path)  # Copy and rename file
        print(f"Moved/Copied: {entry.name} ➝ {new_filename} in {destination_folder}")


# If you're using os.listdir() instead of os.scandir():
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):  # Ensure it's a file
        # Get file's last modified timestamp
        mod_time = os.path.getmtime(file_path)
        formatted_time = time.strftime("%Y-%m-%d", time.localtime(mod_time))  # YYYY-MM-DD
        
        # Extract year and month for folder organization
        year_month = time.strftime("%Y-%m", time.localtime(mod_time))  # YYYY-MM
        
        # Create destination folder for that month
        destination_folder = os.path.join(destination_root, year_month)
        os.makedirs(destination_folder, exist_ok=True)

        # New file name with timestamp
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}_{formatted_time}{ext}"
        new_path = os.path.join(destination_folder, new_filename)

        shutil.copy(file_path, new_path)  # Copy and rename file
        print(f"Copied: {filename} ➝ {new_filename} in {destination_folder}")

print("✅ Files organized successfully by timestamp!")
