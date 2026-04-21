import xlrd
from xlrd import xldate_as_datetime

# Open the workbook and sheet
wb = xlrd.open_workbook("finance_data.xls")
sheet = wb.sheet_by_index(0)

# Find the column index for 'txn_date'
header = sheet.row_values(0)
txn_date_col = header.index('txn_date')

# Read and convert each row
for r in range(1, sheet.nrows):  # Skip header row
    row = sheet.row_values(r)
    cell = sheet.cell(r, txn_date_col)
   
    # Convert if it's a number and cell type is date or number
    if cell.ctype == xlrd.XL_CELL_DATE or cell.ctype == xlrd.XL_CELL_NUMBER:
        try:
            date_obj = xldate_as_datetime(cell.value, wb.datemode)
        except:
            date_obj = None
    else:
        date_obj = None  # Handle 'missing', 'n/a', etc.

    print(f"Row {r}: txn_id={row[0]}, txn_date={date_obj}, client={row[2]}")
    
    
# Reading entire data    
for r in range(1, sheet.nrows):
    cell = sheet.cell(r, txn_date_col)

    # Check if cell is a valid Excel date
    if cell.ctype == xlrd.XL_CELL_DATE or cell.ctype == xlrd.XL_CELL_NUMBER:
        try:
            date_obj = xldate_as_datetime(cell.value, wb.datemode)
            row_values = sheet.row_values(r)
            row_values[txn_date_col] = date_obj  # Replace raw date with datetime object
            print(row_values)
        except:
            continue  # Skip rows with invalid date conversion
    