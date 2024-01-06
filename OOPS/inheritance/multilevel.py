class Vehicle:   #parent class
    def vehicle_info(self):
        print("Inside vehicle class")

class Car(Vehicle):  #parent class
    def car_info(self):
        print("Inside car class")


#child class
class Sportscar(Car):
    def sports_car_info(self):
        print("Inside sports car class")


car = Car()
car.car_info()
car.vehicle_info()


obj = Sportscar()
obj.vehicle_info()