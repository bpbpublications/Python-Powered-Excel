import pandas as pd
import numpy as np
import time
import gc

# 1. Load only required columns and rows ----------------------------
# Loading full data 
start = time.time()
df_full = pd.read_csv("sales_data.csv")
end = time.time() # 0.93 sec

print(f"⏱️ Time taken: {end - start:.2f} sec") # ⏱️ Time taken: 0.72 sec
print("Meomory usage: \n")
df_full.info(memory_usage="deep") # 224.6 MB

# Loading less data
start = time.time()
df_sel = pd.read_csv("sales_data.csv", 
                  usecols=["Date", "Region", "Revenue"], 
                  nrows=100_000)
end = time.time()

print(f"⏱️ Time taken: {end - start:.2f} sec") # ⏱️ Time taken: 0.08 sec
print("Meomory usage: \n")
df_sel.info(memory_usage="deep") # 13.9 MB

# 2. Use Efficient Data Types ----------------------------

print(f"🔍 Before downcasting: {df_full.memory_usage(deep=True).sum() / (1024*1024):.1f} MB") # 224.6

df_downcast = df_full.copy()

# Step 1: Downcast numeric columns all at once
numeric_cols = ['Quantity', 'UnitPrice', 'Revenue', 'Profit', 'Bonus']
df_downcast[numeric_cols] = (df_downcast[numeric_cols]
                             .apply(pd.to_numeric, downcast='float'))

# Step 2: Convert object columns with repeated labels to category
cat_cols = ['Region', 'Product']
df_downcast[cat_cols] = df_downcast[cat_cols].astype('category')

# Step 3: Convert Date column to datetime (for accurate time ops)
df_downcast['Date'] = pd.to_datetime(df_downcast['Date'], errors='coerce')

print(f"✅ After downcasting: {df_downcast.memory_usage(deep=True).sum() / (1024*1024):.1f} MB") # 28.6

del df_full
del df_downcast
gc.collect()

# import pandas_downcast # (if it is installed)
# df_auto_down = df_full.pipe(pandas_downcast.downcast)  # Automatically reduces memory
# df_auto_down.info(memory_usage="deep") 


# Chunking -------------------------------------------------

# Reading full data
start = time.time()
df_full = pd.read_csv("sales_data.csv")
df_full_filtered = df_full[df_full["Revenue"] > 7000]
end = time.time()

print(f"Total time taken_No chunking : {end - start:.2f} seconds") # 0.98 seconds
# 1.35 sec

# Chunked Reading
chunk_size = 200_000
filtered_data = pd.DataFrame()
start = time.time()
# Read in chunks and measure memory per filtered chunk
for chunk in pd.read_csv("sales_data.csv", chunksize=chunk_size):
    filtered = chunk[chunk["Revenue"] > 7000]
    filtered_data = pd.concat([filtered_data, filtered])
    
end = time.time()
print(f"Total time taken: {end - start:.2f} seconds") # 1.13 seconds


# For moderately sized datasets, loading the entire file at once is convenient.
# However, as file sizes grow, chunking helps to control 
# memory usage and avoid system slowdowns or crashes. 
# While chunking may take slightly longer to execute, it enables 
# reliable analysis of datasets far larger than what Excel can handle.

# Sparse Series -----------------------------------------------

df_full["Bonus"].value_counts()

print(df_full["Bonus"].memory_usage(deep=True)/(1024*1024)) # 7.63MB


df_full["Bonus_sparse"] = df_full["Bonus"].astype(pd.SparseDtype("float", fill_value=0.0))


print(df_full["Bonus_sparse"].memory_usage(deep=True)/(1024*1024)) # 5.72 MB


# Vectorized Operation --------------------------------------

# Slow way list comprehension/apply/map
def label_profit(val):
    return "High" if val > 500 else "Low"

start = time.time()
# df_full["ProfitLabel_loop"] = [label_profit(x) for x in df_full["Profit"]]
df_full["ProfitLabel_map"] = df_full["Profit"].map(label_profit)
end = time.time()

print(f"Loop time: {end - start:.2f} seconds") # 0.16

# Fast vectorized way _Using Numpy
start = time.time()
df_full["ProfitLabel_vec"] = np.where(df_full["Profit"] > 500, "High", "Low")
end = time.time()

print(f"Vectorized time: {end - start:.2f} seconds") # 0.08



gc.collect()  # Reclaim memory 3161
