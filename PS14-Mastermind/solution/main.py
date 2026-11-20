import random

DIGITS = "012345"
ATTEMPTS = 8


def score(signal, trial):
    exact = 0
    available_digits = {}
    unmatched_trials = []
    for signal_digit, trial_digit in zip(signal, trial):
        if trial_digit == signal_digit:
            exact += 1
        else:
            available_digits[signal_digit] = available_digits.get(signal_digit, 0) + 1
            unmatched_trials.append(trial_digit)

    misplaced = 0
    for digit in unmatched_trials:
        if available_digits.get(digit, 0) > 0:
            available_digits[digit] -= 1
            misplaced += 1
    return exact, misplaced


def run_trial(signal):
    remaining = ATTEMPTS
    hinted = False
    while remaining > 0:
        trial = input(f"{remaining} trials left. Four digits, hint, or q: ").strip().lower()
        if trial == "q":
            print("Trial ended.")
            return
        if trial == "hint":
            if hinted:
                print("The hint was already used.")
            else:
                print(f"Digit sum: {sum(int(digit) for digit in signal)}")
                hinted = True
                remaining -= 1
            continue
        if len(trial) != len(signal) or any(digit not in DIGITS for digit in trial):
            print("Use four digits from 0 through 5.")
            continue
        remaining -= 1
        exact, misplaced = score(signal, trial)
        print(f"Exact: {exact}. Misplaced: {misplaced}.")
        if exact == len(signal):
            print("Signal matched.")
            return
    print(f"No trials left. The signal was {signal}.")


def main():
    mode = input("p for practice, or Enter for a random signal: ").strip().lower()
    signal = "2032" if mode == "p" else "".join(random.choices(DIGITS, k=4))
    run_trial(signal)


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("Session ended.")
