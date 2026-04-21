import os
import pandas as pd

os.getcwd() # Excel_Python folder created for the book

# As we will be reading multiple files from Data folder inside Excel_Python
# Setting working directory to Data Folder

data_path = os.path.join(os.getcwd(), 'Data')  # Data folder inside Excel_Python folder
os.chdir(data_path)

# Reading files -----------------------------------------------

# Reading CSV Data
csv_data = pd.read_csv('employees.csv'); csv_data.shape

# Reading JSON data
json_data = pd.read_json('employees.json'); json_data.shape

# Reading HTML data
html_data = pd.read_html('employees.html'); html_data 
type(html_data)               # It's a list
html_data = html_data[0]                # grab first (and only) table
type(html_data)    # now a DataFrame
html_data.shape

# More about reading CSV/Flat files (with different separators) --------------

df_sc = pd.read_csv("semicolon_sep.txt"); df_sc.shape #(20, 1)
# Not reading correctly as default sep is ','

df_sc = pd.read_csv("semicolon_sep.txt", sep=';'); df_sc.shape #(20, 7)
df_sc.head(2)

df_sc = pd.read_csv("semicolon_sep.csv", sep=';'); df_sc.shape #(20, 7)
df_sc.head(2)

df_p = pd.read_csv("pipe_sep.txt", sep='|'); df_p.shape #(20, 7)
df_p.head(2)

df_p = pd.read_csv("pipe_sep.csv", sep='|'); df_p.shape #(20, 7)
df_p.head(2)

df_t = pd.read_csv("tab_sep.csv", sep="\t"); df_t.shape # (20, 7)
df_t = pd.read_csv("tab_sep.txt", sep="\t"); df_t.shape # (20, 7)
df_t = pd.read_csv("tab_sep.tsv", sep="\t"); df_t.shape # (20, 7)


# When working with tab-separated files, always use sep='\t' (not '/t').
df_t = pd.read_csv("tab_sep.txt", sep='/t'); df_t.shape

# If you ever see a warning about "falling back to the Python engine", 
# it usually means pandas thinks you're using a complex separator. 
# In most cases, it's just a typo in the separator string.

df_c = pd.read_csv("caret_sep.txt", sep='^'); df_c.shape #(20, 7)

df_multi = pd.read_csv("multi_sep.txt", 
                       sep=r'[,;\t]', engine='python')
df_multi

# NOTE POINTS: 1. Use raw string (r'') for regex-based sep
# 2. Must use engine='python'
# 3. May be slower for large files

# Reading unlabelled data from url and assigning column names ----------------

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url); df.head(3)

columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv(url, names=columns); df.head(3)

# Reading selected columns ---------------------------------------------

df_cols = pd.read_csv('employees.csv', usecols=[0,1,4]); df_cols.shape
columns = ['emp_id', 'name', 'sal']
df_cols = pd.read_csv('employees.csv', usecols=columns); df_cols.shape

# Reading fewer (10 here) rows only --------------------------------------

df_rows = pd.read_csv('employees.csv', nrows=10); df_rows.shape


df_sample = pd.read_csv('employees.csv', 
                        nrows=10,
                        usecols=[0,1,4]); df_sample.shape

# Skipping first few rows (Metadata) ---------------------------------------

df_skip = pd.read_csv('employees_metadata.csv',
                      skiprows=2); df_skip.shape

# Blankrows in the begining are skipped automatically
# Blankrows in between are showing up nan
df_blankRow = pd.read_csv('employees_blankRows.csv')
df_blankRow.shape


# Skip first 3 rows while reading the file 

# Try changing skiprows to 0
df = pd.read_csv("sample_with_headers.csv", skiprows=3)
df

df = pd.read_csv("sample_with_blank_rows.csv", skiprows=3)
df

# Setting and resetting index column ------------------------------

df = pd.read_csv('employees.csv')
df.head(2)

df_indexed = pd.read_csv('employees.csv', index_col='emp_id')
df_indexed.head(2)

# Alternately, set 'emp_id' as the new index after reading the data
df_indexed = df.set_index('emp_id')

# Reset index (bring 'emp_id' back as a column)
df_reset = df_indexed.reset_index()
df_reset.head(2)

# Another example: Set the index inplace without needing to reassign

df.set_index('emp_id', inplace=True)
print("\nDataFrame after inplace set_index:")
print(df.head())

# Convert index to column manually by resetting the index
df_reset = df.reset_index()
print("\nFinal DataFrame with index as column again:")
print(df_reset.head())


# More with excel files ------------------------------------------

df = pd.read_excel('finance_data.xlsx')

df_jan = pd.read_excel('finance_data.xlsx',
                       sheet_name=0)

df_feb = pd.read_excel('finance_data.xlsx',
                       sheet_name="Feb")

df_jan_feb = pd.read_excel('finance_data.xlsx',
                       sheet_name=[0, 1])

df_jan_feb = pd.read_excel('finance_data.xlsx',
                       sheet_name=[0, "Feb"])

df_jan_feb = pd.read_excel('finance_data.xlsx',
                       sheet_name=["Jan", "Feb"])

print(type(df_jan_feb)); len(df_jan_feb)

df_jan_feb.get(0).shape # First dataframe

df_all_sheet = pd.read_excel('finance_data.xlsx',
                       sheet_name=None)

print(type(df_all_sheet)) # <class 'dict'>
print(len(df_all_sheet)) # 3
print(df_all_sheet.keys())      # dict_keys(['Jan', 'Feb', 'Mar'])
print(type(df_all_sheet['Jan'])) # <class 'pandas.core.frame.DataFrame'>

# To fetch data from sheet named 'Jan'
df_all_sheet.get('Jan')
 

# Read the data from XLSM (macro enabled file)
df_xlsm = pd.read_excel('employees.xlsm'); df_xlsm

# Read the data from the XLS file 
df_xls = pd.read_excel('finance_data.xls')

# It uses xlrd engine to read xls files 
df_xls = pd.read_excel('finance_data.xls', engine='xlrd')

# Make sure xlrd is installed, if you are to read legacy xls files. 
# xlrd is not installed by default with Python or pandas


# Read the data from the XLSB file using pyxlsb engine
# This will work, if you have pyxlsb installed (Do it in if you use xlsb files)

df_xlsb = pd.read_excel('employees.xlsb', engine='pyxlsb')

# Writing Data ----------------------------------------------

# Write DataFrame to xlsx/csv/json format 

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Score': [85.5, 92.1, 78.9, 88.0]
}

# Create the DataFrame
toy_df = pd.DataFrame(data)

# Print the DataFrame
print(toy_df)


toy_df.to_excel("xlsx_export_by_pandas.xlsx", index=False)
toy_df.to_csv("csv_export_by_pandas.csv", index=False)
toy_df.to_json("json_export_by_pandas.json", index=False)
