# if Condition:

sales = 1200 # Try changing values of this variable
if sales > 1000:
    print("Eligible for bonus")

# if-else Statement

revenue = 950        # Try changing values of this variable
if revenue > 1000:   # assuming expense = 1000
    print("Profit")
else:
    print("Loss")

# if-elif-else Statement
sales = 1500

if sales > 2000:
    performance = "Excellent"
elif sales > 1500:
    performance = "Good"
elif sales > 1000:
    performance = "Average"
else:
    performance = "Needs Improvement"

print(performance)

# Inventory Management    
    
inventory = 75

if inventory < 20:
    action = "Order Immediately"
elif inventory < 50:
    action = "Restock Soon"
elif inventory < 100:
    action = "Monitor"
else:
    action = "Sufficient Stock"

print(action)
 
# Expense Tracker

expenses = 700
if expenses > 1000:
    print("Over Budget")
elif expenses > 500:
    print("Warning: Approaching Budget")
else:
    print("Within Budget")

# Nested if-else:
    
# Example 1: User Authentication
# When checking both username and password to authenticate a user:

username = "admin"
password = "password123"

if username == "admin":
    if password == "password123":
        print("Access granted.")
    else:
        print("Incorrect password.")
else:
    print("Unknown user.")


item_available = True
item_price = 45
budget = 50

if item_available:
    if item_price <= budget:
        print("Item can be purchased.")
    else:
        print("Item is too expensive.")
else:
    print("Item not available.")


user_role = "editor"
has_permission = True

if user_role == "admin":
    print("Full access granted.")
else:
    if user_role == "editor":
        if has_permission:
            print("Editor access granted.")
        else:
            print("Permission required.")
    else:
        print("Read-only access granted.")


likes = 750
shares = 50

if likes > 500:
    if shares > 100:
        print("Viral Post!")
    else:
        print("Popular but not Viral")
else:
    print("Needs Improvement")


# Short-hand Notation

revenue = 950; "Profit" if revenue > 1000 else "Loss" # 'Loss'

status = "Profit" if revenue > 1000 else "Loss"
print(status)

sales = 1200
if sales > 1000: print("Eligible for bonus")