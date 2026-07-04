###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import random

print("Welcome to Juni Archery, prepare your bow!")

num_hits = 0
for i in range(1, 6):
    for j in range(1, 4):
        if random.randint(1, 3) == 1:
            print("Round", str(i) + ", arrow", str(j) + ": X")
            num_hits += 1
        else:
            print("Round", str(i) + ", arrow", str(j) + ": O")

print("You hit the bullseye " + str(num_hits) + " times!")
