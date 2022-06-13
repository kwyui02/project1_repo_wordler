import re


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
            yellows = yellows + letter
            print(guess)

        elif color == "GREEN":
            guess[index] = letter
            print(guess)

        else:
            # repeat input
            print("Invalid input")

    return grays, yellows


def guesser():
    """analyzes for the next best guess"""
    # open wordle dictionary
    wl = open('valid-wordle-words.txt', 'r')
    wordlist = wl.read().splitlines()  # split txt file into word list
    wl.close()

    words_string = "".join(wordlist)
    # print(words_string)

    results = re.findall(r"\by\w*\b", words_string)
    print(results)

    # regex pattern matching
    pattern = r"\sa\w*"
    results = re.findall(pattern, words_string)
    
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

    # TODO next guess
    # print("your next best guess is " + next_guess)

    guesser()

if __name__ == "__main__":
    main()
