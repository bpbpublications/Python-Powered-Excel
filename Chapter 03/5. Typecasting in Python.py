# Type casting in Python

# Convert to numbers -----------------------------------

sales = "500"  # Stored as a string (text)
type(sales)

sales_num = int(sales)  # Convert to a number
type(sales_num)
print(sales_num * 2)  # 1000 (works like a number now)

age = "  30  "
type(age)
int(age) # 30
float(age) # 30.

batch = 'python' 
int(batch) # ValueError as such strings/texts can not be converted to numbers

passed = True
int(passed) # 1

present = False
int(present) # 0

# Convert to bools -----------------------------------

status_text = "True"  
status_bool = bool(status_text)  # Converts any non-empty string to True — even "False" or "No"!
print(status_bool)  # True (but be careful!)


bool("False")     # True
bool("No")        # True
bool("")          # False as only empty string is False

status_text = "True" 
status_bool = status_text.lower() == "true"
print(status_bool)

status_text = "False" 
status_bool = status_text.lower() == "true"
print(status_bool)


bool(10)   # True
bool(0)    # False
bool(-1)   # True

# Convert to text -----------------------------------

x = 15; str(x)
y = True; str(y)