# Vectorized Operations --------------------------

import pandas as pd
import numpy as np

# Create a pandas Series
s = pd.Series([1, 2, 3, 4])

# Vectorized addition for pandas series
s + 10

# pandas series holds a numpy array under the hood
print(type(s.values))  # Output: <class 'numpy.ndarray'>

# vectorized operation for numpy array
sales = np.array([1500, 2200, 1850, 2400.])
price = np.array([5, 7.5, 7, 8])
revenue = sales*price
revenue

new_sales = np.array([1000, 2000, 3000, 4000])
total_sales = sales + new_sales 
total_sales

# Broadcasting -----------------------------------
unit_price = 5 # Zero dimentional array or scalar
new_revenue = sales * unit_price
new_revenue

cost = 7
profit = price - cost
profit

sales_qtr = np.array([[1500, 1700, 1600], 
                      [2200, 2100, 2300]])
revenue_qtr = sales_qtr * unit_price
revenue_qtr 

# Statistical Functions --------------------------

sales.sum()
sales.mean()

sales_qtr.sum()
sales_qtr.sum(axis=1)

sales_qtr.mean()
sales_qtr.mean(axis=1)

sales_qtr.std()

# NumPy offers both methods like `arr.sum()` and 
# functions like `np.sum(arr)` that do the same thing. 

np.sum(sales_qtr)
np.sum(sales_qtr, axis = 1)

# Other Mathematical Functions ---------------------

np.sqrt(sales_qtr)
np.argmin(sales_qtr)
np.argmax(sales_qtr)
np.prod(sales_qtr)
np.percentile(sales_qtr, 10)
np.cumsum(sales_qtr)
np.cumprod(sales_qtr)

# Statistical Functions --------------------------

sales.sum()
sales.mean()

sales_qtr.sum()
sales_qtr.sum(axis=1)

sales_qtr.mean()
sales_qtr.mean(axis=1)

sales_qtr.std()
sales_qtr.std(axis = 1)

# Numpy offers both methods like `arr.sum()` and 
# functions like `np.sum(arr)` that do the same thing. 

np.sum(sales_qtr)
np.sum(sales_qtr, axis = 1)

# Other Mathematical Functions ---------------------

np.sqrt(sales_qtr)
np.argmin(sales_qtr)
np.argmax(sales_qtr)
np.prod(sales_qtr)
np.percentile(sales_qtr, 10)
np.cumsum(sales_qtr)
np.cumprod(sales_qtr)