from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) :
        pass

class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius

    def area (self):
        return 3.14 * self.radius * self.radius



class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width