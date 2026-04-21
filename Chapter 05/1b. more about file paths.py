import os

# To check if a given path exists or not, whether it’s a file, directory, 
# or other types of entities, you can use os.path.exists()

# To check if the file exists ----------------------

filename = 'test.py'

if os.path.exists(filename):
    print(f"The file '{filename}' exists in the current working directory.")
else:
    print(f"The file '{filename}' does not exist in the current working directory.")

# To check if the path exists ----------------------

os.path.exists('D:\\Excel_Python\\test.py') 

# check if the given path is a file (NOT folder) that exists -----------

os.path.isfile('1. absolute and relative paths.py') # True if it is a file that exists
os.path.isfile('D:\\Excel_Python\\test.py') # False if file does not exist
os.path.isfile('D:\\Excel_Python') # False, if it's a folder not a file

# check if the given path is a folder (directory) that exists -----------

os.path.isdir('D:\\Excel_Python') # True if it is a folder that exists
os.path.isdir('1. absolute and relative paths.py') # False if it is a file

# Creating file/folder path by concatenating/joining path segments -----------

# If we use string concatenation, we need to carefully supply separator
current_folder = os.getcwd()
file_name = "test.py"
current_folder + "\\" + file_name # on windows
current_folder + "/" + file_name # on macOS

# Note that you would need a '/' and a '\' if you're working on 
# Mac/Linux or Windows operating system. 
# Hence, creating path using string concatenation is not recommended.
# We should always write code that works on all machines

# Instead, we can use os.path.join() to join paths intellegently
# (which is portable cross-platform)
current_folder = os.getcwd() # It will be your working directory

# If you are on windows machine and your current working directory is 'D:\\Excel_Python'
current_folder = 'D:\\Excel_Python' # Suppose it's this folder 
full_path = os.path.join(current_folder, file_name)
print(full_path) # D:\Excel_Python\test.py

# If you are on mac or linux machine and your current working directory is 'D:/Excel_Python'
current_folder = '/home/gaurav/Excel_Python' # Suppose it's this folder 
full_path = os.path.join(current_folder, file_name)
print(full_path) # /home/gaurav/Excel_Python/test.py

# You must have realised, os.path.join() return path that are specific to your
# machine's operating system. 
# In order to create reproducible code, we should use one more step
# Using os.path.normpath() can help us create paths independent to OS.
# We will discuss it shortly


# More examples

# On Windows
print(os.path.join("C:\\Users", "Nisha", "Documents"))
# Output: C:\Users\Nisha\Documents

# On Linux/macOS
print(os.path.join("/home", "nisha", "docs"))
# Output: /home/nisha/docs

# more than 2 path segments --------

# current_folder = os.getcwd()
current_folder = 'D:\\Excel_Python' # Suppose it's this folder
subfolder = "scripts"
filename = "test.py"

full_path = os.path.join(current_folder, subfolder, filename)
print(full_path) # D:\Excel_Python\scripts\test.py on windows


# NOTE POINTS: 
    # 1. If you pass an empty string, it just ignores it

os.path.join("folder", "")  # 'folder\\'

    # 2. If the second argument starts with a separator (absolute path), 
    # it overrides the first

os.path.join('D:\\Excel_Python', '\scripts\\test.py') # 'D:\\scripts\\test.py'
    
os.path.join("/home/user", "/etc")  # '/etc'

os.path.join("C:/Users/UserName/Documents", "/Sales_Report.xlsx")  
#  It ignores "C:/Users/UserName/Documents" completely
# Output: C:/Sales_Report.xlsx (Unexpected path - absolute path from root)

os.path.join("C:/Users/UserName/Documents", "Sales_Report.xlsx")  
# Output: C:/Users/UserName/Documents/Sales_Report.xlsx (This is what we wanted!)

    # 3. If any component is an absolute path, all previous components are discarded 
    # and joining continues from that absolute path.

os.path.join('D:\\Excel_Python\\test.py', 'C:\\scripts')

os.path.join('C:\\scripts', 'D:\\Excel_Python\\test.py')

    # 4. It doesn’t check if the path actually exists (use os.path.exists() for that).

# Creating Platform-independent path -----------------

# we can create consistent format of file paths using os.path.normpath() 
# We should prefer to use methods that are platform-independent 
# (e.g., works correctly on Windows and Unix-like systems).

# It ensures that the correct path separator 
# (\ on Windows, / on Unix-like systems) is used automatically.
# os.path.normpath() creates platform-independent paths

folder = input('Enter File Path: ') # Type to the prompt_ D:/Excel_Python
# or set manully to reprodce the same example
folder = 'D:/Excel_Python'
filename = "test.py"

full_path = os.path.join(folder, filename)
print(full_path) # D:/Excel_Python\test.py on windows (gives mixed slashes)

os.path.normpath(full_path) # 'D:\\Excel_Python\\test.py'

# to fetch a file name from a full file path ---------------------------------

full_path = 'D:\\Excel_Python\\test.py'
file_name = os.path.basename(full_path) # test.py
print(file_name)

file_path = "D:/Projects/Reports/marketing_data.xlsx"
file_name = os.path.basename(file_path) # Output: marketing_data.xlsx
print(file_name)

# Fetching file name without extention or file name:
os.path.splitext(file_name) # It's a tuple

os.path.splitext(file_path)[0] # file name without extension
os.path.splitext(file_path)[1] # file extension
