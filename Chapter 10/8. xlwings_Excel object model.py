import xlwings as xw

Book = xw.Book() 
Sheet = Book.sheets['Sheet1']
Range = Sheet.range('A1:E6')

Book # <Book [Book1]>
Sheet # <Sheet [Book1]Sheet1>
Range # <Range [Book1]Sheet1!$A$1:$E$6>

# Alternately

xw.Book().sheets['Sheet1'].range('A1:E6')
# <Range [Book2]Sheet1!$A$1:$E$6>

# Climbing up the ladder --------------

Range.sheet # <Sheet [Book1]Sheet1>

Range.sheet.book # <Book [Book1]>

Range.sheet.book.app
Book.app

# Collection of active xlwings App objects
xw.apps
# List active xlwings App objects (keys are app identifiers)
xw.apps.keys()
# Get the process id (PID) of the currently active xlwings App
xw.apps.active.pid

with xw.App() as app:
    print(app.books)

# NOTE: 
    # By default, opening several workbooks (whether from Explorer, Excel UI, 
    # or via xw.Book() against the same xw.App) will place them in the same Excel process;
    # you will see one Excel.exe in Task Manager even though there are multiple workbook windows.


# If you create multiple excel instances -----------

app1 = xw.App(visible=True)

app2 = xw.App(visible=True)

# NOTE Continued: 
    # If you explicitly start separate Excel instances (launch Excel separately, 
    # or create separate xw.App() objects in xlwings), each instance runs 
    # in its own process and will appear as a separate Excel.exe in Task Manager.
