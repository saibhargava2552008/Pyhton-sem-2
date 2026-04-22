class namedisplay:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "Student name is :"+self.name
nd=namedisplay("raju")
print(nd)
