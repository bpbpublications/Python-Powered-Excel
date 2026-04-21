import matplotlib

print(matplotlib.__version__) 


import pandas as pd
import matplotlib.pyplot as plt # need it to customize plots such as labels


df = pd.read_csv('plotting_data.csv')
df.info()

df['Date'] = pd.to_datetime(df['Date'])

# Bar chart
df.groupby('Region')['Profit'].mean().reset_index()
plt.bar(x = df['Region'], height=df.groupby('Region')['Profit'].mean())

# Bar chart region-wise sales
# preparing data
sales_reg = (df
             .groupby('Region')[['Sales', 'Profit']]
             .sum()
             .sort_values(by = 'Sales', ascending=False)
             .reset_index())
sales_reg

# chart
plt.bar(x = sales_reg['Region'], height = sales_reg['Sales'])
plt.title("Region-wise Sales")

# Stacked bar chart                                                    
plt.bar(sales_reg['Region'], sales_reg['Sales'], label="Sales")
plt.bar(sales_reg['Region'], sales_reg['Profit'], 
        bottom=sales_reg['Sales'], label="Profit")

plt.title("Region-wise Sales & Profits")
plt.legend()
# Use df.plot(kind="bar", stacked=True)  or sns.barplot()
# for a direct stacked bar chart without multiple plt.bar() calls

# Pie chart _ Category wise sales
cat_sale = (df
             .groupby('Category')['Sales']
             .sum()
             .reset_index())

# chart
plt.pie(x = cat_sale['Sales'], labels = cat_sale['Category'], 
        autopct='%1.1f%%')
plt.title('Sales Share by Category')

# Example2
# Pie Chart_Sales Share by Region
plt.pie(x = sales_reg['Sales'], labels = sales_reg['Region'],
        autopct='%1.1f%%')
plt.title('Sales Share by Region')

# Histogram_Sales Distribution
plt.hist(df['Sales'], bins=30)
plt.title('Sales Distribution', 
          loc = 'left',       # font alignment
          fontsize=16,        # font size
          color="royalblue",   # font color
          fontname="Arial")   # font family


# Using desnities instead of frequencies
plt.hist(df['Sales'], bins=30, density= True)

# Boxplot _Sales Distribution
plt.boxplot(df['Sales'])

# Violin plot _Sales Distribution
plt.violinplot(df['Sales'])

# Line chart_Sales Over Time
plt.plot(df['Date'], df['Sales'])
plt.title('Sales Over Time')

# If you need monthly data for a single column
monthly_sales = (df
                 .set_index('Date')
                 .resample('ME')['Sales']
                 .sum()
                 .reset_index())

monthly_sales

plt.plot(monthly_sales['Date'], monthly_sales['Sales'])
plt.title('Sales Over Time')

# Multi-line chart (sales and profit together) 
monthly_sales = (df
                 .set_index('Date')
                 .resample('ME')[['Sales', 'Profit']]
                 .sum()
                 .reset_index())

monthly_sales

plt.plot(monthly_sales['Date'], monthly_sales['Sales'], label = 'Sales')
plt.plot(monthly_sales['Date'], monthly_sales['Profit'], label = 'Profit')
plt.title('Sales Over Time')
plt.legend()

# Learn More:
    # https://matplotlib.org/stable/users/index
    # https://matplotlib.org/stable/tutorials/index.html
    # https://seaborn.pydata.org/tutorial.html