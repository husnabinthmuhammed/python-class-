# __________________________________________________________
class Rectagle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    @classmethod
    def create_square(cls, side):
        return cls(side, side * side)


rectangle = Rectagle(7, 6)
print(rectangle.area())
print(rectangle.perimeter())

square = Rectagle.create_square(4)
print(square.area())
print(square.perimeter())


# ____________________________________________________________

class Bankaccount:
    interest_rate = 0.08

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insuficient funds..!")

    def calculate_interest(self):
        return self.balance * self.interest_rate

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate
        print("classmethod, interest updated")


bank = Bankaccount("SBI7778", 10000)
print(Bankaccount.interest_rate)
Bankaccount.set_interest_rate(0.07)
print(Bankaccount.interest_rate)
interest = bank.calculate_interest()
print(interest)

# _______________________________________________________
