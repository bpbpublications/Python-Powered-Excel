# Ch 12: Try-it-out exercise 2
import xlwings as xw
import pandas as pd

@xw.func
@xw.arg('data', ndim=2)
@xw.ret(expand='table')
def avg_stock_by_category(data):
    """
    Computes average stock per product category.
    Args:
        data: 2D Excel range with columns [Product, Category, Quantity]
    Returns:
        DataFrame (as list of lists) with Category and Average Quantity
    """
    df = pd.DataFrame(data[1:], columns=data[0])  # first row as header
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    summary = (
        df.groupby('Category')['Quantity']
        .mean()
        .reset_index()
        .rename(columns={'Quantity': 'Avg Quantity'})
    )
    return [summary.columns.tolist()] + summary.values.tolist()
