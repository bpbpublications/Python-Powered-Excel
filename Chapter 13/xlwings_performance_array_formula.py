import xlwings as xw
import numpy as np

# Inefficient Way
@xw.func
def sales_year(last_year, growth_rate, period = 0):
    last_year = float(last_year)
    growth_rate = float(growth_rate)
    return last_year * ((1 + growth_rate) ** period)


# Array-Formula (Efficient)
@xw.func
@xw.arg("period", np.array)
@xw.ret(expand='down')
def sales_growth(last_year, growth_rate, period):
    """Returns 5 years of projected sales"""
    last_year = float(last_year)
    growth_rate = float(growth_rate)
    return last_year * ((1 + growth_rate) ** period)


# @xw.func
# # @xw.ret(raw=True)
# def simple_raw_return():
#     return [["A", "B", "C"], [1, True, '1/11/2025']]

@xw.func
@xw.ret(raw=True)
def simple_raw_return():
    return [["A", "B", "C"], [1, True, '1/11/2025']]
