"""
8.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.
"""

class shape:
    def __init__(self,area):
        self.area = 0
    def areas(self):
        print(self.area)

class square(shape):
    def __init__(self,length):
        super().__init__("sh")
        self.length = length
    def areas(self):
        area = self.length*self.length
        print(area)

obj = square(4)
obj.areas()
obj1 = shape(5)
obj1.areas()