"""

1.Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

"""

class strr:
    def __init__(self):
        self.strr=''
    def getstring(self):
        self.str = input("enter a string:")
    def pritsting(self):
        print(f'uppercase:{self.str.upper()}')
    def tests(self):
        print("test the class methods")
strr=strr()
strr.getstring()
strr.printstring()
strr.tests()