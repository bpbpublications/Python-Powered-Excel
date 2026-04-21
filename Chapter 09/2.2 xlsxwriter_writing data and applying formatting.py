import xlsxwriter

wb = xlsxwriter.Workbook('toy_data.xlsx')
ws = wb.add_worksheet('products')

header_format = wb.add_format({'bold': True, 
                              'bg_color': '#DCE6F1', 
                              'font_color': '#223A54'})

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
    
# Got more data /a new vaieble called units_sold 
units_sold = [5, 8, 15, 30, 6, 10, 20]

# header with formatting in a cell
ws.write(0, len(headers), 'Units Sold', header_format) 

# Writing data column-wise (starting row=1 since row=0 is header)
ws.write_column(1, len(headers), units_sold)
# write_col() fills down as many rows as needed

ws.set_column('A:E', 15)
        
wb.close()        