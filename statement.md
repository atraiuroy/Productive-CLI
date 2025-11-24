1. Problem Statement

Individuals often require a simple, immediate tool to manage and track short-term tasks or reminders without the overhead of installing complex software or accessing web-based applications. The need is for a lightweight, command-line utility that provides essential task management functionality (adding, viewing, and deleting tasks) during a user's active session.

2. Scope of the Project

The scope of this project is strictly limited to a console-based application implemented in Python.

Inclusions:

A text-based menu interface for navigation.

In-memory storage of tasks (data is not saved when the program exits).

Functions to add, view, and delete tasks by index.

Basic input validation (handling non-numeric input for deletion).

Exclusions:

Permanent data storage (no database, file I/O, or local storage).

Advanced features like task prioritization, due dates, or marking tasks as complete.

A graphical user interface (GUI).

Multi-user support.

3. Target Users

This application is designed for users who prioritize simplicity and speed over feature richness.

Beginner Programmers/Students: Used as a practical example to learn basic Python programming concepts (lists, loops, functions, I/O).

Individuals Needing Ephemeral Task Tracking: Users who need a quick list for tasks related to their current computer session (e.g., "Install package X," "Check configuration Y," "Reply to email Z").

Developers/System Administrators: For quick, on-the-fly task management within a terminal environment.

4. High-Level Features

The application provides the following core capabilities:

Feature Name

Description

Task Creation

Users can input a string to quickly add a new task to the list.

Task Listing

Displays the current list of tasks, numbered sequentially for easy reference.

Task Deletion

Allows the user to select and remove a task from the list using its numbered index.

Interactive Menu

A clear, loop-based menu system guiding the user through the available options (Add, View, Delete, Exit).

Session Persistence

Tasks remain stored in memory for the duration of the program's execution.
