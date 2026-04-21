import dtale
import pandas as pd

# To launch GUI in browser
dtale.show(open_browser=True)

df = pd.read_csv('sales_data.csv', nrows=1000)

dtale.show(df)
# It outputs a URL, paste the same in your browser

# It might ask you to permit

# Alternately, you can run
dtale.show(df, subprocess=True)