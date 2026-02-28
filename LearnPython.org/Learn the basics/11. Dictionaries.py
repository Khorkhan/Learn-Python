# how to create Dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# 1. put info to use
print(person["name"]) # Output: Alice

# 2. add or update info
person["job"] = "developer" # add new key name job
person["age"] = 31 # update age

# 3. remove info
del person["city"] # remove city key

# Loop in dictionary
# Loop only key
for k in person:
    print(k) # Output: name, age, job

for k,v in person.items():
    print(f"Topic: {k}, info: {v}")

# Exercise
# 1. Create Dictionary Name Menu
menu = {
    "Pizza": 250,
    "Burger": 150,
    "Pasta": 200
}

# 2. add new menu (add salad 100)
menu["Salad"] = 100

# 3. print price menu
print(f"price's Pizza is: {menu['Pizza']} Baht")
print("-" * 20)

# 4. Use for loop print all menu and price
print("--- Add Menu ---")
for food, price in menu.items():
    print(f"{food}: {price:>5} Baht")