import os
import pandas as pd

os.getcwd() # Excel_Python folder created for the book

# As we will be reading files from Data folder inside Excel_Python
# Setting working directory to Data Folder

data_path = os.path.join(os.getcwd(), 'Data')  # Data folder inside Excel_Python folder
os.chdir(data_path)

# Importing & Inspecting Data ------------------------------------------------

# we can consider 'Video Id' as index because it contains unique id for each video 
df = pd.read_excel('YT_data.xlsx', index_col='Video Id'); df.shape

df.info()                # no missing

# Checking for duplicates -------------------------------------
df.duplicated().sum() # No duplicate row in the data
df.index.duplicated().sum()  # No duplicates in the Index column
df.duplicated().any()    # no duplicates


df.columns

# Rename columns to shorter, consistent, and code-friendly names

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


# Show the updated column names
df.columns

df_backup = df.copy()

# The columns 'playlist' is a categorical variable conceptually
df['playlist'].unique()
# Let's treat it as a category data type
df['playlist'] = df['playlist'].astype('category')

# Frequency Table --------------------------------------------
df['playlist'].value_counts()
df['playlist'].value_counts(normalize = True).round(2)


# Summary of data --------------------------------------------

df.describe(exclude = 'datetime').round(2)
df.describe(include = 'number').round(2)
df.describe(include = 'all')

df['playlist'].describe()


# Analysis ----------------------------------------------------

# Using apply() function
# Add a flag if a video is shorter than 5 minutes
df['video length'] = df['duration_min'].apply(lambda x: 'Short' if x < 10 else 'Long').astype('category')

# As the code is lengthy, we can use blackslash or parenthesis
 # to spread a long code line over multiple lines
 
df['video length'] = (df['duration_min'] \
                        .apply(lambda x: 'Short' if x < 10 else 'Long') \
                        .astype('category'))

# Or    
df['video length'] = (
                        df['duration_min']
                        .apply(lambda x: 'Short' if x < 10 else 'Long')
                        .astype('category')
                    )


# Or using series.map()
df['video length'] = (
                       df['duration_min']
                       .map(lambda x: 'Short' if x < 10 else 'Long')
                       .astype('category')
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

# Here, map() will not work
df.map(tag_performance) # Error
# df.map() works column-wise and element-wise, not row-wise.

# Here, 'published' column is a datetime type so 

# Define a mapping function: label "Old" or "New" based on date
cutoff_date = pd.Timestamp('2023-06-01')
df['video_age'] = (
                    df['published']
                   .map(lambda x: 'Old' if x < cutoff_date else 'New')
                   )

# View the new column
df[['published', 'video_age']].head()
df['video_age'].value_counts()

# Sorting and Rearranging --------------------------------------

# Sort rows by 'views' in descending order
df.sort_values(by='views', ascending=False)

df.sort_values(by='views', ascending=False)[['title', 'views']]
df.sort_values(by='views', ascending=False)[['title', 'views']].tail(3)

# Sort by playlist (A-Z), then by watch time (descending)
playlist_watchTime = (
                        df.sort_values(
                            by=['playlist', 'watch_min'], 
                                    ascending=[True, False]
                                    )
                        [['title', 'playlist', 'watch_min']]
                        )

# Sort by 'impressions' with NaN values shown first
df.sort_values(by='impressions', na_position='first')

# Sort by 'impressions' with NaN values shown last (default)
df.sort_values(by='impressions', na_position='last')

# Reorder all columns alphabetically
df = df[sorted(df.columns)]

# Random Sampling ---------------------------------------------

# Randomly sample 5 rows _ (results vary on each run).
df.sample(5) 

# Randomly sample 5 rows _ ensures reproducibility by setting a fixed seed
df.sample(5, random_state = 5)

# Randomly shuffle all the rows 
df.sample(frac=1, random_state = 5)


# cumsum() and cumprod() -----------------------------------

# Cumulative Views so far after each video
# Running total of views (like Excel running SUM)
df['running_views'] = df['views'].cumsum()

# Imagine daily return column as % changes

# Creating a DataFrame with sample daily returns
df1 = pd.DataFrame({'daily_return': [1.01, 0.99, 1.03]})  # +1%, -1%, +3%
df1
# Calculating the cumulative return
df1['cumulative_return'] = df1['daily_return'].cumprod()
df1