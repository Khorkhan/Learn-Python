# 1. For loop
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(f"I like {x}.")

for i in range(5):
    print(f"Round {i}")

# 2. While loop
count = 1
while count <= 3:
    print(f"Count is {count}")
    count += 1 # Important to avoid infinite loop

# 3. Control statements (break and continue)
for num in range(1,6):
    if num == 3:
        continue # Skip 3
    print(num)

# Exercise
# 1. Setting Multiplication Table
multiplier = 2

# 2. Use for loop with range(1, 13)
# fyi, range(1, 13) generates numbers from 1 to 12
for i in range(1, 13):
    result = multiplier * i
    print(f"{multiplier} x {i} = {result}")