import models
class FinanceManager:
    def __init__(self):
        self.transactions = []


    def add_transaction(self, transaction):
        # add_q = input(f"Would you like to add a new transaction? y/n: ")
        # if add_q == "y" or add_q == "Y":
        #     transaction_cost = int(input("How much?: "))
        self.transactions.append(transaction)
    
    
    def get_balance(self):
        return self.get_income() - self.get_expences()


    def get_expences(self):
        total_expences = 0
        for transaction in self.add_transactions:
            if transaction.type == "expence":
                total_expences +=transaction.amount
            return total_expences


    def get_income(self):
        total_income = 0
        for transaction in self.transactions:
            if transaction.type == "income":
                total_income += transaction.amount
            return total_income