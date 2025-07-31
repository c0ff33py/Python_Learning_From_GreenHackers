# Exercise : Encapsulation

class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = Account(10000)
acc.deposit(500)
print("Balance:", acc.get_balance())
