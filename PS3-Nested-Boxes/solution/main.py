maximum = int(input("Largest box size, at least 3: "))

for size in range(3, maximum + 1):
    for row in range(size):
        for column in range(size):
            if row in (0, size - 1) or column in (0, size - 1):
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()
