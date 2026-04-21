import xlsxwriter

wb = xlsxwriter.Workbook('charts.xlsx')
ws = wb.add_worksheet('products')

header_format = wb.add_format({'bold': True, 
                              'bg_color': '#DCE6F1', 
                              'font_color': '#223A54',
                              'align': 'center'})

headers = ['product_id', 'product_name', 'product_category', 'product_price', 
           'Units Sold', 'Revenue']

ws.write_row(0, 0, headers, header_format)


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
    ws.write_row(row = row_num, col = 0, data = row_data)

units_sold = [5, 8, 15, 30, 6, 10, 20]
ws.write_column(1, 4, units_sold)

ws.set_column('A:F', 15)
        

for row_num in range(1, len(data) + 1):
    price_cell = f'D{row_num + 1}'         
    units_cell = f'E{row_num + 1}'         
    formula = f'={price_cell}*{units_cell}'
    ws.write_formula(row_num, 5, formula)  
    
    
# Create a column chart
chart = wb.add_chart({'type': 'column'})

# Configure the series: Units Sold (Column E), Product Names (Column B)
chart.add_series({
    'name':       'Units Sold',
    'categories': f'=products!$B$2:$B${len(data)+1}',  # Product Names
    'values':     f'=products!$E$2:$E${len(data)+1}',  # Units Sold
    'fill':       {'color': '#4F81BD'},
    'border':     {'color': '#1F497D'},
    'trendline':  {'type': 'linear', 'display_equation': True, 
                   'line': {'color': '#C00000',
                            'width': 2.25,
                            'dash_type': 'long_dash'}}
})

# Add chart title and axis labels
chart.set_title({'name': 'Units Sold by Products'})
chart.set_x_axis({'name': 'Units Sold'})
chart.set_y_axis({'name': 'Product Name'})

# Optional: Set chart style
chart.set_style(11)

# Insert the chart into the worksheet
ws.insert_chart('A10', chart, {'x_offset': 25, 'y_offset': 10})        


combo_chart = wb.add_chart({'type': 'column'})

# Revenue series
combo_chart.add_series({
    'name': 'Price',
    'categories': f'=products!$B$2:$B${len(data)+1}',
    'values':     f'=products!$D$2:$D${len(data)+1}',
    'fill':       {'color': '#4472C4'}
})

# Units Sold series (secondary axis)
combo_chart.add_series({
    'name': 'Units Sold',
    'categories': f'=products!$B$2:$B${len(data)+1}',
    'values':     f'=products!$E$2:$E${len(data)+1}',
    # 'y2_axis': True,
    'fill': {'color': '#ED7D31'}
})

combo_chart.set_title({'name': 'Price vs Units Sold'})
combo_chart.set_x_axis({'name': 'Product'})
combo_chart.set_y_axis({'name': 'values'})
# combo_chart.set_y_axis({'name': 'Price'})
# combo_chart.set_y2_axis({'name': 'Units Sold'})
ws.insert_chart('F10', combo_chart, {'x_offset': 25, 'y_offset': 10})


# Inserting image 

image = 'BPB_logo.png'
ws.insert_image('I2', image)

# Embedding image in a cell (only available in Excel 365 versions from 2023 onwards)
ws.embed_image('K2', image)

wb.close()        
