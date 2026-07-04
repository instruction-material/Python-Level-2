import random

rand_num = random.randint(1, 50)
num_guesses = 1

guess = int(
    input("I am thinking of a random number between 1 and 50. Guess what it is! ")
)

while guess != rand_num:
    if guess > rand_num:
        print("That's too high!")
    else:
        print("That's too low!")

    guess = int(input("Enter a new guess: "))
    num_guesses += 1

print("You got it! I was thinking of the number " + str(guess) + "!")
print("It took you " + str(num_guesses) + " tries to guess my number.")
