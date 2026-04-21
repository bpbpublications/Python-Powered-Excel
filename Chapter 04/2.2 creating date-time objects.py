# To Create a specific date object

from datetime import date

# Create a date object ---------------------------
# for date October 30, 2025

specific_date = date(2025, 10, 30)
print(specific_date)
type(specific_date)  # datetime.date

# Avoid using two-digit years to prevent confusion
incorrect_date = date(25, 10, 30)  # Incorrect: Year 25, October 30
print(incorrect_date)
print(incorrect_date.year)

# Try Giving Invalid values or using leading zeros
date(2025, 13, 10) # ValueError: month must be in 1..12
date(22, 01, 15) # SyntaxError: leading zeros in decimal integer literals are not permitted

# To create specific time instance (independent of date) ----------------------

from datetime import time

specific_time = time(13, 45, 5, 23)
print(specific_time)
type(specific_time)  # datetime.time
 
# To create a date and time instance ----------------------
 
# optional arguments: hour, minute, second

from datetime import datetime

dt1 = datetime(year=2025, month=3, day=31, 
               hour=13, minute=14, second=31)

print(dt1)
type(dt1)  # datetime.datetime

dt2 = datetime(year=2025, month=3, day=31, 
               hour=13)

print(dt2)

dt3 = datetime(year=2025, month=3, day=31)

print(dt3)

datetime(year=2025, month=3) # TypeError: function missing required argument 'day' (pos 3)
