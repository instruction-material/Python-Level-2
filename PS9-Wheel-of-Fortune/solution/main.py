target = "programming"
target_letters = set(target)
attempts = set()
remaining = 15


def reveal(word, guesses):
    visible = []
    for letter in word:
        visible.append(letter if letter in guesses else "_")
    return " ".join(visible)


while remaining > 0:
    print(reveal(target, attempts))
    guess = input(f"Guess a letter ({remaining} remaining): ").strip().lower()
    if len(guess) != 1 or not guess.isascii() or not guess.isalpha():
        print("Enter one letter from A to Z.")
        continue
    if guess in attempts:
        print("That letter has already been guessed.")
        continue
    attempts.add(guess)
    remaining -= 1
    if target_letters.issubset(attempts):
        print(reveal(target, attempts))
        print(f"Puzzle solved in {15 - remaining} guesses!")
        break
else:
    print(f"No guesses remain. The word was {target}.")
