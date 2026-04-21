import os, shutil

# Setting working directory to Chapter 05 folder (inside Excel_Python)

chapter_directory = os.path.join(os.getcwd(), 'Chapter 05')
os.chdir(chapter_directory)

# To compress entire folder --------------------------------

# Use current directory as base path
base_path = os.getcwd()

# Folder you want to compress (inside current dir)
folder_to_compress = 'Back-upFiles'

# Location where you want to save the zip
zip_location = os.path.join(base_path, 'Backup', 'Back-upFiles') # No extension here
# Try changing zip location
# zip_location = os.path.join(base_path, 'Back-upFiles') 

# Archive format
format = 'zip'  # or 'tar', 'gztar', 'bztar', 'xztar'

# Create the archive
shutil.make_archive(zip_location, format, folder_to_compress)
print("✅ Zipped successfully!")


# To decompress a folder -----------------------------------
    
# Path to the archive/zipped file (Add extension in filename)
archive_path = os.path.join(base_path, 'Backup', 'Back-upFiles.zip')

# Folder where you want to extract/unzip the contents
extract_to = os.path.join(base_path, 'restored_oldFiles')

# Unpack the archive
shutil.unpack_archive(archive_path, extract_to)   
print("✅ Unzipped successfully!")

# More Example:
tar_location = os.path.join(base_path, 'Backup', 'Back-upFiles')
shutil.make_archive(tar_location, 'tar', folder_to_compress)
    
archive_path_tar = os.path.join(base_path, 'Backup', 'Back-upFiles.tar')
extract_to = os.path.join(base_path, 'new_tar')
shutil.unpack_archive(archive_path_tar, extract_to)  

# NOTE:  when creating, Python handles the extension automatically. 
# When unpacking, you point to an existing file, so give the full name!