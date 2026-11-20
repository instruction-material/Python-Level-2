target = 27
guess = int(input("Guess a whole number from 1 to 50: "))

if guess == target:
    print("Correct!")
elif guess < target:
    print("Too low!")
else:
    print("Too high!")

# Repeat and count guesses before switching to a random target.
