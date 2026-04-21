# For the purpose of this demo, I've created 2 excel files (you can use any other file too)
# 'Attendance Records.xlsx' and 'marks.xlsx'  in 'Chapter 05' folder

# Set 'Chapter 05' folder as your working directory

import os, shutil
         
current_chapter = "Chapter 05"
chapter_directory = os.path.join(os.getcwd(), current_chapter)
os.chdir(chapter_directory)

# To copy a file in the same directory ----------------------------
source = 'Attendance Records.xlsx' # Name or Path of the file that you want to copy
destination = 'Attendance Records_Backup.xlsx' # Name or path of copied file
shutil.copy(source, destination)

    
# To copy a file from some folder to another folder -----------------
# (Try this with any file/path): 
    
source = 'D:/Excel_Python/test.docx' # Name or Path of the file that you want to copy
destination = 'D:/test_copy.docx' # Name or path of copied file
shutil.copy(source, destination)

# Another Example:
    
os.mkdir('Back-upFiles')
source = 'Attendance Records.xlsx'
destination = 'Back-upFiles/Attendance Records_Backup.xlsx'
shutil.copy(source, destination)

shutil.copy('empty.xlsx', 'Back-upFiles/empty.xlsx')

# To copy entire folder (with all files inside) ---------------------
    
source = 'Back-upFiles'
destination = 'Archive_Back-upFiles'
shutil.copytree(source, destination)

# To move a file to another folder -----------------------------------
    
source = 'marks.xlsx' # Any file that you want to move
destination = 'Back-upFiles' # Any existing folder location

shutil.move(source, destination)
