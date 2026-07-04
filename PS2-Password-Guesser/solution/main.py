###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

password = "ilovecs"

user_guess = input("Enter the password: ")
num_guesses = 1
while user_guess != password:
    user_guess = input("Incorrect password. Try again: ")
    num_guesses = num_guesses + 1

print(
    "System unlocked! It took you " + str(num_guesses) + " tries to guess the password."
)
