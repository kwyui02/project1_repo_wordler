import re
import os


# declaration of starting variables
test_word = "dimes"
guess = {1: "_",
         2: "_",
         3: "_",
         4: "_",
         5: "_"}


def word_length_check():
    """checks if the input word is 5 letters long"""
    valid_length = 5
    while True:
        guess_word = input("Enter your word! I suggest adieu or crane.\n").upper()
        if len(guess_word) == valid_length:
            return guess_word
        elif len(guess_word) > valid_length:
            print("The word is too long!")
        else:
            print("The word is too short!")


def char_check(guess_word):
    """checks for any special characters in the input word"""
    # TODO regex
    return guess_word


def database(word, letter, grays, yellows):
    """interprets received data and updates the database"""
    # input color
    color = ""
    while color not in ["GRAY", "YELLOW", "GREEN"]:
        color = input("What color was the letter " + letter + "?\nPlease enter gray, yellow, or green\n").upper()

        # process color chosen
        if color == "GRAY":
            grays = grays + letter
            print(guess)

        elif color == "YELLOW":
            yellows = yellows + letter
            print(guess)

        elif color == "GREEN":
            index = word.index(letter) + 1
            guess[index] = letter
            print(guess.values())

        else:
            # repeat input
            print("Invalid input")

    return grays, yellows


def guesser():
    """analyzes for the next best guess"""
    # open wordle dictionary
    wl = open('valid-wordle-words.txt', 'r')
    wordlist = wl.readlines()
    wl.close()
    words_string = "".join(wordlist)
    print(words_string)

    pattern = r"^y.*"
    results = re.search(pattern, words_string)

    print(results)
    # TODO return next_guess


def main():
    # declare list of grays and yellows
    grays = ""
    yellows = ""

    # introduction
    print("Welcome! I am wordler the wordle solver.\n")
    print("GUIDE: ")
    print("GRAY = wrong letter")
    print("YELLOW = right letter, wrong position")
    print("GREEN = right letter, right position\n")

    # input word
    guess_word = word_length_check()

    # special character check
    guess_word = char_check(guess_word)

    # loop for letter colors
    for letter in guess_word:
        grays, yellows = database(guess_word, letter, grays, yellows)

    # TODO next guess
    # print("your next best guess is " + next_guess)

    # TODO guesser()


if __name__ == "__main__":
    main()
