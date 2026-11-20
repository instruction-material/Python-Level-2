runner1 = float(input("Runner 1 time in seconds: "))
runner2 = float(input("Runner 2 time in seconds: "))
runner3 = float(input("Runner 3 time in seconds: "))
runner4 = float(input("Runner 4 time in seconds: "))

average = (runner1 + runner2 + runner3 + runner4) / 4
print(f"Average: {average} seconds")

if runner1 < average:
    print("Runner 1 was faster.")
elif runner1 == average:
    print("Runner 1 ran the average pace.")
else:
    print("Runner 1 was slower.")

# Add the corresponding comparison for the other three runners.
