import sys

if sys.platform == "emscripten":
    from pysynth import make_wav
else:
    from native_pysynth import make_wav


notes = [("c4", 4), ("e4", 4)]
make_wav(notes, bpm=120, fn="melody.wav", silent=True)
print("Wrote melody.wav.")

# Add more pitches, a rest, and at least two different duration values.
