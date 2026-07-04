num_students = int(input("Enter the number of students: "))
num_tests = int(input("Enter the number of tests each student took: "))

test_scores = {}

# ask the user to enter each student's name
for i in range(num_students):
    name = input("Enter student " + str(1 + i) + "'s name: ")
    test_scores[name] = []

# ask the user to enter each test score
for i in range(num_tests):
    for name in test_scores:
        score = int(input("Enter " + name + "'s score on test " + str(i + 1) + ": "))
        test_scores[name].append(score)

print(test_scores)

# calculate each student's average exam score
averages = {}
for name in test_scores:
    sum = 0
    for score in test_scores[name]:
        sum += score
    averages[name] = sum / len(test_scores[name])

print(averages)
