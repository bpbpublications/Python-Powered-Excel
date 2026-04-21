# You can create a dictionary by enclosing a comma-separated list of key-value pairs in curly braces {}.
# A colon : separates each key from its associated value.
employees = {"E101": "Prateek", "E102": "Pragya"}
employees

# Accessing elements/Indexing (LOOKUP Employee Name by Employee Id)
employees["E101"]
employees["E103"] # Indexing for non-existing key gives KeyError

# You can avoid getting this error by using dict.get() method
employees.get("E101") # same result
print(employees.get("E103") ) # None

# It safely handles  missing keys 
# You can also print a msg as you prefer for missing keys
employees.get("E103", "Not Found")


# Nested dictionary (to store more information of each employee)
employees = {'E101': {'name': 'Prateek', 'age': '27', 'sex': 'Male'},
          'E102': {'name': 'Pragya', 'age': '22', 'sex': 'Female'}}
employees
type(employees)
len(employees)

# Accessing elements/Indexing
employees["E101"]
employees["E101"]['name']

# Merging two dictionaries (Much easier than Excel)

products_prices = {
    "Apple": 120,
    "Banana": 60
}

new_prices = {
    "Mango": 280,
    "Banana": 100
}

# Python 3.9 introduced | operator to merge dictionaries
updated = products_prices | new_prices; updated
# create new merged dictionary, keeping original dictionary unchanged

# |= updates a dictionary in place by merging another dictionary’s key–value pairs.
products_prices |= new_prices; products_prices

# Or you can use unpacking operators **

updated = {**products_prices, **new_prices}
print(updated)
# create new merged dictionary, keeping original dictionary unchanged

# Using update method
# update method modifies the original dictionary in place.
products_prices.update(new_prices)


# Another Example
excel_tools = {
    "data_entry": "Excel",
    "data_cleaning": "Excel formulas",
    "data_visualization": "Excel Charts",
    "automation": "VBA",
    "reporting": "Pivot Tables",
}

modern_tools = {
    "data_cleaning": "Python pandas + Excel",
    "data_visualization": "matplotlib + openpyxl",
    "automation": "xlwings",
    "reporting": "Jupyter Notebooks",
    "predictive_analysis": "Python scikit-learn"
}

# Python 3.9 introduced | operator to merge dictionaries
latest = excel_tools | modern_tools
latest
# {'data_cleaning': 'Python pandas + Excel',
#  'data_visualization': 'matplotlib + openpyxl',
#  'automation': 'xlwings',
#  'reporting': 'Jupyter Notebooks',
#  'predictive_analysis': 'Python scikit-learn'}

# Another option is to use |= operator (python 3.9+)
excel_tools |= modern_tools
excel_tools

# Or you can do using **
latest = {**excel_tools, **modern_tools}
latest

# You can reverse a dictionary using dictionary comprehension
{ val: key for key, val in latest.items() }


# Reverse lookup using a loop (There are many other ways to acheive the same)
# You will be able to figure out by the end of this chapter
target_price = 100
for product, price in updated.items():
    if price == target_price:
        print(product)
        break
