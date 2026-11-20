tasks = []

while True:
    command = input("1 add, 2 remove, 3 exit, 4 show: ").strip()
    if command == "3":
        break
    if command == "1":
        task = input("Task: ").strip()
        if task:
            tasks.append(task)
        else:
            print("Enter a task.")
    elif command == "2":
        # Read and validate the displayed position before removing the task.
        print("Add the remove behavior here.")
    elif command != "4":
        print("Choose a command from 1 through 4.")

    if tasks:
        for position, task in enumerate(tasks, start=1):
            print(f"{position}. {task}")
    else:
        print("No tasks.")
