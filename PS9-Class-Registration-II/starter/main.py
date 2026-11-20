design = ["Ari", "Ari", "Bea", "Cleo", "Dara", "Eli", "Fay", "Gus", "Gus", "Hana"]
seen = set()
for name in design:
    if name not in seen:
        seen.add(name)
        print(name)

# Keep separate ordered lists for enrollment and the waiting list.
