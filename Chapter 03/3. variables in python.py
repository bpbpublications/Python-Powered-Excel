
# Assiging value to a variable ----------------------
age = 40 
print(age)

# Valid and invalid names  --------------------------

# Invalid NAMES (You'll get syntax error in these examples): 
total sales = 1200  # Spaces are not allowed in variable names  
discount% = 10  # special characters (like %) are not allowed in variable names  
1batch = 500  # Variable names cannot start with a number

# Valid  NAMES: (For the examples mentioned above)
total_sales = 1200 # Use underscores instead of spaces (snake_case, recommended)  
print(total_sales)  # Output: 1200  

discount_perc = 10  # Use descriptive names without special characters  
print(discount_perc)

batch1 = 500  # Numbers can be used, but not at the start  
print(batch1)

# Different naming conventions ---------------------- 

average_price = 550  # snake_case (Recommended) 
AveragePrice = 550  # PascalCase   
averagePrice = 550  # camelCase 
# Read more about naming conventions: https://peps.python.org/pep-0008/#naming-conventions

# Changing data type of a variable (allowed in Python)   --------------------

x = 10  # x is an integer  
print(x)  # Output: 10  

x = 'ten'  # Now x is a string/text  
print(x)  # Output: ten (Python allows dynamic typing)  