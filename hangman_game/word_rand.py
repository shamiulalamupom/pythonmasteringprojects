import random

def randWord():
    words = ['definition', 'context', 'sir', 'unit', 'candidate']

    for i in range(len(words)):
        word = words[random.randint(0, i)]

    print(f'The length of the word is {len(word)}')

    return word