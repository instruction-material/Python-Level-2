###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import random


def flip_coin():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


num_flips = 1000
num_heads = 0
num_tails = 0

for i in range(0, num_flips):
    heads_or_tails = flip_coin()
    if heads_or_tails == "heads":
        num_heads += 1
    else:
        num_tails += 1
print(str((num_heads / num_flips) * 100) + "% of your flips were heads.")
print(str((num_tails / num_flips) * 100) + "% of your flips were tails.")
