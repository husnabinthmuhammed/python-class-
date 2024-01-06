"""
Create a class called Vehicle with the following attributes and methods:

Attributes:
make: a string representing the make of the vehicle
model: a string representing the model of the vehicle
year: an integer representing the year the vehicle was made
color: a string representing the color of the vehicle
mileage: a float representing the current mileage of the vehicle

Methods:
_init_(self, make, model, year, color, mileage): initializes the attributes with the given values
drive(self, distance): takes a float representing the distance driven and updates the mileage attribute accordingly
get_info(self): returns a string with the vehicle's make, model, year, color, and mileage attributes in a formatted way
Create a subclass called Car that inherits from the Vehicle class with the following additional attributes and methods:

______________________________________________________________________________________________________________________

num_doors: an integer representing the number of doors the car has
engine_type: a string representing the type of engine the car has
Methods:
_init_(self, make, model, year, color, mileage, num_doors, engine_type): initializes the attributes with the given values
get_info(self): overrides the get_info method of the Vehicle class to include the num_doors and engine_type attributes
Create an instance of the Vehicle class and call the drive method with a distance of 100. Then call the get_info method to print out the vehicle's information.

Create an instance of the Car class and call the drive method with a distance of 50. Then call the get_info method to print out the car's information.
"""

"""
Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in init method
    You can init a object with construct parameter or set the value later
"""

class Vehicle():
    def _init_(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def Drive(self, distance):
        distance = distance/self.mileage
        self.mileage = distance

    def get_info(self):
        print(self.make, self.model, self.year, self.color, elf.mileage)


class Car(Vehicle):
    def _init_(self, make, model, year, color, mileage, num_doors, engine_type):
        super().__init__(make, model, year, color, mileage)
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.num_doors = num_doors
        self.engine_type = engine_type

    def get_info(self):
        print(self.make, self.model, self.year, self.color, self.mileage, self.num_doors, self.engine_type)


obj1 = Vehicle("aa",200,2004,"yellow",40)
obj1.Drive(100)
obj1.get_info()


obj2 = Car("qq",22,2008,"blue",50,4,"petrol")
obj2.Drive(100)
obj2.get_info()








