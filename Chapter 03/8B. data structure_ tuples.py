
# Define a tuple of coordinates
coordinates = (10, 20)  # Tuple with two values
coordinates  # (10, 20) 

# You can also create a tuple directly (sep values by  a comma)
coordinates = 10, 20 ; coordinates  # (10, 20) 

# Or you can convert a list to tuple
coordinates = tuple([10,20]); coordinates  # (10, 20) 

# As tuple is immutable, you can't add/remove or change elements
# However, you indexing/slicing is allowed as it is ordered and indexable

# append(), remove() or other similar methods are not available for tuples
coordinates.append(30) # 'tuple' object has no attribute 'append'
coordinates.remove(10) # 'tuple' object has no attribute 'remove'

coordinates[0]
coordinates[1]

# As you understand, you can't modify/reassign it's element
coordinates[0] = 15 # 'tuple' object does not support item assignment

# Hetrogeneous tuple (Mixed Data Type)
product_info = ("Product A", 19.99, 10, True)
product_info

# Counting items in a tuple
tools = ('python', 'excel', 'python', 'vba', 'python')

print(tools.count('excel'))
print(tools.count('python'))

# position of match
tools.index('python') # index of first match
tools.index('python', 1) # start searching from index 1

# Nested Tuples:
# Nested tuples can also be heterogeneous (mixed data type)
# A list of lists representing a table of product details

product_details = (
    ["Product A", 19.99, 10],
    ["Product B", 29.95, 5],
    ["Product C", 9.99, 15],
    ["Product D", 14.49, 8],
    ["Product E", 49.99, 3]
)

# To print this data
product_details

# Accessing elements in the nested list
print("First product details:", product_details[0])  # Prints details of Product A
print("Price of second product:", product_details[1][1])  # Prints price of Product B

# Accessing an element in the nested tuple
product_details[2][2] 

# Next Example
products = (
    ("Product A", 19.99, 10, True),
    ("Product B", 29.95, 5, False)
)
products

for item in products:
    product, price, qty, in_stock = item
    print(f'{product} is Available?: {in_stock}')