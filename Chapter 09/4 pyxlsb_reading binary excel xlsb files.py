from pyxlsb import open_workbook
from pyxlsb import convert_date


wb = open_workbook("finance_data.xlsb")
print("Sheets:", list(wb.sheets))


# Fetching sheet by sheet index or name
sheet = wb.get_sheet(1) # Index is 1-based (1 = first sheet)
sheet = wb.get_sheet('Jan')
print("Sheet name:", sheet.name)
print(f'Sheet Dimensions: {sheet.dimension.h}rows and {sheet.dimension.w}cols')
      

sheet.cols # gives column metadata
sheet.rows # Generator of rows (each a list of cells)
list(sheet.rows())

# Get the second row (index 1)
row = list(sheet.rows())[1]

# Get the second column (index 1) of second row
cell_value = row[1].v

# Convert the Excel serial date
converted = convert_date(cell_value)
print("Converted date:", converted)


# Reading all rows/row values
for row in sheet.rows():
    # print(row)
    print([item.v for item in row])   # print cell values

wb.close()


with open_workbook('finance_data.xlsb') as wb:
    with wb.get_sheet(1) as sheet:  # first sheet
        for row in sheet.rows():
            print([item.v for item in row])   # print cell values

             
# trim trailing blanks
def trim_trailing_nones(row):
    while row and row[-1] is None:
        row.pop()
    return row

with open_workbook('finance_data.xlsb') as wb:
    with wb.get_sheet(1) as sheet:
        for row in sheet.rows():
            values = [item.v for item in row]
            if any(v is not None for v in values):
                trimmed = trim_trailing_nones(values)
                print(trimmed)          
                
# Sheet dimensions  
with open_workbook("finance_data.xlsb") as book:
    for sheet_name in book.sheets:
        with book.get_sheet(sheet_name) as sheet:
            dim = sheet.dimension
            print(f"Sheet '{sheet_name}' has "
                  f"{dim.h} rows and {dim.w} cols")
      
    
# reading binary files using pandas ---------------------
# pandas automatically trims Nones and gives you a clean DataFrame.                
import pandas as pd

df = pd.read_excel("finance_data.xlsb", engine="pyxlsb")
print(df.head())
df.shape                
