class Student:
    def __init__(self, name, age):
        self.name = name # attribute
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name}, age {self.age} years old")

# create object
student1 = Student("Khan", 28)
student1.introduce()