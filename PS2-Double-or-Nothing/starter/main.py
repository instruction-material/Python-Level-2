import random

points = 10
print("Starting points:", points)
choice = input("Press Enter to flip, or q to quit: ")
if choice == "":
    print("Flip:", random.choice(("heads", "tails")))

# Add the point update and repeat until a loss or a quit.
