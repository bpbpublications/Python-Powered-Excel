import os
import pandas as pd
pd.__version__ 

os.getcwd() # Excel_Python folder created for the book

# As we will be reading multiple files from Data folder inside Excel_Python
# Setting working directory to Data Folder

data_path = os.path.join(os.getcwd(), 'Data')  # Data folder inside Excel_Python folder
os.chdir(data_path)


df = pd.read_excel('finance_data.xlsx', 
                    na_values=['missing', '-'])

df.columns # Name of all columns

# Quick Ways to select column(s)  ------------------------------------

# To fetch a single column ------

df['amount'] # Recommended Way
type(df['amount']) # Series

df.amount # Works only when column name is without spaces or special characters

type(df.amount) # Series

df[['amount']] # Only when you need a dataframe
type(df[['amount']]) # Data Frame

# To fetch multiple columns ------

df[['client', 'amount']] # You will see this type of code, however recommended is to use df.loc[]
type(df[['client', 'amount']]) # Data Frame

# Selecting data based on data type ----------------------------------

df.dtypes

# Select all numeric (int or float) columns 
df.select_dtypes('number')
# To get column names of all numeric columns
df.select_dtypes('number').columns

# Select only integer-type columns (returns full DataFrame slice)
df.select_dtypes('int') # no columns
df.select_dtypes('int').columns

# Select only float-type columns 
df.select_dtypes('float')

# Get column names of float-type columns only
df.select_dtypes('float').columns

# Select datetime-type columns 
df.select_dtypes('datetime')

# Select category-type columns (if any column was explicitly set as category)
df.select_dtypes('category')

# String data type
df.select_dtypes('str').columns

# for backward compatibility (in pandas 3.0.0), columns with the new string dtype are currently treated as object when you call select_dtypes('object'). This behavior is deprecated and will be removed in a future release.
# As older versions of pandas, treat text columns also as 'object' data type

# Select object-type columns (ideally, mixed data type)
df.select_dtypes('object')

# 'O' is shorthand for object type (same as above)
df.select_dtypes('O')

# select legacy object and new string dtypes
df.select_dtypes(['object','str'])

# To include or exclude specific data types

# Select all numeric columns (both int and float)
df.select_dtypes(include='number')

# Select all non-numeric columns (object, datetime, category, etc.)
df.select_dtypes(exclude='number')


# Popular and Preferred way to select data -----------------------------

# df.loc[row_index/name/condition, column_name]

df.loc[0] # 1st row, all columns
df.loc[0, :] # 1st row, all columns RECOMMNDED

# df.loc[0, ] # ValueError in pandas 3.0.0

# NOTE: Always prefer df.loc[row, :] for clarity and consistency, 
# even if simpler forms seem to work.

type(df.loc[0]) # series
type(df.loc[0, :]) # series

df.loc[[0], :] # 1st row, all columns WHEN you need a data frame
type(df.loc[[0], :]) # dataframe

df.loc[0, 'client'] # 1st row, client col
df.loc[:, 'client']  # all the rows, client col
type(df.loc[:, 'client']) # Series 

df.loc[:, ['client']] # all the rows, client col
type(df.loc[:, ['client']]) # DataFrame

df.loc[:, ['client', 'region', 'approved']] # all the rows, multiple columns
df.loc[:, 'client' : 'region'] # all the rows, consecutive columns
# NOTE: including 'region' column

# NOTE: with df.loc, slicing : includes the upper end.
df.loc[[0, 2], :] # multiple rows, all columns 
df.loc[0:2, :] # consecutive rows, all columns

# Data with index column

df_index = pd.read_excel('finance_data.xlsx', 
                   na_values='missing',
                   index_col = 'txn_id')

df_index.loc['T001'] # Works but avoid
# df.loc['T001', ] # ValueError

df_index.loc['T001', :] # row with txn_id T001
df_index.loc['T002', 'client'] # row with txn_id T001, client col
df_index.loc[['T001', 'T002'], 'client'] # multiple rows, one column
df_index.loc[['T001', 'T002'], :] # multiple rows, all columns


# Selecting colummns based on names/conditions ---------

# RECOMMNEDED way is to use df.loc for condition based filtering
# Transactions with amount greater than 1000

df.loc[df['amount'] > 1000] # Works but avoid

df.loc[df['amount'] > 1000, :] # Recommended way


# Approved transactions
df.loc[df['approved'] == 1]

# amount greater than 1000 and approved transactions
df.loc[(df['amount'] > 1000) & (df['approved'] == 1)]

# Or
cond1 = df['approved'] == 1
cond2 = df['amount'] > 1000
# Approved transactions with amount > 1000
df.loc[cond1 & cond2]

# To fetch only txn_id and client columns
# for approved transactions with amount > 1000
df.loc[cond1 & cond2, ['client', 'amount']]

# For simple condition based filtering, you can use df[condition directly]
# however, preffered way is to use df.loc[condition]

# Here are same examples without explicitly using .loc -------

# selecting rows by condition
# Transactions with amount greater than 1000
df[df['amount'] > 1000]

# Approved transactions
df[df['approved'] == 1]

# amount greater than 1000 and approved transactions
df[(df['amount'] > 1000) & (df['approved'] == 1)]

# Or
cond1 = df['approved'] == 1
cond2 = df['amount'] > 1000
# Approved transactions with amount > 1000, show txn_id and client
df[cond1 & cond2]

# To fetch only txn_id and client columns
# for approved transactions with amount > 1000
df[cond1 & cond2].iloc[:, [0,2]] # Not elegent, right?

# To fetch rows based on row/col index -----------------

# Not very frequently, but sometimes you might want to fetch data using row/col index
# To select data by column index, you need df.iloc[], here, i stands for index

df.iloc[0] # first row
df.iloc[0:3] # first, second, third row
# Note: it skips index '3', i.e., 4th row

df.iloc[ :3] #upto row-index '2', i.e., third row 

df.iloc[[0, 1, 7]] # first, second, eight row

df.iloc[-1] #last row
# df.iloc[-2] #second last row

# To fetch rows and columns based on index

df.iloc[2, 1] # third row, second column
df.iloc[:, 1]
df.iloc[0:3, 0] # first, second, third row_first column

df.iloc[:5, 0:4] # first 5 rows, first 4 columns
# df.iloc[:5, -1] # first 5 rows, last column

# First, select rows using iloc
df.iloc[[1, 3], [2, 4]]


df.iloc[:5]['amount'] # first 5 rows, amount
df.iloc[:5][['client', 'amount']] # first 5 rows, amount
# same as
df[['client', 'amount']].head()

df.iloc[lambda x: x.index % 2 == 0]


# Delete rows/columns/both ---------------------------
df.shape 
df.columns

# To delete column(s)
df.drop('amount', axis = 1) # Need to write axis = 1

# df.drop('amount') # Will throw error
# KeyError: "['amount'] not found in axis"

df.drop('amount', axis = 1).shape # one less column
df.drop(['amount', 'txn_date'], axis = 1) # drop these columns

# drop row(s)
df.drop(0) # index 0/first row removed
df.drop(0, axis = 0) # same output
df.drop([0, 13, 14]) # drop row indexed 0, 13, 14

df_index.drop('T001')
df_index.drop(['T001', 'T002'])

# drop rows and columns
df.drop(index = 0, columns = 'txn_date')
df.drop(index = 0, columns = 'txn_date', axis = None)

# when index and columns both are supplied to df.drop(),
# pandas interprets it as “use whatever axis applies” 
# based on provided parameters.

df.drop(index = [0, 1], 
        columns = ['txn_date', 'client'])


# Replicating COUNT, COUNTIF, COUNTIFS, SUMIF, SUMIFS ---------------------

# Total number of transactions -> COUNT in Excel
total_txns = df['txn_id'].count() 
print(total_txns)

# Count where 'approved' == 1
approved_count = (df['approved'] == 1).sum()
print(approved_count)

# Alternatively, you can use count
approved_count = df[df['approved'] == 1]['approved'].count()

# NOTE: count() ignores missing values
df.loc[df['approved'] == 1, 'amount'].count() # so the count drops

# Count where approved == 1 and amount > 1000
approved_high_value = ((df['approved'] == 1) & (df['amount'] > 1000)).sum()
print(approved_high_value)


# Sum amounts for approved transactions
sum_approved = df.loc[df['approved'] == 1, 'amount'].sum()
print(sum_approved)


# Sum amounts for approved transactions in 'East' region
sum_approved_east = df.loc[(df['approved'] == 1) & (df['region'] == 'East'), 'amount'].sum()
print(sum_approved_east)

# Advanced Query -------------------------------

# Advanced and elegant way to select data using df.query()===============================
# not needed for simple indexing tasks

df.query("approved == True")

# cleaner/more readable than df[df["approved"] == True] 

df.query("approved == True and region == 'South'")
region = 'East'
df.query("approved == True and region == @region")

# Filter rows where revenue > 100000 and region is 'North'

df.query("amount > 1000")
df.query("amount > 1000 and region == 'South'")

df.query("approved == True and region == 'South'")

# Use variable inside query
region = 'East'
df.query("approved == True and region == @region")

# threshold = 1500
threshold = float(input('Enter Min Amount: '))
df.query("amount > @threshold")
 
# Filter rows where region is in a list
df.query("region in ['East', 'North']")

# Rows where amount is between 1000 and 1500
df.query("amount.between(1000, 1500)")

# Multiple clients with OR condition
df.query("client in ['Alice', 'Bob', 'Charlie']")

# Transactions in a date range
df['txn_date'] = pd.to_datetime(df['txn_date'], errors='coerce' )  # Ensure txn_date is datetime
df.query("txn_date >= '2024-01-20' and txn_date <= '2024-01-25'")

df.query("'2024-01-20' <= txn_date <= '2024-01-25'")

# Variable dates

start_date = pd.Timestamp('2024-01-20')
end_date = pd.Timestamp('2024-01-25')

df.query("txn_date >= @start_date and txn_date <= @end_date")

# Using df.filter() -----------------------------------

# It selects rows or columns based on labels, not values.

# Select columns by exact column names
df.filter(items=['client', 'amount'])

# Select columns containing a pattern (like Excel wildcard *)
df.filter(like='txn')

# Select columns starting with a string
df.filter(regex='^txn_')

# It is useful in dynamic selection in wide datasets
    
# Select rows by index labels
df.filter(items=[0, 2], axis=0) 