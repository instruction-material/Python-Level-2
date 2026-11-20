players = {
    "Suarez": "Uruguay",
    "Messi": "Argentina",
    "Coutinho": "Brazil",
    "Vidal": "Chile",
    "Rakitic": "Croatia",
    "Busquets": "Spain",
    "Roberto": "Spain",
    "Pique": "Spain",
    "Lenglet": "France",
    "Alba": "Spain",
    "Ter Stegen": "Germany",
}

countries = set()
for player in players:
    countries.add(players[player])

print(f"Sample players: {len(players)}")
print(f"Distinct countries: {len(countries)}")
for country in sorted(countries):
    print(country)
