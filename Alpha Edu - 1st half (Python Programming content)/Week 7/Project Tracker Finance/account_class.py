class Account:
    def __init__(self):
        # Initial balance is 0
        self.balance = 0
        #List of storage for all transactions
        self.transactions = []

    # Method for adding transaction to list and
    def add_transaction(self, transaction): # Uses the object from class Transaction
        self.transactions.append(transaction)  #Adding transaction to list
        self.balance += transaction.amount # Updating balance based on the amount of transaction

    # Method for retrieving current balance
    def get_balance(self):
        return self.balance

    # Method for getting all the transactions
    def get_transaction(self):
        return self.transactions

    def __dir__(self):
        return f"{self.balance}"

# account = Account()
# dengi = Transaction(90, "Food")
# account.add_transaction(dengi)


