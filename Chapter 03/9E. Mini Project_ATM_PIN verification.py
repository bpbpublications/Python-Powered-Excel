# There are usually multiple ways of approaching the same problem.
# You solution can differ from the given solution

attempt = 1
PIN = '123456'

while attempt <= 3:
  pin = input("Please enter PIN: ")
  if pin == PIN:
    print("Access Granted!")
    break
  else:
    attempt += 1
    print("Wrong PIN!")
else:
  print("Card blocked. Too many wrong attempts.")  