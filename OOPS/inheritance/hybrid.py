"""
combination of different inheritance is called hybrid inheritance
"""

class Vehicle:
    def info(self):
        print("This is vehicle")

class Car(Vehicle):
    def car_info(self,name):
        print("car name is:",name)

class Truck(Vehicle):
    def truck_info(self,name):
        print("truck name is:",name)

class Sportcar(Car,Truck):
    def sport_car_info(self):
        print("inside the sports car class")



s_car = Sportcar()
s_car.truck_info("TATA")