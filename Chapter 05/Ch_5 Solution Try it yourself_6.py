# Try It Yourself ________________________________________________

# 6. Using Python, create a folder ‘Finance_Reports’ in D drive or 
# your current directory. And replicate the folder structure

import os

chapter_directory = os.path.join(os.getcwd(), 'Chapter 05')
os.chdir(chapter_directory)

# Define the root folder
root_folder = os.path.join(os.getcwd(), "Finance_Reports")

# Define nested folder structure (4 levels)
folders = [
    "2024/Q1/January",
    "2024/Q1/February",
    "2024/Q1/March",
    "2024/Q2/April",
    "2024/Q2/May",
    "2024/Q2/June"
]

# Create folders using makedirs()
for folder in folders:
    os.makedirs(os.path.join(root_folder, folder), exist_ok=True)

# Define sample files to create inside each month
files = ["Revenue.csv", "Expenses.csv", "Customers.csv", "Report.txt"]

# Create sample files inside each month
for folder in folders:
    for file in files:
        file_path = os.path.join(root_folder, folder, file)
        with open(file_path, 'w') as f:
            f.write(f"Dummy data for {file} in {folder}")  # Writing sample content

# Print folder structure using os.walk()
print("\n📂 Finance Reports Folder Structure:\n")
for dirpath, dirnames, filenames in os.walk(root_folder):
    level = dirpath.replace(root_folder, "").count(os.sep)  # Determine folder depth
    indent = "   " * level  # Indentation for better visualization
    print(f"{indent}📁 {os.path.basename(dirpath)}")  # Print folder name
    for file in filenames:
        print(f"{indent}   📄 {file}")  # Print file names
