import xlwings as xw

# Open the macro-enabled workbook
vba_book = xw.Book("game_macro.xlsm")

# Grab the macros
greet = vba_book.macro("Module1.GreetPlayer")
double_score = vba_book.macro("Module1.DoubleScore")

# Call the Sub (shows message box in Excel)
greet("Python Learners!")

# Close the MessageBox first

# Call the Function (returns a value to Python)
new_score = double_score(150)
print("New doubled score:", new_score)

vba_book.sheets[0]['A1'].value = 150
vba_book.sheets[0]['B1'].value = double_score(vba_book.sheets[0]['A1'])

# Close the workbook
vba_book.close()