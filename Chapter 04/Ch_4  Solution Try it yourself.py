# Exercise 1: Creating a Date-Time Object ----------------------

from datetime import datetime

# Employee joined on 12th August 2023 at 9:30 AM
joining_date = datetime(2023, 8, 12, 9, 30)
print("Joining Date:", joining_date)

# Exercise 2: Formatting Date-Time as String --------------------

# Format joining date as "12-Aug-2023 09:30 AM"
formatted_date = joining_date.strftime("%d-%b-%Y %I:%M %p")
print("Formatted Joining Date:", formatted_date)

# Exercise 3: Converting String to Date-Time Object --------------

# Application date as string
date_str = "04/03/2025 14:45"

# Convert to datetime object
application_date = datetime.strptime(date_str, "%d/%m/%Y %H:%M")
print("Application Date:", application_date)

# Exercise 4: Adding & Subtracting Dates -------------------------

from datetime import date, timedelta
# Customer signup date
signup_date = date(2025, 3, 1)

# Add 30 days for trial end date
trial_end = signup_date + timedelta(days=30)
print("trial Ends On:", trial_end)

# Calculate days passed till 4th March 2025
current_date = date(2025, 3, 4)
days_passed = (current_date - signup_date).days
print("Days Passed:", days_passed)

# Exercise 5: Time Zones (Intermediate) --------------------------

from dateutil import tz

# Meeting time in IST (Asia/Kolkata)
ist_zone = tz.gettz("Asia/Kolkata")
meeting_time = datetime(2025, 3, 4, 16, 0, tzinfo=ist_zone)
print('Meeting Time in India', meeting_time)

# Convert meeting time to New York time
ny_zone = tz.gettz("America/New_York")
ny_time = meeting_time.astimezone(ny_zone)

print("Meeting Time in New York:", ny_time)

# Exercise 6: Global Report Scheduling ---------------------------

# Report time in Sydney time zone
sydney_zone = tz.gettz("Australia/Sydney")
report_time_sydney = datetime(2025, 3, 10, 9, 0, tzinfo=sydney_zone)
print("Report Time in Sydney:", report_time_sydney)

# Convert Sydney time to UTC
utc_zone = tz.gettz("UTC")
report_time_utc = report_time_sydney.astimezone(utc_zone)
print("Report Time in UTC:", report_time_utc)