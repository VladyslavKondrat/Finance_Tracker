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


    @classmethod
    def from_dictionary(cls, data):
        return cls(
            data["amount"],
            data["category"],
            data["type"],
            data["date"],
            data["description"]
        )
