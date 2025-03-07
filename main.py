import re


guess = ['_', '_', '_', '_', '_']
valid_length = 5


def input_letter(letter: str) -> str:
    print(f"What color was the letter {letter}?", end=" ")
    color = input("Please enter gray, yellow, or green.\n").upper()
    while color not in ["GRAY", "YELLOW", "GREEN"]:
        print("Invalid input.", end=" ")
        color = input("Please enter gray, yellow, or green.\n").upper()
    return color


def print_guide() -> None:
    print("Welcome! I am wordler the wordle solver.\n")
    print("GUIDE: ")
    print("GRAY = wrong letter")
    print("YELLOW = right letter, wrong position")
    print("GREEN = right letter, right position\n")


def validate_word() -> str:
    def input_word() -> str:
        return input("Enter your word: \n").upper()
    
    def word_length_check(guess_word: str) -> int:
        """ 
            checks if the input word is 5 letters long, returns:
            1 if the word is valid
            0 if the word is too long
            -1 if the word is too short
        """
        if len(guess_word) == valid_length:
            return 1
        elif len(guess_word) > valid_length:
            return 0
        else:
            return -1

    def char_check(guess_word: str) -> bool:
        """
            checks for any special characters in the input word
            returns True if there are no special characters
        """
        return re.search(r"^[A-Za-z]*$", guess_word) is not None

    guess_word = input_word()
    while True:
        is_right_length = word_length_check(guess_word)
        if is_right_length == 1:
            break
        if is_right_length == 0:
            print("The word is too long!\n")
        else:
            print("The word is too short!\n")
        guess_word = input_word()

    while True:
        has_no_characters = char_check(guess_word)
        if has_no_characters:
            break
        print("Invalid input. Please remove any special characters.")
        guess_word = input_word()

    return guess_word


def database(word: str, grays: str, yellows: 
             dict[str, int]) -> tuple[str, dict[str, int]]:
    """interprets received data and updates the database"""
    for index in range(valid_length):
        letter = word[index]
        color = input_letter(letter)
        if color == "GRAY":
            grays += letter
        elif color == "YELLOW":
            yellows[index] += letter
        elif color == "GREEN":
            guess[index] = letter
    return grays, yellows


def value_check(index: int, grays: str, 
                yellows: dict[str, int]) -> str:
    value = guess[index]
    if value == "_":
        return r"[^{grays}{yellow}]".format(grays=grays, yellow=yellows[index])
    else:
        return value


def guesser(grays: str, yellows: dict[str, int]) -> list[str]:
    """analyzes for the next best guess"""
    # take guess and filter results
    with open('valid-wordle-words.txt', 'r') as f:
        wordlist = f.readlines()

    words_string = "".join(wordlist).upper()
    letters = [value_check(i, grays, yellows) for i in range(5)]

    pattern = r"\b{letter1}{letter2}{letter3}{letter4}{letter5}\b"
    pattern = pattern.format(letter1=letters[0], 
                             letter2=letters[1], 
                             letter3=letters[2], 
                             letter4=letters[3], 
                             letter5=letters[4])
    results = re.findall(pattern, words_string)

    results_str = "\n".join(results).upper()
  
    # for yellow letters
    n = 0
    yellow_class = ""

    for value in yellows.values():
        if value != "":
            n += 1
            yellow_class += value

    for yellow_char in yellow_class:
        pattern = r"\b.*[{yellow_char}].*\b"
        pattern = pattern.format(yellow_char=yellow_char)
        results_str = re.findall(pattern, results_str)
        results_str = "\n".join(results_str)

    
    return results_str.split("\n")


def main() -> None:
    grays = ""
    yellows = {
        0: "",
        1: "",
        2: "",
        3: "",
        4: ""
    }
    is_solved = False
    guess_ctr = 1

    print_guide()
    while not is_solved:
        if guess_ctr == 1:
            print("It's your first word! "
                "Try beginning with the word CRANE :)")

        guess_word = validate_word()
        grays, yellows = database(guess_word, grays, yellows)
        guesses = guesser(grays, yellows)
        guesses_num = len(guesses)
        print(f"\nTry one of these!: {guesses}")
        print(f"There are {guesses_num} possible words left.")

        while True:
            solve_input = input("Is the Wordle solved yet? (Yes/No) ").upper()
            if solve_input not in ["YES", "NO"]:
                print("Invalid input")
            else:
                if solve_input == "YES":
                    is_solved = True
                elif solve_input == "NO":
                    is_solved = False
                    guess_ctr += 1
                break

    print(f"\nCongratulations! You have solved the wordle in {guess_ctr + 1} " 
          "tries!")


if __name__ == "__main__":
    main()
