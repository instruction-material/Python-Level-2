import sys

if sys.platform == "emscripten":
    from pysynth import make_wav
else:
    from native_pysynth import make_wav


PITCHES = {"c4", "d4", "e4", "f4", "g4", "a4", "b4", "c5", "r"}
DURATIONS = {"1", "2", "4", "8"}
MAX_NOTES = 6


def read_song():
    song = []
    while len(song) < MAX_NOTES:
        try:
            pitch = input("Pitch c4 through b4, c5, r, or q: ").strip().lower()
            if pitch in {"q", "1"}:
                break
            if pitch not in PITCHES:
                print("Choose one of the listed pitches or r for a rest.")
                continue

            duration = input("Duration 1, 2, 4 or 8: ").strip()
            while duration not in DURATIONS:
                print("Choose 1, 2, 4 or 8.")
                duration = input("Duration 1, 2, 4 or 8: ").strip()
        except EOFError:
            break
        song.append((pitch, int(duration)))
        print(f"Added {pitch} with duration {duration}.")
    return song


song = read_song()
if song:
    print(f"Song: {song}")
    make_wav(song, bpm=120, fn="song.wav", silent=True)
    print("Wrote song.wav.")
else:
    print("No notes entered.")
