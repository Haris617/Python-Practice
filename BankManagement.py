# Task 02:
# Write a C++ program for a bank account management system. The program should present a menu to the user with the following options:
# 1.	Create Account
# 2.	Deposit
# 3.	Withdraw
# 4.	Display Accounts
# 5.	Exit
# •	When the user selects option 1, the program should prompt the user to enter an account number, account holder name, and initial balance.
#   It should then create a new account and store the account details.

# •	When the user selects option 2, the program should prompt the user to enter an account number and the amount to deposit.
#   It should find the account based on the account number and update the account balance by adding the deposited amount.

# •	When the user selects option 3, the program should prompt the user to enter an account number and the amount to withdraw.
#   It should find the account based on the account number and check if the account balance is sufficient for the withdrawal.
#   If so, it should update the account balance by subtracting the withdrawn amount; otherwise, it should display an error message.

# •	When the user selects option 4, the program should display all the existing bank accounts.
#   It should print the account number, account holder name, and account balance in a formatted manner.

# •	When the user selects option 5, the program should exit with a goodbye message.

#   The program should use separate arrays (accountNumbers, accountHolderNames, accountBalances) to store the account details, with a maximum capacity of 100 accounts.
#   It should also include input validation to handle incorrect inputs and appropriate error messages for invalid account numbers or insufficient balances.

#   In addition to the menu options, your program should also include the following:

# •	Proper user prompts and informative messages to guide the user throughout the program.
# •	Use of functions for each menu option, including the creation of a new account, depositing into an account, withdrawing from an account, and displaying all accounts.
# •	Error handling for cases where the maximum number of accounts is reached, an account number is not found, or a withdrawal amount exceeds the account balance.
# •	Proper code indentation, meaningful variable names, and comments for better readability and maintainability.

accNumber = []
accHolder = []
accBalance = []

def menu():
    print('1. Create Account \n2. Deposit \n3. Withdraw \n4. Display Account \n5. Exit')

def create_account():
    tempID = int(input('Enter Account ID: '))

    if tempID in accNumber:
        print('Account already exists')

    else:
        accNumber.append(tempID)
        accHolder.append(str(input('Enter Account Holder: ')))
        accBalance.append(int(input('Enter Account Balance: ')))

def deposit():
    tempID = int(input('Enter Account ID: '))
    if tempID in accNumber:
        index = accNumber.index(tempID)

        accBalance[index] += int(input('Enter Account Balance: '))

        print('{} Deposited'.format(tempID))
    else:
        print('Invalid Account ID')

def display():
    for a,h,b in zip(accNumber, accHolder, accBalance):
        print('Account Number : {} \nAccount Holder : {} \nAccount Balance : {}'.format(a,h,b))

def withDraw():
    tempID = int(input('Enter Account ID: '))
    if tempID in accNumber:
        index = accNumber.index(tempID)
        tempAmount = int(input('Enter Withdraw Amount: '))

        if tempAmount > accBalance[index]:
            print('Withdraw Amount Exceeded Balance')
        else:
            accBalance[index] -= tempAmount
    else:
        print('Invalid Account ID')


while(True):
    menu()
    option = int(input('Enter Option: '))

    match (option):
        case 1:
            create_account()
        case 2:
            deposit()
        case 3:
            withDraw()
        case 4:
            display()
        case 5:
            exit()
