# Importing os module 
import os 

# To get current working directory
os.getcwd()

# To change working directory, you can give path of your own folder/directory
# os.chdir("D:/Path/That/You Choose")  

# To change working directory to 'D:\Excel_Python' 
# (On Windows Machine, folder path shows up using backslashes (\) while
# on Mac or Linux it is forward slash (/))
os.chdir("D:\Excel_Python")

# Backslashes work only if they don’t form escape sequences. Try os.chdir("D:\new")
# Use double backslashes (\\), forward slash (/) or raw strings (r"...")

os.chdir("D:\\Excel_Python") 
## or
# os.chdir("D:/Excel_Python")
## or
# os.chdir(r"D:\Excel_Python")

# NOTE:
    # 1. Backslashes work only if they don’t form escape sequences. Try os.chdir("D:\new")
    # 2. Raw strings r"D:\Excel_Python" are not always suited for windows paths. 
    # From the link, raw strings will work as long as you don't end them in \
    #     (Try r"D:\Excel_Python\")
        

# To verify it again
os.getcwd()        