from hangman_game import word_rand as ranw

def game():
    word = ranw.randWord()
    guess = input('Guess the word: ')

    if word == guess:
        print('You guess the word.')
        print()
        return 1
    else:
        print('You are wrong.')
        return 0

class HangmanGame():
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
# from hangman_game.game import HangmanGame
#
# HangmanGame()
