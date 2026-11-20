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

print(f"Starting time: {minutes_remaining} minutes.")
for ride, duration in rides_dict.items():
    print(f"{ride}: {duration} minutes")
