import random


def show_menu():
    while True:
        menu = input("Enter 'menu' for Menu: ")
        if menu.lower() == 'menu':
            print('Type Start - to start the game')
            print('Type quit - to Quit!')
        elif menu.lower() == "quit":
            return False
        elif menu.lower() == "start":
            guess_rand_num()
        else:
            print("invalid input!")



def guess_rand_num():
    declared_max_num = int(input("Pick a number to be the celling maximum: "))
    guess_count = 0
    random_num = random.randint(0,declared_max_num)

    while True:
        guess = int(input(f'Take a guess [Reminder: {declared_max_num} is the max!]: '))
        guess_count += 1
        if guess == random_num:
            print(f'You got it! Number of guesses needed: {guess_count}')
            break
        else:
            print("Wrong guess")



show_menu()