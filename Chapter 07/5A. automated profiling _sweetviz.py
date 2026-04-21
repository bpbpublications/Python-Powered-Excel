import sweetviz as sv
import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

df.isna().sum().sum()
df_cleaned = df.dropna()

# Generate a report
report = sv.analyze(df)

# Show the report
report.show_html("sales_sweetviz_report.html") # Default arguments will generate to "SWEETVIZ_REPORT.html"

# Compare two data sets
comp_report = sv.compare([df, "Data"], [df_cleaned , "cleaned Data"])
comp_report.show_html("sales_sweetviz_compare_report.html") 