#8. Write a program to demonstrate encapsulation and abstraction using classes.
from abc import ABC, abstractmethod

# Abstraction
class Bank(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

# Encapsulation
class SavingsAccount(Bank):
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def calculate_interest(self):
        return self.__balance * 0.05

# Creating an object
account = SavingsAccount(1000)

account.deposit(500)

print("Balance:", account.get_balance())
print("Interest:", account.calculate_interest())
