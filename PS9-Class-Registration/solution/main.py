biology = [
    "Sarah",
    "Ahmed",
    "Fred",
    "Gillian",
    "Shradah",
    "Max",
    "Max",
    "Sara",
    "Max",
    "Esther",
]

computer_science = [
    "Sarah",
    "John",
    "Fred",
    "Gillian",
    "Jermaine",
    "Max",
    "Sara",
    "Juan",
    "Esther",
]

english = [
    "Nico",
    "Sharjeel",
    "Isabella",
    "Taylor",
    "Ali",
    "Ali",
    "Jean-Baptiste",
    "Jean-Baptiste",
    "Jean-Baptiste",
    "William",
]


rosters = {
    "Biology": biology,
    "Computer Science": computer_science,
    "English": english,
}

for class_name, roster in rosters.items():
    students = sorted(set(roster))
    print(f"{class_name}: {len(students)} students enrolled.")
    print(", ".join(students))
