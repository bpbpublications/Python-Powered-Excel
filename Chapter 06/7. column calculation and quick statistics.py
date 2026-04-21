import os
import pandas as pd

os.getcwd() # Excel_Python folder created for the book

# As we will be reading files from Data folder inside Excel_Python
# Setting working directory to Data Folder

data_path = os.path.join(os.getcwd(), 'Data')  # Data folder inside Excel_Python folder
os.chdir(data_path)

# Example 

df = pd.read_excel('finance_data.xlsx', 
                   na_values=['missing', '-'])
df = df.head()
df_backup = df.copy()
df

# df['days_since_txn'] = pd.Timestamp.today() - df['txn_date']
df

# Column calculations 

df['fee'] = df['amount'] * 0.05 
df['net_amount'] = df['amount'] - df['fee']
df['cashback'] = df['approved'] * 100
# NaNs will be produced for missing values in the above operations


# or fill missing values before applying operation
df = df_backup.copy()

# Fill missing with 0 (temporarily) before calculation
df['fee'] = df['amount'].fillna(0) * 0.05  
df['net_amount'] = df['amount'].fillna(0) - df['fee']

# That line creates a `'fee'` column by replacing `NaN` values in `'amount'`
 # with 0 temporarily and multiplying the result by 0.05. 
 # It doesn’t alter the original `'amount'` column.


# Better way
df = df_backup.copy()
df['fee'] = df['amount'].mul(0.05, fill_value = 0)
df['net_amount'] = df['amount'].sub(df['fee'], fill_value = 0)
df['cashback'] = df['approved'].mul(100, fill_value = 0)
df

df['amount'] += 50
df['amount']

# Example with Pandas Series ----------------------

# Example _1

A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])

print(A)
print(B)
print(A + B)  # Shows all rows and fills NA where values are not found

A.add(B, fill_value=0) 

# Example _2
area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                  'California': 423967}, name='area')
area

population = pd.Series({'California': 38332521, 'Texas': 26448193,
                        'New York': 19651127}, name='population')
population

population / area

population.div(area, fill_value= 1) # may not make sense, just showing .div() method

area.index.intersection(population.index)

# Example _3

s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20], index=['b', 'c'])

s1 + s2                   # returns NaN where index is missing
s1.add(s2)                # returns NaN where index is missing
s1.add(s2, fill_value=0)  # fills missing values before adding


# Common mathematical functions -------------------

df['amount'].min()
df['amount'].max()
df['amount'].mean()
df['amount'].median()
df['amount'].sum()

# Advanced Functions ------------------------------

# df.assign() to create multiple columns dynamically 
# without modifying the original table ----------

# Best for method chaining (with other methods df.pipe(), df.query()), 
# enhancing readability.

df.assign(fee = df.amount * 0.05)

# This can be done with lambda function as well
df.assign(fee = lambda x: x['amount'] * 0.05)

# In pandas 3.0.0, pd.col() introduced
df.assign(fee=pd.col('amount') * 0.05)  

# Let us see when using lambda functions becomes important

# To create multiple columns at once

# The following code will not work # SEE FROM HERE
# AttributeError: 'DataFrame' object has no attribute 'fee'
df.assign(fee = df.amount * 0.05, 
          tot_amount = df.amount + df.fee)

# Using lambda ensures 'fee' is recognized 
# before calculating 'tot_amount'

df.assign(fee = df.amount * 0.05, 
          tot_amount = lambda x: x.amount + x.fee)

df.assign(fee = lambda x: x.amount * 0.05, 
          tot_amount = lambda x: x.amount + x.fee)

# This WORKS with pd.col() _ a simplified alternative to lambda functions
df.assign(fee=pd.col('amount') * 0.05,
          tot_amount=pd.col('fee') + pd.col('amount')) 

# Chaining multiple methods together ---------------

# Using full data set for these examples

df_full = pd.read_excel('finance_data.xlsx', 
                   na_values=['missing', '-'])


# Creating 'net_amount' as 90% of 'amount', 
# filters for 'East' region, 
# then sorts by 'net_amount

df_full.assign(net_amount = df_full['amount'] * 0.9) \
                              .query("region == 'East'") \
                              .sort_values('net_amount', ascending=True)
                              
                              
# Using backslash
df_full.assign(net_amount = df_full['amount'] * 0.9) \
       .query("region == 'East'") \
       .sort_values('net_amount', ascending=True)

# Using parenthesis
(df_full.assign(net_amount = df_full['amount'] * 0.9)
        .query("region == 'East'")
        .sort_values('net_amount', ascending=True))
                              