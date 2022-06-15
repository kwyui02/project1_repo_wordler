import re
import os


# declaration of starting variables
test_word = "dimes"
guess = ['_', '_', '_', '_', '_']


def input_word():
    guess_word = input("Enter your word! I suggest adieu or crane.\n").upper()
    return guess_word


def word_length_check(guess_word):
    """checks if the input word is 5 letters long"""
    valid_length = 5
    if len(guess_word) == valid_length:
        return True
    elif len(guess_word) > valid_length:
        print("The word is too long!\n")
        return False
    else:
        print("The word is too short!\n")
        return False


def char_check(guess_word):
    """checks for any special characters in the input word"""
    result = re.search(r"^[A-Z]*$", guess_word)
    if result is not None:
        return False
    else:
        # invalid input, ask to input again
        print("Invalid input! :(")
        return True


def database(word, index, grays, yellows):
    """interprets received data and updates the database"""
    # input color
    letter = word[index]
    color = ""
    while color not in ["GRAY", "YELLOW", "GREEN"]:
        color = input("What color was the letter " + letter + "?\nPlease enter gray, yellow, or green\n").upper()

        # process color chosen
        if color == "GRAY":
            grays = grays + letter
            print(guess)

        elif color == "YELLOW":
            yellows[str(index)] = yellows[str(index)] + letter  # update dictionary of yellows at the letter's position
            print(guess)

        elif color == "GREEN":
            guess[index] = letter
            print(guess)

        else:
            # repeat input
            print("Invalid input")

    return grays, yellows


def yellow_last_letter(last_letter):
    print("Choose a letter with the letter " + last_letter)


def value_check(index, grays, yellows):
    value = guess[index]
    if value == "_":
        if yellows[str(index)] != "":  # means there is a yellow character
            char = r"[^{grays}{yellow}]".format(grays=grays, yellow=yellows[str(index)])  # except grays and that yellow
            if yellows[str(index)] != "" and index == 4:  # for if the yellow character is the last
                last_yellow_letter = yellows[str(index)]
                yellow_last_letter(last_yellow_letter)
            return char
        else:
            char = r"[^{grays}]".format(grays=grays, yellows=yellows[str(index)])
            return char
    else:
        return value


def guesser(grays, yellows):
    """analyzes for the next best guess"""
    # open wordle dictionary
    wl = open('valid-wordle-words.txt', 'r')
    wordlist = wl.readlines()  # split txt file into separated lines
    wl.close()
    words_string = "".join(wordlist).upper()  # join lines into single word string

    # value check for letters
    letter1 = value_check(0, grays, yellows)
    letter2 = value_check(1, grays, yellows)
    letter3 = value_check(2, grays, yellows)
    letter4 = value_check(3, grays, yellows)
    letter5 = value_check(4, grays, yellows)

    # regex pattern matching
    pattern = r"\b{letter1}{letter2}{letter3}{letter4}{letter5}\b"
    pattern = pattern.format(letter1=letter1, letter2=letter2, letter3=letter3, letter4=letter4, letter5=letter5)
    results = re.findall(pattern, words_string)

    yellow_last_letter()

    # print possible words that fit current grays, yellows, and greens
    print("Possible words: ", results)

    # print current grays and yellows
    print("grays: {}".format(grays))
    print("yellows: {}".format(yellows))


def main():
    # declare list of grays and yellows
    grays = ""
    yellows = {
        "0": "",
        "1": "",
        "2": "",
        "3": "",
        "4": ""
    }

    # introduction
    print("Welcome! I am wordler the wordle solver.\n")
    print("GUIDE: ")
    print("GRAY = wrong letter")
    print("YELLOW = right letter, wrong position")
    print("GREEN = right letter, right position\n")

    # wordle solver, loop until word is solved
    is_solved = False
    guess_num = 1
    while not is_solved:
        # input word
        guess_word = input_word()

        # check for length of word
        while True:
            is_right_length = word_length_check(guess_word)
            if is_right_length:
                break
            guess_word = input_word()

        # special character check
        while True:
            has_characters = char_check(guess_word)
            if not has_characters:
                break
            guess_word = input_word()

        # loop for letter colors
        for index in range(len(guess_word)):
            grays, yellows = database(guess_word, index, grays, yellows)

        # runs guesser function
        guesser(grays, yellows)

        # check if wordle is solved
        while True:
            solve_input = input("Is the Wordle solved yet? (Yes/No) ").upper()
            if solve_input not in ["YES", "NO"]:
                print("Invalid input")
            else:
                if solve_input == "YES":
                    is_solved = True
                elif solve_input == "NO":
                    is_solved = False
                    guess_num += 1
                break

    # after the wordle is solved
    print("\nCongratulations! You have solved the wordle in {} tries!".format(guess_num))


if __name__ == "__main__":
    main()
