# Export data to pdf/xlsm, xlsb

import xlwings as xw


wb = xw.Book()
ws = wb.sheets[0]

# Export in any format
wb.save('binaryfile.xlsb')
wb.save('macroenabled.xlsm')
wb.save('XLSfile.xls')

# Adding sheet data
ws['A1'].value = 'PDF'

# Exporting sheet data to PDF
ws.to_pdf()
# https://docs.xlwings.org/en/latest/api/book.html#xlwings.Book.to_pdf
# https://stackoverflow.com/questions/57724345/print-excel-to-pdf-with-xlwings    

# Adding another sheet
ws2 = wb.sheets.add()
ws2['A1'].value = 'Text in new sheet'

# Export Excel file as pdf
wb.to_pdf('PDFfile')