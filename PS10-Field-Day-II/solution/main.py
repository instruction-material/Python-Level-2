import random


def assign_teams(roster, trace=False):
    unassigned = list(dict.fromkeys(roster))
    red = []
    blue = []
    next_team = red
    while unassigned:
        index = random.randrange(len(unassigned))
        next_team.append(unassigned.pop(index))
        next_team = blue if next_team is red else red
        if trace and (next_team is red or not unassigned):
            print(f"Red: {', '.join(red) or 'none'}")
            print(f"Blue: {', '.join(blue) or 'none'}")
            print(f"Unassigned: {len(unassigned)}")
    return red, blue


roster = ["Ari", "Bea", "Cleo", "Dara", "Eli", "Fay", "Gus", "Hana", "Ira", "Jai"]
red, blue = assign_teams(roster, trace=True)
print(f"Team Red ({len(red)}): {', '.join(red) or 'none'}")
print(f"Team Blue ({len(blue)}): {', '.join(blue) or 'none'}")
