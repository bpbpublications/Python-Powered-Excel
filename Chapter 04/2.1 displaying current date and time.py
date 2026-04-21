# Getting started with date and time

# To Display Current Date, import date class ----------------------

from datetime import date 

# Get the current date
current_date = date.today()
print(current_date)


# Access and print individual components of the date  ---------

current_year = current_date.year
current_month = current_date.month
current_day = current_date.day


print(f'Year: {current_year}\nMonth: {current_month}\nDate: {current_day}')


# To Display Current Date-Time, import datetime class  ----------------------

from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()
print(current_datetime)

# Remove microseconds from the current date and time
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)
print(current_datetime_without_microseconds)

# Access and print individual components of the date and time -----------------

current_year = current_datetime.year
current_month = current_datetime.month
current_day = current_datetime.day
current_hour = current_datetime.hour
current_minute = current_datetime.minute
current_second = current_datetime.second
current_microsecond = current_datetime.microsecond

print(f'''Year: {current_year}\nMonth: {current_month}\nDate: {current_day}\nHour: {current_hour}\nMinute: {current_minute}\nSecond: {current_second}\nMicroSecond: {current_microsecond}''')