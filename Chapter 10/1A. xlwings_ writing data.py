import numpy as np
import pandas as pd
import xlwings as xw

# xw.Book()
# xw.books.active
# xw.books.active.close()

# Create Workbook, access sheet/sheet name, save ----------------------
wb = xw.Book() 
wb.name

wb.sheets
wb.sheet_names

ws1 = wb.sheets[0]
ws1 = wb.sheets['Sheet1']
ws1.name = 'Scores'

wb.save('gaming.xlsx')

# Accessing individual cell ----------------------------------

ws1.range('A1') # recommended and most flexible. 
# Supports chaining like .value, .color, .formula.
ws1.range(1, 1) # useful in calculation positioning and loops

ws1['A1']  # Clean, readable, convinient
ws1[0, 0]  # Useful in loops, USES ZERO_BASED indexing

ws1.cells(1,1) #  ONE_BASED indexing

# ws['A1'] and ws[0, 0] are just syntactic sugar.
#  Under the hood, they call range().
# This means everything xlwings can do with Excel ranges 
# (values, colors, formulas, resizing, expanding, merging, clearing, etc.) 
# is exposed consistently through range().

# print(ws1.range('A1').expand())
# print(ws1.range(1, 1).value)
# print(ws1['A1'].expand())
# print(ws1[0, 0].value)
# print(ws1.cells(1,1).value)

# Writing a scalar (single value) to a single cell
# Using cell notation
ws1.range('A1').value = 'PlayerA'
# or Using index
ws1.range(1, 2).value = 'PlayerB'
# B1 cell is row-0, col-1 (index starts with 0) wrong

# Writing a row using python list
players = ["PlayerC", "PlayerD", "PlayerE"]
ws1.range('C1').value = players   # writes across C1:E1

# If you need to force horizontal/vertical use options 

# writing a col using python list
scoreA = [105, 90, 98, 69, 85]
# Option 1: provide as nested list/list of lists (each inner list = row)
ws1.range('A2').value = [[v] for v in scoreA]  # writes down A2:A6

# Option 2: use .options(transpose=True)
scoreB = [75, 59, 38, 79, 26]
ws1.range('B2').options(transpose=True).value = scoreB  # writes down B2:B6


# Writing vertically from nested list
scores = [
    [110, 96, 83, 79, 86],
    [97, 99, 94, 89, 104],
    [120, 98, 102, 87, 118],
    ]
ws1.range('c2').options(transpose=True).value = scores # writes a block D1:F4

# wb.save()

ws2 = wb.sheets.add() # creates sheets in the beginning similar to Excel's insert sheet
wb.sheets[0]
wb.sheets[0].delete() # Permanently deletes sheet

# To create sheet after Scores sheet
ws2 = wb.sheets.add(name='Ranks', after=wb.sheets['Scores'])
ws2 = wb.sheets['Ranks']


# Writing from DataFrame
leaderboard = pd.DataFrame([
    ["PlayerA", 12500],
    ["PlayerB", 11840],
    ["PlayerC", 11010],
], 
    columns = ["Player", "TotalScore"],
    index = ['Rank1', 'Rank2', 'Rank3'])


ws2.range('A1').value = leaderboard 

wb.save()

# ws2.range('B1').clear_contents()  # Clears value in cell B1
# ws2.range('A1:C4').clear_contents()  # Clears values in a block
ws2.range('G1').options(header=False, index = False).value = leaderboard 

# Assigning names
ws1.range('A2').name = 'A_score2'
ws2.range('A1:C4').name = 'top_players'

wb.names

named_range = wb.names['top_players'].refers_to_range
named_range.value

wb.names['A_score2'].delete() # To delete a named range
wb.names['A_score2'].refers_to_range

ws2['A1']
ws2['A1'].expand()

ws2['A1'].expand('down')
ws2['A1'].expand('right')


# assigning named range using expand()
ws2['A1'].expand('right').name = 'variables'

ws2.range('A2').expand().value

ws2.range('A2').expand().options(pd.DataFrame, index=False).value
type(ws2.range('A2').expand().options(pd.DataFrame, index=False).value)

ws2.range('A1').value = 'Rank'
ws2.range('A1').api.Font.Bold = True
ws2.range('A1').api.Font.Color = 0x0000FF  # Blue
ws2.range('A1').api.Font.Size = 14
ws2.range('A1').api.Interior.Color = 0xFFFF00  # Yellow fill

ws2.range('C2').number_format = '#,##0.00'  # Comma-separated with 2 decimals

ws2['D2'].value = 5000

# Writing numpy array -----------------------------------

# match durations (float), 1D -> column
arr1d = np.array([120.5, 145.2, 160.0, 90, 180])   # minutes
ws1.range('G2').options(transpose=True).value = arr1d  # write as column H2:H5


# 2D NumPy array -> table
arr2d = np.array([
    [1, 120, 'PlayerA'],
    [2, 95, 'PlayerB'],
])
ws1.range('I2').value = arr2d  # writes 2 rows × 3 columns block

# Writing pandas series ----------------------------------
# Gaming example: in-game purchases per hour (Series)
s = pd.Series([10, 12, 8, 15], 
              index=['00:00','06:00','12:00','18:00'], 
              name='Purchases')
# Default writes only values
ws1.range('M2').value = s.values                # values only
# To keep index as a column, convert to DataFrame
df_from_series = s.reset_index()
ws1.range('M4').value = df_from_series.values   # index + values as block

# NOTE: You will understand this after learning about options and coverters in the next section
# ensure single-row list is treated as 1D, not split incorrectly
# row = [1,2,3]
# ws1.range('P2').options(ndim=1).value = row     # forces 1D behavior
# # Force transpose or shape:
# ws1.range('P4').options(transpose=True, ndim=1).value = row  # writes vertically

# Close File
wb.close()