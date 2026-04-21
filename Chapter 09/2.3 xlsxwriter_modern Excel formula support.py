import xlsxwriter

wb = xlsxwriter.Workbook('formula.xlsx')
wb = xlsxwriter.Workbook('newer_formula.xlsx', 
                         {'use_future_functions': True})

ws = wb.add_worksheet('products')

header_format = wb.add_format({'bold': True, 
                              'bg_color': '#DCE6F1', 
                              'font_color': '#223A54',
                              'align': 'center'})

headers = ['product_id', 'product_name', 'product_category', 'product_price']

ws.write_row(0, 0, headers, header_format)


# Sample data (nested list)
data = [
    [101, 'Wireless Mouse', 'Electronics', 25.99],
    [102, 'Yoga Mat', 'Fitness', 15.50],
    [103, 'Notebook', 'Stationery', 3.99],
    [104, 'Pen', 'Stationery', 10.00],
    [105, 'USB Cable', 'Electronics', 150.00],
    [106, 'Chair', 'Furniture', 45.50],
    [107, 'Water Bottle', 'Fitness', 10.00]
]

# Writing data row-wise from row 1 and col 0 (in excel second row and first col)
for row_num, row_data in enumerate(data, start=1):
    ws.write_row(row = row_num, col = 0, data = row_data)
    
# The write_row method automatically fills across as many columns as needed,
# based on the length of each row_data list. No need to specify column count manually.
    
# Adding a new data/variable
units_sold = [5, 8, 15, 30, 6, 10, 20]

ws.write(0, len(headers), 'Units Sold', header_format) # header with formatting

# Writing data column-wise (starting row=1 since row=0 is header)
ws.write_column(1, len(headers), units_sold)
# write_col() fills down as many rows as needed

ws.set_column('A:F', 15)
        
# Add "Revenue" header
ws.write(0, len(headers) + 1, 'Revenue', header_format)

# Write formula row-wise (as Excel Formula)
for row_num in range(1, len(data) + 1):
    price_cell = f'D{row_num + 1}'         # Column D = product_price
    units_cell = f'E{row_num + 1}'         # Column E = Units Sold
    formula = f'={price_cell}*{units_cell}'
    # print(formula)
    ws.write_formula(row_num, len(headers) + 1, formula)    
        
# wb.close()        

ws.write_formula('I2', '=TEXTJOIN(": ", TRUE, B2:C2)')
ws.write_formula('H2', '=IFS(F2>500, "High", F2>300, "Medium", F2>0, "Low")')


ws.write_formula('E9', '{=SUM(E2:E8)}') # Works
ws.write_formula('F9', '{=SOMME(F2:F8)}') # French. Error on load


ws.write_row('A10', ['Unique Cat', 'Sorted Products'], header_format)
ws.merge_range('D10:F10', 'Filtered Data (Price>20)', header_format)
ws.write_dynamic_array_formula('A11:A15', '=UNIQUE(C2:C8)')
ws.write_dynamic_array_formula('B11:B15', '=SORT(B2:B8)')
ws.write_dynamic_array_formula('D11:D20', '=FILTER(B2:D8, D2:D8 > 20)')

# CHECK THIS IN EXCEL 2019
ws.write_formula('A18:A22', '=UNIQUE(C2:C8)')
# ws.write_formula('B11:B15', '=SORT(B2:B8)')
# ws.write_formula('D11:D20', '=FILTER(B2:D8, D2:D8 > 20)')

# ALSO check delete cell value in higher version of xlsxwriter????


ws.write('K1', 'Using Lambda', header_format)
ws.write_formula('K2', 
                 '=LAMBDA(_xlpm.price, _xlpm.units, _xlpm.price * _xlpm.units)(D2, E2)')

ws.write('L1', 'Lambda for Dynamic range', header_format)


# # Write a dynamic array formula that spills down from G2
ws.write_dynamic_array_formula('L2',
    '=LAMBDA(_xlpm.price, _xlpm.units, _xlpm.price * _xlpm.units)(D2:D8, E2:E8)')

ws.set_column('K:L', 18)
ws.set_column('K:L', 25)

# To hide some columns for screenshot
# ws.set_column("A:C", None, None, {"hidden": True})
# ws.set_column("H:J", None, None, {"hidden": True})

wb.close()        