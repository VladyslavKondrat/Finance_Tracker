import manager
class Transaction:
    def __init__(self, amount, category, type, date, description):
        self.amount = amount
        self.category = category
        self.type = type
        self.date = date
        self.description = description


    def to_dictionary(self):
        return {
            "amount" : self.amount,
            "category" : self.category,
            "type" : self.type,
            "date" : self.date,
            "description" : self.description
        }


    def from_dictionary(self):
        pass



t1 = Transaction(1000, "salary", "income", "2026-03-01", "monthly salary")
manager.add_transactions(t1)