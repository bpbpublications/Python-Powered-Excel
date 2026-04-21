import xlrd

# Opening .xls file
wb = xlrd.open_workbook("finance_data.xls")

print(wb.nsheets) # Number of all sheets
print(wb.sheet_names()) # List of all sheet names


# Loop through the sheet objects
for sheet in wb.sheets():
    print(sheet.name)

# Get the first sheet by index
sheet = wb.sheet_by_index(0)

# Get a sheet by it’s name
sheet = wb.sheet_by_name("Jan")

# Sheet metadata
print("Sheet name:", sheet.name)
print("Visibility:", sheet.visibility)   
# 0=visible, 1=hidden, 2=very hidden
print("Number of rows:", sheet.nrows)
print("Number of columns:", sheet.ncols)

print(sheet.row_values(0))   # First row
print(sheet.row_values(1))  # Second row

# In Excel, a sheet marked as **"very hidden"** (value `2`) is hidden in a way 
# that it **cannot be unhidden through the Excel interface**—
# not even via the "Unhide" option in the right-click menu or ribbon.
# To make it visible again, you’d need to use:
# - VBA (Visual Basic for Applications) code  
# - A third-party tool or library like `xlrd` or `openpyxl`
# This feature is often used to protect sensitive sheets from casual users 
# or to hide configuration sheets that support macros or dashboards.


# Read a specific cell value
cell_value = sheet.cell_value(rowx=0, colx=0)
print("Cell (0,0):", cell_value)

# Inspecting data type
cell_type = sheet.cell_type(rowx=0, colx=0)
print("Cell (0,0):", cell_type)

# cell type: 1 means a Unicode string

# Read the whole sheet
for r in range(sheet.nrows):
    row_values = sheet.row_values(r)
    print(row_values)

 
    
# Date System used by Excel
print("Datemode (0=1900, 1=1904):", wb.datemode) 
# - 0 means the 1900 date system (default on Windows)
# - 1 means the 1904 date system (default on older Mac versions)


# this cell contains a date
cell_value = sheet.cell_value(rowx=1, colx=1) # B2 cell
date_value = xlrd.xldate_as_tuple(cell_value, wb.datemode) 

print(f'Raw Value: {cell_value}\t Date: {date_value}')

cell = sheet.cell(1, 1)
if sheet.cell_type(1, 1) == xlrd.XL_CELL_DATE:
    date_tuple = xlrd.xldate_as_tuple(cell.value, wb.datemode)
    print("Date:", date_tuple)
 
    
# inspecting data type in each column

sheet.cell_type(rowx = 0, colx = 1)

for r in range(sheet.ncols):
    print(r)
    col_types = sheet.cell_type(rowx = 0, colx = r)
    print(col_types)
    
# inspecting data type in each cell    
for c in range(sheet.ncols):
    print(f"Column {c}:")
    for r in range(sheet.nrows):
        cell = sheet.cell(r, c)
        print(f"  Row {r} - Type: {cell.ctype}, Value: {cell.value}")

# xlrd doesn't automatically assign a single data type to an entire column,
# because Excel columns can contain mixed types—text, numbers, dates, blanks—all in the same column.
    
# xlrd exposes cell types using constants like:
# XL_CELL_NUMBER (2) → numbers (General, Number format in Excel)
# XL_CELL_DATE (3) → dates (Excel serial numbers)
# XL_CELL_TEXT (1) → strings
# XL_CELL_BOOLEAN (4) → TRUE/FALSE
# XL_CELL_EMPTY (0) → blank
# XL_CELL_ERROR (5) → errors (#DIV/0!, #REF!, etc.)

# Most common data type of each column
for c in range(sheet.ncols):
    type_counter = {}
    for r in range(sheet.nrows):
        cell_type = sheet.cell_type(r, c)
        if cell_type in type_counter:
            type_counter[cell_type] += 1
        else:
            type_counter[cell_type] = 1

    # Find the most common type manually
    most_common_type = max(type_counter, key=type_counter.get)
    print(f"Column {c} - Most common type: {most_common_type}")
    
# using collection module
from collections import Counter

for c in range(sheet.ncols):
    type_counter = Counter()
    for r in range(sheet.nrows):
        cell_type = sheet.cell_type(r, c)
        type_counter[cell_type] += 1
    most_common_type = type_counter.most_common(1)[0][0]
    print(f"Column {c} - Most common type: {most_common_type}")    