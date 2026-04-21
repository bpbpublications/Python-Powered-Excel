import os
import pandas as pd
import matplotlib.pyplot as plt # need it to customize plots such as labels

os.getcwd() # Excel_Python folder created for the book

# As we will be reading  files from Data folder inside Excel_Python
# Setting working directory to Data Folder

data_path = os.path.join(os.getcwd(), 'Data')  # Data folder inside Excel_Python folder
os.chdir(data_path)

df = pd.read_csv('plotting_data.csv')

# Histogram Sales Distribution
df['Sales'].plot(kind='hist', bins=30, 
                 title='Sales Distribution')
# plt.show()   # If needed (will work only if matplotlib.pyplot is imported)

# Scatterplot Sales vs Profit
df.plot(kind='scatter', x='Sales', y='Profit', 
        alpha=0.5, title='Sales vs Profit', figsize=(7, 5))

# Bar chart region-wise sales
# region-wise sales data
sales_reg = (df
             .groupby('Region')['Sales']
             .sum())
sales_reg

#plot
(sales_reg
     .plot(kind='bar', title='Total Sales by Region', 
               ylabel='Sales', figsize=(7,4)))
# You can do in one step
(df
 .groupby('Region')['Sales']
 .sum()
 .plot(kind='bar', title='Total Sales by Region', 
       ylabel='Sales', figsize=(7,4)))


# Stacked bar chart_ Sales by Region and Category
(df
 .groupby(['Region', 'Category'])['Sales']
 .sum().unstack()
 .plot(kind='bar', figsize=(8,5), 
       title='Sales by Region and Category'))
# notive y axis has no labels

# Stacked bar chart_ Profit by Region and Category
# adding y label too, although titles says it but just to show you how to add labels
(df
 .groupby(['Region', 'Category'])['Profit'].sum()
 .unstack()
 .plot(kind='bar', stacked=True, 
       figsize=(8,5), ylabel = 'Profit',
       title='Profit by Region and Category'))

(df
 .groupby(['Region', 'Category'])['Profit'].sum()
 .unstack()
 .plot(kind='bar', stacked=True, 
       figsize=(8,5), title='Profit by Region and Category'))
plt.ylabel('Profit') # y label (although titles says it but just to show you how to add labels)

# Pie chart _ Category wise sales
(df
 .groupby('Category')['Sales'].sum()
 .plot(kind='pie', autopct='%1.1f%%', 
       title='Sales Share by Category', figsize=(6,6), 
       ylabel = '')) # Remove y-label

# Or
(df
 .groupby('Category')['Sales'].sum()
 .plot(kind='pie', autopct='%1.1f%%', 
       title='Sales Share by Category', figsize=(6,6))) 
plt.ylabel('')
 
# Boxplot
df.plot(kind = 'box', column='Sales', by='Region', 
           figsize=(8,5), ylabel = 'Sales', 
           title = 'Sales Distribution by Region')
# suptitle is there, which seems redundant

# alternate way
df.boxplot(column='Sales', by='Region', figsize=(8,5))
plt.title('Sales Distribution by Region')
plt.suptitle('') # Remove default title
plt.ylabel('Sales')

# Line chart_Sales Over Time
df.plot(x='Date', y='Sales', kind='line', 
        figsize=(8,5), title='Sales Over Time')

# Multi-line chart (sales and profit together) 
df.plot(x='Date', y=['Sales', 'Profit'], kind='line', 
        figsize=(8,5), title='Sales & Profit Over Time')


# Changing Date frequency to 'Monthly'
df['Date'] = pd.to_datetime(df['Date'])

monthly_data = df.set_index('Date').resample('ME').sum()
monthly_data.plot(y='Sales', kind='line', figsize=(8,5), 
                  title='Monthly Sales')

monthly_data.plot(y=['Sales','Profit'], kind='line', 
                  figsize=(8,5), title='Monthly Sales & Profit')

# If you need monthly data for a single column
monthly_sales = df.set_index('Date').resample('ME')['Sales'].sum()
monthly_sales.plot(kind='line', marker='o', figsize=(8,4), 
                   title='Monthly Sales Trend')
plt.ylabel('Sales')

# Resample monthly and group by Region
monthly_region = (df
                  .set_index('Date')
                  .groupby('Region')
                  .resample('ME')['Sales']
                  .sum()
                  .unstack('Region'))

# Multi-line Plot Monthly Sales for each Region
monthly_region.plot(figsize=(9,5), title='Monthly Sales by Region')
plt.ylabel('Sales')

# KDE plot needs scipy
# df['Sales'].plot(kind='kde') # needs scipy

# Backend for all these plots
pd.options.plotting.backend # 'matplotlib'
# for more customization options, check appendix
# or refer https://matplotlib.org/stable/tutorials/index