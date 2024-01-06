
class Math:
    @staticmethod
    def multiply(a,b):
        return  a * b

    @staticmethod
    def is_even(number):
        return number % 2 == 0

result  = Math.multiply(5,3)
print(result)
print(Math.is_even(10))
print(Math.is_even(7))