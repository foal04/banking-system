# banking_system.py

from account import Account
from customer import Customer
from transaction import Transaction

# Create accounts
account1 = Account(1, 1000.0)
account2 = Account(2, 2000.0)

# Create customers
customer1 = Customer(101, "Alice", "alice@example.com")
customer2 = Customer(102, "Bob", "bob@example.com")

# Create transactions
transaction1 = Transaction(1001, account1, customer1, 500.0)
transaction2 = Transaction(1002, account2, customer2, 700.0)

# Display information
print("Transaction Information:")
transaction1.display_info()
print()
transaction2.display_info()
