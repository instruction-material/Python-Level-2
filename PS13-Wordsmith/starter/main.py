"""Wordsmith starter: the original dictionary setup is supplied."""
import random
import time

with open("valid_words.txt", encoding="utf-8") as word_file:
    valid_words = {line.strip().lower() for line in word_file if line.strip()}

# Build a set of seven distinct random lowercase letters.
# Accept guesses, rejecting words outside that alphabet or valid_words.
# Track accepted words in a set so each word scores len(word) only once.
# Use a 60-second time.monotonic() deadline; check before and after input().
# Ignore a submission that returns at or after the deadline.
# Finish on :quit, end-of-input or the deadline, then print the final score.
