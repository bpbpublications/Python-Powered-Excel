import pandas as pd
import ydata_profiling

# Load dataset
df = pd.read_csv("sales_data.csv")

# Generate a profile report
profile = ydata_profiling.ProfileReport(df)

# Save and view the report
profile.to_file("pandas_profiling_report.html")

# From your working directory, open this html file

# Earlier ydata-profiling was known as pandas_profiling
# you might see this code but it's deprecated

import pandas as pd
import pandas_profiling
# DeprecationWarning: `import pandas_profiling` is going to be deprecated
# by April 1st. Please use `import ydata_profiling` instead.

# Load dataset
df = pd.read_csv("sales_data.csv")

# Generate a profile report
profile = pandas_profiling.ProfileReport(df)

# Save and view the report
profile.to_file("pandas_profiling_report.html")


# This is now deprecated:
# https://pypi.org/project/pandas-profiling/
