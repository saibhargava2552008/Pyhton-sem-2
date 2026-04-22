class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("My name is :", self.name)
        print("Age is :", self.age)
s1 = Student("Ravi", 20)
s1.display()
s2 = Student("Bhargava",17)
s2.display()
