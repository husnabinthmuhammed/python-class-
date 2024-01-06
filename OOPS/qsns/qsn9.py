"""
7.Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.


"""

class Rectangle:
    def __init__(self,length,width):
        self.length= length
        self.width = width

    def getpara(self):
        print("lenght,width",self.length,self.width)
    def getarea(self):
        area  = self.length*self.width
        print("arae of tha rectagle is :",area)

c = Rectangle(5,7)
c.getpara()
c.getarea()