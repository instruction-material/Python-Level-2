import random

points = 10
while points > 0:
    print("Current points:", points)
    choice = input("Press Enter to flip, or q to quit: ")
    if choice == "q":
        break
    if choice != "":
        print("Use Enter to flip or q to quit.")
        continue

    flip = random.choice(("heads", "tails"))
    if flip == "heads":
        points *= 2
        print("Heads. Points doubled.")
    else:
        points = 0
        print("Tails. The round ends.")

print("Final points:", points)
