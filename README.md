# Productive-CLI
The PyTasker project is a command-line To-Do List application built in Python. It allows users to manage daily tasks by adding, viewing, marking complete, and deleting items. The application demonstrates core programming concepts like functions, lists, and control flow, with persistent data storage achieved via local file I/O.
 PyTasker: Command-Line To-Do List Application

 Project Title

PyTasker: Command-Line To-Do List Application

 Overview of the Project

PyTasker is a lightweight, menu-driven To-Do List application developed in pure Python for a first-semester programming project. It addresses the real-world need for a simple, non-web-based tool to manage daily tasks.

The application demonstrates core programming concepts, including functions for modular design, list data structures, and persistent storage using basic file input/output (I/O). All task data is saved locally to a file named todo.txt.

 Features

PyTasker provides a full set of management operations for tasks:

View Tasks (Read): Displays all current tasks with an index number and a completion status ( Complete or  Pending).

Add New Task (Create): Prompts the user for a task description and adds it to the list.

Mark as Complete (Update): Allows the user to input a task number to toggle its status to complete.

Delete Task (Delete): Removes a task permanently from the list and the storage file.

Persistent Storage: Automatically loads tasks on startup and saves changes to todo.txt, ensuring data is kept between sessions.

Input Validation: Includes basic error handling for non-numeric or out-of-range user inputs when managing tasks.

 Technologies/Tools Used

Category

Tool / Concept

Application in Project

Language

Python 3.x

All core logic and implementation.

Data Structure

Python List of Dictionaries

Used to store tasks in memory: [{'task': '...', 'completed': True/False}, ...]

Storage

File I/O (.txt file)

Used the built-in open(), read(), and write() functions to save and load data from todo.txt.

Modular Design

Functions

The code is organized using dedicated functions (load_tasks, add_task, main) following Top-Down Design principles.

 Steps to Install & Run the Project

Since this is a Python-only command-line application, installation is simple.

Clone the Repository (or download the file):

git clone [Your-GitHub-Repository-URL]
cd [Your-Project-Directory]


Ensure Python is Installed:
Verify you have Python 3.x installed on your system.

python --version
# or
python3 --version


Run the Application:
Execute the main script from your terminal:

python todo_list.py
# or
python3 todo_list.py


 Instructions for Testing

To ensure the project is working correctly, follow these test steps:

Test Case

Steps

Expected Outcome

Add & View

Run the app, select 2. Add New Task. Add "Buy milk". Then select 1. View To-Do List.

The task "Buy milk" should appear as number 1 with a  status.

Mark Complete

Select 3. Mark Task as Complete. Enter the index 1. Then select 1. View To-Do List.

The task "Buy milk" should now show a status.

Persistence

Add a few tasks, mark one complete. Select 5. Exit Application. Rerun the script.

All tasks and their statuses should be correctly re-loaded from todo.txt.

Delete Task

Select 4. Delete Task. Enter the index of any task.

The task should be immediately removed from the displayed list.

Invalid Input

When prompted for a task number (options 3 or 4), enter text like "abc" or a number outside the range (e.g., 99).

The program should display an error message ( Error: Invalid task number. or Error: Please enter a valid number.) and return to the main menu without crashing.

 Screenshots (Optional but Recommended)

(Students should place relevant screen captures here after running the program. E.g., showing the main menu, the list of tasks, and the final exit message.)
