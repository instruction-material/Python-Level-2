print("Welcome to your todo list!\n")
tasks = []

while True:
  input_num = input("What would you like to do with your todo list? \n 1. Add a task \n 2. Remove a task \n 3. Exit \nType in the number here: ")

  print("")
  if input_num == "1":
    task = input("Please type in the task you'd like to add: ")
    tasks.append(task)
  elif input_num == "2":
    remove_num = input("Please type in the number of the task you'd like to remove: ")
    tasks.remove(tasks[int(remove_num)-1])
  elif input_num == "3":
    break

  # print todo list
  print("")
  print("Here's your updated list: ")
  for i in range(0,len(tasks)):
    print(str(i+1) + ". " + tasks[i])
  print("")