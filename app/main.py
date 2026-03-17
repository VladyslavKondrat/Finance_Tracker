from manager import FinanceManager
from models import Transaction
from file_handler import save_data

def print_menu():
    print('--Finance Tracker by VK--')
    print('What do you want to do?')
    print('Add income: 1')
    print('Add expence: 2')
    print('Show my balance: 3')
    print('Show all transactions: 4')
    print('Save data: 5')
    print('Exit: 0')

def get_transaction_data():
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = input("Date: ")
    description = input("Description: ")

    return amount, category, date, description

while True:
    print_menu()
    try:
        user_choice = int(float(input('Choose option (integers only): ')))
    except ValueError:
        print('Invalid data type. Try again.')
    
    
    if user_choice == 1:
        try:
            amount_of_income = int(float(input('What is the income amout?: ')))
        except ValueError:
            print('Invalid data type. Try again.')
            continue
        
        category = input("Enter category: ")
        date = input("Enter date (DD-MM-YYYY): ")
        description = input("Enter description: ")

        transaction = Transaction(amount_of_income, category, 'income', date, description)
        FinanceManager.add_transaction(transaction)

        print('Income added successfully')
    
   
    elif user_choice == 2:
        try:
            amount_of_expence = int(float(input('What is the expence amout?: ')))
        except ValueError:
            print('Invalid data type. Try again.')
            continue

        category = input("Enter category: ")
        date = input("Enter date (DD-MM-YYYY): ")
        description = input("Enter description: ")

        transaction = Transaction(amount_of_expence, category, 'expence', date, description)
        FinanceManager.add_transaction(transaction)

        print('Expence added successfully')


    
    elif user_choice == 3:
        my_balance = FinanceManager.get_balance()
        print(f'The balance is: {my_balance}')


    
    elif user_choice == 4:
        list_of_transactions = FinanceManager.transactions
        if not list_of_transactions:
            print("No transactions found.")
        else:
            for n in list_of_transactions:
                print(f'{n.date} | {n.type} | {n.category} | {n.amount} | {n.description}')
    
    
    
    elif user_choice == 5:
        save_data(FinanceManager.transactions)
        print("Data saved")
    
    
    elif user_choice == 0:
        save_data(FinanceManager.transactions)
        print("Data saved")
        break