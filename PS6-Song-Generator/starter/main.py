import sys

if sys.platform == "emscripten":
    from pysynth import make_wav
else:
    from native_pysynth import make_wav


song = [("c4", 4)]
print(f"Song: {song}")
make_wav(song, bpm=120, fn="song.wav", silent=True)
print("Wrote song.wav.")

# Read each pitch and duration before appending it. Stop at six pairs or q.
