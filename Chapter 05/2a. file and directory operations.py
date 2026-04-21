import os
import shutil

# Comfortable with file paths now?
# Set 'Chapter 05' folder as your working directory
# To create/delete/rename or move test files from the same folder
     
current_chapter = "Chapter 05"
chapter_directory = os.path.join(os.getcwd(), current_chapter)
os.chdir(chapter_directory)

# All available files/folders:
    
os.scandir() # An iterator containing all files/folders in current directory
list(os.scandir())# list of files/folders from your current working directory
len(list(os.scandir())) # Numer of files/folders

folder = 'D:/Excel_Python' # write path of any folder on your machine
list(os.scandir(folder))# list of files from folder

# one more way

os.listdir() # gives a list of all files and folders in current working directory
len(os.listdir())

# from a given folder
folder = 'D:\\Excel_Python'
os.listdir(folder) 

# The os.scandir() function is significantly faster and more efficient than os.listdir()

# --------------------------------------------------------------

# Folder Creation:

# To create a folder 'test' in current directory
# If the folder already exists, this will raise a FileExistsError

os.mkdir('test') 

# Create a folder in some other path
os.mkdir("D:/another_test")
os.mkdir(os.path.join(folder, "one_more_test"))

# To create a subfolder inside 'test' folder 

# If the subfolder already exists, this will raise FileExistsError
os.mkdir('test/subfolder1')

# If you try to create a subfolder in a non-existance folder, this will raise FileNotFoundError
os.mkdir('test2/subfolder1')

# To create a folder structure/directory tree/nested or recursive directories: 
    
# If the folder already exists, this will raise a FileExistsError
os.makedirs('Folder1/SubFolder1/NextLevel Folder1')
os.makedirs('Folder1/SubFolder1/NextLevel Folder2')
os.makedirs('Folder1/SubFolder2/testFolder1')

# You can set exist_ok=True (python 3.2 onwards) to avoid FileExistsError, 
# if the folder already exists
os.makedirs('Folder1/SubFolder1/NextLevel Folder1', exist_ok=True)

# --------------------------------------------------------------

# To delete a folder: 
os.rmdir('test') # Can not delete non-empty folder

os.rmdir('test/subfolder1') # Subfolder deleted
os.rmdir('test') # Now, this is deleted too

# To remove nested directories (Only if empty)
os.removedirs('Folder1/SubFolder1/NextLevel Folder1')

# To delete NON-EMPTY nested directly completely 
# (Be careful, it will delete entire directory tree)
shutil.rmtree('Folder1')

# --------------------------------------------------------------

# To rename a folder or a file:
    
os.makedirs('test/subfolder1')
os.rename('test', 'new_test')
os.rename('new_test/subfolder1', 'new_test/new_subfolder1')

# rename file (Keep a text file named ‘empty.txt’ in your current dir)
os.rename('empty.txt', 'no_data.txt')
# rename file (Keep an excel file named ‘empty.xlsx’ in your current dir)
os.rename('empty.xlsx', 'no_data.xlsx')

# delete a file
os.remove('no_data.txt')
os.remove('no_data.xlsx')

# os.remove(path) deletes a file (not folders).
# os.rename(source, destination) renames or moves any file or folder.
# Yes, you can evem move files using os.rename() by giving a different path to destination 
# provided you are moving on same drive (D drive to D drive)

# For more flexiblility with moving files across drives 
# or between USBs, cloud dirs, etc. you can use shutil.move()
# We will discuss it in next code file