"""
The circle class models a circle with a radius and color

attributes : radius , color

methods :

Circle
getRadius()
getCircumference()
getArea()


"""

class Circle():
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def Circle(self):
        pass

    def getaRadius(self):
        print("radius of the circle :",self.radius)

    def getCircumfernce(self):
        print("circumference of circle :",2*3.14*self.radius)

    def getArea(self):
        print("Area of the circle :",3.14*self.radius*self.radius)


obj = Circle(6,"white")
obj.Circle()
obj.getaRadius()
obj.getCircumfernce()
obj.getArea()


