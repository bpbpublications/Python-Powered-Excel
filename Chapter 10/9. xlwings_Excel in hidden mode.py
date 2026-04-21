import xlwings as xw

# Start Excel in hidden mode
app = xw.App(visible=False)
wb = app.books.open('gaming.xlsx')

# Do something quietly
wb.sheets[0]['A20'].value = 'Updated by Python'

# Save and close
wb.save('updated_new.xlsx')
app.quit()