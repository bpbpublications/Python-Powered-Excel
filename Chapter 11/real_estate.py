import xlwings as xw
import pandas as pd

def main():
    wb = xw.Book.caller()   # Connect to Excel
    sheet = wb.sheets["Sheet1"]

    # Load data
    df = sheet.range("A1").options(pd.DataFrame, header=1, index=False, expand="table").value

    # --- Formatting Rules ---
    # Highlight rows with missing dates
    missing_dates = df[df["date_listed"].isna()].index + 2   # +2 = header + 1-based index
    for row in missing_dates:
        sheet.range(f"B{row}").color = (255, 200, 200)  # light red

    # Highlight prices above 800k
    high_price = df[pd.to_numeric(df["price"], errors="coerce") > 800000].index + 2
    for row in high_price:
        sheet.range(f"G{row}").color = (200, 255, 200)  # light green
