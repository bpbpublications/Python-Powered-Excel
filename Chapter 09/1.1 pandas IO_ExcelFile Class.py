import pandas as pd

file = pd.ExcelFile("demo_sales.xlsx")
# Read multiple sheets without reloading the file
df1 = file.parse("Customers") # Using sheet name
# or Using sheet index (0-based)
df1 = file.parse(0) # first sheet

df2 = file.parse(1)
df3 = file.parse(2)



# Sheet names
file.sheet_names
# Loop through all sheets
dfs = {sheet: file.parse(sheet) for sheet in file.sheet_names}
dfs.get('Sales_Jan')

# Using context manager
with pd.ExcelFile("demo_sales.xlsx") as file:
    df1 = file.parse("Customers") # with sheet name
    df2 = file.parse(1)      # or with sheet index
    df3 = file.parse(2)

# Next Example_Using in loop 
with pd.ExcelFile("demo_sales.xlsx") as file:
    all_dfs = []
    for sheet in file.sheet_names:
        if sheet.startswith('Sales'):    # only sales related sheets
            df = file.parse(sheet_name=sheet)
            df["sheet"] = sheet                     
            all_dfs.append(df)

combined = pd.concat(all_dfs, ignore_index=True)
print(combined)