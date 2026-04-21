import os
import pandas as pd

os.getcwd() # Excel_Python folder created for the book

# As we will be reading  files from Data folder inside Excel_Python
# Setting working directory to Data Folder

data_path = os.path.join(os.getcwd(), 'Data')  # Data folder inside Excel_Python folder
os.chdir(data_path)

df = pd.read_csv('plotting_data.csv')

# Default pandas backend is matplotlib
pd.options.plotting.backend # matplotlib

df['Sales'].plot(kind='hist') # static plot

# Individual plot with plotly backend becomes interactive
fig = df['Sales'].plot(kind='hist', backend = 'plotly')
fig.write_html('myplot1.html')

# Using plotly backend
pd.options.plotting.backend = 'plotly' 
# Or
pd.set_option('plotting.backend', 'plotly')

# now backend is changed
pd.options.plotting.backend # 'plotly'

fig = df['Sales'].plot(kind='hist', bins=30, title='Sales Distribution')
fig.write_html("myplot2.html")


# Alternate way to display each plot directly in browser
# (without saving to html)

import plotly.io as pio
pio.renderers.default = "browser"   

df['Sales'].plot(kind='hist', bins=30, title='Sales Distribution')