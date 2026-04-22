class numbers:
    def __init__(self):
        self.x=100
    def display(self):
        y=40
        print("Instance Variable",self.x)
        print("Normal Variables is",y)
n=numbers()
n.display()
print("Outside Method The Value is",n.x)
print(y)
