import re
import os

test_word = "dimes"
guess = {1: "_",
         2: "_",
         3: "_",
         4: "_",
         5: "_"}

def database(word, letter, color):
    """interprets received data and updates the database"""
    # note to self, make one for if the user makes a typo
    grays = ""
    yellows = ""
    if color == "GRAY":
        grays = grays + letter
        print(guess)

    elif color == "YELLOW":
        yellows = yellows + letter
        print(guess)

    else:
        index = word.index(letter) + 1
        guess[index] = letter
        print(guess.values())

def guesser():
    """analyzes for the next best guess"""
    re.search(pattern, possible_answers)
    # wl = open('/usr/share/dict/words', 'r')
    # wordlist = wl.readlines()
    # wl.close()
    # words_string = "".join(wordlist)
    # print(type(words_string))
    #
    # pattern = r"z.*"
    # result = re.search(pattern, words_string)
    #
    # print(result)
    return next_guess

print("Welcome! I am wordler the wordle solver.")

guess_word = input("Enter your  word! I suggest adieu or crane.\n").upper()
for letter in guess_word:
    color = input("What color was the letter " + letter + "?\nPlease enter gray, yellow, or green\n").upper()
    database(guess_word, letter, color)

print("your next best guess is " + next_guess)