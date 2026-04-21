# Function with no input ---------------------------------

# Defining the function

def welcome():
    print("Hello, welcome to Python!")

# Calling the function
welcome() 

# Adding docstring (Optional but often useful) ------------------------

def welcome():
    """"A simple function that prints a welcome msg"""  # ← This is a docstring
    print("Hello, welcome to Python!")

# Calling the function
welcome() 

# A quick way to inspect/get help on a function
?welcome 

# Doc string of built-in functions
?len


# Function with one input ---------------------------------

# Defining the function
def add_10(a):
    print(a + 10) # prints input + 10

# Calling the function
add_10(20)        # 30
add_10(a = 20)    # Same Result

# You need to supply exactly one input, no more, no less
add_10()     # TypeError: add_10() missing 1 required positional argument: 'a'
add_10(20, 30) # TypeError: add_10() takes 1 positional argument but 2 were given

# Function with more than one inputs -------------------------------     

def add_num(a, b):
    return a + b

add_num(5, 15)

# Storing the result of this function in a new variable called result
result = add_num(5, 15); print(result) # 20

print("Sum is:", result)

# Notice, you can not store and use the value
# from add_10() function as it does not return anything

x = add_10(20); x+50 # Error
print(x) # None

# print and/or return -------------------------------

def show_total(price, qty):
    total_rev = price * qty
    print("Total Revenue is:", total_rev) # Only shows it doesn’t save it

show_total(50, 2)              # Just prints

result = show_total(50, 2) # prints because calling function prints "Total Revenue is:", total_rev
print(result) # None as there’s nothing stored

def get_total(price, qty):
    return price * qty  # Can use the result later as it’s saved

get_total(50, 2) # prints because python prints the value of last executed line

# Try this
get_total(50, 2); 5000 # it prints only last statement

total = get_total(50, 2)
print("Total revenue is:", total)   # Reusable

# Order of arguments matter -------------------------------

def balance(income, expense):
    return income - expense

# Calling the function
print(balance(5000, 3500))  # 1500 (Profit or balance)
print(balance(3500, 5000))  # -1500 (Loss)
balance(expense = 3500, income = 5000) # 1500

# More example
def profit(sp, cp):
    print(sp-cp)
    
profit(cp = 1000, sp = 1200)    
    
# Default Value -------------------------------

def greet(name="friend"):
    print(f"Hello, {name}!")
    
greet()            # Hello, friend! -> Uses default
greet("Nisha")    # Hello, Nisha! -> Uses input

# More example
def balance(income, expense=0):
    return income - expense

print(balance(5000))  # 5000 (No expense provided, so it takes the default expense = 0)
print(balance(5000, 1000)) # 4000 (it takes expense = 1000)

#  This will raise an SyntaxError
balance(expense=3500, 5000) # positional argument follows keyword argument
# Always keep positional args before keyword args, or use all as keyword.

balance(5000, expense=3500) # Works Now

# In the same way, while defining the function, you must write parameter(s) 
# that take(s) default value(s) after parameter(s) without default(s). 
# If you do otherwise, you will get ‘SyntaxError: parameter without a default follows parameter with a default’
# See example:
    
def balance(income=100, expense):
    return income - expense

def balance(expense, income=100):
    return income - expense

# *args _ Passing multiple values
def total_bill(*items): # Accepts any number of arguments
    return sum(items)

print(total_bill()) # No input
print(total_bill(100, 200, 50)) # three inputs 
print(total_bill(100, 200, 50, 120)) # four inputs


 # **kwargs — Passing Multiple Named Arguments 
def product_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

product_info(name="Laptop", price=50000)
product_info(name="Laptop", price=50000, stock=10)

# *args — Passing Multiple Values
def total_bill(*items):
    return sum(items)


# Use-Cases
# Example 1: Calculate Discount Price
def apply_discount(price, discount=10):  # default 10% discount
    return price * (1 - discount / 100)

print(apply_discount(200))       # → 180.0
print(apply_discount(500, 20))   # → 400.0


# Example 2: Return Pass/Fail Status (Like Grading in Excel)
def grade(score):
    if score >= 40:
        return "Pass"
    else:
        return "Fail"

print(grade(75))  # → Pass

# You can create function with built-in object's names BUT YOU MUST AVOID IT
def int():
    print('h')
    
int()    
int(2.3)

del int
int(2.3)
int('two')
