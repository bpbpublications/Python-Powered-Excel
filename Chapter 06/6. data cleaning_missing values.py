import os
import pandas as pd

os.getcwd() # Excel_Python folder created for the book

# As we will be reading  files from Data folder inside Excel_Python
# Setting working directory to Data Folder

data_path = os.path.join(os.getcwd(), 'Data')  # Data folder inside Excel_Python folder
os.chdir(data_path)

df = pd.read_excel('finance_data.xlsx')
df.info()

# shows (missing -> null) (Figure 6.4 in book)
# 2 missing in txn_id column
# 3 missing in txn_date, client and amount columns
# 4 missing in approved
# 5 missing in region

# Reading 'missing' and '-' as missing values
df = pd.read_excel('finance_data.xlsx', 
                   na_values=['missing', '-'])
df.info() # Now, you can see more missing values
# Refer (Figure 6.5 in book)

# Count missing values in each column
df.isna()
df.isna().sum()

# any particular column
df['amount'].isna().sum()
df['amount'].isna().any()

# Count missing values in each row
df.isna().sum(axis=1)

# Overall missing values count
df.isna().sum().sum()
df.isna().sum(axis=1).sum()

df.notna().sum().sum()

df_backup = df.copy() # Data Back-up to avoid accidental change

# Filling missing values by some constant ------------------

# Filling missing values in amount columns as 500
df['amount'].fillna(500) # Does not change original data
df['amount']
df['amount'] = df['amount'].fillna(500)  # Changes original data
# or
df.fillna({'amount': 500}, inplace=True) # Changes original data

# Avoid using the older way as it's deprecated
df['amount'].fillna(500, inplace = True) # Changes original data


# As we've changed data, going back to original data for demo purpose
df = df_backup.copy() # Now again df has missing values in amount column

# filling missing values in multiple columns
df.fillna({'amount': 500, 'approved': 1})

# Filling missing values by forward/backward value -----------------
df['txn_date'].ffill() # Recommended Way
df['client'].bfill() 

# in client column the last value is not available, 
# so the missing entry will stay unfilled, 
# which you can fill with a constant value or use other strategies.
df['client'].bfill().fillna('Alex')

# Deprecated method (you might see somewhere) since version 2.1.0, gives TypeError: in version 3.0.0
# df['txn_date'].fillna(method = 'ffill') 

# Filling missing values based on some condition --------------------

df.loc[df['client'] =='Alice', 'region'] = 'East'
df.loc[df['amount'] > 1500, 'approved'] = 0

# Filling missing values based on statistical measures --------------------

# Mean replacement
mean_amt = df['amount'].mean()
df['amount'].fillna(mean_amt.round(1))

# Median Replacement
df['amount'].fillna(df['amount'].median())

# Replacement by Interpolation (by default linear interpolation)
df['amount'].interpolate()

# Other interpolation methods (needs scipy)
df['amount'].interpolate(method='polynomial', order=2)  # Polynomial interpolation (order 2)
df['amount'].interpolate(method='nearest')  # Nearest neighbor interpolation
df['amount'].interpolate(method='spline', order=3)  # Spline interpolation (cubic)

# Mode/ Most Frequent Value Replacement
most_fre_region = df['region'].value_counts().idxmax()
df['region'].fillna(most_fre_region)


# Filling missing values based group-wise stats --------------------
 
# Fill missing 'amount' with region-wise mean
east_mean_amt = df.loc[df['region'] == 'East', 'amount'].mean()

df.loc[(df['region'] == 'East') & (df['amount'].isna()), 'amount'] = east_mean_amt

# There are better option to fill group-wise mean 
# (you will learn in upcoming sections)

# More about missing value treatment  ------------------------------

# globally forward-fill txn_date and client
df[['txn_date','client']] = df[['txn_date','client']].ffill()


# Deleting missing values ---------------------------

df = df_backup.copy()

df.dropna()  # deletes all the rows with 'any' missing value
df           # No change in original data

df.dropna(how='all') # delete only the row(s) with 'all' missing values

df.dropna(axis = 1) # delete all the columns with 'any' missing value
df.dropna(axis=1, how='all') # delete only the column(s) with 'all' missing values

# More examples

# Delete rows where txn_id is missing
df.dropna(subset=['txn_id'])  # drop any row with NaN in txn_id
# Or
df[df['txn_id'].notna()]

# Delete rows where txn_id and amount is missing
df.dropna(subset=['txn_id', 'amount'])

# Delete rows with more than 50% missing data
#  calculate threshold = minimum number of non-NA values required to keep the row
threshold = int(df.shape[1] * 0.5) + 1       # e.g. if 6 cols, need at least 4 non-NA
df.dropna(thresh=threshold)     # drop rows with fewer than threshold non-NA values


# Delete columns with more than 50% missing data
col_threshold = int(df.shape[0] * 0.5) + 1   # e.g. if 15 rows, need at least 8 non-NA
df.dropna(axis=1, thresh=col_threshold)  # drop cols with fewer than col_threshold non-NA

# In all these examples, original data is not changed.
# To delete rows/columns from the data, you need to use inplace = True argument



# Working with duplicates ----------------------------

# Rows containing duplicates
df[df.duplicated(keep = False)]

# Remove duplicate rows based on all columns
df.drop_duplicates()

# To explore duplicates of a particular column 'txn_id'
df['txn_id'].nunique()
df['txn_id'].unique()
df['txn_id'].duplicated()
df['txn_id'].duplicated().sum()
df.loc[df['txn_id'].duplicated(), :] # duplicated rows

# Remove duplicates based on specific columns (e.g., 'txn_id' )
df.drop_duplicates(subset=['txn_id'])

# To see all rows of duplicates (including the first occurance)
df[df['txn_id'].duplicated(keep=False)]
# Note:
# df['txn_id'].duplicated(keep=False) includes row 5 also
# because Pandas, by default, treats NaN values as duplicates of each other 
# when using duplicated(), and row 16 also has a NaN in 'txn_id'.

df['txn_id'].duplicated().sum() # 3
df['txn_id'].duplicated(keep=False).sum() # 6 as it keeps the first row and also treats NaN as duplicates