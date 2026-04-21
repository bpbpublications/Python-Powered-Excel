# Nested Lists:
# Nested lists can also be heterogeneous (mixed data type)    
# A list of lists representing a table of product details


product_details = [
    ["Product A", 19.99, 10],
    ["Product B", 29.95, 5],
    ["Product C", 9.99, 15]
]



# To print this data
product_details

# Accessing elements in the nested list
print("First product details:", product_details[0])  # Prints details of Product A
print("Price of second product:", product_details[1][1])  # Prints price of Product B

# As elements of this list are lists themselves, we can further subset those
product_details[2][2] # third element of the third list

# Modifying an element in the nested list
product_details[2][2] = 20  # Change the stock of Product C to 20

# Adding a new product to the nested list
product_details.append(["Product D", 14.49, 8])

product_details.extend([["Product E", 49.99, 3], ["Product F", 34.99, 7]])

product_details
    
# You can do more with nested lists:

# Calculate revenue for each product
for item in product_details:
    product, price, qty = item
    revenue = price * qty
    print(f"{product}: ${revenue:.2f}")
    
# In Chapter 6, you'll learn a mighty python library 'pandas' that will allow you to:
    # Sort by revenue
    # Find product with highest sale
    # Calculate total revenue
    # and much more
    
import pandas as pd

# Convert nested list to DataFrame
df = pd.DataFrame(product_details, columns=["Product", "Price", "Quantity"])

df

# Add a new column
df["Revenue"] = df["Price"] * df["Quantity"]
df

# Sort by revenue
df_sorted = df.sort_values(by="Revenue", ascending=False)
print(df_sorted)
   
# Example 2
products = [
    ["Product A", 19.99, 10, True],
    ["Product B", 29.95, 5, False]
]

products

for item in products:
    product, price, qty, in_stock = item
    print(f'{product} is Available?: {in_stock}')


# More Example: Hetro list (Not Nested)
team_info = ["Alice", 28, True, 120.5, "Bob", 34, False, 
             95.0, "Charlie", 22, True, 110.0]

# Loop through the list to extract relevant data and print in a readable format
for i in range(0, len(team_info), 4):
    name = team_info[i]
    age = team_info[i+1]
    is_active = team_info[i+2]
    hours_worked = team_info[i+3]
    
    print(f"Name: {name}, Age: {age}, Active: {is_active}, Hours Worked: {hours_worked}")

# Beginners can skip the following code for now ----------------------------

# A plain nested list in Python doesn’t support named columns—you only access 
# items by index (e.g., row[0], row[1]). But you can introduce column names by 
# switching to a more structured data type

# - List of dictionaries
# Instead of lists inside lists, use dictionaries with keys as column names:

product_details = [
    {"name": "Product A", "price": 19.99, "qty": 10},
    {"name": "Product B", "price": 29.95, "qty": 5},
    {"name": "Product C", "price": 9.99, "qty": 15}
]

product_details

# - Namedtuple (from collections)
# Like tuple it is immutable
# Gives lightweight objects with named fields

from collections import namedtuple

Product = namedtuple("Product", ["name", "price", "qty"])
product_details = [
    Product("Product A", 19.99, 10),
    Product("Product B", 29.95, 5)
]

# - Dataclass (Python 3.7+)
# More modern and flexible than namedtuple

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    qty: int

product_details = [
    Product("Product A", 19.99, 10),
    Product("Product B", 29.95, 5)
]

# - pandas data frame