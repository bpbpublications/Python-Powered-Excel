# List Comprehensions --------------------------------------

# to create a list of squares of numbers from 1 to 5

squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]


# Doing the same with loop

squares = []

for x in range(1, 6):
    squares.append(x**2)
    
print(squares)  # Output: [1, 4, 9, 16, 25]    

# to create a list of squares of even numbers (numbers that are divisible by 2) from 1 to 10

squares_even = []

for x in range(1, 11):
    if x%2 == 0:
        squares_even.append(x**2)
    
print(squares_even) 

# Using list comprehension
[x**2 for x in range(1, 11) if x % 2 == 0] 


# Dictionary Comprehensions ---------------------------------

squares = {x: x**2 for x in range(1, 6)}
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

squares_even = {x: x**2 for x in range(1, 6) if x%2 == 0}
print(squares_even)

# Product-price lookup
products = ["Apple", "Banana", "Mango"]
prices = [120, 60, 280]

product_price = {p: pr for p, pr in zip(products, prices)}
print(product_price) #  {'Apple': 120, 'Banana': 60, 'Mango': 280}
