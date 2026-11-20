total = 0
lowest = 100
highest = 0
for student in range(1, 6):
    entry = input(f"Score {student}: ").strip()
    while not (entry.isascii() and entry.isdecimal() and int(entry) <= 100):
        entry = input("Enter a whole-number score from 0 to 100: ").strip()
    score = int(entry)
    total += score
    if score < lowest:
        lowest = score
    if score > highest:
        highest = score

print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Average: {total / 5}")
