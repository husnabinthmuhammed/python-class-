"""
5.Define a class named American and its subclass NewYorker.

Hints:

Use class Subclass(ParentClass) to define a subclass.

"""

class American:
    def __init__(self,nation):
        self.nation = nation
    def display(self):
        print(f"Nation:{self.nation}")

class NewYorker(American):
    def display(self):
        print("NewYorker")

obj = NewYorker("American")
obj.display()
obj_a=American("American")
obj_a.display()