"""

9.Define a class Person and its two child classes: Male and Female. All classes have a method "getGender"
which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.

"""

class person:
    pass
class male(person):
    def getgender(self):
        print("male")
class female(person):
    def getgenger(self):
        print("female")

obj = person()
obj1=male()
obj1.getgender()
obj2=female()
obj2.getgenger()