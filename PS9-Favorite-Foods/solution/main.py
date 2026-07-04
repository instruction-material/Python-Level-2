###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

student_foods = set()
instructor_foods = set()

print("Student, enter five of your favorite foods.")
for i in range(5):
    student_foods.add(input("Food " + str(i + 1) + ": "))

print("Instructor, enter five of your favorite foods.")
for i in range(5):
    instructor_foods.add(input("Food " + str(i + 1) + ": "))

shared = student_foods.intersection(instructor_foods)

if len(shared) == 0:
    print("You like completely different foods!")
else:
    print("You both share these top foods: " + str(shared))

# Challenge
print("Here are the foods that only the student likes:")
for food in student_foods:
    if food not in instructor_foods:
        print(food)

print("Here are the foods that only the instructor likes:")
for food in instructor_foods:
    if not food in student_foods:
        print(food)
