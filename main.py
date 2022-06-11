import re
import os

test_word = "dimes"
guess = {1: "_",
         2: "_",
         3: "_",
         4: "_",
         5: "_"}


def database(word, letter):
    """interprets received data and updates the database"""
    # input color
    color = input("What color was the letter " + letter + "?\nPlease enter gray, yellow, or green\n").upper()

    # process color chosen
    grays = ""
    yellows = ""
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
        print("Invalid input")
        database(word, letter)


def guesser():
    """analyzes for the next best guess"""
    wl = open('valid-wordle-words.txt', 'r')
    wordlist = wl.readlines()
    wl.close()
    words_string = "".join(wordlist)
    print(words_string)

    pattern = r"^y.*"
    results = re.search(pattern, words_string)

    print(results)
    # return next_guess


def main():
    # introduction
    print("Welcome! I am wordler the wordle solver.")

    # input word
    guess_word = input("Enter your word! I suggest adieu or crane.\n").upper()

    # loop for letter colors
    for letter in guess_word:
        database(guess_word, letter)

    # TODO next guess
    # print("your next best guess is " + next_guess)

    guesser()


if __name__ == "__main__":
    main()
