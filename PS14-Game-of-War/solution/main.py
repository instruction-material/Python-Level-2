import random

PRACTICE_DRAWS = [(9, 4), (2, 8), (5, 5), (6, 2), (7, 10),
                  (8, 8), (10, 3), (4, 9), (2, 2), (7, 6)]


def play_rounds(first, second, cards):
    wins = [0, 0]
    ties = 0
    for round_number, (left, right) in enumerate(cards, start=1):
        print(f"Round {round_number}: {left} versus {right}")
        if left > right:
            wins[0] += 1
            print(f"{first} wins this round.")
        elif right > left:
            wins[1] += 1
            print(f"{second} wins this round.")
        else:
            ties += 1
            print("Round tied.")
    print(f"Final scores: {first} {wins[0]}, {second} {wins[1]}, ties {ties}.")
    if wins[0] == wins[1]:
        print("Overall tie.")
    elif wins[0] > wins[1]:
        print(f"{first} wins overall.")
    else:
        print(f"{second} wins overall.")
    return wins, ties


def main():
    first = input("Player 1 name: ").strip() or "Player 1"
    second = input("Player 2 name: ").strip() or "Player 2"
    mode = input("p for practice, or Enter for random: ").strip().lower()
    if mode == "p":
        draws = PRACTICE_DRAWS
    else:
        draws = ((random.randint(2, 10), random.randint(2, 10))
                 for _ in range(10))
    play_rounds(first, second, draws)


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("Session ended.")
