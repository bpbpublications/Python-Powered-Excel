import os

chapter_directory = os.path.join(os.getcwd(), 'Chapter 05')
os.chdir(chapter_directory)

# os module is imported for changing working directory
# you don't need to import it for using open() method

# Reading and writing files using open() method ------------

# Reading a text file 
with open('sample_1.txt', 'r') as file:
    content = file.read()
print(content)

# Writing to a text file 
with open('sample_2.txt', 'w') as file:
    file.write('Hello, I am learning Python')

# Reading a csv file
with open("sample_3.csv", "r") as file:
    content = file.read()  # Works fine
print(content)

# Writing a CSV file 
with open("sample_4.csv", "w") as file:
    file.write("Date,Product,Quantity,Revenue\n")  # Header row
    file.write("2024-04-01,Laptop,5,5000\n")
    file.write("2024-04-02,Mouse,15,300\n")
    file.write("2024-04-03,Keyboard,10,500\n")

print("CSV file created successfully.")


# You can also Use csv module to read/write csv file -----------

import csv

# Reading csv files

# Reading a CSV file using a context manager
with open('sample_3.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Sample sales data
sales_data = [
    ["Date", "Product", "Quantity", "Revenue"],
    ["2024-04-01", "Laptop", 5, 5000],
    ["2024-04-02", "Mouse", 15, 300],
    ["2024-04-03", "Keyboard", 10, 500],
]

# Writing to a CSV file
with open("sales_report.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sales_data)
print("Sales report saved as 'sales_report.csv'")

# Writing JSON file using json module ---------------------

import json

data = {"name": "Alice", "age": 25}

with open("sample_5.json", "w") as f:
    json.dump(data, f)

# Reading JSON data from JSON file
with open("sample_5.json", "r") as f:
    loaded_data = json.load(f)
print(loaded_data)

# Writing HTML
html_content = "<html><body><h1>Hello, World!</h1></body></html>"
with open("index.html", "w") as f:
    f.write(html_content)

# Reading HTML
with open("index.html", "r") as f:
    html_data = f.read()
print(html_data)

# Writing XML
xml_content = "<root><user>Alice</user></root>"
with open("data.xml", "w") as f:
    f.write(xml_content)

# Reading XML
with open("data.xml", "r") as f:
    xml_data = f.read()
print(xml_data)

# For more, refer: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files