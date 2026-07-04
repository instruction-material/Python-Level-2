import random

def print_welcome():
  print("I am thinking of a random number between 1 and 100. Guess what it is!")


# Get my secret number between 1 and 100!
def get_random_number():
  return random.randint(0,100)


# Ask the user to guess my secret number
def get_guess_from_user():
  return int(input("Enter a new guess: "))


# If the guess is correct, then return True. Otherwise, print out if the guess was too high or too low, and return False
def answer_is_right(answer, guess):
  if answer == guess:
    print("You got it!")
    return True
  elif guess < answer:
    print("You guessed too low!")
    return False
  else:
    print("You guessed too high!")
    return False


def print_score(num_guesses):
  print('It took you ' + str(num_guesses) + ' guesses to guess my number.')
  if num_guesses == 1:
    print("Lucky you, you guessed my secret number on the first try!")
  elif num_guesses < 5:
    print("Pretty solid guessing, it took you less than 5 tries to guess my number!")
  elif num_guesses < 15:
    print("Pretty average guessing!")
  else:
    print("Wow, it took you forever to guess my number!")


def play_game():
  print_welcome()
  answer = get_random_number()

  # Ask the user to guess the secrete number, then check if they got it right. If they didn't get it right, let them keep guessing until they guess correctly!
  guess = get_guess_from_user()
  num_guesses = 1 # Count how many guesses it took for the user to guess the number
  while not answer_is_right(answer, guess):
    guess = get_guess_from_user()
    num_guesses = num_guesses + 1

  print_score(num_guesses)


play_game()

# Bonus: Allow the user type in Y or N at the end of each game to decide whether or not to play again.

'''
keepPlaying = True
while keepPlaying:
  playGame()
  userAnswer = input("Would you like to play again? (Y/N): ')
  if userAnswer == 'N':
    keepPlaying = False
'''