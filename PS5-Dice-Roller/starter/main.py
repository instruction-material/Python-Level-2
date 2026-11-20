import random


def dice_roll():
    return random.randint(1, 6)


first = dice_roll()
second = dice_roll()
print(f"First pair: {first} and {second}, total {first + second}")

# Repeat and count each possible sum from 2 through 12.
