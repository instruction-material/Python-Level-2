remaining_days = int(input("Elapsed days: "))
years = 0

while remaining_days >= 365:
    remaining_days -= 365
    years += 1

print("Years:", years)
print("Days remaining:", remaining_days)

# Count 30-day months and 7-day weeks using the same remainder.
