"""A timed seven-letter word game using the adjacent original dictionary."""
import math
import random
import time

ROUND_SECONDS = 60


def load_words(path="valid_words.txt"):
    with open(path, encoding="utf-8") as word_file:
        return {line.strip().lower() for line in word_file if line.strip()}


def choose_letters(rng=random):
    alphabet = [chr(number) for number in range(ord("a"), ord("z") + 1)]
    return set(rng.sample(alphabet, 7))


def word_score(word):
    """Normal extension: change the score for one accepted word."""
    return len(word)


def check_guess(word, letters, valid_words, found):
    if not word or not set(word).issubset(letters):
        return "unavailable letters"
    if word in found:
        return "already entered"
    if word not in valid_words:
        return "not in the word list"
    return "valid"


def play_round(valid_words, letters, duration=ROUND_SECONDS, read=input,
               write=print, clock=time.monotonic):
    """Check a monotonic deadline before and after each blocking input."""
    if not math.isfinite(duration) or duration <= 0:
        raise ValueError("Round duration must be a positive finite number.")
    score = 0
    found = set()
    deadline = clock() + duration
    reason = "time"
    write("Letters: " + " ".join(sorted(letters)))
    write("Round: " + str(duration) + " seconds. Enter :quit to stop.")
    while clock() < deadline:
        try:
            word = read("Enter a word: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            reason = "input ended"
            break
        if clock() >= deadline:
            break
        if word == ":quit":
            reason = "quit"
            break
        status = check_guess(word, letters, valid_words, found)
        if status == "valid":
            found.add(word)
            score += word_score(word)
            write("Valid word! Your score: " + str(score))
        else:
            write("Rejected: " + status + ". Your score: " + str(score))
    if reason == "time":
        write("Time is up.")
    write("Final score: " + str(score))
    write("Accepted words: " + ", ".join(sorted(found)))
    return {"score": score, "words": sorted(found), "reason": reason}


def main():
    valid_words = load_words()
    letters = choose_letters()
    print("Wordsmith: make words using seven distinct letters.")
    print("Letters may repeat within a word. Repeated words score once.")
    try:
        input("Press Enter to begin: ")
    except (EOFError, KeyboardInterrupt):
        print("Round cancelled.")
        return {"score": 0, "words": [], "reason": "input ended"}
    return play_round(valid_words, letters)


if __name__ == "__main__":
    main()
