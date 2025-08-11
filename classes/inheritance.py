

class shape:

    def __init__(self,name):
        self.name=name

    def describe(self):
        print(f"This shape is called a circle")

#shape1=shape(name="circle")
#shape1.describe()

class Rectangle(shape):
    def __init__(self, length,width):
        super().__init__("Rectangle")
        self.length=length
        self.width=width
    
    def area(self):
        a=self.length*self.width
        print(f"For {self.name} area is {a}")
        return a

r1=Rectangle(length=10,width=20)
r1.describe()
r1.area()
