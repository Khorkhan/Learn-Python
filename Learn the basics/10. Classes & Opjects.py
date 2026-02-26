# 1. Create a class (blueprint)
class Dog:
    # __int__ is special function set in beginning (constructor)
    def __init__(self, name, breed):
        self.name = name # Attribute
        self.breed = breed # Attribute

    # Method (behavior)
    def bark(self):
        print(f"{self.name} says: Woof!")

# 2. Create object (The instance)
# Create an object from the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Max", "Bulldog")

# call info (attributes)
print(my_dog.name) # Output: Buddy

# method call
my_dog.bark() # Output: Buddy says: Woof!

# Exercise
# 1. Create character class
class Character:
    # 2. in __init__ input name and hp
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    # 3. Create method name take_damage (reduce hp 10 each time)
    def take_damage(self):
        self.hp -= 10
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes damage! Remaining HP: {self.hp}")

# 4. Try create object and hero
hero = Character("Dragon Warrior", 100)

# Try Take damage
hero.take_damage()
hero.take_damage()