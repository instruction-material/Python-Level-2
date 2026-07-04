import random

def clear():
  print("\033c", end="")

def get_guess():
  while True:
    guess = input("Enter a guess: ").lower().strip()
    if guess in previous_guesses:
      print("You already guessed that! Try again!")
    elif not guess.isalpha():
      print("That's not a letter! Try again!")
    elif len(guess) != 1:
      print("You typed too much, or nothing at all! Try again!")
    else:
      return guess

def get_groups(letter, words):
  word_groups = {}
  for word in words:
    pattern = get_pattern(letter, word)
    if pattern in word_groups:
      word_groups[pattern].add(word)
    else:
      word_groups[pattern] = set({word})
  return word_groups

def get_pattern(letter, word):
  pattern = ""
  for c in word:
    if c == letter or c in correct_guesses:
      pattern += c
    else:
      pattern += "_"
    pattern += " "
  return pattern

def get_max_pattern(word_groups):
  max_group_size = 0
  max_patterns = []
  for pattern in word_groups:
    if len(word_groups[pattern]) > max_group_size:
      max_group_size = len(word_groups[pattern])
      max_patterns = []
      max_patterns.append(pattern)
    elif len(word_groups[pattern]) == max_group_size:
      max_patterns.append(pattern)
  return random.choice(max_patterns)

def get_words_of_length(length, words):
  temp = set()
  for word in words:
    if len(word) == length:
      temp.add(word)
  return temp
#-----------------------------------------------------

with open("dictionary.txt") as f:
  words = set(f.read().strip().split("\n"))

length = random.randint(3, 8)
status = "_ " * length

words = get_words_of_length(length, words)

correct_guesses = set()
previous_guesses = []
num_guesses = 15

while True:
  clear()
  print(status+"\n")
  print(str(num_guesses) + " guesses left!")
  print("Previous Guesses: " + " ".join(previous_guesses))

  guess = get_guess()
  previous_guesses.append(guess)

  # choose the worst case scenario (that's still possible)
  word_groups = get_groups(guess, words)
  new_status = get_max_pattern(word_groups)

  # update words and status
  words = word_groups[new_status]
  if new_status == status: # "incorrect guess"
    # the worst case (that's still possible) is to not reveal any letters!
    num_guesses -= 1
  else: # "correct guess"
    # the worst case (that's still possible) is to reveal letters...
    correct_guesses.add(guess)
    status = new_status

  if "_" not in status:
    print("\nYOU WIN!\nThe word was: "+list(words)[0])
    break
  elif num_guesses == 0:
    print("\nYOU LOSE!\nThe word was: "+random.choice(list(words)))
    break