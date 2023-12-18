# account.py

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def display_info(self):
        print(f"Account ID: {self.account_id}")
        print(f"Balance: ${self.balance}")
