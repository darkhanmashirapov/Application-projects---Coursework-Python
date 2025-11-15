import json
from account_class import Account
from category_class import Category
from transaction_class import Transaction
import datetime

class FinanceTracker:
    def __init__(self):
        # Initialization of example os class Account, which will store all the data
        self.account = Account()

        # Method for adding the income
        def add_income(self, amount_parameter, category_name_parameter):
            #Create category for income
            category_obj = Category(category_name_parameter)
            # Create transactions with positive values
            transac_obj = Transaction(amount_parameter, category_obj)
            # We add the amount to our recordings
            self.account.add_transaction(transac_obj) #uses class account which is also uses other
            print(f"Income in amount of ${amount_parameter} is added to category {category_name_parameter}.")

        def add_expense(self, amount, category_name):
            # Create category for expense
            category = Category(category_name)
            # Create transactions with negative sign(expenses)
            transaction = Transaction(amount, category)
            # We add the amount to our recordings
            self.account.add_transaction(transaction)
            print(f"Expense is at amount of ${amount} is added to category {category_name}.")


