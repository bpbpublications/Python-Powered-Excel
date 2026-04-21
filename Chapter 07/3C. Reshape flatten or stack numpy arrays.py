import numpy as np

#  Sales data for 4 regions
sales = np.array([15, 20, 25, 30.])
print(sales) # This is like a column of numbers in Excel
sales.dtype # dtype('float64')

# 2D array (2 rows × 3 columns)

# Quarterly sales data for 2 regions
sales_qtr = np.array([[10, 11, 15], 
                      [5, 13, 17]])
print(sales_qtr) # like Excel table
sales_qtr.dtype # dtype('int32')

# Dimension, Size, Shape, Data Type -------------------------------------

print("dimension of sales array is", sales.ndim) # number of dimensions or axes
print("Shape of sales array is:", sales.shape) # Size of array along each dimension
print("size of sales array is", sales.size) # size is the total number of elements in the array
print("type of sales array is", sales.dtype) # data type 

print("dimension of sales_qtr array is", sales_qtr.ndim) # number of dimensions or axes
print("Shape of sales_qtr array is:", sales_qtr.shape) # Size of array along each dimension
print("size of sales_qtr array is", sales_qtr.size) # size is the total number of elements in the array
print("type of sales_qtr array is", sales_qtr.dtype) # data type 

# Reshaping, Flattening and Stacking Arrays --------------------------------------

# Converting 1D array to 2D array
sales.reshape(2, 2)      # Reshape 1D to 2x2
sales.reshape(4, 1)       # Reshape to column format
sales.reshape(1, 4) 
# sales.reshape(3, 1)  # ValueError, incompatible size

# Converting 2D array to 1D array
sales_qtr.flatten()       # Flatten 2D to 1D (copy)
sales_qtr.ravel()         # Also flattens, returns a view (no data copy)

# let's understand flatten() Vs Ravel
# ravel() gives a view (if possible)
r = sales_qtr.ravel()
r[0] = 9999   # change first element
print(sales_qtr)   # original array also changes!

# flatten() always gives a copy
f = sales_qtr.flatten()
f[1] = 8888   # change second element
print(sales_qtr)   # original array stays the same


# Joining arrays
np.concatenate([sales, [35, 40]])      # Combine 1D arrays
np.vstack([sales_qtr, [8, 9, 10]])     # Add a new row (vertically)
np.hstack([sales_qtr, [[20], [30]]])   # Add a new column (horizontally)

# Type Casting -----------------------------------

sales_int = np.array([15, 20, 25, 30.75], dtype=int)
sales_int

sales_f32 = np.array([15, 20, 25, 30.75], dtype='float32')
sales_f32

# Transposition ----------------------------------

# Transpose makes no difference to 1D array, 
# but flips rows and columns for 2D array
sales.T
sales

sales_qtr
sales_qtr.T               # Transpose: flip rows & columns
# or
sales_qtr.transpose()
sales_qtr.T.shape