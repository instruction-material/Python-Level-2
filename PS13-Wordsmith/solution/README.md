# Wordsmith

Build a timed word game using seven distinct letters and the supplied word list.

## Run

Keep main.py and valid_words.txt together. Run python3 main.py from this folder,
or run main.py in the site IDE. Python's standard library is sufficient.
The starter supplies dictionary loading; the reference includes the complete game.

Press Enter to start a 60-second round. Enter a word per prompt or :quit to finish.
Only the seven displayed letters may appear. A letter may be reused within a word.
Each accepted word scores its length once; repeated words do not score again.
Whitespace and uppercase input are normalized before checking.

The console uses blocking input. The deadline is checked before and after every
submission; an answer received at or after the deadline does not score.
If input is left open, the program reports expiration when that input returns.
EOF or interruption ends the round cleanly.

## Build and check

Load valid_words.txt into a set of stripped lowercase words. Choose seven unique
letters, store accepted guesses in a second set, and use len(word) for scoring.
For elapsed time, record deadline = time.monotonic() + 60. Compare the current
clock with that deadline before prompting and after receiving each answer.

For letters a,c,e,i,n,r,t: cat scores 3;another cat scores 0;crate scores 5.
A word containing b is rejected. :quit prints final score 8 for that trace.
Repeated letters within a word are allowed when every letter belongs to the set.
CASES.md gives fixed scoring, timing and input-boundary cases.

## Classroom extension

The reference is the working classroom framework. Change word_score(word) for a
Normal scoring rule and demonstrate its effect on an accepted word.
Hard extensions can add replay, guaranteed vowels, word-length difficulty or
high scores while retaining duplicate rejection and the deadline.
