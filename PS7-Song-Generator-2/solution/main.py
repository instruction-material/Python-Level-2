import sys

if sys.platform == "emscripten":
    from pysynth import make_wav
else:
    from native_pysynth import make_wav


DURATIONS = {"whole": 1, "half": 2, "quarter": 4, "eighth": 8}
PITCHES = {"c4", "d4", "e4", "f4", "g4", "a4", "b4", "c5", "r"}


def collect_song():
    song = []
    while len(song) < 6:
        try:
            pitch = input("Pitch c4 through b4, c5, r, or q: ").strip().lower()
            if pitch in {"q", "1"}:
                break
            if pitch not in PITCHES:
                print("Choose one of the listed pitches.")
                continue
            name = input("Whole, half, quarter or eighth: ").strip().lower()
            duration = DURATIONS.get(name)
            while duration is None:
                print("Choose a duration name from the list.")
                name = input("Whole, half, quarter or eighth: ").strip().lower()
                duration = DURATIONS.get(name)
        except EOFError:
            break
        song.append((pitch, duration))
        print(f"Added {pitch} with {name} = {duration}.")
    return song


song = collect_song()
if song:
    print(f"Song: {song}")
    make_wav(song, fn="named_song.wav", bpm=120, silent=True)
    print("Wrote named_song.wav.")
else:
    print("No notes entered.")
