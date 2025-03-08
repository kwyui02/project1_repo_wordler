from re import findall, search


def print_guide() -> None:
    print("Welcome! I am wordler the wordle solver.\n")
    print("GUIDE: ")
    print("GRAY = wrong letter")
    print("YELLOW = right letter, wrong position")
    print("GREEN = right letter, right position\n")
    print("It's your first word! Try beginning with the word CRANE :)")


def print_finish(guess_ctr: int) -> None:
    if guess_ctr == 1:
        print("\nCongratulations! You have solved the wordle in 1 try!")
    else:
        print(f"\nCongratulations! You have solved the wordle in {guess_ctr}"
            " tries!")


def validate_word() -> str:
    """
        validates the input word\n
        returns the word if it is valid\n
        prompts the user again if it is invalid
    """
    def input_word() -> str:
        return input("Enter your word: \n").upper()
    
    def word_length_check(guess_word: str) -> int:
        """ 
            checks if the input word is the valid length, returns:\n
            1 if the word is valid\n
            0 if the word is too long\n
            -1 if the word is too short
        """
        if len(guess_word) == valid_length:
            return 1
        if len(guess_word) > valid_length:
            return 0
        return -1

    def char_check(guess_word: str) -> bool:
        """
            checks for any special characters in the input word\n
            returns True if there are no special characters
        """
        return search(r"^[A-Za-z]*$", guess_word) is not None

    while True:
        guess_word = input_word()
        is_right_length = word_length_check(guess_word)
        if is_right_length != 1:
            if is_right_length == 0:
                print("The word is too long!\n")
            else:
                print("The word is too short!\n")
            continue

        has_no_characters = char_check(guess_word)
        if not has_no_characters:
            print("Invalid input. Please remove any special characters.")
            continue
        return guess_word


def validate_wordle_solve() -> bool:
    """
        validates the input for wordle solve\n
        returns the input if the input is valid (YES/NO)\n
        prompts the user again if the input is invalid
    """
    while True:
        solve_input = input("Is the Wordle solved yet? (Yes/No) ").upper()
        if solve_input not in ["YES", "NO"]:
            print("Invalid input")
        else:
            return solve_input == "YES"


def update_database(word: str, grays: str, yellows: 
                    list[str]) -> tuple[str, list[str]]:
    """
        interprets received data and updates the database
    """
    def input_letter(letter: str) -> str:
        """
            prompts the user for the color of the letter\n
            returns the color of the letter (GRAY, YELLOW, GREEN)
        """
        print(f"\nWORD: {"".join(guess)}")
        print(f"GRAYS: {"".join(set(grays))}")
        print(f"YELLOWS: {yellows}")
        print(f"What color was the letter {letter}?", end=" ")
        color = input("Please enter gray, yellow, or green.\n").upper()
        while color not in ["GRAY", "YELLOW", "GREEN"]:
            print("Invalid input.", end=" ")
            color = input("Please enter gray, yellow, or green.\n").upper()
        return color

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


def value_check(grays: str, yellows: list[str]) -> str:
    """
        excludes the gray and yellow letters from each letter index
    """
    letters = []
    for index in range(valid_length):
        value = guess[index]
        if value == "_":
            letters.append(rf"[^{grays}{yellows[index]}]")
        else:
            letters.append(value)
    return "".join(letters)


def guesser(grays: str, yellows: list[str]) -> list[str]:
    """
        analyzes for the next best guess
    """
    # for green letters
    letters = value_check(grays, yellows)
    results = findall(rf"\b{letters}\b", words_string)
    results_str = "\n".join(results).upper()
  
    # for yellow letters
    yellow_chars = "".join(yellows)
    for char in yellow_chars:
        results_str = "\n".join(findall(rf"\b.*[{char}].*\b", results_str))
    
    if results_str == "":
        return []
    return results_str.split("\n")


def main() -> None:
    grays = ""
    yellows = [""] * valid_length
    is_solved = False
    guess_ctr = 1

    print_guide()
    while not is_solved:
        guess_word = validate_word()
        grays, yellows = update_database(guess_word, grays, yellows)
        if "_" not in guess:  # check if word is guessed already (all green)
            break
        guesses = guesser(grays, yellows)
        print(f"\nTry one of these!: {guesses}")
        print(f"There are {len(guesses)} possible words left.")
        is_solved = validate_wordle_solve()
        guess_ctr += 1

    print_finish(guess_ctr)


if __name__ == "__main__":
    # process the wordle words into uppercase string format
    guess = ["_" for _ in range(5)]
    valid_length = 5
    with open('valid-wordle-words.txt', 'r') as f:
        wordlist = f.readlines()
    words_string = "".join(wordlist).upper()
    main()
