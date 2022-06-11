import re

test_word = "dimes"
guess = ""

def database(word, letter, color):
    # note to self, make one for if the user makes a typo
    grays = ""
    yellows = ""
    guess = "01234"
    if color == "GRAY":
        grays = grays + letter
        print(guess)

    elif color == "YELLOW":
        yellows = yellows + letter
        print(guess)
    else:
        index = word.index(letter)
def guesser():
    # insert regex
    # pattern =
    # re.search(pattern, possible_answers)

print("Welcome! I am wordler the wordle solver.")

guess_word = input("Enter your  word! I suggest adieu or crane.\n").upper()
for letter in guess_word:
    color = input("What color was the letter " + letter + "?\nPlease enter gray, yellow, or green\n").upper()
    database(guess_word, letter, color)
