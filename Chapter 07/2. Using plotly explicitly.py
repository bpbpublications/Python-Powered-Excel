import os
import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'browser'

os.getcwd() # Excel_Python folder created for the book

# As we will be reading  files from Data folder inside Excel_Python
# Setting working directory to Data Folder

data_path = os.path.join(os.getcwd(), 'Data')  # Data folder inside Excel_Python folder
os.chdir(data_path)
df = pd.read_csv('plotting_data.csv')

# Line Chart
px.line(df, x='Date', y='Profit',
              title='Profit Over Time')

# Multi-line Chart
px.line(df, x='Date', y=['Profit', 'Sales'],
              title='Profit Over Time')

# Scatter Chart 
px.scatter(df, x='Sales', y='Profit',
           title='Sales vs Profit', opacity = 0.5)
# opacity is like alpha in matplotlib, it sets transperency

# Violin Chart
px.violin(df, x='Region', y='Profit', 
                box=True, points='outliers', 
                title='Profit Distribution by Region')

# Data for pie chart/bar chart
reg_profit = df.groupby('Region')['Profit'].sum().reset_index()
reg_profit

# Pie Chart
px.pie(reg_profit, names ='Region', values = 'Profit',
             title='Region Profit Comparision', hole = 0.4)

# Bar Chart
px.bar(reg_profit, x='Region', y='Profit',
             title='Region Profit Comparision')

# Animated bar chart

# Preparing data
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Month'] = df['Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby(['Month', 'Region'])['Sales'].sum().reset_index()
monthly_sales.head()

# chart
px.bar(monthly_sales,
              x='Region', y='Sales',
              animation_frame='Month',
              color='Region',
              title='Monthly Sales by Region (Animated)')

# More info ----------------------------------------
# Or if you do not set pio.renderers.default = 'browser'
# Restart kernel and then run the following code
import pandas as pd
import plotly.express as px

df = pd.read_csv('plotting_data.csv')

fig = px.scatter(df, x='Sales', y='Profit', title='Sales vs Profit',
                   opacity = 0.5)

# write fig object to HTML
fig.write_html('scatterPlot.html')   

# Then open manually from file location or run this code
import webbrowser
webbrowser.open("scatterPlot.html")