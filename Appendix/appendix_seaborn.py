import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt # need it to customize plots such as labels


df = pd.read_csv('plotting_data.csv')
df.info()

df['Date'] = pd.to_datetime(df['Date'])

# Charts for categorical data -------------------------

# Bar chart _ region
# notice you do not need to prepare data bar charts
sns.countplot(data=df, x='Region')

# Alternate way
sns.barplot(data=df, x='Region', y=df.index)

sns.catplot(data=df, x='Region', kind='count')

# Bar chart _ region-wise sales
sns.countplot(data=df, x='Region', hue='Category')

# Another way
sns.barplot(data = df, x='Region', y='Sales')

# Another way
sns.catplot(data=df, x='Region', y='Sales', kind='bar')


# NOTE: 
    # sns.countplot() is preferable when you just want the count of rows
    # E.g., number of orders per region
    # sns.barplot() is used when you have a numeric column (like Sales, Profit)
    # It shows the average (mean) by default for each category
    # E.g., average sales per region
    # (sns.catplot(kind="bar") is also commonly used, as a high level wrapper
    

# Stacked Bar Chart_ Sales by Region and Category
sns.barplot(data = df, x='Region', y='Sales', 
            hue='Category')

# Another way
sns.catplot(data = df, x='Region', y='Sales', 
            hue='Category', kind = 'bar')

# Faceting_One chart per Category
sns.catplot(data=df, x='Region', y='Sales',
    col='Category', kind='bar')

# Setting Title, Suptitle and Axis labels
g = sns.catplot(data=df, x='Region', y='Sales',
    col='Category', kind='bar')

g.set_titles("{col_name}")
g.set_axis_labels("", "Sales")
g.fig.suptitle("Sales by Region (Faceted by Category)", y=1.05)

# Using facet grid 
g = sns.FacetGrid(df, col='Category')
g.map_dataframe(sns.barplot, x='Region', y='Sales')

# Charts for numerical distributions ----------------------

# Histogram_Sales Distribution
sns.histplot(df, x = 'Sales', bins = 30)
sns.histplot(data=df, x='Sales', bins=20, kde=True)

# Histogram_Sales Distribution for different regions
sns.histplot(df, x = 'Sales', 
             bins = 30, hue = 'Region')

# Density plot_Sales Distribution
sns.kdeplot(df, x = 'Sales')

# Sales Distribution for different regions
sns.kdeplot(df, x = 'Sales', 
            hue = 'Region')

sns.kdeplot(df, x = 'Sales', 
                hue = 'Region', fill=True)

# Many options are there, choose the one that make sense for the data and objective
sns.kdeplot(df, x = 'Sales', 
            hue = 'Region', multiple='fill')

sns.kdeplot(df, x = 'Sales', 
            hue = 'Region', multiple='stack')


# Boxplot _Sales Distribution
sns.boxplot(df, y = 'Sales')
sns.boxenplot(df, y = 'Sales')

# Sales Distribution for different regions
sns.boxplot(df, y = 'Sales', 
            hue = 'Region', gap = 0.5, fill = False)
plt.tight_layout() # auto-adjust spacing to prevent overlap


# Boxen plot
sns.boxenplot(df, y = 'Sales', 
            hue = 'Region', gap = 0.5, fill = False)

# Violin plot _Sales Distribution
sns.violinplot(df, y = 'Sales')

# Sales Distribution for different regions
sns.violinplot(df, y = 'Sales', x = 'Region')
sns.violinplot(df, y = 'Sales', hue = 'Region')

sns.violinplot(data=df, hue='Region', y='Sales', inner='quartile')
plt.tight_layout()

ax = sns.violinplot(data=df, hue='Region', y='Sales', inner='quartile')
# ax.legend(loc='upper right')
ax.legend(
    title='Region',
    fontsize=7,
    title_fontsize=9,
    loc='center left',
    bbox_to_anchor=(0.02, 0.85)
)

# Swarmp plot
sns.swarmplot(df, x='Region', y='Sales')

# Line chart_Sales Over Time
sns.lineplot(data = df, x = df['Date'], y = df['Sales'])


# Scatterplot
sns.scatterplot(df, x = 'Sales', y = 'Profit')
sns.scatterplot(df, x = 'Sales', y = 'Profit', 
                hue='Region', alpha = 0.5)

sns.scatterplot(df, x = 'Sales', y = 'Profit', 
                hue='Region', size='Category', alpha = 0.5)

# Scatterplot Matrix
sns.pairplot(df)
sns.pairplot(df.iloc[:, 2:]) # ??? 1: as extra unnamed column to be removed from the data after checking prev chapter code
sns.pairplot(df, vars=['Sales', 'Profit', 'Quantity'])

# heatmap 
corr = df[['Sales', 'Profit', 'Quantity']].corr() 
sns.heatmap(corr, annot=True, cmap='coolwarm') # Useful when you have too many numerical variables
plt.title('Correlation Matrix')

# Line Chart _ Sales pattern over time
sns.lineplot(data = df, x = 'Date', y = 'Sales') # Cluttered
plt.xticks(rotation=45) # rotate x-axis labels for readability
plt.title('Daily Sales Pattern')
plt.xlabel("")
plt.ylabel("")
sns.despine()


# You can plot monthly or quaterly data
monthly_sales = (
    df
    .set_index('Date')
    .resample('ME')['Sales']
    .sum()
    .reset_index()
)

sns.lineplot(data=monthly_sales, x='Date', y='Sales')
plt.xticks(rotation=45)
plt.title('Monthly Sales Pattern')
plt.xlabel("")
plt.ylabel("")
sns.despine()


quaterly_sales = (
    df
    .set_index('Date')
    .resample('QE')['Sales']
    .sum()
    .reset_index()
)

sns.lineplot(data=quaterly_sales, x='Date', y='Sales')
plt.xticks(rotation=45)

# Basic line plot features _may not be useful here
sns.lineplot(data = df, x = 'Date', y = 'Sales', 
             marker='o', linewidth=0.5)
plt.title('Sales Over Time')

# Calculate 7-day moving average
df['Sales_MA7'] = df['Sales'].rolling(window=7).mean()

# Plot raw sales vs moving average
plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Sales'], label='Daily Sales', alpha=0.5)
plt.plot(df['Date'], df['Sales_MA7'], label='7-Day Moving Average', color='red')
plt.title("Sales with 7-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()


# More Examples 

df_ma = (
    df.set_index('Date')
      .resample('ME')['Sales']
      .sum()
      .rolling(3)
      .mean()
      .reset_index()
)

sns.lineplot(data=df_ma, x='Date', y='Sales')
plt.xticks(rotation=45)

# To compare same period across years (YoY trend)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

sns.lineplot(data=df, x='Month', y='Sales', hue='Year')

# To compare march sale_every year
# Example: compare March sales across years
march_sales = (df[df['Month'] == 3]
               .groupby('Year')['Sales']
               .sum())
print(march_sales)



df['is_weekend'] = df['Date'].dt.weekday >= 5

sns.scatterplot(
    data=df,
    x='Date',
    y='Sales',
    hue='is_weekend'
)

peak = df.loc[df['Sales'].idxmax()]

plt.annotate(
    'Peak Sales',
    xy=(peak['Date'], peak['Sales']),
    xytext=(peak['Date'], peak['Sales'] + 200),
    arrowprops=dict(arrowstyle='->')
)


# Multi-line Chart

sns.lineplot(data=df, x='Date', y='Sales', 
             hue='Region', alpha = 0.5, palette='tab10') # Cluttered, right?
plt.xticks(rotation=45)


# Correlation Heatmap
corr = df[['Sales', 'Profit', 'Quantity']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

# Learn More:
    # https://matplotlib.org/stable/users/index
    # https://matplotlib.org/stable/tutorials/index.html
    # https://seaborn.pydata.org/tutorial.html
