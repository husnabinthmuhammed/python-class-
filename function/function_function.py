def create_adder(x):
    def adder(y,z):
        return x+y+z
    return adder
add = create_adder(15)
print(add(10,50))