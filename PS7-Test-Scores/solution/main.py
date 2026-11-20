def read_count(prompt):
    while True:
        entry = input(prompt).strip()
        if entry.isascii() and entry.isdecimal():
            return int(entry)
        print("Enter a nonnegative whole number.")


student_count = read_count("Number of names: ")
test_count = read_count("Number of tests: ")
scores = {}
while len(scores) < student_count:
    name = input("Fictional name: ").strip().lower()
    if name and name not in scores:
        scores[name] = []
    else:
        print("Enter a new, nonempty name.")

for test in range(1, test_count + 1):
    for name, results in scores.items():
        score = read_count(f"Score for {name} on test {test}: ")
        while score > 100:
            print("Use a score from 0 through 100.")
            score = read_count(f"Score for {name} on test {test}: ")
        results.append(score)

if not scores:
    print("No names entered.")
for name, results in scores.items():
    print(f"{name} scores: {results}")
    if results:
        print(f"{name} average: {sum(results) / len(results):g}")
    else:
        print(f"{name}: No scores.")
