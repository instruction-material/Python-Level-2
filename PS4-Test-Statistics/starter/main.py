total = 0
for student in range(1, 6):
    entry = input(f"Score {student}: ").strip()
    while not (entry.isascii() and entry.isdecimal() and int(entry) <= 100):
        entry = input("Enter a whole-number score from 0 to 100: ").strip()
    score = int(entry)
    total += score
    # Compare this score with the highest and lowest values so far.

print(f"Average: {total / 5}")
