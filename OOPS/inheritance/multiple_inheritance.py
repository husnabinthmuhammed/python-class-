"""
one child can inherit from multiple parent classes
"""

class Vehicle:   #parent class
    def vehicle_info(self):
        print("Inside vehicle class")

class Car:  #parent class
    def car_info(self):
        print("Inside car class")


#child class
class Sportscar(Car,Vehicle):
    def sports_car_info(self):
        print("Inside sports car class")


sports_car = Sportscar()
sports_car.car_info()
sports_car.vehicle_info()
