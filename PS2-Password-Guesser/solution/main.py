target_phrase = "blue comet"
guess = input("Enter a guess for the target phrase: ")
attempts = 1

while guess != target_phrase:
    guess = input("Different phrase. Try again: ")
    attempts += 1

print("Phrase matched. Attempts:", attempts)
