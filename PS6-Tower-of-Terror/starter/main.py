weights = []
entry = input("Fictional rider weight or q: ").strip().lower()
if entry.isascii() and entry.isdecimal() and int(entry) > 0:
    weights.append(int(entry))
elif entry != "q":
    print("Enter a positive whole number or q.")

print(f"Recorded weights: {weights}")

# Read up to ten valid entries, then compute the total and mean.
