###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import random
import time


def create_deck():
    deck = []
    for i in range(1, 14):
        for j in range(4):
            deck.append(i)
    return deck


def shuffle(num_shuffles):
    deck = create_deck()

    for i in range(num_shuffles):
        index1 = random.randint(0, len(deck) - 1)
        index2 = random.randint(0, len(deck) - 1)

        temp = deck[index1]
        deck[index1] = deck[index2]
        deck[index2] = temp

    print("\nShuffled deck after " + str(num_shuffles) + " swaps: ")
    print(deck)


print("Sorted deck: ")
print(create_deck())
time.sleep(2)

shuffle(10)
time.sleep(3)

shuffle(50)
time.sleep(3)

shuffle(100)
time.sleep(3)

shuffle(500)
