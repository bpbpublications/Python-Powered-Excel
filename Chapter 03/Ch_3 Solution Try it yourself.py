# Try It Yourself ________________________________________________

# 1.	For a sample email-id such as "user@example.com", extract the domain name.

email = "user@example.com"
email.split('@')[1]   # example.com

# Alternate way

_, domain = email.split("@")
print(domain)   # example.com

# 2.	Repeat the exercise for each email in the given list ["alice@example.com", "bob@company.org", "eve@test.net"]

email_list = ["alice@example.com", "bob@company.org", "eve@test.net"]

# Using for loop
domain_list = []
for email in email_list:
    domain_list.append(email.split('@')[1])
    
print(domain_list) # ['example.com', 'company.org', 'test.net']

# Using list comprehension

domain_list = [email.split('@')[1] for email in email_list]
print(domain_list) # ['example.com', 'company.org', 'test.net']

# Using list-map and lamda function

list(map(lambda email: email.split('@')[1], email_list)) # ['example.com', 'company.org', 'test.net']

# 3A. To rename a file name "file 1.txt" to "file_1.txt", use the string method

filename = "file 1.txt"
new_filename = filename.replace(" ", "_")
print(new_filename)   # file_1.txt

# Using split and join
new_filename = "_".join(filename.split(" "))
print(new_filename)   # file_1.txt

# 3B. use this method and iterate over a list of such names by using loop 
# and by using list comprehension too.

file_names = ["file 1.txt", "file 2.txt", "file 3.txt"]

# Using loop

new_names = []
for file in file_names:
    new_names.append(file.replace(" ", "_"))

print(new_names) # ['file_1.txt', 'file_2.txt', 'file_3.txt']

# Using list comprehension

[file.replace(" ", "_") for file in file_names] 
# ['file_1.txt', 'file_2.txt', 'file_3.txt']

# 4. Mask password "SuperSecret123" by hiding all characters except the last 2

password = "SuperSecret123"
masked = "*"*(len(password) - 2) + password[-2:]
print(masked)   # ************23

# 5. Compute discounted prices for each product (10% discount)

# To simply print

prices = [100, 250, 450, 89, 120]
for price in prices:
    print(price*0.9)
    
# To save in a list

discounted_prices = [price*0.9 for price in prices]
print(discounted_prices)

# 6. 	From the following dictionary, extract only those products that are priced above ₹100:
    
product_prices = {'Apple': 120, 'Banana': 60, 'Mango': 280}

# Using for loop

filtered = {}
for product, price in product_prices.items():
    if price > 100:
        filtered[product] = price

print(filtered) # {'Apple': 120, 'Mango': 280}

# Using dictionary comprehension (Effiecient approach)
filtered = {product: price for product, price in product_prices.items()
            if price > 100}
print(filtered) # {'Apple': 120, 'Mango': 280}

# Using lambda function

filtered = dict(filter(lambda item: item[1] > 100, product_prices.items()))
print(filtered) # {'Apple': 120, 'Mango': 280}

# 7.	Write a function that accepts any number of inputs and returns their average

def average(*args):
    try:
        return sum(args)/len(args)
    except ZeroDivisionError:
        print("Atleast one input number is needed")
        
average()
average(10)
average(10, 20)
average(10, 20, 30)

# 8. From this list, Collect the names of only the CSV files in a new list. 

files = ["report.csv", "data.xlsx", "summary.docx", "sales.csv"]

# Using list comprehension (efficient way)

csv_files = [file for file in files if file.endswith('csv')]
print(csv_files) # ['report.csv', 'sales.csv']

# Using loop

csv_files = []

for file in files:
    if file.endswith('csv'):
        csv_files.append(file)
        
print(csv_files) # ['report.csv', 'sales.csv']

# 9. Prepare the file names for display by removing the prefix and 
# showing only the unique part.

files = ["Report_Sales.xlsx", "Report_Inventory.xlsx", "Report_Expenses.xlsx"]

# To print new names
for file in files:
    print(file.removeprefix("Report_"))
    
# To save in a list
new_names = [file.removeprefix("Report_") for file in files]
print(new_names) # ['Sales.xlsx', 'Inventory.xlsx', 'Expenses.xlsx']


# 10. To detect if a certain field is filled with repeated characters

def all_chars_same(s):
    return len(set(s)) == 1

print(all_chars_same("aaaaaa"))   # True
print(all_chars_same("123456"))   # False
print(all_chars_same("111116"))   # False

# Using lambda function
all_chars_same = lambda s: len(set(s)) == 1

print(all_chars_same("aaaaaa"))   # True
print(all_chars_same("123456"))   # False
print(all_chars_same("111116"))   # False


# 11. for this url list, You need to extract the profile name from each URL.

urls = [
    'https://www.linkedin.com/in/nishaarora/',
    'https://www.linkedin.com/in/johndoe/',
    'https://www.linkedin.com/in/pragyasharma/'
]

profile_names = [url.split('/')[-2] for url in urls]
print(profile_names) # ['nishaarora', 'johndoe', 'pragyasharma']

# 12. Calculate the total amount spent by each customer

transactions = [
    {"customer": "Alice", "product": "Laptop", "amount": 1200},
    {"customer": "Bob", "product": "Mouse", "amount": 25},
    {"customer": "Alice", "product": "Headphones", "amount": 150},
    {"customer": "Bob", "product": "Keyboard", "amount": 75},
    {"customer": "Charlie", "product": "Monitor", "amount": 300},
]

total = 0
for tr in transactions:
    for k, v in tr.items():
        if k == 'amount':
            total += v
        
print(total)

# 13. Calculate the current portfolio value 

portfolio = {
    "AAPL": {"shares": 10, "price": 165.3},
    "GOOGL": {"shares": 5, "price": 2800.5},
    "TSLA": {"shares": 8, "price": 190.1}
}

     
total_value = 0

for stock, data in portfolio.items():
    stock_value = data["shares"] * data["price"]
    print(f"{stock}: ${stock_value:.2f}")
    total_value += stock_value

print(f"\nTotal Portfolio Value: ${total_value:.2f}")

# ____________________All The Best !_______________________