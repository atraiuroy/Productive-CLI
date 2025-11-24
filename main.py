tasks = []


def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("-----------------------")


while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"Task '{task}' added.")
    elif choice == '2':
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\n--- Your Tasks ---")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
            print("------------------")
    elif choice == '3':
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\n--- Your Tasks ---")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
            print("------------------")
            try:
                task_index = int(
                    input("Enter the number of the task to delete: ")) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f"Task '{removed_task}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
