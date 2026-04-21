import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet("Demo")

# Write some data
ws.write(0, 0, "Product")
ws.write(0, 1, "Quantity")
ws.write(0, 2, "Price")

ws.write(1, 0, "Apples")
ws.write(1, 1, 10)
ws.write(1, 2, 2.5)

ws.write(2, 0, "Bananas")
ws.write(2, 1, 5)
ws.write(2, 2, 1.8)

# Save as legacy .xls
wb.save("sales_report.xls")


# Applying formatting

ws = wb.add_sheet("Report")

# Define a bold style
bold_style = xlwt.easyxf('font: bold on; align: horiz center')

# Define a currency style
currency_style = xlwt.easyxf(num_format_str= "$#,##0.00")

# Header row
ws.write(0, 0, "Item", bold_style)
ws.write(0, 1, "Cost", bold_style)

# Data with formatting
ws.write(1, 0, "Laptop")
ws.write(1, 1, 1200, currency_style)

ws.write(2, 0, "Monitor")
ws.write(2, 1, 300, currency_style)

wb.save("formatted_report.xls")

# Inserting a formula

ws = wb.add_sheet("Data")

ws.write(0, 0, "Value1")
ws.write(0, 1, "Value2")
ws.write(0, 2, "Sum")

# Data
ws.write(1, 0, 10)
ws.write(1, 1, 20)

# Formula (calculated by Excel when opened)
ws.write(1, 2, xlwt.Formula("A2+B2"))

wb.save("formula_example.xls")
