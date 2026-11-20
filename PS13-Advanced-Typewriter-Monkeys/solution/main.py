import random
from string import ascii_lowercase

PRACTICE_LETTERS = "xcatmint"
RANDOM_LIMIT = 20_000


def load_words_by_length():
    by_length = {}
    with open("valid_words.txt", encoding="utf-8") as file:
        for line in file:
            word = line.strip().lower()
            if word and all(letter in ascii_lowercase for letter in word):
                by_length.setdefault(str(len(word)), set()).add(word)
    return by_length


def find_word(letters, words, length):
    window = ""
    count = 0
    for count, letter in enumerate(letters, start=1):
        window = (window + letter)[-length:]
        if len(window) == length and window in words:
            return window, count
    return None, count


def main():
    by_length = load_words_by_length()
    lengths = ", ".join(sorted(by_length, key=int))
    try:
        choice = input(f"Word length ({lengths}): ").strip()
        if choice not in by_length:
            print("Choose a length from the word list.")
            return
        mode = input("p for practice or Enter for random: ").strip().lower()
    except EOFError:
        print("Search cancelled.")
        return
    if mode == "p":
        letters = PRACTICE_LETTERS
    else:
        letters = (random.choice(ascii_lowercase) for _ in range(RANDOM_LIMIT))
    word, count = find_word(letters, by_length[choice], int(choice))
    if word is None:
        print(f"No match after {count} letters.")
    else:
        print(f"Found {word} after {count} letters.")


if __name__ == "__main__":
    main()
