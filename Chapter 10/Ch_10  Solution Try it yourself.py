# Exercise 1: Manufacturing (Production Report) --------------

import xlwings as xw

wb = xw.Book()
sht = wb.sheets[0]

# Data
data = [
    ["Machine", "Units Produced", "Defects", "Efficiency"],
    ["M1", 1200, 12, 0.98],
    ["M2", 950, 20, 0.95],
    ["M3", 1500, 10, 0.99]
]
sht.range("A1").value = data

# Header formatting
header = sht.range("A1:D1")
header.font.bold = True
header.color = (0, 51, 102)        # Dark blue
header.font.color = (255, 255, 255)

# Percentage format
sht.range("D2:D4").number_format = "0.00%"

# Autofit
sht.range("A:D").autofit()

wb.close()

# Exercise 2: Web Testing (Bug Report) --------------------

import xlwings as xw

wb = xw.Book()
sht = wb.sheets[0]

# Data
bugs = [
    ["Bug ID", "Description", "Status", "Priority"],
    ["B101", "Login button not working", "Open", "High"],
    ["B102", "Page loads slowly", "Closed", "Medium"],
    ["B103", "Dropdown missing option", "Open", "Low"]
]
sht.range("A1").value = bugs

# Header bold
sht.range("A1:D1").font.bold = True

# Apply formatting row by row
for row in sht.range("A2:D4").rows:
    status = row[2].value
    priority = row[3].value
    
    if status == "Open":
        row.color = (255, 255, 153)  # Light yellow
    
    if priority == "High":
        row[3].font.bold = True
        row[3].font.color = (255, 0, 0)  # Red

sht.range("E1").value = 'Timestamp'
sht.range("E1").font.bold = True

# Adding time stamp column
import pandas as pd

timestamp_data = [pd.to_datetime("2025-09-01 08:00:00"),
                    pd.to_datetime("2025-09-01 08:05:00"),
                    pd.to_datetime("2025-09-01 08:10:00")]


sht.range('E2').options(transpose = True).value = timestamp_data
    
    
# Format timestamp
sht.range("E2").expand('down').number_format = "dd-mmm-yyyy hh:mm"

wb.close()