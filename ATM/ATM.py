import random

user_name = "aniwash"
passwd = 1234
cash_balance = random.randint(500,1000)

def deposit():
    global cash_balance
    deposit_amount = int(input("How much would you like to deposit?"))
    cash_balance += deposit_amount
    print(f'{deposit_amount} added to your balance.   Balance: {cash_balance}')

def withdrawl():
    global cash_balance
    withdrawl_amount = int(input("How much would you like to withdraw?"))
    cash_balance -= withdrawl_amount
    print(f'{withdrawl_amount} withdrawed from your balance.   Balance: {cash_balance}')


while True:
    menu_choice = input('''
    ***Welcome to printside ATM***
    Press 1 - Withdraw
    Press 2 - Deposit
    press 3 - Quit 
    ''')
    if int(menu_choice) == 1:
        withdrawl()
    if int(menu_choice) == 2:
        deposit()
    elif int(menu_choice) == 3:
        print("Thank you for using Printside ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

        after_action_menu = input("Would you like to make another action? (yes/no) ")
        if after_action_menu.lower() != 'yes':
            print("Thank you for using Printside ATM. Goodbye!")
            break

