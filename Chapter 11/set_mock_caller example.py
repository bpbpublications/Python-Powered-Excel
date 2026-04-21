import xlwings as xw

# Load the workbook you want to simulate as the caller
wb = xw.Book("Book1.xlsx")

# Set it as the mock caller
wb.set_mock_caller()

# Now your function can use Book.caller() as if it was triggered from Excel
def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    sheet.range("A1").value = "Hello from mock_caller!"

# Run the function manually
main()
