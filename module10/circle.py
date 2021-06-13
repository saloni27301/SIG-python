class Circle():
    def __init__(self,radius):
        self.r=radius
    def getarea(self):
        return self.r**2*3.14
    def getcircumstances(self):
        return 2 * 3.14 *self.r

Mycircle=Circle(4)
print(Mycircle.getarea())
print(Mycircle.getcircumstances())

