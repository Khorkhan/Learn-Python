# 1. Receiving user input
name = input("Please enter your name: ")

# 2. Receiving birth year and calculating age
year_birth_str = input("Please enter birth year: ")
year_birth = int(year_birth_str) # type casting from string to integer

# 3. Calculating age today is 2026
year_current = 2026
age = year_current - year_birth

# 4. Output
print(f"Hello, {name} New you are {age} years old.")