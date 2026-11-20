import random


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


    return deck


print("Sorted deck:")
print(create_deck())

for swaps in (10, 50, 100, 500):
    print(f"Shuffled deck after {swaps} swaps:")
    print(shuffle(swaps))
