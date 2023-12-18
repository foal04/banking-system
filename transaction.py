# transaction.py

class Transaction:
    def __init__(self, transaction_id, account, customer, amount):
        self.transaction_id = transaction_id
        self.account = account
        self.customer = customer
        self.amount = amount

    def display_info(self):
        print(f"Transaction ID: {self.transaction_id}")
        self.account.display_info()
        self.customer.display_info()
        print(f"Amount: ${self.amount}")
