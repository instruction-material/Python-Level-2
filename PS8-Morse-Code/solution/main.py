import sys

if sys.platform == "emscripten":
    from pysynth import make_wav
else:
    from native_pysynth import make_wav


MORSE = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}

def encode(text):
    words = text.lower().split()
    if not words or any(letter not in MORSE for word in words for letter in word):
        raise ValueError("Use letters A to Z and spaces.")
    return " / ".join(" ".join(MORSE[letter] for letter in word) for word in words)


def decode(code):
    reverse = {symbols: letter for letter, symbols in MORSE.items()}
    words = [word.split() for word in code.split("/")]
    if any(not word or any(token not in reverse for token in word) for word in words):
        raise ValueError("Use known dot-and-dash groups separated by spaces and slashes.")
    return " ".join("".join(reverse[token] for token in word) for word in words).upper()


def rhythm(code):
    notes = []
    for word_index, word in enumerate(code.split("/")):
        if word_index:
            notes.append(("r", 7))
        for letter_index, letter in enumerate(word.split()):
            if letter_index:
                notes.append(("r", 3))
            for symbol_index, symbol in enumerate(letter):
                if symbol_index:
                    notes.append(("r", 1))
                notes.append(("c4", 1 if symbol == "." else 3))
    return notes


def main():
    try:
        choice = input("e to encode or d to decode: ").strip().lower()
        if choice == "e":
            code = encode(input("Text: "))
            text = decode(code)
        elif choice == "d":
            text = decode(input("Morse: "))
            code = encode(text)
        else:
            print("Choose e or d.")
            return
    except EOFError:
        print("Translation ended.")
        return
    except ValueError as error:
        print(error)
        return

    print(f"Text: {text}")
    print(f"Morse: {code}")
    notes = rhythm(code)
    units = sum(duration for _, duration in notes)
    print(f"Audio units: {units}")
    if units <= 100:
        make_wav([(pitch, 8 / units) for pitch, units in notes],
                 fn="morse.wav", bpm=300, pause=0, silent=True)
        print("Wrote morse.wav.")
    else:
        print("Use a shorter message to render audio.")


if __name__ == "__main__":
    main()
