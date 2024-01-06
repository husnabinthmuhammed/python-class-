"""
-child class (derived class,sub class) inherits the properties of parent class (super class,base class)

-code reusability

__________________________
types of inheritance
_________________________

1.Single
2.Multiple
3.Hierarchical
4.Multilevel
5.Hybrid


"""

class Animal:
    def __init__(self, name):    #parent class
        self.name = name

    def speak(self):
        pass

class Dog(Animal):      #child class
    def speak(self):
        print(self.name,"bark")

class Cat(Animal):   #child class
    def speak(self):
        print(self.name,"meows")


obj_dog = Dog("Rocky")
obj_cat = Cat("kitty")
obj_dog.speak()
obj_cat.speak()