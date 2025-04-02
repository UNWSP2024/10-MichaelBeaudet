# Author: Michael Beaudet
# Title: Program 1 Week 10: Compile and run code
# Date: 4/1/25

class BankAccount:
# Create the balance variable
    def __init__(self, bal):
        self.__balance = bal 
# Use the deposit method 
    def deposit(self, amount):
        self.__balance += amount
# Use the withdraw method
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')
# Return the account balance
    def get_balance(self):
        return self.__balance


