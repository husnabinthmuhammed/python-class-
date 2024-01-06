class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width= width

    def __str__(self):
        return f"rectangle with length = {self.length} and width = {self.width}"

obj1= Rectangle(7,8)
print(obj1.__str__())
