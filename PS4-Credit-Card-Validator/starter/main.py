sample = input("Fictional digit string: ").strip()

if len(sample) < 2 or not sample.isascii() or not sample.isdigit():
    print("Enter at least two ASCII digits.")
else:
    total = 0
    for character in sample:
        total += int(character)
    print(f"Unweighted sum: {total}")

    # Add a second total that applies the alternating rule from the right.
