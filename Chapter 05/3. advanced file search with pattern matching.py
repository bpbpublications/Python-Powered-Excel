import os, glob

chapter_directory = os.path.join(os.getcwd(), 'Chapter 05')
os.chdir(chapter_directory)

# To get all the files and folders in a specified folder -----------------

# all files/folders in current working directory
glob.glob('*') 

# names sorted in alphabetical order
sorted(glob.glob('*')) 

# To get a list of only folders in current directory ----------------------

glob.glob('*/')

# To get all files in reports folder inside current working directory ------

reports_folder = os.path.join(os.getcwd(), 'Reports')
content = glob.glob(f"{reports_folder}/*")

print('List of all files/folders: \n', content)

# To get specific types of files -------------------------------------------

glob.glob("*.docx") # all 'docx' files in current working directory   
    
# To fetch all 'docx' files from reports_folder  
  
docx_files = glob.glob(f"{reports_folder}/*.docx")
print('List of all docx files: \n', docx_files)

# To search inside subfolders ---------------------------------------------
    
# To fetch 'xlsx' files from sub-folder Q1
# os.path.join(reports_folder, 'Q1')
xlsx_files = glob.glob(os.path.join(reports_folder, 'Q1', '*.xlsx'))
print('List of all xlsx files in Q1 folder: \n', xlsx_files)

# Fetching all 'xlsx' files in all subfolders can be done easily
xlsx_files = glob.glob(os.path.join(reports_folder, '**/*.xlsx'), recursive=True)
# or
xlsx_files = glob.glob(os.path.join(reports_folder, '**', '*.xlsx'), recursive=True)
print('List of all xlsx files in all subfolders: \n', xlsx_files)

# Fetching all 'xlsx' files from a folder one-level up from reports_folder
xlsx_files = glob.glob(os.path.join(reports_folder, '../*.xlsx'))
print('List of all xlsx files in one level up: \n', xlsx_files)

# To get files by prefix, suffix and more --------------------------------
# (Try out your own examples):
    
# finding files with prefix 'ch_'
book = os.path.join(os.getcwd(), 'Book Writing')
book = 'C:\my D Drive\Learning\Learn Python git hub\Excel_Python\Book Writing'
chapters = glob.glob(os.path.join(book, '*ch_*.docx'))
print('Chapter Drafts: \n', chapters)


# finding files with suffix 'Python'
topic_python = glob.glob(os.path.join(book, '*Python.docx'))
print('Files Related to topic Python: \n', topic_python)

# files that contain 'extras' anywhere
extra_files = glob.glob(os.path.join(book, '*extra*.docx'))
print('Extra stuff for chapters: \n', extra_files)

# To get folders only (ignoring files) ---------------------------
folders = glob.glob(os.path.join(os.getcwd(), "*/"))  # Only folders
print(folders)
