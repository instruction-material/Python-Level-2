def create_deck():
    deck = []
    for rank in range(1, 14):
        for copy in range(4):
            deck.append(rank)
    return deck


print("Sorted deck:")
print(create_deck())

# Pick two valid indexes and swap the cards. Repeat inside a function.
