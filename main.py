import re


guess = ['_', '_', '_', '_', '_']


def input_word():
    guess_word = input("Enter your word!\n").upper()
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
    result = re.search(r"^[A-Za-z]*$", guess_word)
    if result is not None:
        return False
    else:
        print("Invalid input! :(")
        return True


def database(word, index, grays, yellows):
    """interprets received data and updates the database"""
    letter = word[index]
    color = ""
    while color not in ["GRAY", "YELLOW", "GREEN"]:
        color = input("What color was the letter " + letter + "?\nPlease enter gray, yellow, or green\n").upper()

        if color == "GRAY":
            grays = grays + letter

        elif color == "YELLOW":
            yellows[str(index)] = yellows[str(index)] + letter

        elif color == "GREEN":
            guess[index] = letter

        else:
            print("Invalid input")

    return grays, yellows


def value_check(index, grays, yellows):
    value = guess[index]
    if value == "_":
        if yellows[str(index)] != "":
            char = r"[^{grays}{yellow}]".format(grays=grays, yellow=yellows[str(index)])
            return char
        else:
            char = r"[^{grays}]".format(grays=grays, yellows=yellows[str(index)])
            return char
    else:
        return value


def last_char_is_yellow(yellows):
    if yellows[str(4)] != "":
        return True
    else:
        return False


def guesser(grays, yellows, guess_num):
    """analyzes for the next best guess"""
    wl = open('valid-wordle-words.txt', 'r')
    wordlist = wl.readlines()
    wl.close()
    words_string = "".join(wordlist).upper()

    letter1 = value_check(0, grays, yellows)
    letter2 = value_check(1, grays, yellows)
    letter3 = value_check(2, grays, yellows)
    letter4 = value_check(3, grays, yellows)
    letter5 = value_check(4, grays, yellows)

    pattern = r"\b{letter1}{letter2}{letter3}{letter4}{letter5}\b"
    pattern = pattern.format(letter1=letter1, letter2=letter2, letter3=letter3, letter4=letter4, letter5=letter5)
    results = re.findall(pattern, words_string)

    results_str = "\n".join(results).upper()
  
    n = 0
    yellow_class = ""

    for value in yellows.values():
        if value != "":
            n += 1
            yellow_class = yellow_class + value

    for yellow_char in yellow_class:
        pattern = r"\b.*[{yellow_char}].*\b"
        pattern = pattern.format(yellow_char=yellow_char)
        results_str = re.findall(pattern, results_str)
        results_str = "\n".join(results_str)

    final_without_remove = results_str.split("\n")

    if guess_num == 1:
        print("Try SLIPT after CRANE ;D")
    else:
        print("Try one of these!: ", final_without_remove)


def main():
    grays = ""
    yellows = {
        "0": "",
        "1": "",
        "2": "",
        "3": "",
        "4": ""
    }

    print("Welcome! I am wordler the wordle solver.\n")
    print("GUIDE: ")
    print("GRAY = wrong letter")
    print("YELLOW = right letter, wrong position")
    print("GREEN = right letter, right position\n")

    is_solved = False
    guess_num = 1
    while not is_solved:
        if guess_num == 1:
            guess_word = input("Enter your first word! Try beginning with the word CRANE :)\n")
        else:
            guess_word = input_word()

        while True:
            is_right_length = word_length_check(guess_word)
            if is_right_length:
                break
            guess_word = input_word()

        while True:
            has_characters = char_check(guess_word)
            if not has_characters:
                break
            guess_word = input_word()

        for index in range(len(guess_word)):
            grays, yellows = database(guess_word, index, grays, yellows)

        guesser(grays, yellows, guess_num)

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

    print("\nCongratulations! You have solved the wordle in {} tries!".format(guess_num + 1))


if __name__ == "__main__":
    main()
