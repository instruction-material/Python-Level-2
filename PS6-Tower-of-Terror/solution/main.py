def get_weights():
    weights = []
    while len(weights) < 10:
        entry = input(f"Fictional rider {len(weights) + 1} weight or q: ").strip().lower()
        if entry == "q":
            break
        if entry.isascii() and entry.isdecimal() and int(entry) > 0:
            weights.append(int(entry))
        else:
            print("Enter a positive whole number or q.")
    return weights


weights = get_weights()
total = 0
for weight in weights:
    total += weight
print(f"Recorded weights: {weights}")
print(f"Total: {total}")
if weights:
    print(f"Average: {total / len(weights):g}")
else:
    print("Average unavailable. No weights recorded.")
