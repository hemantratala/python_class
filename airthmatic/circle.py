class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
c=Circle(5)
c1=Circle(10)
print(c.area())
print(c1.area())