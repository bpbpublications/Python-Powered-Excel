import xlwings as xw
from datetime import datetime

# Open or create workbook
wb = xw.Book()  # Use existing file or create new
ws = wb.sheets['Sheet1']
ws.name = 'Scores'

# Sample gaming data
data = [
    ['Player', 'Score', 'Level', 'Last Login', 'Status'],
    ['Alex', 9200, 12, datetime(2025, 9, 10), 'Active'],
    ['Blake', None, 8, datetime(2025, 9, 5), 'Inactive'],
    ['Casey', 7800, 10, 'ERROR', 'Active'],
    ['Dana', 10200, 15, datetime(2025, 9, 12), 'Active']
]


# Write data
ws.range('A1').value = data

# Column Autofit
ws.range('A1').expand().columns.autofit()

# Format header row
header = ws.range('A1').expand('right')
header.font.bold = True
header.font.size = 12
header.color = (251, 226, 213)

# ws.tables.add(ws.range('A1').expand(), table_style_name='TableStyleMedium6')

# Format columns (Number & date formats)
ws.range('B2').expand('down').number_format = '#,##0'  # Score with comma
ws.range('D2').expand('down').number_format = 'dd-mmm-yyyy'  # Date format

# Font styling
ws.range('A2').expand('down').font.italic = True  # Player names italic

# Highlight error cells (Login column)
for cell in ws.range('D2').expand('down'):
    if isinstance(cell.value, str) and cell.value.upper() == 'ERROR':
        cell.color = (255, 0, 0)  # Red fill
        cell.font.color = (255, 255, 255)  # White text

# Column width _More customization
#Auto fit
ws.range('A1').expand().rows.autofit()

# custom width/height
ws.range('A:A').column_width = 20 
ws.range('2:5').row_height = 18

# Creating Excel table and styling it
tbl = ws.tables.add(ws.range('A1').expand(), 
                    name = 'MyTable',
                    table_style_name='TableStyleLight1')  

ws.tables

# If needed, save Excel file
# wb.save('formatting_report.xlsx')

# Close File
wb.close()