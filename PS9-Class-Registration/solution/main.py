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

# alternate Pythonic way: biologyStudents = set(biology)
biology_students = set()
for name in biology:
    biology_students.add(name)

print("Biology actually has " + str(len(biology_students)) + " students enrolled.")

computer_science_students = set()
for name in computer_science:
    computer_science_students.add(name)

print(
    "Computer Science actually has "
    + str(len(computer_science_students))
    + " students enrolled."
)

english_students = set()
for name in english:
    english_students.add(name)

print("English actually has " + str(len(english_students)) + " students enrolled.")

# Optional: Write a function getStudents(students) that takes in the list of students and returns the set of students.
