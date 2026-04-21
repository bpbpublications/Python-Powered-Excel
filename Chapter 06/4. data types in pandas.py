import os
import pandas as pd

os.getcwd() # Excel_Python folder created for the book

# As we will be reading files from Data folder inside Excel_Python
# Setting working directory to Data Folder

data_path = os.path.join(os.getcwd(), 'Data')  # Data folder inside Excel_Python folder
os.chdir(data_path)

# Understanding Data Types ----------------------------------

# NOTE: Slight changes in how .info(), .dtypes and some outputs 
# are displayed in pandas < 3.0.0

users = {'name': ['Alice', 'Merry', 'Charvie'],
         'tool': ['Excel', 'R', 'Python'],
         'experience': [10, 15, 14]}

df = pd.DataFrame(users); df
df.info()

# adding a column with mixed data types
df['salary'] = [50, 'not revealed', 90 ] 
df['salary'].dtypes
df.info()

df['gender'] = pd.Categorical(['Male', 'Female', 'Female'])

df['hire_date'] = pd.to_datetime(['2023-01-01', '2024-05-15', '2025-07-15'])

df['training_duration'] = pd.to_timedelta([5, 10, 15], unit='D') 
df.info()

# Let's work with finance data --------------------------------

# To change data types while reading the data -----------------

df = pd.read_excel('finance_data.xlsx')
df.info() # Here, all columns are stored as 'object' data type
# memory usage: 948.0+ bytes
df.dtypes

# while reading data, assigning 'region' column as 'category' data type
#  You can use  dtype argument to define data type of 1 or more column(s)
df = pd.read_excel('finance_data.xlsx', 
                   dtype={'region': 'category'})
df.dtypes
df.info()

# memory usage: memory usage: 1.0+ KB
# Converting object data to categorical typically reduces memory usage, 
# though with very few categories it may increase it.  
# Read here: https://www.linkedin.com/posts/drnishaarora_pandas-learn-python-activity-7336638320438837248-56A0?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAepsJkBv8opllaFHDwGtRtHUfsaCud-TdQ

# Read the Excel file again by defining amount column as float data type

df = pd.read_excel('finance_data.xlsx', 
                   dtype={'amount': 'float64'})

# ValueError: Unable to convert column amount to type float64 (sheet: 0)

# Can not convert to float, printing column tells us about the issue
df['amount']

# it has some text values ('missing')

# Also, 'txn_date' column as some text value ('missing')
df['txn_date']

# We can tell python to treat this specific text as na value by using na_values argument

df = pd.read_excel('finance_data.xlsx', 
                    na_values='missing')
df.dtypes

# Now, it reads columns more accurately,
# 'txn_date' is treated as datetime column and
# 'amount' is treated as a float column

# Also 'approved' column (True/False) is stored as 'object' data type 

df['approved']

# it has missing values and text value as '-'

df = pd.read_excel('finance_data.xlsx', 
                    na_values=['missing', '-'])
df.dtypes

# If we define '-' as missing value, python treats this column as 
# 'float' data type and converts True/False to 1/0 
# Because NaN is fundamentally a float concept. 
# You cannot have NaN in a pure boolean array as booleans can only be True or False


df = pd.read_excel('finance_data.xlsx')
df.dtypes

df = pd.read_excel('finance_data.xlsx',
                   parse_dates = True)

print(df['txn_date'].head(10))
print(df['txn_date'].apply(type).value_counts())

# - parse_dates automatically converts specified columns into datetime64[ns] objects.
# - Can accept list of column names, dict mapping or boolean(True/False) 
# - Mixed formats often cause the column to remain object dtype.

# - Custom parsing is possible with date_parser (e.g., dayfirst=True).
# - Performance overhead: parsing dates inline can slow down large imports.
# - Engine differences (openpyxl vs xlrd) may slightly affect behavior
# - parse_dates=True does not force conversion; it only attempts.

df = pd.read_excel('finance_data.xlsx',
                   parse_dates = ['txn_date'])
df.dtypes
print(df['txn_date'].head(10))

df = pd.read_excel('finance_data.xlsx',
                   parse_dates = ['txn_date'], na_values='missing')
df.dtypes
print(df['txn_date'].head(10))


# To change data type after reading the data ---------------------------

# When you are not sure of appropriate data types upfront, you can read data as is
# and convert data type of column(s) as needed later

# For numeric or date-time conversions, pd.to_numeric() and pd.to_datetime() can be used.
# These functions will allows us to use an argument errors='coerce', 
# with invalid values becoming NaN.

df = pd.read_excel('finance_data.xlsx')
df.dtypes

# pd.to_numeric(df['amount']) # ValueError as expected due to invalid value

df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# Simmilarly
df['txn_date'] = pd.to_datetime(df['txn_date'], errors='coerce')


df.info() # memory usage: 948.0+ bytes

# For converting to category types 

df['region'] = df['region'].astype('category') 
df.info() # memory usage: 861.0+ bytes

df['region'].unique()
df['region'].value_counts()


# If there are no missing or invalid values, you can change data type of other columns to datetime, int, float etc

# Convert multiple columns to numeric

# Sample DataFrame
data1 = pd.DataFrame({
    'col1': ['10', '20', '30'],
    'col2': ['100.5', '200.8', '300.1'],
    'col3': ['invalid', '50', '60']  # Contains a non-numeric value
})

data1.dtypes

# Convert multiple columns to numeric, forcing errors to NaN

data1 = data1.apply(pd.to_numeric, errors='coerce')

data1.dtypes

# Convert multiple columns to datetime

# Sample DataFrame
data2 = pd.DataFrame({
    'start_date': ['2023-06-01', '2023-06-02', '2023-06-03'],
    'end_date': ['2023-06-10', '2023-06-11', '2023-06-12']
})

data2.dtypes

# Convert multiple columns to datetime

data2 = data2.apply(pd.to_datetime, errors='coerce')
data2.dtypes

# Converting multiple columns in one go

data3 = pd.DataFrame({
    "price":    [100, 200, "abc", 400],   # numeric (with 1 bad value)
    "quantity": [10, 20, 30,  "xyz"],   # numeric (with 1 bad value)
    "order_date":  ["2024-01-15", "2024-02-20", "not-a-date", "2024-04-10"],  # datetime (with 1 bad value)
    "ship_date":   ["2024-01-20", "2024-02-25", "2024-03-30", "2024-04-15"],  # datetime
    "product_category": ["Electronics", "Clothing", "Electronics", "Clothing"],       # category
    "region":   ["North", "South", "East", "West"],                           # category
    })

data3.dtypes


# All in one go using assign()
data3 = data3.assign(
    price            = pd.to_numeric(data3["price"], errors="coerce"),      
    quantity         = pd.to_numeric(data3["quantity"], errors="coerce"),   
    order_date       = pd.to_datetime(data3["order_date"], errors="coerce"),
    ship_date        = pd.to_datetime(data3["ship_date"], errors="coerce"),
    product_category = data3["product_category"].astype("category"),
    region           = data3["region"].astype("category")
)

# Or using apply() method

numeric_cols  = ["price", "quantity"]
datetime_cols = ["order_date", "ship_date"]
category_cols = ["product_category", "region"]

data3[numeric_cols]  = data3[numeric_cols].apply(pd.to_numeric, errors="coerce")
data3[datetime_cols] = data3[datetime_cols].apply(pd.to_datetime, errors="coerce")
data3[category_cols] = data3[category_cols].astype("category")

print(data3.dtypes)