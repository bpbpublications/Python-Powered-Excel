import pandas as pd
from pandasgui import show

# To launch the GUI (Check taskbar, it opens a new application)
show()

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Launch the GUI with dataset loaded
show(df)

# Loading one or more sample data sets
from pandasgui.datasets import pokemon, titanic
show(titanic)
show(pokemon, titanic)

# Loading all sample data sets
from pandasgui.datasets import all_datasets
show(**all_datasets)