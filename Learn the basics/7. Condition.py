# if-else statement
score = 75

if score >= 50:
    print("Congratulations! You passed the exam.")
else:
    print("Sorry, you failed the exam. Better luck next time.")

# elif statement
age = 18

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# Nested if statement
is_number = True
total_bill = 600

if is_number:
    print("You are a member.")
    if total_bill > 500:
        print("You get discount 10%!")
    else:
        print("Buy more to get discount!")
else:
    print("Become a member to enjoy discounts!")

# Logical operators
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid username or password.")

# Exercise 1. Set Variables
height = 135
has_ticket = True

# 2. Check conditions
if height >= 120 and has_ticket:
    print("You can play!")
elif height >= 120 and not has_ticket:
    print("You need a ticket to play.")
else:
    print("Sorry, You are not tall enough to play.")