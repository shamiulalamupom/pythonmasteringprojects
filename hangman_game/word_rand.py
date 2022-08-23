import random

def randWord():
    words = ['definition', 'context', 'sir', 'unit', 'candidate']

    word = words[random.randint(0, len(words)-1)]

    print(f'The length of the word is {len(word)}')

    return word