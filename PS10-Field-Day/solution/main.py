choices_by_name = {}
while len(choices_by_name) < 10:
    name = input("Fictional name: ").strip().lower()
    if not name or name in choices_by_name:
        print("Enter a new, nonempty name.")
        continue

    choice = input("1 kickball, 2 flag, 3 both, 4 neither: ").strip()
    while choice not in ("1", "2", "3", "4"):
        choice = input("Choose 1, 2, 3, or 4: ").strip()
    choices_by_name[name] = choice

kickball = []
flag = []
neither = []
for name, choice in choices_by_name.items():
    if choice in ("1", "3"):
        kickball.append(name)
    if choice in ("2", "3"):
        flag.append(name)
    if choice == "4":
        neither.append(name)

print(f"Kickball: {', '.join(kickball) or 'none'}")
print(f"Capture the flag: {', '.join(flag) or 'none'}")
print(f"Neither: {', '.join(neither) or 'none'}")
