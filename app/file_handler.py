import json
from models import Transaction

def save_data(transactions, file_name = "data.json"):
    data = []

    for n in transactions:
        data.append(n.to_dict())

    with open(file_name, 'w') as file:
        json.dump(data, file, indent = 4)


def load_data(file_name = "data.json"):
    transactions = []

    try:
        with open(file_name, 'r') as file:
            data = json.load(file)

            for n in data:
                transaction = Transaction.from_dictionary(n)
                transactions.append(transaction)

    except FileNotFoundError:
        pass

    return transactions