"""
2.Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
(Just try )

Hints:
Consider use yield

"""

class div:
    def __init__(self):
        self.n=''
    def range(self):
        self.n = int(input("enter a number:"))
    def divis(self):
        for i in range(self.n):
            if i%7==0:
                print(i)


div = div()
div.range()
div.divis()