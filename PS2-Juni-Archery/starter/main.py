import random

for shot in range(1, 4):
    result = "X" if random.randint(1, 3) == 1 else "O"
    print(f"Round 1, shot {shot}: {result}")

# Add four rounds and track the total number of X results.
