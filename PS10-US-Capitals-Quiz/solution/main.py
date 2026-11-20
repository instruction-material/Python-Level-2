import random


def read_names(filename):
    with open(filename, encoding="utf-8") as source:
        return [line.strip() for line in source]


states = read_names("states.txt")
capitals = read_names("capitals.txt")

if (
    not states or len(states) != len(capitals)
    or not all(states) or not all(capitals)
    or len(set(states)) != len(states)
):
    raise ValueError("The files must contain one capital per distinct state.")

answers = dict(zip(states, capitals))
score = 0

while True:
    state = random.choice(states)
    try:
        guess = input(f"What is the capital of {state}? ")
    except EOFError:
        break
    if guess.strip().casefold() != answers[state].casefold():
        print(f"Incorrect. The capital of {state} is {answers[state]}.")
        break

    print("Correct!")
    score += 1

print(f"Final score: {score}")
