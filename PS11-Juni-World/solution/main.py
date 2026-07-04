rides_dict = {
  'Tower of Turtles': 90,
  'String Mountain': 130,
  'Debug Track': 5,
  'Concatenation Carousel': 100,
  'Cinderella Casting': 90,
  'Magic For Loop': 10,
  'Pythons of the Carribean': 30
}

minutes_remaining = 360
visited_rides = []

# prints time rmeaining in hours and minutes
def print_as_hours(time):
  num_hours = int(time / 60)
  num_mins = time % 60
  print("Remaining hours: " + str(num_hours))
  print("Remaining minutes: " + str(num_mins))

print("Welcome to Juni World! We have a large selection of rides for you to ride! We'll even help you keep track of how much time you have left in the park after each ride!\n")

while minutes_remaining > 15:
  print("Here's how much time you have left in Juni World:")
  print_as_hours(minutes_remaining)

  print("\nHere are the rides and their wait times: ")
  for ride in rides_dict:
    print(ride + ": " + str(rides_dict[ride]) + " minutes")

  desired_ride = input("\nEnter the ride you wish to go on next: ")
  while desired_ride not in rides_dict:
    desired_ride = input("\nSorry, that ride isn't part of the list. Please enter the ride you wish to go on next: ")

  wait_time = rides_dict[desired_ride]
  print("\nThat was awesome! You rode the " + desired_ride + "\n")

  # update minutesRemaining and visitedRides
  minutes_remaining -= rides_dict[desired_ride]
  visited_rides.append(desired_ride)

print("\nWow! That was a great day. Here's a list of all the rides you visited today, in order: ")
for ride in visited_rides:
  print(ride)
print("\nThanks for visiting Juni World! Come back again soon!")