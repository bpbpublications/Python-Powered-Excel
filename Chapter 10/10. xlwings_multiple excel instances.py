import xlwings as xw

# First Excel instance (opens a workbook)
app1 = xw.App(visible=True)
        

wb1 = app1.books.open('C:/path/to/file1.xlsx')
wb1.sheets[0]['A1'].value = 'Updated by Instance 1'

# Second Excel instance
app2 = xw.App(visible=True)
wb2 = app2.books.open('C:/path/to/file2.xlsx')
wb2.sheets[0]['A1'].value = 'Updated by Instance 2'



xw.apps.keys()        # List of running Excel instances
app1.pid              # Process ID of first Excel instance
app2.pid              # Process ID of second Excel instance
xw.apps.active.pid    # PID of the currently active Excel instance

# Save and close both
wb1.save()
wb2.save()
app1.quit()
app2.quit()


import xlwings as xw

# Create first Excel instance
app1 = xw.App(visible=True)
wb1 = app1.books.open('gaming.xlsx')

# Create second Excel instance
app2 = xw.App(visible=True)
wb2 = app2.books.open('xlwings_formula.xlsx')

app1.pid
app2.pid
xw.apps.keys()
xw.apps.active.pid

wb1 = app1.books.open('xlwings_formula.xlsx')
app1.quit()
app2.quit()