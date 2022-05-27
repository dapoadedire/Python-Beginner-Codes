accountname = ''
accountnumber = ''
balance = 0
accountpassword = ''
account_list = []

def newAccount(name, password):
    global accountname, accountnumber, balance, accountpassword
    accountname = name
    accountpassword = password
    accountnumber = 123456789
    balance = balance
    print(f"Your account number is {accountnumber}")
    
    
    

def show():
    global accountname, accountnumber, balance, accountpassword
    print(f"Account name: {accountname}")
    print(f"Account number: {accountnumber}")
    print(f"Balance: ${balance}")
    print("\n")

def getBalance(number, password):
    global accountname, accountnumber, balance, accountpassword
    if password == accountpassword and number == accountnumber:
        print(f"Your balance is: ${balance}")
    else:
        print("Incorrect password")

def deposit(amountToDeposit, number, password):
    global accountname, accountnumber, balance, accountpassword
    if amountToDeposit > 0:    
        if password == accountpassword and number == accountnumber:
            balance = balance + amountToDeposit
            print(f"Your new balance is: ${balance}")
        else:
            print("Incorrect password")
    else:
        print("Invalid amount")


def withdraw(amountToWithdraw, number, password):
    global accountname, accountnumber, balance, accountpassword
    if amountToWithdraw < 0 or amountToWithdraw > balance:
        print("Invalid amount")
    else:
        if password == accountpassword and number == accountnumber:
            balance = balance - amountToWithdraw
            print(f"Your new balance is: ${balance}")
        else:
            print("Incorrect password")
name = input("Enter your name")
password = input("Enter your desired password")
newAccount(name, password)
while True:
    print()
    print("Press b to check your account balance.")
    print("Press d to make a deposit.")
    print("Press w to withdraw.")
    print("Press s to show account information.")
    print("Press q to quit.")
    print()
    

    action = input("Enter one of the above options.").lower()[0]
    print()

    if action == "b":
        print("Get balance.")
        number= int(input("Enter your account number"))
        password= input("Enter your password: ")
        getBalance(number, password)
    elif action == "d":
        amountToDeposit = int(input("Enter your amount to deposit"))
        number= int(input("Enter your account number"))
        password= input("Enter your password: ")
        deposit(amountToDeposit, number, password)

    elif action == "w":
        amountToWithdraw = int(input("Enter your amount to withdraw"))
        number= int(input("Enter your account number"))
        password= input("Enter your password: ")
        deposit(amountToWithdraw, number, password)

    elif action == "s":
        show()

    elif action == "q":
        break


print("Thank for banking with us.")

