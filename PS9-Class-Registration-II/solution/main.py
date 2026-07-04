biology = ["Sarah", "Ahmed", "Fred", "Gillian", "Shradah", "Max", "Max", "Sara", "Max", "Esther"]

computer_science = ["Sarah", "John", "Fred", "Gillian", "Jermaine", "Max", "Sara", "Juan", "Esther"]

english = ["Nico", "Sharjeel", "Isabella", "Taylor", "Ali", "Ali", "Jean-Baptiste", "Jean-Baptiste", "Jean-Baptiste", "William"]

def generate_waitlist(students):
  enrolled = set()
  waitlist = set()
  for name in students:
    if len(enrolled) < 6:
      enrolled.add(name)
    elif name not in enrolled:
      waitlist.add(name)
  return waitlist

print("Waitlisted for Biology: " + str(generate_waitlist(biology)))
print("Waitlisted for Computer Science: " + str(generate_waitlist(computer_science)))
print("Waitlisted for English: " + str(generate_waitlist(english)))