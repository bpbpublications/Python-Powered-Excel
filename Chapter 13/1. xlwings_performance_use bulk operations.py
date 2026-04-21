import pandas as pd
import numpy as np
import xlwings as xw
import time

n = 30_000
df = pd.DataFrame({
    "A": np.random.randn(n),
    "B": np.random.randn(n),
    "C": np.random.randint(0,100, size=n)
})

wb = xw.Book()          # opens a new Excel workbook
sheet = wb.sheets[0] 

#%%
start = time.time()
for idx, row in df.iterrows():
    sheet.range(f"A{idx + 1}").value = row["A"]
    sheet.range(f"B{idx + 1}").value = row["B"]
    sheet.range(f"C{idx + 1}").value = row["C"]

end = time.time()
print("Iterrows time:", time.time() - start) 

# This code will take long to run, have patience 
# or use shorter data size

#%%
sheet.clear()                # clear previous write

#%%
start = time.time()
sheet.range("A1").options(index=False).value = df
end = time.time()
print("Bulk write time:", time.time() - start) 

