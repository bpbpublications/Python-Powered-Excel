# analysis.py
import pandas as pd
import xlwings as xw


def insert_data():
    wb = xw.Book.caller()
    df = pd.DataFrame({"A": [10, 20, 30], "B": [100, 200, 300]})
    wb.sheets[0].range('A1').value = df
    
def analyze_data():
    wb = xw.Book.caller()
    df = pd.DataFrame({"A": [10, 20, 30], "B": [100, 200, 300]})
    
    if "Summary" in [s.name for s in wb.sheets]:
        wb.sheets["Summary"].clear()
    else:
        wb.sheets.add(name = "Summary", after=wb.sheets[0])
        
    wb.sheets["Summary"].range('A1').value = df.describe()   