# This script removes all .xlsx and .xls files that haven't been modified in over 3 years.

import os, time

chapter_directory = os.path.join(os.getcwd(), 'Chapter 05')
os.chdir(chapter_directory)
folder_path = os.path.join(os.getcwd(), 'demo') # Change to your folder path

year = 3 

three_years_ago = time.time() - (year * 365 * 24 * 60 * 60)  # Convert years to seconds

for entry in os.scandir(folder_path):
    file_path = entry.path

    if entry.is_file() and entry.name.endswith(('.xlsx', '.xls')):
        mod_time = os.path.getmtime(file_path)  # Last modified time
        # print(mod_time)

        if mod_time < three_years_ago:  # Check if older than 3 years
            print(file_path)
            os.remove(file_path)  # Delete file
            print(f"Deleted old file: {entry.name}")

# Using os.listdir():
    
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path) and filename.endswith(('.xlsx', '.xls')):
        mod_time = os.path.getmtime(file_path)  # Last modified time

        if mod_time < three_years_ago:  # Check if older than 3 years
            os.remove(file_path)  # Delete file
            print(f"Deleted old file: {filename}")

print("✅ Old Excel files deleted successfully!")
