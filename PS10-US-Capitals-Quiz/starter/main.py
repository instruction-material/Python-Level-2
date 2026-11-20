def read_names(filename):
    with open(filename, encoding="utf-8") as source:
        return [line.strip() for line in source]


states = read_names("states.txt")
capitals = read_names("capitals.txt")

print(f"Loaded {len(states)} states and {len(capitals)} capitals.")
