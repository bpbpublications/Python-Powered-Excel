import pandas as pd
import matplotlib.pyplot as plt
import xlwings as xw

# Load workbook and sheets
wb = xw.Book('gaming.xlsx')
ws1 = wb.sheets['Scores']
ws2 = wb.sheets['Ranks']

# === Bar Chart: Total Scores by Player ===
bar_chart = ws2.charts.add(top = ws2.range('E2').top, 
                           left = ws2.range('E2').left)
bar_chart.chart_type = 'column_clustered'
bar_chart.set_source_data(ws2.range('B1:C4'))  # Hardcoded data range Player vs TotalScore

bar_chart.width = 500
bar_chart.height = 250

bar_chart.name
bar_chart.parent

# Delete Chart
bar_chart.delete()

# Creating again using dynamic range
bar_chart = ws2.charts.add(top = ws2.range('E2').top, 
                           left = ws2.range('E2').left)
bar_chart.chart_type = 'column_clustered'
bar_chart.set_source_data(ws2.range('B1').expand()) 

# Export Chart and data as pdf/png
bar_chart.to_pdf('ExportedByxlwings.pdf')
ws2.range('B1').expand().to_pdf('ChartDataExported.pdf')
ws2.range('B1').expand().to_png('ChartDataExported.png')

# === Line Chart (defining position later): Player Performance Over Rounds === 
line_chart = ws1.charts.add()
line_chart.chart_type = 'line_markers'
line_chart.set_source_data(ws1.range('A1').expand())
line_chart.name = 'PerformanceTrend'
line_chart.top = ws1.range('G2').top
line_chart.left = ws1.range('G2').left
line_chart.width = 500
line_chart.height = 300

# Add matplotlib figure (multiple approaches are there)

# Approach1: via PyPlot interface
df = ws2.range('A1').expand('table').options(pd.DataFrame).value
fig = plt.figure()
plt.bar(df['Player'], df['TotalScore'])

ws2.pictures.add(fig, top = ws2.range('E18').top, 
                           left = ws2.range('E18').left)

# # Approach2: Also via PyPlot interface
plt.bar(df['Player'], df['TotalScore'])
fig = plt.gcf()
ws2.pictures.add(fig, top = ws2.range('E18').top, 
                           left = ws2.range('E18').left)

# Approach3: via pandas:
ax = df.plot(x = 'Player', y = 'TotalScore', kind = 'bar')
fig = ax.get_figure()
ws2.pictures.add(fig, top = ws2.range('E18').top, 
                           left = ws2.range('E18').left)

# Add plotly static chart
import plotly.express as px

fig = px.bar(df, x = 'Player', y = 'TotalScore')
ws2.pictures.add(fig, top = ws2.range('N2').top, 
                           left = ws2.range('N2').left)


# Add image from file
# It can be chart exported from other libraries or any other image 
# in format that your Excel version supports. 

image = r'path/to/image.png'            # Replace with your actual image path

ws2.pictures.add(
    image= image,       
    name='GameLogo',                    # Optional name for the image
    left=ws2.range('A19').left,           # Position relative to cell G2
    top=ws2.range('A19').top,
    width=200,                          # Optional: resize image
    height=100,
    update=True                         # Replace if image with same name exists
)

ws2.pictures # All Pictures in sheet ws2

# If needed, save Excel file
# wb.save('xlwings_chart.xlsx')

# Close File
wb.close()