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

players_set = set()
for player in players:
    players_set.add(players[player])

print(
    "FC Barcelona has players from " + str(len(players_set)) + " different countries."
)

print("FC Barcelona's players come from:")
for nation in players_set:
    print(nation)
