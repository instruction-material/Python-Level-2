import random


def clear():
    print("\033c", end="")


def get_correct(code, guess):
    num_correct = 0
    for i in range(len(guess)):
        if code[i] == guess[i]:
            num_correct += 1
    return num_correct


def get_close(code, guess):

    # remove correct digits from both strings
    new_code = ""
    new_guess = ""
    for i in range(len(guess)):
        if code[i] != guess[i]:
            new_code += code[i]
            new_guess += guess[i]
    code = new_code
    guess = new_guess

    # calculate the correct number of close digits
    num_close = 0
    while len(code) > 0:
        for i in range(len(guess)):
            if guess[i] == code[0]:
                guess = guess[0:i] + guess[i + 1 :]
                num_close += 1
                break
        code = code[1:]
    return num_close


def create_secret_code(digits):
    code = ""
    for i in range(digits):
        code += str(random.randint(0, 4))
    return code


# ------------------------------------------------------------------

RULES = """Mastermind
The secret code is composed of 4 random digits between 0-4.

Enter a 4 digit guess and see how close you are!
\t-Correct: correct number, correct location
\t-Close: correct number, incorrect location
"""

print(RULES)
input("Press enter to start:")
clear()

NUM_DIGITS = 4
correct = 0
close = 0
code = create_secret_code(NUM_DIGITS)

while correct < NUM_DIGITS:

    while True:
        guess = input("Type in a " + str(NUM_DIGITS) + " digit guess (0-4): ").strip()
        if len(guess) == NUM_DIGITS and guess.isdigit():
            break

    correct = get_correct(code, guess)
    close = get_close(code, guess)
    print("Correct:", correct)
    print("Close:", close)
    print()

print("YOU WIN!!")
