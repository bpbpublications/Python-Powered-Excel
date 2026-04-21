import xlwings as xw

# Connect to the active Excel workbook
wb = xw.Book()      
app = wb.app

# --- Turn OFF expensive Excel features ---
app.screen_updating = False
app.calculation = 'manual'
app.display_alerts = False
app.enable_events = False

# --- Your fast operations ---
sheet = wb.sheets[0]
for i in range(1, 2000):
    sheet.range(i, 1).value = i   # 2000 write operations


# --- Turn everything back ON ---
app.screen_updating = True
app.calculation = 'automatic'
app.display_alerts = True
app.enable_events = True

wb.close()