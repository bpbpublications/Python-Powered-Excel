import xlwings as xw

# Open the macro-enabled workbook
wb = xw.Book(r"game_macro_more.xlsm")

# 1. From Standard Module (works fine)
greet = wb.macro("Module1.GreetPlayer")
double_score = wb.macro("Module1.DoubleScore")

greet("Alex")                      # Shows message box
print(double_score(10))            #  Prints 20.0

# 2. From Sheet1 Module
greet_sheet = wb.macro("Sheet1.GreetPlayerSheet")
double_score_sheet = wb.macro("Sheet1.DoubleScoreSheet")

greet_sheet("Maya")                #  Shows message box
print(double_score_sheet(10))      #  Will NOT return value to Python (None)


# 3. From ThisWorkbook Module
greet_wb = wb.macro("ThisWorkbook.GreetPlayerWB")
double_score_wb = wb.macro("ThisWorkbook.DoubleScoreWB")

greet_wb("Sam")                    #  Shows message box
print(double_score_wb(10))         #  Will NOT return value to Python (None)

# Grab the wrapper macro
double_score_fixed = wb.macro("Module1.DoubleScoreSheetWrapper")

# Call it
print(double_score_fixed(15)) 