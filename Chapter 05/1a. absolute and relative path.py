import os
# Getting Absolute path from relative path ___________________________________

# Relative path 
# (uncomment these relative paths one by one to notice the diff)

relative_path = 'test.py'
relative_path = 'scripts/test.py'

# If file is outside the current directory, (../ indicates one level up)

relative_path = "../test.py"  # # ../ means test.py is one level up from your working directory

relative_path = "../../test.py"  # 2 level up from working directory
# However, it cannot go beyond the root directory (e.g., C:/ or D:/). 

# Convert to absolute path
absolute_path = os.path.abspath(relative_path)  
print("Absolute Path:", absolute_path)  # Now it's a full path

# Again Getting Relative Path from absolute path
rel_path = os.path.relpath(absolute_path)
print('\nAgain Getting Relative Path:', rel_path)
