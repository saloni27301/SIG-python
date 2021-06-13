print("1803010120 saloni")
class student:
    def __init__(self, rollno,name):
        self.rollno=rollno
        self.name=name
    def display(self):

        print(self.rollno,self.name,self.age,self.marks)
    def setAge(self):
        self.age=int(input("Enter age : "))
    def setMarks(self):
        self.marks=int(input("Enter marks : "))
s1=student(120,"Saloni")
s2=student(100,"Riya")
s1.setAge()
s1.setMarks()
s2.setAge()
s2.setMarks()
s1.display()
s2.display()