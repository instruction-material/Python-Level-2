import time
import random

sentences = ["Peter Piper picked a peck of pickled peppers", "She sells seashells by the sea shore", "How much wood could a woodchuck chuck if a woodchuck could chuck wood?", "If a dog chews shoes, whose shoes does he choose?", "If you notice this notice, you will notice that this notice is not worth noticing", "I saw Susie sitting in a shoe shine shop"]

input("Welcome to Type Racer. Press Enter to play.")
print("Ready....")
time.sleep(1)
print("Set....")
time.sleep(1)
print("Type!")

sentence = sentences[random.randint(0, 5)]
print(sentence)
start_time = time.time()
typed_input = input("Type: ")
while typed_input != sentence:
  print("The sentences do not match! Please try again.")
  typed_input = input("Type: ")
end_time = time.time()

print("You finished typing in " + str(end_time - start_time) + " seconds!")