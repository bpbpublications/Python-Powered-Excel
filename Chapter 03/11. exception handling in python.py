# Basic Structure: try and except

x1 = 100; x2 = 20
# Uncomment this line and then run try-except block
x1 = 100; x2 = 0

try:
    print(x1/x2)  
except:
    print('Something went wrong!')    

# If you know what specific error can you get, you can catch that accordingly

try:
    result = 100 / 0  # This will cause a ZeroDivisionError
    print(result)
except ZeroDivisionError:
    print("Oops! Can't divide by zero.")  # Safe fallback
   
    
data = [10, 20, 30]
try:
  print(data[3])
except IndexError:
  print("You've supplied wrong index")


# If you're expecting different types of errors, 
# you can catch them with different error messages
   
x1 = 100; x2 = 0 # Change x2
del x1 # Comment or uncomment

try:
    print(x1/x2)  
except ZeroDivisionError:
    print("Oops! Can't divide by zero.")     
except NameError:
    print('Data is missing!')  
except:
    print('Something else went wrong!')



del data 

try:
  print(data[3])
except IndexError:
  print("You've supplied wrong index")
except:
    print('Something else went wrong!')
    
    


data = [10, 20, 30]
del data # Uncomment/comment this line for different results

try:
  print(data[3])
except NameError:
  print('There is no such list in your enviornment')
except IndexError:
  print("You've supplied wrong index")  
    
# Converting text to numbers
data = ["100", "250", "abc", "400"]

for value in data:
    try:
        num = int(value)  # Try converting to integer
        print("Converted:", num)
    except ValueError:
        print(f"Skipped invalid value: {value}")

# reading files (You will understand this example after learning about open method _chapter 5)
filename = "sales_data.csv"

try:
    with open(filename, 'r') as f:
        content = f.read()
        print("File loaded!")
except FileNotFoundError:
    print(f"'{filename}' not found. Please check the name.")

# else and finally
try:
    x = int("500")
except ValueError:
    print("Not a number!")
else:
    print("Converted successfully.")
finally:
    print("Task done.")

# Python Errors: https://www.linkedin.com/posts/drnishaarora_do-you-often-get-annoyed-by-those-errors-activity-7025681778610753536-xxG3?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAepsJkBv8opllaFHDwGtRtHUfsaCud-TdQ