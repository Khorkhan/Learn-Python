# 1. Receiving user input
name = input("What is your name?: ")
print(f"Nice to meet you, {name}")

# 2. Type Casting
age = input("How old are you?: ")
# print (age + 1) <-- This will error! Because Python can't take "Massage" + "Number"

# 3. Output
print("Python", "Java", "C++", sep=" |")
# results in: Python | Java | C++

print("Hello", end=" ")
print("World!")
# results in: Hello World!