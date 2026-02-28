text = "Python is Fun"
print(len(text))  # length of the string
print("Fun" in text)  # check if substring is in the string

name = "   Python   "
print(name.upper()) # "   PYTHON   "
print(name.strip()) # "Python"

# slicing
word = "HelloWorld"
print(word[0:5])  # "Hello" ("Pull the characters from index 0 to 4")
print(word[5:])   # "World" ("Pull the characters from index 5 to the end")
print(word[:5])   # "Hello" ("Pull the characters from the beginning to index 4")

phrase = "I love Apple"
new_phrase = phrase.replace("Apple", "Python")
print(new_phrase)  # "I love Python"

data = "Red, Green, Blue"
colors = data.split(", ")
print(colors)  # ['Red', 'Green', 'Blue']

# Exercise 1. Set Starting Variables
raw_data = "   Programming is amazing!   "

# 2. Clean the data
clean_data = raw_data.strip().lower().replace("programming", "Python")

# 3. Print with f string
print(f"Cleaned data: '{clean_data}'")