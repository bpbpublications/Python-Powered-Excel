import os
import pandas as pd

os.getcwd() # Excel_Python folder created for the book

# As we will be reading files from Data folder inside Excel_Python
# Setting working directory to Data Folder

data_path = os.path.join(os.getcwd(), 'Data')  # Data folder inside Excel_Python folder
os.chdir(data_path)

df = pd.read_excel('YT_data.xlsx', index_col='Video Id')

# Rename columns to shorter, consistent, and code-friendly names

# Rename columns: short, lowercase, and consistent
df.rename(columns={
    'Video Title': 'title',
    'Playlist Name': 'playlist',
    'Video Duration (Mins)': 'duration_min',
    'Video_Publish_Date': 'published',
    'Watch Time (Mins)': 'watch_min',
    'Views': 'views',
    'Impressions': 'impressions',
    'Subscribers': 'subs_net',
    'Subscribers Gained': 'subs_gained',
    'Subscribers Lost': 'subs_lost',
    'Average Percentage Viewed': 'avg_view_pct',
    'Likes': 'likes',
    'Comments': 'comments',
    'Shares': 'shares',
    'Dislikes': 'dislikes'
}, inplace=True)

df_backup = df.copy()


# Simple Pivot Table _ Playlist-wise total views

# Pivot table: rows = playlist, values = views, aggfunc = sum
df.pivot_table(values='views',
               index='playlist',
               aggfunc='sum')

# Adding Total views by setting margins = True
df.pivot_table(values='views',
               index='playlist',
               aggfunc='sum',
               margins = True, # To add a totals
               margins_name = 'Grand Total') # Custom name for totals

# By default values are sorted in order of playlist names, 
# To sort in decreasing order of views

# lengthy code can be written using ()

(df
    .pivot_table(values='views', 
                   index='playlist', 
                   aggfunc='sum')
    .sort_values(by='views', ascending=False))


# Multi-dimensional Pivot Table ---------------------------

# First create published_month column
df['published_month'] = df['published'].dt.month

# Playlist vs Published Month — sum of views

# Including sub-columns in pivot table
# Pivot: rows = playlist, columns = published_month

df.pivot_table(values='views',
               index='playlist',
               columns='published_month',
               aggfunc='sum')

# Whereever value is not available (e.g., no video published in Linear Algera playlist in Jan and Feb)
# It shows NA, we can fill a custom value as 0 using fill_value

df.pivot_table(values='views',
               index='playlist',
               columns='published_month',
               aggfunc='sum',
               fill_value=0)  # Fill missing combos with 0

df.pivot_table(values='views',
               index='playlist',
               columns='published_month',
               aggfunc='sum',
               fill_value='No Video')  # Any value can be filled


df.pivot_table(values='views',
               index='playlist',
               columns='published_month',
               aggfunc='sum',
               margins = True, # Will give total for both rows and columns
               margins_name = 'Grand Total') # margins_name argument must be a string

# If you need only row total, there's no direct argument
pivot_df = df.pivot_table(values='views', 
                          index='playlist', 
                          columns='published_month', 
                          aggfunc='sum')

# Add row totals manually
pivot_df['Total'] = pivot_df.sum(axis=1)
pivot_df

# Add column totals manually
pivot_df.loc['Total', :] = pivot_df.sum(axis=0)
pivot_df

# Multi-index 
# Including sub-rows in pivot table
# Pivot: rows = playlist, and published_month
df.pivot_table(values='views',
               index=['playlist', 'published_month'],
               aggfunc='sum') 


# Multiple Aggregations (like Excel Value Field Settings) -------------------

# Sum & Mean of Views per Playlist

df.pivot_table(values='views',
               index='playlist',
               aggfunc=['sum', 'mean'])

# Excel equivalent = adding same field twice to Values (one Sum, one Average)

# to define the formatting to be used for floating-point numbers.
# pd.set_option("display.float_format", "${:,.2f}".format)

df.pivot_table(values='views',
               index='playlist',
               aggfunc=['sum', 'mean'])

# Alternately, using context manager:
with pd.option_context("display.float_format", "${:,.2f}".format):
    print(df.pivot_table(values='views',
                   index='playlist',
                   aggfunc=['sum', 'mean']))


# To apply different aggregation functions to different columns
df.pivot_table(values=['views', 'subs_net'],
               index='playlist',
               aggfunc={'subs_net':'sum', 'views':'mean'})

    
# More Tables -----------------

df.pivot_table(values=['views', 'impressions'],
               index='playlist',
               aggfunc=['sum','mean'])


df.pivot_table(values='views',
               index=['playlist', 'published_month'],
               aggfunc=['sum', 'mean'])

df.pivot_table(values='views',
               index='playlist',
               columns=['published_month', 'subs_net'],
               aggfunc='sum',
               fill_value=0) 


# Adding Filters & Slicers ---------------------------------------------------
# No direct method to add Excel like interactive filters/slicers

# Filter only videos published in August
month = 8
# month = int(input('Enter Month Number: '))

df_filtered = df[df['published_month'] == month]
# You can use df.query() and df.loc[] as pre-slicing your data


# Then pivot
df_filtered.pivot_table(values='views',
                        index='playlist',
                        aggfunc='sum')


# Data Model / Combining Multiple Tables ---------------------------------------
# Excel "Add to Data Model" lets you use related tables in one PivotTable.

# In Pandas, use merge() (like Excel’s VLOOKUP or Power Query Merge)

# E.G., you had a playlist info table (e.g., playlist → category mapping)

playlist_info = pd.DataFrame({
    'playlist': ['Excel', 'Linear Algebra' , 'Statistics', 'R Programming','Python', 'Data Storytelling', 'Science Experiments', 'Career Advice'],
    'category': ['Beginner to Advanced', 'Beginner','Intermediate' ,'Beginner', 'Beginner to Advanced', 'Intermediate', 'Kids Learning', 'Educational']
})

playlist_info

# You will learn more about merging in next section
df_merged = df.merge(playlist_info, 
                     on='playlist', 
                     how='left')

pd.crosstab(df_merged['category'], df_merged['playlist'])
pd.crosstab(df_merged['playlist'], df_merged['category'])

# Now pivot with new info
df_merged.pivot_table(values='views',
                      index='category',
                      aggfunc='sum')


# Group by category + playlist
(df_merged 
    .groupby(['category', 'playlist'])
        ['views'].sum())


# Measures and KPIs (Excel Power Pivot) --------------------------------
# Excel users create calculated fields (like CTR = clicks / impressions).
# In Pandas → use .assign() or simple column creation:


# Create CTR (Click-through rate)
df['ctr'] = (df['views'] / df['impressions']) * 100

df = df.assign(ctr = (df['views'] / df['impressions']) * 100)

# Then pivot with it
df.pivot_table(values='ctr',
               index='playlist',
               aggfunc='mean')

# Without creating addtional column for CTR

df.pivot_table(values=['views', 'impressions'],
               index='playlist',
               aggfunc='mean').assign(
    ctr = lambda x: (x['views'] / x['impressions'])*100
)

# Another Example                   
# Views per min (views / watch_min) directly inside aggfunc
df.pivot_table(values=['views', 'watch_min'],
               index='playlist',
               aggfunc='sum').assign(
    views_per_min = lambda x: x['views'] / x['watch_min']
)

                   
# For interactive pivot tables, check pivottablejs libraryoffer