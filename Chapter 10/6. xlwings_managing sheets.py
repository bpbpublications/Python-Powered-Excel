import xlwings as xw

wb = xw.Book('gaming.xlsx')
wb.sheet_names

ws2 = wb.sheets[1]

# Copy Sheet
ws2.copy(name='CopyRanks')

# Apply formatting
ws3 = wb.sheets['CopyRanks']

# Format header row
header = ws3.range('A1').expand('right')
header.font.bold = True
header.font.size = 12
header.color = (251, 226, 213)

# capturing the state before the destructive operation ---------------
# Backup values and formats
backup = ws2.range('A1').expand().value

# Clear cell contents (but keep formatting) 
ws3.clear_contents() 

# Restore if needed (to simulate undo) ----------
ws3.range('A1').expand().value = backup

# Clear cell contents and also formatting
ws3.clear()

# Delete Sheet
ws3.delete()

# Excel Sheet last row or column
ws2.cells.last_cell
ws2.cells.last_cell.row
ws2.cells.last_cell.column