class person:
    def __init__(self,id):
        self.id=id
        print("Student ID is",self.id,"created")
    def __del__(self):
        self.id=id
        print("The deleted student", self.id,"deleted")
p=person(1)
del p
