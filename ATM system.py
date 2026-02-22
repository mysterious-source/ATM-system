transactions = []
balance = 0
def login():
    print("=== ACCOUNT SETUP ===")
    username = input("Enter a username: ")
    global correct_pin,balance
    correct_pin = input("Enter your pin: ")
    if len(correct_pin) < 6:
        print("Pin must be at least 6 digits")
        correct_pin = input("Enter your pin: ")
    pass    
    verify_pin = input("Verify pin: ")
    while correct_pin != verify_pin:
        print("The pins are different retry again")
        correct_pin = input("Enter: ")
        verify_pin = input("Verify pin: ")
    else:
        print("Let's proceed")
    balance = int(input("Enter your starting balance: "))
    print("Account created successfully!\n")
def verify_pin():
    count = 0
    pin2 = input("Enter pin: ")
    while pin2 != correct_pin and count < 3:
        print("Your pin is incorrect")
        pin2 = input("Enter pin again: ")
        count += 1
    pass    
def check_balance():
    global balance
    print("Before we continue you have to enter your pin to verify")
    verify_pin()
    if balance == 0:
        print("Please there haven't been activity on this account")
    else:
     print("Ok your balance is",balance)
     transaction_check_balance = {}
     transaction_check_balance['type'] = "balance check"
     transaction_check_balance["amount"] = balance
     transactions.append(transaction_check_balance)

def deposit():
    global balance
    print("Let's verify it's you by entering your pin")
    verify_pin()
    print("How much do u want to deposit?")
    amount1 = int(input("Enter amount: "))
    print("Ok the amount has been deposited with no complication ")
    transaction_deposit = {}
    transaction_deposit['type'] = "deposit"
    transaction_deposit["amount"] = amount1
    transactions.append(transaction_deposit)
    balance += amount1

def withdraw():
    global balance
    print("To proceed please verify your pin")
    verify_pin()    
    print("Ok let's proceed")
    withdraw_amount = int(input("Enter the amount: "))
    if withdraw_amount > balance :
        print("Insufficient amount")
    else:
     print("Amount has been successfully withdrew")
     transaction_withdraw = {}
     transaction_withdraw['type'] =  "withdraw"
     transaction_withdraw["amount"]=  withdraw_amount
     transactions.append(transaction_withdraw)
    balance -= withdraw_amount
   

def show_transaction():
    if  transactions == []:
        print("A transaction hasn't been made")
    else:
        for t in transactions:
         print(t)


print("Welcome to the ATM\n")
login()

while True:
    print("\n=== MENU ===")
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Transaction History")
    print("4 - Check Balance")
    print("5 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        show_transaction()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid option. Try again.")



