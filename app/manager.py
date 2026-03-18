class FinanceManager:
    def __init__(self):
        self.transactions = []


    def add_transaction(self, transaction):
        self.transactions.append(transaction)
    
    
    def get_balance(self):
        income = 0
        expenses = 0

        for t in self.transactions:
            if t.type == "income":
                income += t.amount
            elif t.type == "expense":
                expenses += t.amount
        
        return self.get_income() - self.get_expences()


    def get_expences(self):
        total_expences = 0
        for transaction in self.transactions:
            if transaction.type == "expense":
                total_expences +=transaction.amount
            
        return total_expences


    def get_income(self):
        total_income = 0
        for transaction in self.transactions:
            if transaction.type == "income":
                total_income += transaction.amount
            
        return total_income