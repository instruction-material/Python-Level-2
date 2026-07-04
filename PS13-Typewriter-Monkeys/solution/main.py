###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import random

# reads words into list
f = open("valid_words.txt")
valid_words = f.readlines()
valid_words = [x.strip() for x in valid_words]
f.close()

monkey_str = ""
print("Here's what the monkeys are typing on the typewriter:")
while True:
    # add a random character to the end of the monkeys' typing
    monkey_str += chr(random.randint(ord("a"), ord("z")))
    print(monkey_str)

    # check if last three letters are a valid word
    if len(monkey_str) >= 3:

        # get the last three letters of what has been typed
        # Pythonic shortcut: lastThreeLetters = monkeyStr[len(monkeyStr)-3:len(monkeyStr)]
        last_three_letters = ""
        for i in range(len(monkey_str) - 3, len(monkey_str)):
            last_three_letters += monkey_str[i]

        if last_three_letters in valid_words:
            print("The monkeys did it! " + last_three_letters + " is a word!")
            break
