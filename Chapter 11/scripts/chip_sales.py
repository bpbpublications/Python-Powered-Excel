import xlwings as xw
import pandas as pd


def main():
    # --- Step 1: Connect to Excel & Grab sheets ---
    wb = xw.Book.caller()
    ws_jan = wb.sheets["Jan"]
    ws_feb = wb.sheets["Feb"]


    # --- Step 2: Load data from Excel files ---
    jan = ws_jan.range("A1").options(pd.DataFrame, header=1, index=False, expand="table").value
    feb = ws_feb.range("A1").options(pd.DataFrame, header=1, index=False, expand="table").value
    
    # --- Step 3: Merge ---
    df = pd.concat([jan, feb])

    # --- Step 4: Pivot (total revenue by region & product) ---
    pivot = pd.pivot_table(df, 
                           values="revenue", 
                           index="region", 
                           columns="product", aggfunc="sum")

    # --- Step 5: Write back to Excel ---
    try:
        # out = wb.sheets.add("Summary", after=wb.sheets[-1])
        out = wb.sheets["Summary"]
        out.clear()
    except:
        out = wb.sheets.add("Summary", after=wb.sheets[-1])
    out.range("A1").value = df
    out.range("J1").value = pivot
