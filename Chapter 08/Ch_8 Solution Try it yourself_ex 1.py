import os
from openpyxl import Workbook

# 1. Create the folder named 'ABC'
folder_name = "new_department_logs"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")

# 2. Define small datasets for each file
datasets = {
    "electronics": [
     ("product_id", "product_name", "product_category", "product_price",  "Units Sold"), 
     (101, "Smartphone", "Electronics", 699.99, 120), 
     (102, "Bluetooth Speaker", "Electronics", 49.99, 200),
     (103, "Laptop", "Electronics", 999.99, 80)
     ],
    
    "fitness": [
     ("product_id", "product_name", "product_category", "product_price",  "Units Sold"), 
     (201, "Yoga Mat", "Fitness", 25, 150), 
     (202, "Dumbbelss Set", "Fitness", 45.99, 90),
     (203, "Fitness Tracker", "Fitness", 89.99, 60)
     ],
    
   "stationery":  [
     ("product_id", "product_name", "product_category", "product_price",  "Units Sold"), 
      (301, "Notebook", "Stationery", 3.99, 500), 
      (302, "Ballpoint Pen", "Stationery", 1.49, 1000),
      (303, "Desk Organizer", "Stationery", 12.99, 300)
      ]
}

# 3. Create 3 .xlsx files and write data
for name, rows in datasets.items():
    wb = Workbook()
    ws = wb.active
    ws.title = "products"

    # Write the data rows to the sheet
    for row in rows:
        ws.append(row)

    # Define the file path inside the 'ABC' folder
    file_name = f"{name}.xlsx"
    file_path = os.path.join(folder_name, file_name)

    # Save the file
    wb.save(file_path)
    print(f"Saved: {file_path}")

print("\nTask complete!")