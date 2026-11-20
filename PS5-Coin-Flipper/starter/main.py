import random


def flip_coin():
    if random.randint(0, 1) == 0:
        return "heads"
    return "tails"


print(f"One flip: {flip_coin()}")

# Add a loop and separate counts for heads and tails.
