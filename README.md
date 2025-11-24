The PyTasker project is a text-based command-line To-Do List application written in Python. It allows users to manage daily tasks by adding, viewing, marking complete, and deleting items. The application applies core programming concepts such as functions, lists, control flow, and data persistence via local file I/O. This is a simple command-line To-Do List application written in Python. It allows users to add, view, and delete tasks in a persistent list for the duration of its execution.

Features Add Task: Add a new task to your list.

View Tasks: Shows all the current tasks with numbered indices.

Task Deletion: Remove a task by its numbered index.

Menu-Driven: Simple interactive console interface.

Save the Code: Save the following Python code into a file called for instance todo_list.py.

Run from Terminal: Open a terminal or command prompt and execute the script using the Python interpreter:

Bash

python todo_list.py Usage via Menu: This program will display a menu. Type 1, 2, 3, or 4 to choose an action.

Structure of Code The application centers around a number of key components:

tasks List:

An initially empty list to hold all the to-do items as strings; this was initialized at the start, tasks = []. This will provide data storage for the program.

display_menu() Function:

This is a method that prints, to the console, the interactive menu options: Add, View, Delete and Exit.

Main while Loop:

The core of the application. It runs continuously (while True) until the user selects the 'Exit' option.

It calls display_menu(), takes user input (choice), and then executes the corresponding logic using if/elif/else blocks.

Option Logic:

Choice '1' (Add Task): Prompts the user for a task string and uses tasks.append() to add it.

Choice '2' (View Tasks): Checks if the list is empty. If not, it uses enumerate() to iterate through the list and print each task with a 1-based index.

Choice '3' (Delete Task):

First, displays the tasks (similar to Choice '2').

Prompts the user for the task number.

Uses a try-except block to handle potential ValueError if the user enters non-numeric input.

Converts the 1-based index to a 0-based list index (- 1).

Checks if the index is valid (0 <= task_index < len(tasks)).

If valid, uses tasks.pop(task_index) to remove the task and prints a confirmation.

Choice '4' (Exit): Prints a farewell message and uses break to exit the while True loop, terminating the program.

 Example Usage
--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
-----------------------
Enter your choice: 1
Enter the task: Buy groceries
Task 'Buy groceries' added.

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
-----------------------
Enter your choice: 2

--- Your Tasks ---
1. Buy groceries
------------------

--- To-Do List Menu ---
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
-----------------------
Enter your choice: 4
Exiting To-Do List. Goodbye!
