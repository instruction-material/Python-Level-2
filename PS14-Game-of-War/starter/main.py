left = 9
right = 4
print(f"Round 1: {left} versus {right}")
if left > right:
    print("Player 1 wins this round.")
elif right > left:
    print("Player 2 wins this round.")
else:
    print("Round tied.")

# Play ten rounds and count the wins for each player and all ties.
