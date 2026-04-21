import xlwings as xw
import numpy as np
import pandas as pd

wb = xw.Book('gaming.xlsx')
ws1 = wb.sheets[0]

# Accessing cell, row, col, ranges -----------------

# Using range() method -------
ws1.range('A1')
ws1.range(1, 1) # 1-based index
ws1.range('A1:E5')
ws1.range((2, 2), (3, 4)) # B2:D3
# starting cell: row 2, column 2 → B2 and ending cell: row 3, column 4 → D3

# Slicing ------------
ws1.range('A1:E5')[1, 1]
ws1.range((2, 2), (3, 4))[:, 1]

ws1['A1:E5'][1, 1]
ws1[1:3, 1:4][1, 1]

# Using cell notation (without range) ------
ws1['A1']
ws1['A1:E5']

# Using index (without range) -------
ws1[0, 0] # 0-based index
ws1[1:3, 1:4] # B2:D3
# rows 2 to 3 (Python index 1 and 2) and columns B to D (Python index 1, 2, 3)

# Reading data  -----------------

ws1.range('A1').value      # scalar
ws1.range('A1:A7').value   # list
ws1.range('A1:E1').value   # list

# options method ------

# list with blank cell as None
ws1.range('A1:A7').value  
# replacing blank cell with 'unknown'
ws1.range('A1:A7').options(empty = 'Unknown').value 

# ndim=1: FORCE everything into a 1D flat list
ws1.range('A1').options(ndim=1).value    # list
ws1.range('A1:A7').options(ndim=1).value #  list_no change
ws1.range('A1:E1').options(ndim=1).value #  list_no change  

# ndim=2: FORCE everything into 2D nested lists (preserve orientation)
ws1.range('A1').options(ndim=2).value   # nested-list
ws1.range('A1:A7').options(ndim=2).value #  nested-list: column
ws1.range('A1:E1').options(ndim=2).value  # nested-list: : row

# ndim='natural': SMART behavior - preserves vertical orientation only
ws1.range('A1').options(ndim='natural').value 
ws1.range('A1:E1').options(ndim='natural').value 
ws1.range('A1:A7').options(ndim='natural').value 

# expand
ws1.range('A1').options(expand = 'table').value
ws1.range('A1').options(expand = 'right').value
ws1.range('A1').options(expand = 'down').value
# same as
ws1.range('A1').expand().value
ws1.range('A1').expand('right').value
ws1.range('A1').expand('down').value

ws1.range('A2').value
type(ws1.range('A2').value) # float by default

ws1.range('A2').options(numbers = int).value
type(ws1.range('A2').options(numbers = int).value) # int

# Converters ------

# numpy array
ws1.range('A1').options(np.array).value       # 0-D
ws1.range('A1:A7').options(np.array).value    # 1-D
ws1.range('A1:A7').options(np.array, ndim = 2).value  #2-D

# pandas dataframe
ws1.range('A1:E6').options(pd.DataFrame, index = False).value

# More verbose
ws1.range('A1:E6').options('df', expand='table', index = False).value

ws1.range('A1:E6').options('df', index = False).value

# Dictionary Converter
ws2 = wb.sheets[1]
ws2.range('B2:C4').options(dict).value

ws1.range('A1:B2').options(dict, transpose=True).value

# Close File
wb.close()