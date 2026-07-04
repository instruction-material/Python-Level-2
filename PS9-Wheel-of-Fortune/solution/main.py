###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

correct_word = "programming"
guessed_letters = set()
num_guesses_remaining = 15

# fill up set with the correct letters
# Pythonic shortcut: correctLetters = set(correctWord)
correct_letters = set()
for letter in correct_word:
    correct_letters.add(letter)

print(
    "Welcome to the Wheel of Fortune! You have "
    + str(num_guesses_remaining)
    + " guesses to figure out the correct word. Good luck!"
)

# alternatively, could use while numGuessesRemaining > 0
while True:
    # print out the current state of the guessed word
    current_state = ""
    for letter in correct_word:
        if letter in guessed_letters:
            current_state += letter + " "
        else:
            current_state += "_ "
    print(current_state)
    print("")

    # ask for a guess
    guessed_letter = input(
        "Guess a letter! You have " + str(num_guesses_remaining) + " guesses remaining."
    )
    num_guesses_remaining -= 1

    # add the guessed letter to the set if it's a correct letter
    if guessed_letter in correct_letters:
        guessed_letters.add(guessed_letter)

    # check if all of the letters have been guessed
    if len(guessed_letters) == len(correct_letters):
        print("Congratulations, you win!")
        break

    # check if the player is out of guesses
    if num_guesses_remaining == 0:
        print("Sorry, you're out of guesses!")
        break
