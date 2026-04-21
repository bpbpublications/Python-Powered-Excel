import pandas as pd

# Create Pandas DataFrame --------------------------------------

# Using a list of lists
users = [['Excel', 10], ['R', 15], ['Python', 14]]

df = pd.DataFrame(users); df
df = pd.DataFrame(users, columns=['Tool', 'User_Count']); df
df = pd.DataFrame(users, 
                  columns=['Tool', 'User_Count'],
                  index = ['R1', 'R2', 'R3']); df

# Using a dictionary of lists
users = {'Tool': ['Excel', 'R', 'Python'],
         'User_count': [10, 15, 14]}

df = pd.DataFrame(users); df

# Using a list of dictionaries
users = [{'Tool': 'Excel', 'User_Count': 10}, 
         {'Tool': 'R', 'User_Count': 15},
         {'Tool': 'Python', 'User_Count': 14}]
df = pd.DataFrame(users); df

# Different list for each column
tool = ['Excel', 'R', 'Python']
user_count = [10, 15, 14]
col_names = ['Tool', 'User_Count']

df = pd.DataFrame(list(zip(tool, user_count)), 
                  columns=col_names); df

# Using Pandas series to create dataframe
s1 = pd.Series(['Excel', 10], 
               index=col_names); s1
s2 = pd.Series(['R', 15], 
               index=col_names)
s3 = pd.Series(['Python', 14], 
               index=col_names)

df = pd.DataFrame([s1, s2, s3])
print(df)

# Create Pandas Series ---------------------------------

# From List
s_list = pd.Series([10, 20, 30]); s_list

# From Tuple
s_tuple = pd.Series((10, 20, 30)); s_tuple

# From Dictionary (keys become index)
s_dict = pd.Series({'0': 10, '1': 20, '2': 30}); s_dict

# From range()
s_range = pd.Series(range(10, 40, 10)); s_range