from random import randint

def game():
    guess = int(input('Enter your guess(1-10): '))
    num = randint(1, 10)
    if guess == num:
        print()
        print(f'You guessed it correctly.\nThe number was {num}')
        return 1
    else:
        print()
        print(f'You guessed it wrong.\nThe number was {num}')
        return 0

class NumberGuessingGame():
    def start():
        start = 1
        points = 0
        while True:
            if start != 1:
                out = game()
                if out == 1:
                    points += 1
                    pass
                else:
                    print()
                    print('Total points: ', points)
                    print('----Quitting The Game----')
                    break
            if start == 1:
                start = 0

    start()

# To start the game:(copy and paste it in the main.py)
# from num_guessing_game.game import NumGuessingGame
#
# NumGuessingGame()