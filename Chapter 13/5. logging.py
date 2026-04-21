import logging
import pandas as pd

# Example 1: ----------------------------

# Set up logging to file
logging.basicConfig(
    filename='sales_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Step 1: Create sample data
data = {
    'region': ['North', 'South', 'East', 'West'],
    'units_sold': [120, 85, 90, 110],
    'unit_price': [10.0, 12.5, 9.5, 11.0]
}

df = pd.DataFrame(data)
logging.info("Created initial sales DataFrame")

# Step 2: Calculate total sales
df['total_sales'] = df['units_sold'] * df['unit_price']
logging.info("Calculated total_sales column")

# Step 3: Save to Excel
output_file = 'regional_sales.xlsx'
df.to_excel(output_file, index=False)
logging.info(f"Saved processed data to {output_file}")

# Example 2: ----------------------------

# df = pd.read_csv(r'https://raw.githubusercontent.com/arora123/Data/refs/heads/master/2014_us_cities.csv')

# logging.basicConfig(
#     filename='automation.log',
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# def process_data(df):
#     logging.info(f"Starting with {len(df)} rows")
#     df['pop_m'] = df['pop'] /1000000
#     logging.info("Calculated population in million")
#     return df

# process_data(df)

# df.to_csv("new_data.csv")
# logging.info("Saved output to new_data.csv")