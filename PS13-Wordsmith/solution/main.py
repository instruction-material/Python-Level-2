import random
import time

# reads words into list
f = open("valid_words.txt")
valid_words = f.readlines()
valid_words = [x.strip() for x in valid_words]
f.close()

# pick 7 random letters (use a set to avoid duplicates)
letters = set()

while len(letters) < 7:
    start_num = ord("a")
    end_num = ord("z")
    random_num = random.randint(start_num, end_num)
    letter = chr(random_num)
    letters.add(letter)

# sets up score
score = 0

# sets up set of correctly guessed words
words = set()

# prints instructions
input(
    "Welcome to Wordsmith! In this game, come up with as many words as you can using the 7 letters you are given. Press Enter to begin!"
)
print("Ready....")
time.sleep(1)
print("Set....")
time.sleep(1)
print("Go!")

print("Your random letters are:")
print(letters)

while True:
    word = input("Enter a word: ")
    is_valid = True
    for letter in word:
        if letter not in letters:
            is_valid = False
    if is_valid:
        if word in valid_words and word not in words:
            score += len(word)
            words.add(word)
            print("Valid word! Your score: " + str(score) + "\n")
        elif word in words:
            print("You already entered this word! Your score: " + str(score) + "\n")
        else:
            print("Invalid word! Your score: " + str(score) + "\n")
    else:
        print("You can only use the 7 letters you were given!\n")
