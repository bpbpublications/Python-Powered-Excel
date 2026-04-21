import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Flight": ["AI101", "BA202", "LH303"],
    "Passengers": [180, 220, 150]
})

# Write DataFrame to a custom sheet name
df.to_excel("flights.xlsx", sheet_name="Aviation_Report", index=False)

# Zero-indexed in pandas, so Excel shows it as row 6, col C

df.to_excel("flights_offset.xlsx", sheet_name="Flights", 
		startrow=5, startcol=2, index=False)