import xlrd
from xlutils.copy import copy

rb = xlrd.open_workbook("finance_data.xls")  # read-only
wb = copy(rb)                               # make a writable copy
ws = wb.get_sheet(0)
ws.write(1, 2, "Updated Value")
wb.save("finance_data_updated.xls")