import random


def roll():
    min_value = 1
    max_value = 6
    random_roll = random.randint(min_value,max_value)
    return random_roll



while True:
    players_count = input("Players playing? (2-4)")
    if players_count.isdigit():
        players_count = int(players_count)
        if 1 <= players_count <= 4:
            print(f'{players_count} players joined the lobby')
            break
        else:
            print("Invalid number")
    else:
        print("invalid input!")

max_score = 10
players_score = [0 for _ in range(players_count)]

while max(players_score) < max_score:
    for players_index in range(players_count):
        print(f'Player {players_index} is taking his turn ...')
        print(f'Your total score is {players_score[players_index]}')

        player_score = 0

        while True:
            roll_now = input("To roll the dice - type roll")
            if roll_now.lower() != "roll":
                print("invalid choice!")
                break


            value = roll()
            if value == 1:
                print("Rolled 1 Turn done!")
                player_score = 0
                break
            else:
                player_score += value
                print(f"Rolled {value}")
                print(f"Player {players_index} score: {player_score}")

max_score = max(player_score)
winning_player = players_score.index(max_score)
print(f'Player number {winning_player + 1} is the winner with a score of {max_score}')


