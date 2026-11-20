import random
import time

PRACTICE_SENTENCE = "Rain taps on the glass."
SENTENCES = [
    PRACTICE_SENTENCE,
    "A yellow kite crossed the field.",
    "Six green beads rolled off the table.",
]


def run_round(target, read=input, write=print, clock=time.monotonic):
    write(f"Target: {target}")
    start = clock()
    attempts = 0
    while True:
        try:
            response = read("Type the sentence (or :quit): ")
        except EOFError:
            response = ":quit"
        if response == ":quit":
            write("Round ended.")
            return
        attempts += 1
        if response == target:
            elapsed = clock() - start
            write(f"Exact match in {attempts} attempt(s).")
            write(f"Elapsed: {elapsed:.2f} seconds.")
            return elapsed, attempts
        write("The text differs from the target. Try again.")


def main():
    try:
        mode = input("Enter for a random target, or p for practice: ").strip().lower()
    except EOFError:
        print("Round ended.")
        return
    if mode == "p":
        run_round(PRACTICE_SENTENCE)
        return
    for label in ("Ready", "Set"):
        print(label)
        time.sleep(1)
    print("Type!")
    run_round(random.choice(SENTENCES))


if __name__ == "__main__":
    main()
