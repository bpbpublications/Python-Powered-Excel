# Lambda functions -------------

add_10 = lambda x: x + 10

print(add_10(5))                          # 15

# Another example:
discount = lambda price: price * 0.9      # 10% off
print(discount(100))                      # 90.0

# Lambda functions can also be used without giving any name 
# That's why lambda function are also known as anonymous function
(lambda x: x + 10)(5)
(lambda price: price * 0.9)(100)

# Operations on each element of a list --------------------------
prices = [100, 250, 450, 390, 120]

# Using for loop:
    
discounted_prices = []
    
for p in prices:
    discounted_prices.append(p * 0.9)

print(discounted_prices)  

# Using list comprehension

discounted_prices = [p * 0.9 for p in prices]
print(discounted_prices)  
    
# Using list map
discounted_prices = list(map(lambda p: p * 0.9, prices))
print(discounted_prices)                  

# Using dictionary comprehension

discounted_prices = {p: p * 0.9 for p in prices}
print(discounted_prices)  
    
# Useful Operations such as filtering/sorting --------------------------

# Use-Cases  --------------------------

# Filtering Prices > 300
high_prices = list(filter(lambda p: p>300, prices))
print(high_prices) 

# Add 10% tax to each price
final_prices = list(map(lambda price: price * 1.10, prices))
print(final_prices)   

# Filtering Profitable Deals
revenues = [500, 1500, 700, 2000]
# Keep only revenues greater than 1000
profitable = list(filter(lambda revenue: revenue > 1000, revenues))
print(profitable)   # [1500, 2000]

# Calculating Bonuses from Sales
sales = [3000, 4500, 6000]
# Bonus is 5% of sales
bonuses = list(map(lambda sale: sale * 0.05, sales))
print(bonuses)   # [150.0, 225.0, 300.0]

# Aggregating Total Profit
from functools import reduce

profits = [200, 350, 400, 250]
total_profit = reduce(lambda x, y: x + y, profits)
print(total_profit)   # 1200

# Sorting names alphabetically
names = ["Ravi", "Anita", "Suresh", "Rajiv"]

# Sort alphabetically
sorted_names = sorted(names, key=lambda name: name)
print(sorted_names)

# Sorting Sales Records by Revenue
sales = [
    {"product": "Pen", "revenue": 700},
    {"product": "Notebook", "revenue": 800},
    {"product": "Eraser", "revenue": 500}
]

sorted_sales = sorted(sales, key=lambda record: record["revenue"], reverse=True)
print(sorted_sales)