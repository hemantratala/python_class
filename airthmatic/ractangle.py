class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
r1=Rectangle(10,5)
r2=Rectangle(20,4)
r3=Rectangle(30,6)
print(r1.area())
print(r2.area())
print(r3.area())