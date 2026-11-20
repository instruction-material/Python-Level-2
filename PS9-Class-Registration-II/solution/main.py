def register(signups, capacity):
    seen = set()
    enrolled = []
    waiting = []
    for name in signups:
        if name in seen:
            continue
        seen.add(name)
        if len(enrolled) < capacity:
            enrolled.append(name)
        else:
            waiting.append(name)
    return enrolled, waiting


rosters = {
    "Design": ["Ari", "Ari", "Bea", "Cleo", "Dara", "Eli", "Fay", "Gus", "Gus", "Hana"],
    "Computing": ["Ira", "Jai", "Kit", "Lee", "Mo", "Nia", "Nia"],
    "Studio": ["Paz", "Quin", "Rey", "Paz"],
}
for course, signups in rosters.items():
    enrolled, waiting = register(signups, 6)
    print(f"{course} enrolled: {', '.join(enrolled) or 'none'}")
    print(f"{course} waiting: {', '.join(waiting) or 'none'}")
