# Date and time Airthmatics __________________________________________________
 
from datetime import date, time, datetime, timedelta
from dateutil.relativedelta import relativedelta

# Adding/Subtracting days ---------------------

today = date.today()

# Add/Subtract Days
next_week = today + timedelta(days=7)
yesterday = today - timedelta(days=1)

print(f'Today: {today}, Yesterday: {yesterday}, Next_week: {next_week}')

# Add/Subtract Months and Years  ---------------------

# For adding/subtracting months or years, we can use 
# dateutil.relativedelta from dateutils library 
# as timedelta does not handle months and years.


next_month = today + relativedelta(months=1)
last_year = today - relativedelta(years=1)

print("Today:", today)
print("Next Week:", next_week)
print("Next Month:", next_month)
print("Last Year:", last_year)

print(f'Today: {today}, Next Month: {next_month}, Last Year: {last_year}')

# Add/Subtract Time Components   ---------------------

now = datetime.now()
after3hours = now + timedelta(hours = 3)
minus_30_seconds = now - timedelta(seconds=30)

print(f"Current Time: {now.strftime('%H:%M:%S')}, Time after 3 hours: {after3hours.strftime('%H:%M:%S')}, Time Difference: {after3hours - now}")

print(now.strftime('%H: %M: %S'))
print(after3hours.strftime('%H: %M: %S'))
print(after3hours - now)
print("30 Seconds Ago:", minus_30_seconds)


# Difference between Dates and Time in days and weeks   ---------------------

start = date(2025, 3, 1)
end = date(2025, 3, 23)

difference = end - start; difference
print("Difference in Days:", difference.days)
print("Difference in Weeks:", difference.days // 7)

# Difference of days, months, and years   ---------------------

start = date(2024, 3, 1)
end = date(2025, 6, 15)

end - start

difference = relativedelta(end, start); difference
print("Years:", difference.years)
print("Months:", difference.months)
print("Days:", difference.days)
print(f"Years: {difference.years}, Months: {difference.months}, Days: {difference.days}")

# difference of hours, minutes, and seconds

start = datetime(2025, 3, 1, 12, 0, 0)  # March 1st, 12:00 PM
end = datetime(2025, 3, 1, 15, 30, 0)   # March 1st, 3:30 PM

difference = end - start

print("Total Seconds:", difference.total_seconds())
print("Hours:", difference.total_seconds() // 3600)
print("Minutes:", difference.total_seconds() // 60)

# Replacing part of date, time or datetime objects   ---------------------


# Current date and datetime
today = date.today()
now = datetime.now()

print("Today:", today)
print("Now:", now)

# Using replace on date
new_date = today.replace(year=2027, month=12, day=25)
print("Replaced date:", new_date)

# Using replace on datetime
new_datetime = now.replace(hour=9, minute=0, second=0, microsecond=0)
print("Replaced datetime:", new_datetime)


# More examples

# Create a date object
d = date(2025, 3, 15)
print("Original date:", d) # Original date: 2025-03-15

# Replace year and month
d_replaced = d.replace(year=2026, month=12) # Replaced date: 2026-12-15
print("Replaced date:", d_replaced)

# Create a time object
t = time(14, 30, 45)
print("Original time:", t) # Original time: 14:30:45

# Replace hour and minute
t_replaced = t.replace(hour=9, minute=0)
print("Replaced time:", t_replaced) # Replaced time: 09:00:45

# Create a datetime object
dt = datetime(2025, 3, 15, 14, 30, 45)
print("Original datetime:", dt) # Original datetime: 2025-03-15 14:30:45

# Replace day and hour
dt_replaced = dt.replace(day=20, hour=8)
print("Replaced datetime:", dt_replaced) # Replaced datetime: 2025-03-20 08:30:45
