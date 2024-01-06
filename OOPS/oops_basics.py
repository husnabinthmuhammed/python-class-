"""
class Car():
   s = "My car"

A = Car()
print(str(A))

"""


class Car():

    def __init__(self, car_name, model, color):   #constuctor  ,  self parameter is used to access variables that belong to the class

        self.car_name = car_name
        self.model = model
        self.color = color

    def drive(self):                #inside  class a  function is declared ,drive is a method
        print("Driving ",self.car_name,self.model)

    def humen(self):
        print("is having a",self.car_name,"car",self.model,"moldel")


obj = Car("BMW", 2023, "Grey")
print(obj.car_name)
print(obj.color)
obj.drive()
obj.humen()

"""
_________
   oops
_________

1.class------------Its collections of objs
2.objects----------Instance of class
3.Inheritance
4.Polymorphism
5.Encapsulation
6.Abstraction





"""