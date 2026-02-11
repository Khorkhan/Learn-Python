class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof Woof")

class Cat(Animal):
    def speak(self):
        print("Meow Meow")

dog = Dog()
cat = Cat()

dog.speak() #Woof Woof
cat.speak() #Meow Meow 