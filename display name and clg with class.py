class student:
    college="Aditya"
    def display(self,name):
        print("name is :",name)
        print("college name is:",student.college)
s1=student()
s1.display("Hari")
student.college="Aditya University"
s1=student()
s1.display("Hari")
