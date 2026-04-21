
# Adding Bonus score (+2) for each participant
score_list = [23, 39, 46, 38, 27]

print('After adding Bonus, Scores are: \n')
for score in score_list: 
    print(score + 2)

# Printing each product name in lower case    
products = ["Apple", "banana", "MANGO", "ORANGE"]

print('After text cleaning, product names: \n')
for item in products:
    print(item.lower())  
    

for i in range(5):
    print(i+10)

# Looping with condition (like filtering rows in Excel)    
# Print products priced above 100    
prices = {"Apple": 120, "Banana": 60, "Mango": 280, "Orange": 145}

for product, price in prices.items():
    if price > 100:
        print(product, "is premium product")  # Like a FILTER formula in Excel 365

# 🚦 Transfer Statements in Python (Break, Continue, Pass)
    
# Find the first product over ₹100
for product, price in prices.items():
    if price > 100:
        print("Found:", product)
        break  # Stops after first match

# break → stop the loop when a match is found    

# continue → skip current iteration
    
# Print only items under ₹150
for product, price in prices.items():
    if price > 150:
        continue  # Skip expensive items
    print(product, "is affordable")

# pass → do nothing (placeholder, often used while drafting logic)
for product, price in prices.items():
    if price > 150:
        pass  # Not Sure what to do yet


for product in products:
    if product == "MANGO":
        pass  # Logic to be written later
    else:
        print("Processed:", product)
    

# Looping through rows of a table (nested list)    
product_data = [
    ["Apple", 120],
    ["Banana", 60],
    ["Mango", 280]
]

for row in product_data:
    name, price = row
    print(f"{name}: ₹{price}")  # Like reading rows from Excel
 
# range() function

# starts from 0
range(5)           # range(0, 5)

# View elements in form of list
list(range(5))     # [0, 1, 2, 3, 4]

# can provide starting point
list(range(1, 5))     # [1, 2, 3, 4]

# Works with negative numbers too
list(range(-3, 5)) # [-3, -2, -1, 0, 1, 2, 3, 4]

# You can also use it with start and step:
list(range(1, 10, 2))  # [1, 3, 5, 7, 9]


# Using in a for loop
for i in range(3):
    print("Hello", i)

# Send 3 reminder messages
for i in range(1, 4):
    print(f"Reminder {i}: Please submit your report.")


# enumerate() – Add Index to Loops
# enumerate() lets you loop with both index and value:
fruits = ["Apple", "Banana", "Mango"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
    
employees = ['Neha', 'Krishna', 'Joy', 'Ted']

print('Employee ID: Employee Name\n')
for i, name in enumerate(employees, start = 100):
    print(f"{i}: {name}")
    
    
# zip - Combine product names with prices
# Like merging two columns side by side.

products = ["Apple", "Banana", "Mango"]
prices = [120, 60, 280]

combined = list(zip(products, prices))
print(combined)
# [('Apple', 120), ('Banana', 60), ('Mango', 280)]