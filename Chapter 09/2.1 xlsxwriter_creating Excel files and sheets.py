import xlsxwriter

wb = xlsxwriter.Workbook('toy_data.xlsx')
ws = wb.add_worksheet('products')

header_format = wb.add_format({'bold': True, 
                              'bg_color': '#DCE6F1', 
                              'font_color': '#223A54'})

headers = ['product_id', 'product_name', 'product_category', 'product_price']

# for col_num, header in enumerate(headers):
#     ws.write(0, col_num, header, header_format)
    
# Or
ws.write_row(row=0, col=0, data = headers, cell_format = header_format)    
    
wb.close()

# Row index 0 -> first row
# Col index 0 -> first columns


column_data = ['A001', 'A002', 'A003', 'A004']
ws.write_column('E2', column_data)  # Writes down from cell E2

analytics_ws = wb.add_worksheet('Analytics_Report')
analytics_ws.set_tab_color('#1072BA')

wb.close()