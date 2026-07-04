###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

sum = 0
num_students = 5

min_score = 100
max_score = 0
sum = 0

for i in range(num_students):
    score = int(input("Enter student " + str(i + 1) + "'s score: "))

    sum += score

    if score < min_score:
        min_score = score
    if score > max_score:
        max_score = score

average = sum / num_students
print("The highest score was: " + str(max_score))
print("The lowest score was: " + str(min_score))
print("The class average was: " + str(average))
