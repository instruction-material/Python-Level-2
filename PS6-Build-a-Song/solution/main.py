import pysynth


notes = [("c4", 4), ("e4", 8), ("f4", 8), ("r", 4), ("d4", 4), ("a4", 2)]
pysynth.make_wav(notes, bpm=120, fn="melody.wav", silent=True)
print("Wrote melody.wav.")
