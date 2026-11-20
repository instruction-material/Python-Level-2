rides_dict = {
    'Tower of Turtles': 90,
    'String Mountain': 130,
    'Debug Track': 5,
    'Concatenation Carousel': 100,
    'Cinderella Casting': 90,
    'Magic For Loop': 10,
    'Pythons of the Caribbean': 30,
}

minutes_remaining = 360
visited_rides = []
shortest_ride = min(rides_dict.values())

print(f"Starting time: {minutes_remaining} minutes.")
while minutes_remaining >= shortest_ride:
    for ride, duration in rides_dict.items():
        print(f"{ride}: {duration} minutes")
    try:
        choice = input("Choose a ride or q to finish: ").strip()
    except EOFError:
        break
    if choice.lower() == "q":
        break
    if choice not in rides_dict:
        print("Choose a ride from the menu.")
        continue

    duration = rides_dict[choice]
    if duration > minutes_remaining:
        print(f"{choice} takes {duration} minutes. Remaining: {minutes_remaining} minutes.")
        continue

    minutes_remaining -= duration
    visited_rides.append(choice)
    print(f"Added {choice}. Remaining: {minutes_remaining} minutes.")

print("Plan:")
for ride in visited_rides:
    print(ride)
if not visited_rides:
    print("No rides selected.")
print(f"Unused time: {minutes_remaining} minutes.")
