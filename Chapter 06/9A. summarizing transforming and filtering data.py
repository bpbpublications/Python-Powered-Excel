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

# Grouping, Aggregation and Pivoting -------------------------

# # Total views per playlist
df.groupby('playlist')['views'].sum() # series

df.groupby('playlist')[['views']].sum() # dataframe
type(df.groupby('playlist')[['views']].sum())

# Here 'playlist' column becomes an index
df.groupby('playlist')[['views']].sum().shape

# to convert it to regular column
df.groupby('playlist')[['views']].sum().reset_index()


# Mutiple columns
# Group by playlist and get total views + total watch time
df.groupby('playlist')[['views', 'watch_min']].sum()


# Resetting index
(
 df.groupby('playlist')[['views', 'watch_min']]
     .sum()
     .reset_index()
     )


# Count number of distinct video titles per playlist 
df.groupby('playlist',
           observed = False)['title'].count()   

df['playlist'].value_counts()             # Faster for simple counts

# Count distinct / nunique in groups

(df.groupby('playlist')['title']
     .nunique()
     .reset_index(name='unique_titles'))

# Multiple Aggregations at once --------------------

# Multiple summary stats per playlist
df.groupby('playlist')['views'].agg(['sum', 'mean', 'max'])

(df.groupby('playlist')['views']
     .agg(['sum', 'mean', 'max'])
     .reset_index())

# Applying multiple aggregations for different columns
df.groupby('playlist').agg({'views': 'sum', 'watch_min': 'mean'})

# with meaningful column names

(df
 .groupby('playlist')
 .agg(total_views=('views', 'sum'), 
        avg_watch_min=('watch_min', 'mean')))


# multiple summary functions to multiple columns without grouping
df.agg({'views': ['sum', 'mean'], 'watch_min': ['max', 'min']})

# Applying agg() on dataframe without grouping -------------

# Mean of all numeric columns
df.select_dtypes('number').mean()
df.select_dtypes('number').agg('mean')

# Mean and Max of all numeric columns
df.select_dtypes('number').agg(['mean', 'max'])


# More examples 

cutoff_date = pd.Timestamp('2023-06-01')
df['video_age'] = (
                    df['published']
                   .map(lambda x: 'Old' if x < cutoff_date else 'New')
                   )

# Categorize videos based on performance
def tag_performance(row):
    if row['views'] > 5000 and row['watch_min'] > 200:
        return 'High'
    elif row['views'] < 1000:
        return 'Low'
    else:
        return 'Medium'

df['performance'] = df.apply(tag_performance, axis=1)  # axis=1 applies row-wise

# Views by playlist and video_age
df.groupby(['playlist', 'video_age'])['views'].sum().reset_index()

# Views by playlist and performance tag
df.groupby(['playlist', 'performance'])['views'].sum().reset_index()


# Custom function in agg() ------------------------------

(df
 .groupby('playlist', 
           observed = False)['views']
 .agg(['min', 'max', lambda x: x.max() - x.min()]))

# Custom aggregation with lambda with clean custom names (like showing RANGE of views in group)
(df
 .groupby('playlist')['views']
 .agg(
    min_views='min',
    max_views='max',
    range_views=lambda x: x.max() - x.min())
.reset_index())

# Other uses of agg() ------------------

# df.agg() is useful when you just want 
# summary stats without splitting data into groups.

# Aggregate stats on entire DataFrame
df.agg({'views': ['sum', 'mean'], 'watch_min': ['sum', 'mean']})

# Aggregation on single column (no group)
df['views'].agg(['sum', 'mean'])

# use groupby() without specifying an aggregation immediately -----

grouped = df.groupby('playlist')
# Now grouped is a GroupBy object, you can loop / aggregate as needed

grouped['views'].agg(['sum', 'mean'])
grouped.agg({'views': ['sum', 'mean'], 'watch_min': ['sum', 'mean']})

for group, data in grouped:
    print(f"Group: {group}")
    print(data.head(2))  # Displays first few rows of the group

# To broadcast group-level stats back to all rows using transform() -------------

# Add playlist-level average views to each video row
df['playlist_avg_views'] = (df
                            .groupby('playlist')['views']
                            .transform('mean'))

# It returns a series of the same shape as the original data, broadcasting group-level stats back to all rows.
# Let's view few columns
df[['playlist', 'title', 'views', 'playlist_avg_views']].head()

df[['playlist', 'views', 'playlist_avg_views']].tail()

# Alternately
(
 df.assign(playlist_avg_views=df.groupby('playlist')['views']
           .transform('mean'))
           [['playlist', 'views', 'playlist_avg_views']]
           .tail()
 )


# df.filter() ----------------------

# When using groupby().filter(), always pass a function 
# (like a lambda or named function) that returns True/False for the entire group

# Grouping by 'playlist' and summarize 'views' for each playlist 
# _ one row per group
df.groupby('playlist')['views'].sum()

# To filter groups based on some criterial (total views > 30,000)
# It keeps original rows but removes groups/playlists that don't meet the considions

# Filtering playlists where total playlist views > 30,000
filtered_df = (
                df.groupby('playlist')
                .filter(lambda x: x['views']
                        .sum() > 30000)
                )

filtered_df[['playlist', 'views']]

# Or using a named function
def has_enough_views(group):
    return group['views'].sum() > 30000

filtered_df = df.groupby('playlist').filter(has_enough_views)

# To keep playlists where:
# Total views > 30,000 AND Average watch time > 5 minutes

filtered_df = (df
               .groupby('playlist')
               .filter(
                   lambda g: (g['views'].sum() > 30000) and (g['watch_min'].mean() > 5)
                       ))


# More on filter() function ---------------
df.filter(['title'])
df.filter(['title', 'views'])

df.filter([col for col in df.columns if 'min' in col], )
df.filter([col for col in df.columns if 'sub' in col], )

df.filter(like='min')
df.filter(like='sub')
df.filter(regex = 'sub|min').columns
df.filter(regex = '.*views').columns

df.filter(like = 'V_003') # This is not what we want
df.filter(like = 'V_003', axis = 'rows')
df.filter(regex = 'V_003|V_005', axis = 'rows')
