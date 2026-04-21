import xlwings as xw
import numpy as np
import pandas as pd

# UDF adding 10 to a given input
@xw.func
def add_ten(a):
    return a + 10

# UDF adding two numbers
@xw.func
def my_sum(a, b):
    return a + b

# UDF accepting 1‑D ranges like A3:B3 (row) or B2:B3 (column)
@xw.func
def my_sum_range(values):
    return sum(values)

# UDF accepting2‑D ranges using ndim=2
@xw.func
@xw.arg("data", ndim = 2)
def my_sum_range2(data):
    return sum([sum(row) for row in data])

# UDF accepting both 1‑D and 2‑D ranges using ndim='natural'
@xw.func
@xw.arg("data", ndim='natural')
def my_sum_range3(data):
    # If it's a 1D list, wrap it to make it 2D
    if isinstance(data[0], (int, float)):
        data = [data]

    return sum(sum(row) for row in data)

# UDF with numpy converter decorator 
@xw.func
@xw.arg("data", np.array)
def my_sum_array(data):
    return data.sum()

# UDF with pandas converter
@xw.func
@xw.arg('df', pd.DataFrame, index=False, header=False)
def describe(df):
    return df.describe()

# UDF with pandas converter_ Controling the output format
@xw.func
@xw.arg('df', pd.DataFrame, index=False, header=False)
@xw.ret(index=False, header=False)
def correlation(df):
    return df.corr()

# UDF_simulating dynamic array formula
@xw.func
@xw.ret(expand='table')
def dynamic_array(r, c):
    return np.random.randn(int(r), int(c))

# Volatile UDF
@xw.func(volatile = True)
def volatile_function(n=10):
    return np.random.randint(n)
