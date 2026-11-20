target = "programming"
guess = input("Guess one letter: ").strip().lower()
visible = []
for letter in target:
    visible.append(letter if letter == guess else "_")
print(" ".join(visible))

# Keep a set of guesses and draw the updated puzzle after each attempt.
