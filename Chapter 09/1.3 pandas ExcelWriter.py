import pandas as pd

# Sample DataFrames
flights = pd.DataFrame({
    "Flight": ["AI101", "BA202", "LH303"],
    "Passengers": [180, 220, 150]
})

cargo = pd.DataFrame({
    "Flight": ["AI101", "BA202", "LH303"],
    "Cargo_Tons": [20, 35, 15]
})

# Use ExcelWriter to control placement
with pd.ExcelWriter("aviation_report.xlsx", engine="openpyxl") as writer:
    flights.to_excel(writer, sheet_name="Summary", startrow=1, startcol=0, index=False)
    cargo.to_excel(writer, sheet_name="Summary", startrow=1, startcol=4, index=False)


# New data
new_flights = pd.DataFrame({
    "Flight": ["UA404", "EK505"],
    "Passengers": [190, 210]
})


# Append data to existing sheet without writing column headers again
with pd.ExcelWriter("aviation_report.xlsx", engine="openpyxl", 
                    mode="a", if_sheet_exists="overlay") as writer:
    new_flights.to_excel(writer, sheet_name="Summary", 
                         startrow=5, startcol=0, index=False, header=False)    