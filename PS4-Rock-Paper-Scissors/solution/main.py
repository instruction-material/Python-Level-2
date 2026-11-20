move1 = input("Player 1 move: ").strip().lower()
move2 = input("Player 2 move: ").strip().lower()

if move1 not in ("rock", "paper", "scissors") or move2 not in ("rock", "paper", "scissors"):
    print("Each move must be rock, paper, or scissors.")
elif move1 == move2:
    print("Tie!")
elif (
    (move1 == "rock" and move2 == "scissors")
    or (move1 == "scissors" and move2 == "paper")
    or (move1 == "paper" and move2 == "rock")
):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
