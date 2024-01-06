class AnimalClass:
    def __init__(self, identity, age):
        self.identity = identity
        self.age = age

    def feature(self):
        if self.age == "10":
            return True
        else:
            return False


ac = AnimalClass('Lion', '10')
print(ac.__dict__)  