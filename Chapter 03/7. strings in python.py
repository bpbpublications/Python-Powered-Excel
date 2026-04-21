# Strings in Python

# String Creation  ________________________________________________________
    
book = 'Python-Powered Excel'
book = "Python-Powered Excel"
print(book)
    
name = "Nisha Arora"; print(name)
address = '123, Lane Name, City'; print(address)

s1 ='"Python-Powered Excel" is the best book for learning Excel-Python integration.'; print(s1)
s2 = "Explanation in the book 'Python-Powered Excel' is simple, yet powerful and practical."; print(s2)

# Escape Sequence  -------------

s3 = "He said, \"Python-Powered Excel\" is a great book."; print(s3)    
s4 = 'It\'s a wonderful book for learning Excel-Python integration.'; print(s4)

using_tab = 'tool:\tPython'
print(using_tab)

using_new_line = 'tools:\nPython\nExcel'
print(using_new_line)


info = 'Book:\tPython-Powered Excel\nAuthor:\tDr Nisha Arora\nPublisher:\tBPB Publications'
print(info)

# Multi-line string  -------------

feedback = """I use Excel for my work. Learning python for Excel was the best decision, I've ever made. 
The book 'Python-Powered Excel' by Dr Arora made it simple, effective, and efficient."""
print(feedback)

# Essential String Operations _________________________________________________

# Length of the string  -------------

len('Nisha Arora')     

# Changing Case  -------------

text = "Hello, Excel Users!"
print(text.upper())      # HELLO, EXCEL USERS!
print(text.title())      # Hello, Excel Users!
print(text.lower())      # hello, excel users!
print(text.capitalize()) # Hello, excel users!

# Removing Extra Spaces -------------

text  = "  Learning Python is Fun!  "
print(text.strip()) # Removes both leading and trailing spaces
text.lstrip()       # Removes only leading (left) spaces
text.rstrip()       # Removes only trailing (right) spaces

# Replacing Character in a string/text -------------

text  = "Python is easy."
text.replace('easy', 'simple yet powerful')

sentence = "I love VBA"
print(sentence.replace("VBA", "Python"))  # I love Python
# Excel Equivalent: =SUBSTITUTE()

# Counting & Finding position of a character -------------

email = "user@example.com"
print(email.count("@"))  # 1
print(email.find("@"))   # 4 (index)

# Splitting String -------------

text = 'Python-Powered Excel'
print(text.split()) # ['Python-Powered', 'Excel']
print(text.split(sep='-')) # ['Python', 'Powered Excel']

text = 'Nisha Arora'
text.split() # Output is a list, can be further sliced
text.split()[0] # Nisha

# Validating Strings -------------

filename = "report.xlsx"
print(filename.endswith(".xlsx"))  # True
print(filename.startswith("report"))  # True

# Concatenating Strings using '+' operator -------------

folder = "C:/Documents"
filename = "report.xlsx"
path = folder + "/" + filename # 'C:/Documents/report.xlsx'
print(path)  # C:/Documents/report.xlsx

# Removing Prefix/Suffix -------------

name = "Ms Nisha Arora, PhD"
print(name.removeprefix("Ms "))   # Nisha Arora, PhD
print(name.removesuffix(", PhD")) # Ms Nisha Arora

# Great thing is you can chain together string methods
cleaned = name.removeprefix("Ms ").removesuffix(", PhD")
print(cleaned)              #  Nisha Arora


url = 'https://www.linkedin.com/in/drnishaarora/'
url.removeprefix('https://')
url.removesuffix('drnishaarora/')
url.removeprefix('https://').removesuffix('/drnishaarora/')

file_name = 'Python Powered Excel.pdf'
file_name.removesuffix('.pdf')

# '*' operator with strings performs repetition -------------

'Ram '*3

# Fetching Parts/Substrings of Strings_________________________________________

# String Indexing -------------
    
text = 'python'
text[0] # first character
text[3] # index 3, i.e., 4th character
text[-1] # last character
text[-2] # index 2 from the end, second last character

# Slicing -------------

name = "Microsoft Excel"
print(name[0:9])   # Microsoft (characters from 0 to 8)
print(name[:9])    # same as before as it starts from index ‘0’, if we don’t mention explicitly
print(name[10:])   # Excel (from index 10 to end)
print(name[-5:])   # Excel (from 5th last or index -5 till end)

# Strides -------------

print(name[0:9:2]) # output: Mcoot -> every alternate chracter from index 0 to 8
print(name[::2])   # McootEcl -> every alternate chracter
print(name[::-1])  # lecxE tfosorciM -> negative step reverses the string

# In Python, [::-1] is slicing syntax that means:
# Start from the end (-1 step), and Go backwards through the string

print(name[1::-1]) # 'iM' -> starts at index 1 ('i'), and Go backwards through the string 
print(name[3::-1]) # 'rciM' -> starts at index 3 ('r'), and Go backwards through the string
print(name[3::-2]) # 'ri' ->  starts at index 3 ('r'), and Go backwards through the string and print every alternate chracter

# Inserting variable or performing calculations inside the string _____________

# using f-string method ----------------

# Simple Calculation -------------
print(f'2+2 is {2+2}')

#Variable Inside String -------------

x = 10; y = 20
print(f'x is {x} and y is {y}')
print(f'Total of x and y: {x+y}')

book = "Python-Powered Excel"
author = 'Dr Nisha Arora'
print(f'The book {book} is written by {author}')

# Number Formatting inside String -------------
score_perc = 0.234551
print(f"Score {score_perc:.2%}")


# Variable and Formula inside String -------------
cl = 140; imp = 800
print(f"Clicks: {cl}, Impressions: {imp}") # Clicks: 140, Impressions: 800
print(f"Click Through Rate (CTR): {cl/imp:.2%}") # Click Through Rate (CTR): 17.50%

product_sold = 1568
product_price = 349.9999
product_sold * product_price
print(f"Total_Revenue: ${product_sold * product_price:,.2f}")


# Function inside String (You'll learn about functions very soon!) -----------
def format_currency(value):
    return f"${value:,.2f}"

total_sales = 15400.75
print(f"Total Sales: {format_currency(total_sales)}")
# Output: Total Sales: $15,400.75

# NOTE: Strings are IMMUTABLE ________________________________________________

text = "Hello, Excel Users!"
print(text.upper())      # HELLO, EXCEL USERS!
print(text)              # Hello, Excel Users! -> 'text' does not change

text = "I love Python"
new_text = text.replace('Python', 'Excel')
print(new_text)   # I love Excel
print(text)       # I love Python -> 'text' does not change

name = 'reena'
name[0] = 't' # Error: 'str' object does not support item assignment

new_name = 't' + name[1:]
new_name    

# Simple Use-Cases ____________________________________________________________
    
# You might not understand some of the examples completely yet
# However, I would recommend you to do these exercises in Both Excel 
# and Python using the code given below

# While Excel 365 has caught up in many ways, Python still has several text/strings features 
# that go far beyond what Excel can offer — both in terms of flexibility, dynamic handling, and logic-building capabilities.
# Python is a GAME CHANGER for dealing with text/strings. Let's see how

# Build file paths or names -------------
# (will help you in automating file management; chapter 5)

month = "March"
year = 2025
filename = f"Sales_Report_{month}_{year}.xlsx"
print(filename) # Sales_Report_March_2025.xlsx
    
    
# Extracting the domain from an email address -------------
email = "nisha.arora@university.edu"
domain = email.split("@")[1]
print(domain)  # Output: university.edu

# Clean moile number data to remove country code -------------
Mobile_num = "+91-9876543210"
without_country_code = Mobile_num.removeprefix("+91-")
print(without_country_code ) 
    
# Fetching the profile name from a LinkedIn profile URL -------------
url = 'https://www.linkedin.com/in/drnishaarora/'
len('https://www.linkedin.com/in/') # 28
url[28:]
profile_name = url[len('https://www.linkedin.com/in/'):]
print(profile_name)  # Output: drnishaarora

url = "https://www.linkedin.com/in/drnishaarora/"
profile = url.rstrip("/").split("/")[-1]   # Strips trailing slash, splits URL, and gets the last segment
print(profile)  # Output: drnishaarora
url.split("/")[-2] # same result

# Extracting and Reporting a File Extension -------------
filename = "report_Q1.xlsx"
ext = filename.split(".")[-1]              # Splits the filename by '.' and gets the extension
print(f"The file extension is: {ext}")      # Output: The file extension is: xlsx

# String Cleaning Tasks -------------  

text = "  Error: User not found!  "
cleaned = text.strip().lower().replace("error: ", "")  # 'user not found!'
print(cleaned)

text = "   TOTAL: 500   "
cleaned = text.strip().removeprefix("TOTAL: ")
print(cleaned)  # '500'

# Standardizing Phone Numbers -------------  

phone = "(123) 456-7890"
cleaned = phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")  # '1234567890'
print(cleaned)
# Excel can do this, but it's tedious and error-prone when chaining more transformations.

# Dynamic String Formatting -------------  

name = "Alice"
sales = 3500
print(f"{name} closed sales worth ${sales:,} this quarter.")  
# Output: Alice closed sales worth $3,500 this quarter.

# Flexible Splitting & Rejoining -------------  
# You'll learn about lists in the in next section (same chapter)

sentence = "Data|Analytics|Python|Excel"
sentence.split("|") # list
parts = sentence.split("|")[1:-1]
parts
print("-".join(parts))  # 'Analytics-Python'

# Conditionally Modify Strings  -------------  
# You'll learn conditions soon in the same chapter

desc = "Limited Offer"
if "offer" in desc.lower():
    print("✓ Mark as promotional")
    
# List Comprehension with Strings  -------------
# to quickly apply transformations over multiple strings  
# You'll learn about list comprehension in the same chapter

names = ["Alice ", " Bob", "charlie"]
cleaned = [name.strip().title() for name in names]
print(cleaned)  # ['Alice', 'Bob', 'Charlie']

# Encoding/Decoding, Byte Strings  -------------

# You can work with encodings (UTF-8, ASCII, etc.) — useful for reading/writing files.
# Verify here: https://www.browserling.com/tools/utf8-encode
text = "Café"
encoded = text.encode('utf-8')
print(encoded)  # b'Caf\xc3\xa9'

# Handling Large Text Data  -------------
# (You will learn control flow in the same chapter and reading files using open() method in chapter 5)
# With Python, you can manipulate thousands of lines of text efficiently.

with open("log.txt") as f:
    for line in f:
        if "ERROR" in line:
            print(line.split("-")[1].strip())  


with open("log.txt") as f:
    errors = [line for line in f if "ERROR" in line]
    print(errors)

# Excel Limitation:
#     Excel 2019/365 can handle ~1,048,576 rows max.
#     But all rows + heavy string manipulation — will lag or crash.

# string interpolation: https://www.linkedin.com/posts/drnishaarora_pep-498-literal-string-interpolation-activity-7024232686038761472-f81n?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAepsJkBv8opllaFHDwGtRtHUfsaCud-TdQ
# string format method: https://www.linkedin.com/posts/drnishaarora_python-supports-multiple-ways-to-format-text-activity-7023507396652142592-zurQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAepsJkBv8opllaFHDwGtRtHUfsaCud-TdQ
# f strings: https://www.linkedin.com/posts/drnishaarora_an-f-string-or-formatted-string-literal-activity-7024956964254224384-sh5q?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAepsJkBv8opllaFHDwGtRtHUfsaCud-TdQ