import random

random_number = random.randint(0,2)
options_computer = ["rock","papers","scissors"]



def menu_rps():
    print("Welcome to Rock Papers Scissors!")
    menu = input("Start - start a game!")
    if menu.lower() == "start":
        start_game()
    elif menu.lower() == "quit":
        quit()

def start_game():
    player_wins = 0
    computer_wins = 0
    while True:
        computer_pick = options_computer[random_number]
        player_pick = input("Pick your weapon!")
        if player_pick.lower() == "rock" and computer_pick.lower() == "scissors":
            player_wins += 1
            print(f'Comp chooses {computer_pick}')
            print("You win!")
        elif player_pick.lower() == "scissors" and computer_pick.lower() == "paper":
            player_wins += 1
            print(f'Comp chooses {computer_pick}')
            print("You win!")
        elif player_pick.lower() == "paper" and computer_pick.lower() == "rock":
            player_wins += 1
            print(f'Comp chooses {computer_pick}')
            print("You win!")
        elif player_pick.lower() == "score":
            print(f'Your score: {player_wins} : Computer : {computer_wins}')
        elif player_pick.lower() == "quit":
            return False
        else:
            computer_wins += 1
            print("you lose!")


menu_rps()