# Wait for Correct Password_ Try giving different inputs to the prompt
password = ""
while password != "open123":
    password = input("Enter password: ")
print("Access granted!")

# Countdown Timer
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Go!")


# Infinite loop (Use stop button to interrupt)
while True:
    print('hello')
    