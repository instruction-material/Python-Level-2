money = input("Tell me how much money you have (in cents), and I'll tell you how many quarters you can have. ")

money = int(money)
num_qtrs = 0
while (money - 25 >= 0):
  money -= 25
  num_qtrs += 1

print("You can have " + str(num_qtrs) + " quarters.\n\n")

money = input("Tell me how much money you have (in cents), and I'll tell you how many quarters and how many dimes you can have. ")

money = int(money)
num_qtrs = 0
num_dimes = 0
while (money - 25 >= 0):
  money -= 25
  num_qtrs += 1
while(money - 10 >= 0):
  money -= 10
  num_dimes += 1

print("You can have " + str(num_qtrs) + " quarters and " + str(num_dimes) + " dimes.\n\n")

money = input("Tell me how much money you have (in cents), and I'll tell you the amount of change you can have. ")

money = int(money)
num_qtrs = 0
num_dimes = 0
num_nickels = 0
num_pennies = 0
while (money - 25 >= 0):
  money -= 25
  num_qtrs += 1
while(money - 10 >= 0):
  money -= 10
  num_dimes += 1
while(money - 5 >= 0):
  money -= 5
  num_nickels += 1
while(money - 1 >= 0):
  money -= 1
  num_pennies += 1

print("You can have " + str(num_qtrs) + " quarters, " + str(num_dimes) + " dimes, " + str(num_nickels) + " nickels, and " + str(num_pennies) + " pennies.")