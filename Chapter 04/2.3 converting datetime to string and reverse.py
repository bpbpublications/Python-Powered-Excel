from datetime import datetime

# Convert Date-Time to String in required format ----------------------

my_date = datetime(2025, 10, 30, 4, 30)
print(my_date)
print(type(my_date)) # Datetime object

str(my_date) # String

# formatting as string in specified format

formatted_date = my_date.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) 
print(type(formatted_date))

short_date = my_date.strftime("%d/%m/%Y")
print(short_date) 
print(type(short_date))

long_date = my_date.strftime("%A, %B %d, %Y")
print(long_date)

other_format = my_date.strftime("%d-%b-%y")
print(other_format)

# Convert strigs to date or datetime object ----------------------

# Example 1
date_string = "2025-03-04"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(parsed_date)  # Output: 2025-03-04 00:00:00

# Example 2
# when formats do not match, you get ValueError
date_string = "31-01-2020 14:45:37"
format_string = "%m-%d-%Y %H:%M:%S"

datetime.strptime(date_string, format_string)
# ValueError: time data '31-01-2020 14:45:37' does not match format 
# '%m-%d-%Y %H:%M:%S'

# Let's correct the format string
date_string = "31-01-2020 14:45:37"
format_string = "%d-%m-%Y %H:%M:%S"
datetime.strptime(date_string, format_string) # 2020-01-31 14:45:37

# Example 3
dt_string = "12/11/2018 09:15:32"

# Considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1 =", dt_object1, '\n')

# Considering date is in mm/dd/yyyy format
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)

# Difference between strptime() and strftime()

date_string = "27 Mar, 2025"

print("date_string =", date_string)
print("type of date_string =", type(date_string))

date_object = datetime.strptime(date_string, "%d %b, %Y")

print("date_object =", date_object)
print("type of date_object =", type(date_object))

# Converting datetime object to a string again (in a new format)

datetime.strftime(date_object, "%d/%m/%y") # '27/03/25'