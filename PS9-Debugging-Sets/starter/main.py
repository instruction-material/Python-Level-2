# Repair each set operation in order. The first run stops during setup.

# Start the game with all of the players free (i.e. no one has been captured yet)
team1free = set()
team1free.append("Jared", "Rachel", "Khalif", "Claudia")
team2free = set()
team2.append("Zeinab", "Michael", "Matthew", "Valerie")

team1captured = set()
team2captured = set()


# Keep playing until either someone steals the flag or an entire team gets captured
while True:
  capturedFlag = input("Did someone capture the flag? (Y/N): ")
  if capturedFlag.lower() == "y":
    print("Game over, someone captured the flag!")
    break
  else:
    captured = input("Did someone get captured? (Y/N): ")
    if captured.lower() == "y":
      name = input("Who got captured? ")
      # Check which team the player was on
      if name in team1free:
        # Move captured player from free to captured set
        team1free[name] = 0
        team1captured.append(name)
      elif name in team2free:
        # Move captured player from free to captured set
        team2free[name] = 0
        team2captured.append(name)
      else:
        print("I don't see that player out on the field!")

    # Print everyone who is free on each team
    print("Here are the players who are still on the field for team 1:")
    for i in range(len(team1free)):
      print(team1free[i])
    print("Here are the players who are still on the field for team 2:")
    for i in range(len(team2free)):
      print(team2free[i])

    # Print everyone who is in jail
    print("Here are the players who are in jail:")
    totalCaptured = team1captured.team2captured.union()
    for name in totalCaptured:
      print(name)

    # Check if an entire team has been captured
    if team1free == 0:
      print("All of team 1 is in jail, so team 2 wins!")
      break
    elif team2free == 0:
      print("All of team 2 is in jail, so team 1 wins!")
      break
