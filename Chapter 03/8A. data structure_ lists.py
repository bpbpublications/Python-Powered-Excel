# Create lists
products = ['mobile', 'laptop', 'tablet', 'mobile']; products
stock = [120, 38, 55]; stock
demo = ['Nisha', 40, True]; demo

# Define a list of prices for 10 products
prices = [19.99, 29.95, 9.99, 14.49, 49.99, 4.99, 5.49, 39.99, 24.99, 44.99]

# Add a new price to the list
prices.append(34.99)

# Add multiple elements to the list
prices.extend([100, 101])

# Remove a price from the list
prices.remove(14.49) # It removes only first occurance

# Change the price of the first product
prices[0] = 21.99

# Print the updated list of prices
print("Updated prices:", prices)

# Sort the list in asending/descending order
print(f'Sorted Prices in ascending order: {sorted(prices)}')
print(f'Sorted Prices in descending order: {sorted(prices, reverse =True)}')

# List Concatanation using '+' to create a new list

# Merging monthly sales data
jan_sales = [12000, 15000]
feb_sales = [18000, 16000]
mar_sales = [20000, 18000]
q1_sales = jan_sales + feb_sales + mar_sales
q1_sales # [12000, 15000, 18000, 16000, 20000, 18000]

# Creating Master product list

fruits = ['A101', 'A102', 'A103']
vegetables = ['B201', 'B202']
product_ids = fruits + vegetables
print(product_ids) # ['A101', 'A102', 'A103', 'B201', 'B202']

# List Concatanation using 'expand()' to expand the existing list

#  Continuously Adding Weekly Sales to a List
# you are updating a single sales list as each new week’s data arrives.
weekly_sales = [5000, 7000, 6200]  # Week 1–3
week4_sales = [8000, 7500]

# Add Week 4 sales to existing list
weekly_sales.extend(week4_sales)
print(weekly_sales) # [5000, 7000, 6200, 8000, 7500]

# Appending New Hires to an Existing Employee List
# You maintain a running employee list, and new joiners come in a separate list each month.

employees = ['Amit', 'Priya', 'John']
new_joinees = ['Sara', 'Leo']

employees.extend(new_joinees)
print(employees) # ['Amit', 'Priya', 'John', 'Sara', 'Leo']


# Hetrogeneous list (Mixed Data Type)
product_info = ["Product A", 19.99, 10, True]
product_info

# Counting items in a list
tools = ['python', 'excel', 'python', 'vba', 'python']

print(tools.count('excel'))
print(tools.count('python'))

# position of match
tools.index('python') # index of first match
tools.index('python', 1) # start searching from index 1

# Example of a nested list: Next CODE file