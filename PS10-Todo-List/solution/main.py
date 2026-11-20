def show_tasks(tasks):
    if tasks:
        for position, task in enumerate(tasks, start=1):
            print(f"{position}. {task}")
    else:
        print("No tasks.")


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
        if tasks:
            position = input("Position to remove: ").strip()
            if position.isascii() and position.isdecimal() and 1 <= int(position) <= len(tasks):
                print(f"Removed: {tasks.pop(int(position) - 1)}")
            else:
                print("Choose one of the displayed positions.")
    elif command != "4":
        print("Choose a command from 1 through 4.")
    show_tasks(tasks)
