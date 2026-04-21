# Try It Yourself ________________________________________________

# 7.	You have many zipped files saved in your Downloads folder. Write a Python script to:
# a.	Find all .zip files in the Downloads folder, and
# b.	Unpack them into a single folder named ‘restored_old_files’ inside your current working directory.

import os, glob, shutil

# Step 1: Get user's Downloads folder path (cross-platform)
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Step 2: Get all .zip files from Downloads (non-recursive)
zip_files = glob.glob(os.path.join(downloads_folder, '*.zip'))

# Step 3: Folder to extract all zips
extract_to = os.path.join(os.getcwd(), 'restored_old_files')
os.makedirs(extract_to, exist_ok=True)

# Step 4: Unpack each zip file
for zip_file in zip_files:
    try:
        shutil.unpack_archive(zip_file, extract_to)
        print(f"✅ Unpacked: {os.path.basename(zip_file)}")
    except Exception as e:
        print(f"⚠️ Failed to unpack {zip_file}: {e}")
    
# NOTE:os.path.expanduser("~") → gets the path to the current user’s home folder

