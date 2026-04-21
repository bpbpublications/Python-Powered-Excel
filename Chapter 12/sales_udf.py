# Ch 12: Try-it-out exercise 1

import xlwings as xw
import numpy as np

@xw.func
@xw.arg('sales', ndim=2)  # Accepts a 2D Excel range
@xw.ret(expand='table')   # Returns a 2D array (auto "spill" in Excel)
def sales_performance(sales, target=10000):
    """
    Identifies which regions exceeded sales target.
    Args:
        sales: 2D array of numbers (Excel range)
        target: numeric target value
    Returns:
        2D array with 'Above Target' or 'Below Target'
    """
    sales_array = np.array(sales, dtype=float)
    result = np.where(sales_array >= target, "Above Target", "Below Target")
    return result
