import random

# reads words into list
f = open("valid_words.txt")
valid_words = f.readlines()
valid_words = [x.strip() for x in valid_words]
f.close()


def find_valid_word(n):
    monkey_str = ""
    print("Here's what the monkeys are typing on the typewriter:")
    while True:
        # add a random character to the end of the monkeys' typing
        monkey_str += chr(random.randint(ord("a"), ord("z")))
        print(monkey_str)

        # check if last n letters are a valid word
        if len(monkey_str) >= n:

            # get the last n letters of what has been typed
            # Pythonic shortcut: lastThreeLetters = monkeyStr[len(monkeyStr)-n:len(monkeyStr)]
            last_n_letters = ""
            for i in range(len(monkey_str) - n, len(monkey_str)):
                last_n_letters += monkey_str[i]

            if last_n_letters in valid_words:
                print("The monkeys did it! " + last_n_letters + " is a word!")
                break


while True:
    length = int(input("How long should the word be? "))
    find_valid_word(length)
