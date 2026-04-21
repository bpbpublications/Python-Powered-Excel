# Operators in Python

# Arithmetic or mathematical operators -------------

a = 10; b = 3 

print(a + b)   # Addition (10 + 3 = 13)
print(a - b)   # Subtraction (10 - 3 = 7)
print(a * b)   # Multiplication (10 * 3 = 30)
print(a / b)   # Division (10 / 3 = 3.33)
print(a ** b)  # Exponentiation (10^3 = 1000)
print(a // b)  # Floor Division (Quotient part of the division 10/ 3 = 3)
print(a % b)   # Modulus (remainder of 10 / 3 = 1)

# Comparison or relationship operators -------------

price1 = 500; price2 = 700  
print(price1 > price2)  # False (500 is not greater than 700)
print(price1 == 500)    # True (equal to 500, similar to A1=500 in Excel)
print(price1 != price2) # True (similar to A1<>B1 in Excel)

# Logical operators -------------

True and True
True and False
False and True
False and False

True or True
True or False
False or True
False or False

not True
not False

stock = 50; price = 200  
print(stock > 20 and price < 500)  # True (Both conditions met)
print(stock > 100 or price < 500)  # True (At least one condition met)
print(not (price > 500))           # True (Reverses the condition)


a = False
b = 1 / 0  # would normally raise error
result = a and b  # doesn't raise error because `a` is False, so Python skips b
result

a = True
b = 1 / 0
result = a or b  # no error, because `a` is True, Python skips b
result
# Excel always evaluates all conditions in AND() and OR(), no short-circuiting.

# Read more about short circuiting in Python: https://www.linkedin.com/posts/drnishaarora_ever-heard-of-short-circuiting-not-the-activity-7373920420141559808-p8Tx?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAepsJkBv8opllaFHDwGtRtHUfsaCud-TdQ

# Membership operators -------------

products = ["Laptop", "Phone", "Tablet"]  
print("Laptop" in products)  # True (Found in the list)
print("Camera" not in products)  # True (Not in the list)

'a' in 'apple'
2 in [2,5,6,9]
3 in [2,5,6,9]
2 not in [2,5,6,9]
3 not in [2,5,6,9]