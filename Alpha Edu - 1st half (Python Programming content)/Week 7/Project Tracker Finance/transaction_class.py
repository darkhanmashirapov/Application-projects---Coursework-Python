import datetime

# Class Transaction shows each separate transaction (income or expense)
class Transaction:
    def __init__(self, amount, category, date=None):
        # amount: sum of transactions (positive for income negative for expense
        # category" category of transaction
        # date: date of the transaction of not given just current date
        self.amount = amount
        self.category = category
        self.date = date or datetime.date.today() # If not given use current date

    def display(self):
        #returns date, category and amount
        if self.amount >= 0:
            sign = "+"
        else:
            sign = "-"

    #Get the absolute value of the amount
        amount_str = f"${abs(self.amount)}"

    #Construct the string representation
        return f"{self.date} - {self.category}: {sign}{amount_str}"

