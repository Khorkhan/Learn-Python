# f strings
name = "Khan"
age = 30

# using f strings
massage = f"My name is {name} and I am {age} years old."
print(massage)

print(f"Next year, I will be {age + 1} years old.")

# using format method
massage2 = "My name is {} and I am {} years old.".format(name, age)
print(massage2)

# number formatting
pi = 3.141592653589793
print(f"Pi is approximately {pi:.2f}.")  # 2 decimal places

price = 1500000
# :, adds a comma as a thousand separator
print(f"The price of the house is ${price:,}.")

# Exercise 1. Make Variables
item_name = "Americano Coffee"
price = 6.5
quantity = 3

# 2. Calculate total cost
total_cost = price * quantity

# 3. use f string to print the result
print(f"Buying {item_name} quantity {quantity} total cost is ${total_cost:.2f} dollars.")
