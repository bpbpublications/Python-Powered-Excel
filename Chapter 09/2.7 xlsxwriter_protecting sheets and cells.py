import xlsxwriter
wb = xlsxwriter.Workbook('protected.xlsx')

ws = wb.add_worksheet('products')
header_format = wb.add_format({'bold': True, 
                              'bg_color': '#DCE6F1', 
                              'font_color': '#223A54',
                              'locked': True})

headers = ['product_id', 'product_name', 'product_category', 'product_price']

ws.write_row(0, 0, headers, header_format)
    
locked_format = wb.add_format({'locked': True})
unlocked_format = wb.add_format({'locked': False})
hidden_formula_format = wb.add_format({'locked': True, 'hidden': True})

# Write data rows (unlocked)

data = [
    [101, 'Wireless Mouse', 'Electronics', 25.99],
    [102, 'Yoga Mat', 'Fitness', 15.50],
    [103, 'Notebook', 'Stationery', 3.99],
    [104, 'Pen', 'Stationery', 10.00],
    [105, 'USB Cable', 'Electronics', 150.00],
    [106, 'Chair', 'Furniture', 45.50],
    [107, 'Water Bottle', 'Fitness', 10.00]
]

     
for row_num, row_data in enumerate(data, start=1):
    ws.write_row(row_num, 0, row_data, unlocked_format)        
        
# Adding a new column
units_sold = [5, 8, 15, 30, 6, 10, 20]

ws.write(0, len(headers), 'Units Sold', header_format)
ws.write_column(1, len(headers), units_sold, unlocked_format)

# Add "Revenue" column (Formula Hidden)
ws.write(0, len(headers) + 1, 'Revenue', header_format)

for row_num in range(1, len(data) + 1):
    price_cell = f'D{row_num + 1}'         
    units_cell = f'E{row_num + 1}'         
    formula = f'={price_cell}*{units_cell}'
    ws.write_formula(row_num, len(headers) + 1, formula, hidden_formula_format)  
 
ws.set_column('A:F', 15)    
    
ws.protect()    

wb.close()