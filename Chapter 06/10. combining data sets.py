import os
import pandas as pd

os.getcwd() # Excel_Python folder created for the book

# As we will be reading files from Data folder inside Excel_Python
# Setting working directory to Data Folder

data_path = os.path.join(os.getcwd(), 'Data')  # Data folder inside Excel_Python folder
os.chdir(data_path)

customers = pd.read_excel('demo_sales.xlsx', sheet_name='Customers')
orders = pd.read_excel('demo_sales.xlsx', sheet_name='Orders')
products = pd.read_excel('demo_sales.xlsx', sheet_name='Products')
sales_jan = pd.read_excel('demo_sales.xlsx', sheet_name='Sales_Jan')
sales_feb = pd.read_excel('demo_sales.xlsx', sheet_name='Sales_Feb')

# Appending ---------------------

sales_jan_feb  = pd.concat([sales_jan, sales_feb])
print(sales_jan_feb) # Both tables are stacked one below the other (like Append in Excel)

sales_jan_feb = pd.concat([sales_jan, sales_feb], 
                          ignore_index = True)
print(sales_jan_feb) 


# using axis = 1 simply stitches columns together by index → there’s no matching logic
# To get meaningful joins, use merge() when adding tables side by si
pd.concat([orders, customers], axis = 1)

# NOTE: df.append() is a special case of pd.concat() and is deprecated


# Inner Join (Keep matching rows only)_ Like Excel's XLOOKUP or VLOOKUP
# Orders with Customer Names

merged_inner = pd.merge(orders, customers, 
                        on='CustomerID', 
                        how='inner')
print(merged_inner) # Only Orders where CustomerID exists in both tables are kept.

# Left Join (Keep all Orders, even if no customer info)
# all Orders — if Customer is missing, leave blank

merged_left = pd.merge(orders, customers, 
                       on='CustomerID', 
                       how='left')
print(merged_left) #All Orders are kept. If Customer info is missing (like C005), we get NaN (like Excel's #N/A)

# Right Join (Keep all Customers, even if no orders)** — Rare, mention briefly
# All Customers — even if they didn’t order


merged_right = pd.merge(orders, customers, 
                        on='CustomerID', 
                        how='right')
# (You won’t need this often. Usually Left Join covers most cases.)
merged_right

# Outer Join (Keep everything, show gaps)
# "Give me everything — all orders and all customers"

merged_outer = pd.merge(orders, customers, 
                        on='CustomerID', 
                        how='outer')
# (Rare. Useful if you’re auditing mismatches between lists.)
merged_outer

merged_cross = pd.merge(orders, customers,  
         how='cross')
merged_cross
# Although rare, but might be useful for theoretical scenarios like mapping potential product recommendations for each customer.