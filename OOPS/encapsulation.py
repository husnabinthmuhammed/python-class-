"""
Wrapping the data in a single unit.

Access Modifiers
------------------
public
private
protect

"""
#____________________PRIVATE___________________
class Bank:
    def __init__(self, b_name, b_transaction):
        self.name = b_name
        self.__trans = b_transaction

bank = Bank('SBI', 12345678)

#print(bank._tans)

class Customer(Bank):
    def bank_data(self):
        #print(self.name)
        print(self.__trans)

obj = Customer("SBI", 4567654)
obj.bank_data()

#___________________protected________________

class Bank:
    def __init__(self, b_name, b_transaction):
        self.name = b_name
        self._trans = b_transaction

bank = Bank('SBI', 12345678)

#print(bank._tans)

class Customer(Bank):
    def bank_data(self):
        #print(self.name)
        print(self._trans)

obj = Customer("SBI", 4567654)
obj.bank_data()