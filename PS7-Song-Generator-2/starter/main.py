import sys

if sys.platform == "emscripten":
    from pysynth import make_wav
else:
    from native_pysynth import make_wav


DURATIONS = {"whole": 1, "half": 2, "quarter": 4, "eighth": 8}

pair = ("c4", DURATIONS["quarter"])
print(f"Quarter note pair: {pair}")
make_wav([pair], fn="named_song.wav", bpm=120, silent=True)

# Look up each duration name before appending its pitch and value.
