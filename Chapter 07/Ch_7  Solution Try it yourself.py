import pandas as pd
import numpy as np

# Exercise 1: 
    # to create synthetic dataset of 2000 rows 
# Reproducibility
np.random.seed(42)

# Define size
n = 2000

# Generate synthetic data
regions = ['North', 'South', 'East', 'West']
categories = ['Furniture', 'Office Supplies', 'Technology']

df = pd.DataFrame({
    'Region': np.random.choice(regions, size=n),
    'Category': np.random.choice(categories, size=n),
    'Sales': np.random.uniform(100, 1000, size=n).round(2),
    'Profit': np.random.uniform(-100, 300, size=n).round(2),
    'Date': pd.to_datetime(np.random.choice(pd.date_range('2022-01-01', '2023-12-31'), size=n))
})

     # a side-by-side bar chart using Plotly Express
import plotly.express as px

# Aggregate sales and profit by category
agg_df = df.groupby('Category')[['Sales', 'Profit']].sum().reset_index()

# Melt data to long format for grouped bar chart
long_df = agg_df.melt(id_vars='Category', value_vars=['Sales', 'Profit'], var_name='Metric', value_name='Amount')

# Create grouped bar chart
fig = px.bar(long_df, x='Category', y='Amount', color='Metric', barmode='group',
             title='Total Sales and Profit by Category')
fig.write_html('ex1.html')

     # a scatter plot using pandas with default backend
import matplotlib.pyplot as plt
df.plot.scatter(x='Sales', y='Profit', 
                     alpha=0.6, color='royalblue', figsize=(8, 5))

plt.show()

     # a density plot using pandas

df['Sales'].plot(kind='kde', color='darkorange', linewidth=2, figsize=(8, 4))


# --------------------------------------------------------
# Exercise 2: 
# Forecast Retirement Corpus Scenarios
import numpy_financial as npf
import pandas as pd
import matplotlib.pyplot as plt

    # required monthly investment
# Inputs
target_corpus = 2e7  # ₹2 crore
years = 25
periods = years * 12  # monthly
rate = 0.08  # Annual interest rate   
monthly_rate = rate / 12 
    
pmt = npf.pmt(rate=monthly_rate, nper=periods, pv=0, fv=-target_corpus)
print(f'Required monthly investment: {round(pmt, 2)}')

    #	Simulate the same for different interest rates
# Inputs
target_corpus = 2e7  # ₹2 crore
years = 25
periods = years * 12  # monthly
rates = [0.06, 0.08, 0.10]  # Annual interest rates

    # Calculate monthly contribution for different interest rates

results = []
for r in rates:
    monthly_rate = r / 12
    pmt = npf.pmt(rate=monthly_rate, nper=periods, pv=0, fv=-target_corpus)
    results.append((f"{int(r*100)}%", round(pmt, 2)))
    print(f'At interest rate {r}, required investment is {round(pmt, 2)}')
    

     # Create a simple line plot
# Convert to DataFrame for display and plotting
df = pd.DataFrame(results, columns=["Rate", "Monthly Investment"])
print(df)

# Plot
plt.figure(figsize=(6,4))
plt.bar(df["Rate"], df["Monthly Investment"], color='teal')
plt.title("Monthly Investment Needed for ₹2 Cr Retirement")
plt.ylabel("₹ per month")
plt.xlabel("Annual Return Rate")
plt.tight_layout()
plt.show()