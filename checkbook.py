import os

# function to first initialize the balance
def initialize_balance():
    balance = 0
    if os.path.exists("checkbook_ledger.txt"):
        with open("checkbook_ledger.txt", "r") as file: # r is for reading the txt file
            try:
                balance = float(file.read())
            except ValueError:
                balance = 0
    return balance
# Above function attempts to find and read a balance from the txt file to display, will show 0 otherwise.



# function to display the current balance
def display_balance(balance):
    print(f'Current Balance: ${balance:.2f}') # two decimal points

    
    
# function to add a credit (deposit) to the balance
def add_credit(balance):
    try:
        credit = float(input('Enter the amount to deposit: $'))
        balance += credit #easy way to add the deposit
        print(f'\nsuccessfully deposited ${credit:.2f}')
        return balance
    except ValueError:    # These are easy ways to respond to non-float inputs
        print('Invalid input. Please enter a valid amount.')
        return balance
    

# function to add a debit (withdrawal) from the balance 
def add_debit(balance):
    try:
        debit = float(input('Enter the amount to withdraw: $'))
        if balance - debit >= 0:  # This means it you can't withdraw more than what you have
            balance -= debit
            print(f'\nsuccessfully withdrew ${debit:.2f}') 
        else:
            print('Insufficient funds.')
        return balance
    except ValueError:   # These are easy ways to respond to non-float inputs
        print('Invalid input. Please enter a valid amount.')
        return balance
    
# function to SAVE the balance to a file
def save_balance(balance):
    with open('checkbook_ledger.txt', 'w') as file: # will 'w'rite what it shows
        file.write(str(balance))  # str used to make it simpler since won't be needing to handle it as a int or float

# MAIN program loop
def main():
    balance = initialize_balance()
    print("~~~ Welcome to Josue's Checkbook App! ~~~")
    
    while True:
        print('\nHello! What would you like to do today?\n')
        print('1. View Current Balance')
        print('2. Record a credit (deposit)')
        print('3. Record a debit (withdraw)')
        print('4. Exit')
        
        choice = input('\nPlease enter your choice: ')
        
        if choice == '1':
            display_balance(balance)
            
        elif choice == '2':
            balance = add_credit(balance)
            
        elif choice == '3':
            balance = add_debit(balance)
            
        elif choice == '4':
            save_balance(balance)
            print(' Thank you for using Josue\'s Checkbook App! Your balance has been recorded.')
            break
            
        else:
            print('Invalid choice. Please select a valid option.')

if __name__ == "__main__":
    
    main()