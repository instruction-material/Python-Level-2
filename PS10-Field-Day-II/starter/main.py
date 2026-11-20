import random


roster = ["Ari", "Bea", "Cleo", "Dara", "Eli", "Fay", "Gus", "Hana", "Ira", "Jai"]
unassigned = roster.copy()
first_index = random.randrange(len(unassigned))
red = [unassigned.pop(first_index)]
blue = []
print(f"First red team member: {red[0]}")
print(f"Unassigned: {len(unassigned)}")

# Keep alternating teams until the working list is empty.
