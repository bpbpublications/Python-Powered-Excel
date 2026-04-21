# Extra code for rank, vlookup etc

import xlwings as xw

# Load workbook and sheets
wb = xw.Book('gaming.xlsx')
ws1 = wb.sheets['Scores']
ws2 = wb.sheets['Ranks']

# ws1.range('G2:P7').clear_contents()


# === Sheet1: Add Total and Average for each Player ===

# Write headers
ws1.range('F1').value = 'Total'
ws1.range('G1').value = 'Average'
    
# SUM formulas in single cell ----
ws1.range('F2').formula = '=SUM(A2:E2)'


# Using f-strings to create dynamic formulas for each cell in F col
for i in range(3, 7):
    ws1.range(f'F{i}').formula = f'=SUM(A{i}:E{i})'
    
for i in range(2, 7):
    ws1.range(f'G{i}').formula = f'=AVERAGE(A{i}:E{i})'    

# To read formula again
ws1.range("G3").formula

# To fetch column name
xw.utils.col_name(2)

# Using it to find column-wise SUM and AVERAGE -------------

# Apply formulas for each player (columns B to F)
for col in range(1, 7):  # Columns B to F (PlayerA to PlayerE)
    col_letter = xw.utils.col_name(col)
    ws1.range(f'{col_letter}8').value = f'=SUM({col_letter}2:{col_letter}6)'
    ws1.range(f'{col_letter}9').value = f'=AVERAGE({col_letter}2:{col_letter}6)'
    
# Dynamic Array Formula (Excel 365) -------------

# values from the row, which are greater than 100
ws1.range('I2').formula2 = '=FILTER(A2:E2, A2:E2 > 100)' 


# # Old way (will only produce one value_NO spill in older Excel
# Will work in Excel 365_double click 

# ws1.range('T2').formula_array = '=FILTER(A2:E2, A2:E2 > 100)'    


# BYROW - Average each row
ws1['M2'].formula2 = '=BYROW(A2:E6, LAMBDA(row, AVERAGE(row)))'

# BYCOL - Average each col
ws1['A11'].formula2 = '=BYCOL(A2:E6, LAMBDA(row, AVERAGE(row)))'

# LAMBDA - Classify scores  
ws1['O2'].formula2 = '''=MAP(A2:E6, 
    LAMBDA(x, IF(x>=100, "High", IF(x>=80, "Medium", "Low"))))'''    

# Returns the address of the range in the specified format
ws1['A1'].get_address()
ws1['A1'].get_address(False, False)
ws1['A1'].get_address(False, True)

ws1['A2:E6'].get_address()
ws1['A2:E6'].get_address(True, False)
ws1['A2:E6'].get_address(True, False, True)
ws1['A2:E6'].get_address(True, False, True, external=True)


# If needed, save Excel file
wb.save('xlwings_formula.xlsx')

# Close File
wb.close()
