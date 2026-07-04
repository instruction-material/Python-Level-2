import random

def dice_roll():
  return random.randint(1,6)

num_rolls = 1000
num_twos = 0
num_threes = 0
num_fours = 0
num_fives = 0
num_sixes = 0
num_sevens = 0
num_eights = 0
num_nines = 0
num_tens = 0
num_elevens = 0
num_twelves = 0

for i in range(0,num_rolls):
  roll_num = dice_roll() + dice_roll()
  if roll_num == 2:
    num_twos += 1
  elif roll_num == 3:
    num_threes += 1
  elif roll_num == 4:
    num_fours += 1
  elif roll_num == 5:
    num_fives += 1
  elif roll_num == 6:
    num_sixes += 1
  elif roll_num == 7:
    num_sevens += 1
  elif roll_num == 8:
    num_eights += 1
  elif roll_num == 9:
    num_nines += 1
  elif roll_num == 10:
    num_tens += 1
  elif roll_num == 11:
    num_elevens += 1
  elif roll_num == 12:
    num_twelves += 1

print(str((num_twos/num_rolls) * 100) + "% of your rolls were 2.")
print(str((num_threes/num_rolls) * 100) + "% of your rolls were 3.")
print(str((num_fours/num_rolls) * 100) + "% of your rolls were 4.")
print(str((num_fives/num_rolls) * 100) + "% of your rolls were 5.")
print(str((num_sixes/num_rolls) * 100) + "% of your rolls were 6.")
print(str((num_sevens/num_rolls) * 100) + "% of your rolls were 7.")
print(str((num_eights/num_rolls) * 100) + "% of your rolls were 8.")
print(str((num_nines/num_rolls) * 100) + "% of your rolls were 9.")
print(str((num_tens/num_rolls) * 100) + "% of your rolls were 10.")
print(str((num_elevens/num_rolls) * 100) + "% of your rolls were 11.")
print(str((num_twelves/num_rolls) * 100) + "% of your rolls were 12.")