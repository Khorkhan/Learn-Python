# 1. Definition
def say_hello():
    print("Hello! Nice to meet you.")

# Calling
say_hello()

# 2. Parameters & Arguments
def greet(name):
    print(f"Hello, {name}! Welcome to the world of Python.")

greet("Alice")
greet("Bob")

# 3. Return Statement
def add_numbers(a, b):
    result = a + b
    return result

# Collecting the return value
sum_result = add_numbers(10, 5)
print(f"Sum: {sum_result}")

# Exercise
# 1. Function Definition
def calculate_price(price, amount):
    # Calculate total price
    total_price = price * amount
    # Return the total price
    return total_price

# 2. Function Call
# Example Goods price is 50 buy 5 items
result = calculate_price(50, 5)

# 3. Output the result
print(f" Total Price: {result}")

# Exercise 2
# Make it more flexible
p = int(input("Add price: "))
a = int(input("add amount: "))

# send variable p and a to function
final_total = calculate_price(p, a)
print(f" Total Price: {final_total}")