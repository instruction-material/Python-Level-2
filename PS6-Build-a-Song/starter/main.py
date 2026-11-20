import pysynth


notes = [("c4", 4), ("e4", 4)]
pysynth.make_wav(notes, bpm=120, fn="melody.wav", silent=True)
print("Wrote melody.wav.")

# Build a longer original phrase with different durations and a rest.
