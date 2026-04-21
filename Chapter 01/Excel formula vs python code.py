# Just run the code for each example one by one and observe the output
# Do not worry if you can't understand why it works
# You will learn everything from scratch in Chapter 3

# To find unique values in a column ----------------------

import pandas as pd

data = pd.DataFrame({
                    "tools":
                     ['Excel', 'Python', 'Python', 'VBA', 'Python']
                     })
    
print(data) # To value table-like data


data["tools"].nunique() # number of unique values in data
data["tools"].unique()  # which are the unique values
data["tools"].value_counts() # frequency/count of each unique value


# Sum of values _ High or Low -------------------------

values = [10, 15, 20, 25, 30, 5, 10, 10, 10, 5, 10]

if sum(values)> 100:
    print('High')
else:
    print('Low') 


"High" if sum(values) > 100 else "Low" # another way of doing if-else block

print("High" if sum(values) > 100 else "Low")
