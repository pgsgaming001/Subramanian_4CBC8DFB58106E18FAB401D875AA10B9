# Python implementation of the `BankAccount` class as described:

class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance:.2f}"

# Creating an instance of BankAccount
account = BankAccount("025901000025252", "Aruna J", 10000.0)

# Testing deposit and withdrawal functionality
account.deposit(500.0)
account.withdraw(200.0)

print(account.display_balance())  # To Display the result￼Not
