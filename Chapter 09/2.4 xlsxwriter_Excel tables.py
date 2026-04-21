import xlsxwriter

wb = xlsxwriter.Workbook("tables_name.xlsx")
ws = wb.add_worksheet()

# Header
headers = ["Item", "Qty", "Price"]
ws.write_row(0, 0, headers)

# Data
rows = [
    ["Apple", 10, 0.5],
    ["Banana", 5, 0.3],
    ["Cherry", 20, 1.2],
]

for i, row in enumerate(rows, start=1):
    ws.write_row(i, 0, row)

# Add a table named "InventoryTable"
end_row = len(rows)      # data starts at row 1, header at row 0
end_col = len(headers) - 1

ws.add_table(0, 0, end_row, end_col, 
             {"name": "InventoryTable",
              "columns": [{"header": h} for h in headers]
})

# Adding more data
headers2 = ["SKU", "Name", "Category"]
rows2 = [
    ["SKU001", "Widget", "Gadgets"],
    ["SKU002", "Gizmo", "Gadgets"],
]

start_col = len(headers) + 2
ws.write_row(0, start_col, headers2)

for j, row in enumerate(rows2, start=1):
    ws.write_row(j, start_col, row)

# Writing another table named "ProductsTable"    
end_row2 = len(rows2)
end_col2 = start_col + len(headers2) - 1
ws.add_table(0, start_col, 
             end_row2, end_col2, 
             {"name": "ProductsTable",
              "columns": [{"header": h} for h in headers2]})


wb.close()