from random import choice

def run_game():
    word: str = choice(["banana","apple","wizard"])

    username: str = input("What is your username ")
    print(f"Hello {username}")

    guessed: str = ''
    tries: int = 10


    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char,end='')
            else:
                print('_',end='')
                blanks+=1

        print() # Add Blank line


        if blanks == 0:
            print("You got it")
            break

        guess: str = input("Enter a letter")

        if guess in guessed:
            print(f'You allready used: "{guess}". Please try with another letter!')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry that was wrong.. {tries}: tries remaining!')

            if tries == 0:
                print("No more tries remaining lose")
                break


if __name__ == '__main__':
    run_game()