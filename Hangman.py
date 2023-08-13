import os
import emoji
from random import choice


HangmanList = [
        '''
            +---+
                |
                |
                |
                |
               ===
        ''',
        '''
            +---+
            O   |
                |
                |
                |
               ===
        ''',
        '''
            +---+
            O   |
            |   |
                |
                |
               ===
        ''',
        '''
            +---+
            O   |
           /|   |
                |
                |
               ===
        ''',
        '''
            +---+
            O   |
           /|\\  |
                |
                |
               ===
        ''',
        '''
            +---+
            O   |
           /|\\  |
           /    |
                |
               ===
        ''',
        '''
            +---+
            O   |
           /|\\  |
           / \\  |
                |
               ===
        '''
    ]


def Game():
    os.system('cls')
    WordsList = ['Esmail', 'Mohammed', 'Hossam', 'Eyad', 'Ahmed', 'Computer', 'IS']
    RandomWord = choice(WordsList)
    Choosed = list('_' * len(RandomWord))
    Counter = 0
    while Counter != 6:
        if '_' in Choosed:
            Letter = input('Enter a letter:')
            while len(Letter) != 1:
                print('Enter only one letter!')
                Letter = input('Enter a letter:')
            if Letter.lower() in RandomWord.lower():
                for index, letter in enumerate(RandomWord):
                    if Letter.lower() == letter.lower():
                        Choosed[index] = letter
                GussedWord = ''
                for index, letter in enumerate(Choosed):
                    GussedWord = GussedWord + letter
                print(GussedWord)
            else:
                Counter += 1
                print(HangmanList[Counter])
        else:
            GussedWord = ''
            for index, letter in enumerate(Choosed):
                GussedWord = GussedWord + letter
            print(emoji.emojize(":slightly_smiling_face:") + " You gussed the word:", GussedWord, emoji.emojize(":thumbs_up:"))
            break
    if Counter == 6:
        print("You lost!" + emoji.emojize(":face_with_tongue:"))


Game()