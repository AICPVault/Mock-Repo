"""
Day 20: Project - Task Tracker CLI
==================================

Let's combine what we've learned this week about error handling, file I/O,
JSON, and logging to build a persistent command-line task tracker.

Project Goals:
1.  Allow users to add new tasks.
2.  Allow users to view all tasks.
3.  Allow users to mark tasks as complete.
4.  Persist tasks to a JSON file so they are not lost when the app closes.
5.  Implement logging to track application events and errors.
6.  Use custom exceptions for specific error conditions.
7.  Structure the code cleanly with functions.
"""

import json
import logging
from pathlib import Path
from typing import TypedDict, NotRequired

# =============================================================================
# 0. SETUP AND DATA STRUCTURE
# =============================================================================

# --- Data Structure for a Task ---
# Using TypedDict for clear structure and type hints
class Task(TypedDict):
    id: int
    description: str
    completed: bool
    notes: NotRequired[str] # An optional field

# --- Setup Logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='task_tracker.log',
    filemode='a'
)

# --- Define Global Variables and Custom Exceptions ---
DATA_FILE = Path("tasks.json")

class TaskError(Exception):
    """Base exception for task-related errors."""
    pass

class TaskNotFoundError(TaskError):
    """Raised when a task ID is not found."""
    pass


# =============================================================================
# 1. FILE I/O FUNCTIONS
# =============================================================================

def load_tasks() -> list[Task]:
    """Loads tasks from the JSON file. Returns an empty list if not found."""
    if not DATA_FILE.exists():
        logging.info("Data file not found. Starting with an empty task list.")
        return []
    try:
        with DATA_FILE.open("r") as f:
            tasks: list[Task] = json.load(f)
            logging.info(f"Successfully loaded {len(tasks)} tasks from {DATA_FILE}.")
            return tasks
    except (json.JSONDecodeError, IOError) as e:
        logging.exception(f"Error loading tasks from {DATA_FILE}. Returning empty list.")
        # In a real app, you might want to handle this differently (e.g., backup file)
        return []

def save_tasks(tasks: list[Task]) -> None:
    """Saves the list of tasks to the JSON file."""
    try:
        with DATA_FILE.open("w") as f:
            json.dump(tasks, f, indent=2)
            logging.info(f"Successfully saved {len(tasks)} tasks to {DATA_FILE}.")
    except IOError:
        logging.exception(f"Could not save tasks to {DATA_FILE}.")


# =============================================================================
# 2. CORE TASK MANAGEMENT FUNCTIONS
# =============================================================================

def get_next_id(tasks: list[Task]) -> int:
    """Calculates the next unique ID for a new task."""
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task(tasks: list[Task], description: str) -> list[Task]:
    """Adds a new task to the list."""
    if not description:
        raise ValueError("Task description cannot be empty.")

    new_task: Task = {
        "id": get_next_id(tasks),
        "description": description,
        "completed": False
    }
    tasks.append(new_task)
    logging.info(f"Added new task: '{description}' with ID {new_task['id']}.")
    return tasks

def view_tasks(tasks: list[Task]) -> None:
    """Displays all tasks to the user."""
    if not tasks:
        print("\nNo tasks found. Add one!")
        return

    print("\n--- Your Tasks ---")
    for task in sorted(tasks, key=lambda t: t['id']):
        status = "✅" if task['completed'] else "❌"
        print(f"{status} [{task['id']}] {task['description']}")
    print("------------------")

def complete_task(tasks: list[Task], task_id: int) -> list[Task]:
    """Marks a specific task as complete."""
    for task in tasks:
        if task['id'] == task_id:
            if task['completed']:
                print(f"Task {task_id} is already marked as complete.")
                return tasks
            task['completed'] = True
            logging.info(f"Marked task {task_id} as complete.")
            return tasks
    # If the loop finishes without finding the task
    raise TaskNotFoundError(f"Task with ID {task_id} not found.")


# =============================================================================
# 3. MAIN APPLICATION LOOP
# =============================================================================

def print_menu():
    """Prints the user menu."""
    print("\nTask Tracker Menu")
    print("1. View tasks")
    print("2. Add a new task")
    print("3. Mark a task as complete")
    print("4. Exit")

def main():
    """The main function to run the CLI."""
    logging.info("Application starting.")
    tasks = load_tasks()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                view_tasks(tasks)
            case "2":
                try:
                    desc = input("Enter task description: ")
                    tasks = add_task(tasks, desc)
                    save_tasks(tasks)
                    print("Task added successfully.")
                except ValueError as e:
                    print(f"Error: {e}")
                    logging.warning(f"Failed to add task: {e}")
            case "3":
                try:
                    task_id_str = input("Enter the ID of the task to complete: ")
                    task_id = int(task_id_str)
                    tasks = complete_task(tasks, task_id)
                    save_tasks(tasks)
                    print("Task marked as complete.")
                except ValueError:
                    print("Error: Please enter a valid number for the task ID.")
                except TaskNotFoundError as e:
                    print(f"Error: {e}")
                    logging.warning(f"Failed to complete task: {e}")
            case "4":
                logging.info("Application shutting down.")
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
