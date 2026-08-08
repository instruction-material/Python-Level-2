import random

players = [
    "Alex",
    "Barbara",
    "Cole",
    "Devyn",
    "Eric",
    "Fanny",
    "George",
    "Harsha",
    "Ignacio",
    "Julia",
]

team_red = []
team_blue = []

while len(players) > 0:
    # choose player for Team Red
    rand_ind = random.randint(0, len(players) - 1)
    red_player = players[rand_ind]
    team_red.append(red_player)
    players.remove(red_player)
    print("Team Red: " + str(team_red))

    # choose player for Team Blue
    rand_ind = random.randint(0, len(players) - 1)
    blue_player = players[rand_ind]
    team_blue.append(blue_player)
    players.remove(blue_player)
    print("Team Blue: " + str(team_blue))

    print("Players left: " + str(players) + "\n")
