#___________parameterised constructor______________

class Myclass:
    def __init__(self,name,age):
        self.name = name
        self.age=age

obj = Myclass("husna",22)


#__________________default const_____________________

class Myclass:
    nmae = "husna"
    def __init__(self):
        pass


obj = Myclass()


#_____________default by parameter__________________________

class Myclass:
    def __init__(self):
        self.name = "husna"
        self.age=22

obj = Myclass()
print(obj.name)


