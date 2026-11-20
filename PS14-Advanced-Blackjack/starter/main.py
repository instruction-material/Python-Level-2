face_values = {"J": 10, "Q": 10, "K": 10, "A": 1}


def base_total(hand):
    total = 0
    for rank in hand:
        if rank in face_values:
            total += face_values[rank]
        else:
            total += int(rank)
    return total


hand = ["A", "6"]
print(f"Base total: {base_total(hand)}")

# Treat an ace as 11 when adding ten keeps the hand at 21 or below.
