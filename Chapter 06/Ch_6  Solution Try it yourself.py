# Questions 1 and 2:
    # Do these yourselves
    
    
# Question 3: Project_ Business insights from superstore data

import pandas as pd
import os

os.getcwd() # Excel_Python folder created for the book

# As we will be reading  files from Data folder inside Excel_Python
# Setting working directory to Data Folder

data_path = os.path.join(os.getcwd(), 'Data')  # Data folder inside Excel_Python folder
os.chdir(data_path)

df = pd.read_csv('Sample - Superstore.csv', 
                 encoding="latin1")

df.to_csv("output.csv", index=False)

# df.to_csv("output.csv", index=False, encoding="utf-8-sig")

df = pd.read_csv('output.csv') # UnicodeDecodeError:

# Part 1: Basic inspection -------------

df.info()
df.isnull().sum()  # Check missing values
df.isnull().sum().sum()
print(f'Number of missing values in the data: {df.isnull().sum().sum()}')

# Display the first 5 rows
df.head()

# Check the time range of the data (Earliest and Latest Order Dates)
df['Order Date'] = pd.to_datetime(df['Order Date']).dt.date  # Convert Order Date to datetime format
df['Ship Date'] = pd.to_datetime(df['Ship Date']).dt.date  # Convert Ship Date to datetime format

# the time range of the data 
# Find earliest and latest order dates
earliest_order = df['Order Date'].min()
latest_order = df['Order Date'].max()

print(f"Earliest Order Date: {earliest_order}")
print(f"Latest Order Date: {latest_order}")

print(f'Time range of order dates: {(latest_order - earliest_order).days}')

# Part 2: Sales Overview ---------------------

# Total Sales and Total Profit
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print(f"Total Sales: {total_sales}")
print(f"Total Profit: {total_profit}")

# Region-wise total Sales and highest average Profit per order
region_sales = df.groupby("Region")["Sales"].sum()
region_profit_avg = df.groupby("Region")["Profit"].mean()

print(region_sales)
print(f'Region with highest sales: {region_sales.idxmax()}')

print(region_profit_avg)
print(f'Region with highest average profit: {region_profit_avg.idxmax()}')

# Total Sales and average Discount per Product Category
category_sales = df.groupby("Category")["Sales"].sum()
category_discount_avg = df.groupby("Category")["Discount"].mean()

print(f'Total sales for each product category :\n\n {category_sales}')
print(f'Total average discount for each product category :\n\n {category_discount_avg}')


# Part 3: Customer Insights ---------------------------

# Unique Customers
unique_customers = df["Customer ID"].nunique()
print(f"Total Unique Customers: {unique_customers}")

# Top 3 Customers by Sales
top_customers = (
    df.groupby('Customer Name')['Sales']
      .sum()
      .sort_values(ascending=False)
      .head(3)
)

# OR
top_customers = df.groupby("Customer Name")["Sales"].sum().nlargest(3)
print(top_customers)

print(f'Three customers brought in the highest total sales are: \n\n{list(top_customers.index)}')


# Average Order Value (AOV) per Customer
# Total Sales / Number of Orders (Order ID is order identifier)
aov_per_customer = (
    df.groupby('Customer Name')
      .agg(total_sales=('Sales', 'sum'), num_orders=('Order ID', 'nunique'))
)

aov_per_customer['AOV'] = aov_per_customer['total_sales'] / aov_per_customer['num_orders']
print("\nAverage Order Value (AOV) per Customer:")
print(aov_per_customer[['AOV']].sort_values('AOV', ascending=False).head())

#  OR
aov_per_customer = df.groupby("Customer Name")["Sales"].sum() / df.groupby("Customer Name")["Order ID"].count()
print(aov_per_customer.head())

# Part 4: Product Performance ---------------------------

# Sub-Category with highest total Sales and Profit
sub_category_sales = df.groupby("Sub-Category")["Sales"].sum()
sub_category_profit = df.groupby("Sub-Category")["Profit"].sum()

highest_sales_subcat = sub_category_sales.idxmax()
highest_profit_subcat = sub_category_profit.idxmax()

print(f"Highest Sales Sub-Category: {highest_sales_subcat}")
print(f"Highest Profit Sub-Category: {highest_profit_subcat}")

# Top 3 Most Profitable Products
top_profitable_products = df.groupby("Product Name")["Profit"].sum().nlargest(3)
print(top_profitable_products)

# Best-selling Sub-Category per Region

best_subcat_per_region = (
    df.groupby(['Region', 'Sub-Category'])['Sales']
      .sum()
      .reset_index()
      .sort_values(['Region', 'Sales'], ascending=[True, False])
      .groupby('Region')
      .first()
)
print("\nBest-selling Sub-Category per Region:")
print(best_subcat_per_region)


# OR

best_selling_per_region = df.groupby(["Region", "Sub-Category"])["Sales"].sum().groupby("Region").idxmax()
print(best_selling_per_region)


# Part 5: Shipping Efficiency -------------------
# Average delivery time (days between Order Date and Ship Date)
df["Delivery Time"] = (df["Ship Date"] - df["Order Date"]).dt.days
avg_delivery_time = df["Delivery Time"].mean()
print(f"Average Delivery Time: {avg_delivery_time:.2f} days")

# Region with fastest average shipping time
fastest_shipping_region = df.groupby("Region")["Delivery Time"].mean().idxmin()
print(f"Region with Fastest Shipping Time: {fastest_shipping_region}")


# Clean column names (for ease), we could do _ optional 
df.rename(columns={'Sub-Category': 'SubCategory', 'Product Name': 'Product'}, inplace=True)

# Part 6: Data-driven recommendations -------------------

# Do it yourself