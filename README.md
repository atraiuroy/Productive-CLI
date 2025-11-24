# Productive-CLI
The PyTasker project is a command-line To-Do List application built in Python. It allows users to manage daily tasks by adding, viewing, marking complete, and deleting items. The application demonstrates core programming concepts like functions, lists, and control flow, with persistent data storage achieved via local file I/O.
This is a simple command-line To-Do List application written in Python. It allows users to add, view, and delete tasks in a persistent list (for the duration of the program's execution).

 Features
Add Task: Easily append a new task to your list.

View Tasks: Display all current tasks with numbered indices.

Delete Task: Remove a task by its numbered index.

Menu-Driven: Simple interactive console interface.

 How to Run
Save the Code: Save the provided Python code into a file named, for example, todo_list.py.

Run from Terminal: Open your terminal or command prompt and run the script using the Python interpreter:

Bash

python todo_list.py
Use the Menu: The program will present a menu. Enter the corresponding number (1, 2, 3, or 4) to select an option.

 Code Structure
The application is structured around a few key components:

tasks List:

An empty list initialized at the start (tasks = []) which stores all the to-do items as strings. This list acts as the program's data storage.

display_menu() Function:

A function responsible for printing the interactive menu options (Add, View, Delete, Exit) to the console.

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
