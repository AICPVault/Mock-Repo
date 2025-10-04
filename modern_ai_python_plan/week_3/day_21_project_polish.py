"""
Day 21: Project Continuation/Polish + Ruff Integration
======================================================

Today is about refining yesterday's project and ensuring it meets high
code quality standards by fully integrating Ruff. We will add a new feature
and then apply our linting and formatting rules.

Project Goals for Today:
1.  Add a "delete task" feature to the Task Tracker.
2.  Refactor the code for clarity and simplicity where possible.
3.  Set up `pyproject.toml` with Ruff configuration.
4.  Run Ruff to format and lint the entire project.
5.  Reflect on the improvements and the importance of code quality tools.
"""

# NOTE: This file is a continuation of Day 20's project.
# We will show the NEW and MODIFIED parts of the code.

# =============================================================================
# 0. RUFF CONFIGURATION (`pyproject.toml`)
# =============================================================================
"""
Before we start coding, let's create our `pyproject.toml` file in the project's
root directory. This file will define our project's standards.

--- pyproject.toml ---
[tool.ruff]
line-length = 88
target-version = "py311" # Or your python version

[tool.ruff.lint]
# Enable Flake8 ("F"), Pyflakes ("E"), isort ("I"), and PEP8 Naming ("N")
select = ["E", "F", "I", "N"]

[tool.ruff.format]
quote-style = "double"
# ---

Action: Create this file before proceeding.
"""

# =============================================================================
# 1. ADDING A "DELETE TASK" FEATURE
# =============================================================================

# We need a new function in our "CORE TASK MANAGEMENT FUNCTIONS" section.
# This function will remove a task by its ID.

# Import statements (Ruff will sort these)
import json
import logging
from pathlib import Path
from typing import TypedDict, NotRequired

# (Keep all the existing setup code from Day 20 here)
# ... Task class, logging setup, DATA_FILE, custom exceptions ...

# --- MODIFIED: CORE TASK MANAGEMENT FUNCTIONS ---

# (Keep `get_next_id`, `add_task`, `view_tasks`, `complete_task` here)
# ...

# --- NEW: `delete_task` function ---
def delete_task(tasks: list[TypedDict], task_id: int) -> list[TypedDict]:
    """Deletes a task by its ID."""
    original_length = len(tasks)
    # A list comprehension is a concise way to rebuild the list without the target task
    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(updated_tasks) == original_length:
        # If the list length hasn't changed, the task was not found
        raise TaskNotFoundError(f"Task with ID {task_id} not found for deletion.")

    logging.info(f"Deleted task with ID {task_id}.")
    return updated_tasks


# =============================================================================
# 2. INTEGRATING THE NEW FEATURE INTO THE MAIN LOOP
# =============================================================================

# We need to update the menu and the `match` block in our `main` function.

# --- MODIFIED: `print_menu` and `main` functions ---

def print_menu():
    """Prints the user menu."""
    print("\nTask Tracker Menu")
    print("1. View tasks")
    print("2. Add a new task")
    print("3. Mark a task as complete")
    print("4. Delete a task") # New option
    print("5. Exit") # Updated option number

def main():
    """The main function to run the CLI."""
    logging.info("Application starting.")
    tasks = load_tasks() # Assume load_tasks is defined as before

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
            # --- NEW CASE for deletion ---
            case "4":
                try:
                    task_id_str = input("Enter the ID of the task to delete: ")
                    task_id = int(task_id_str)
                    tasks = delete_task(tasks, task_id)
                    save_tasks(tasks)
                    print("Task deleted successfully.")
                except ValueError:
                    print("Error: Please enter a valid number for the task ID.")
                except TaskNotFoundError as e:
                    print(f"Error: {e}")
                    logging.warning(f"Failed to delete task: {e}")
            case "5": # Updated case number for exit
                logging.info("Application shutting down.")
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

# (Keep the if __name__ == "__main__": block)

# =============================================================================
# 3. RUNNING RUFF TO POLISH THE CODE
# =============================================================================
"""
Now that the new feature is in, it's time to clean up our entire project
(both Day 20 and Day 21 code).

Action:
1. Open your terminal in the project's root directory.
2. Run the formatter:
   > ruff format .
   - This will fix quotes, spacing, and other style issues.

3. Run the linter and auto-fixer:
   > ruff check --fix .
   - This will sort imports, remove unused variables (if any), and fix other
     common errors.

4. Check for remaining issues:
   > ruff check .
   - This final check should report no errors. If it does, they are likely
     issues that Ruff cannot fix automatically and require your manual attention.

By doing this, you ensure that your project not only works but is also clean,
consistent, and easy for others (and your future self) to read.
"""

# =============================================================================
# EXERCISES AND REFLECTION
# =============================================================================

# 1. Add another feature:
#    - Implement an "update task description" feature. It should take a task ID
#      and a new description as input.
#    - Add it to the main menu and logic.
#    - Remember to use `save_tasks` to persist the change.

# 2. Refactor `find_task_by_id`:
#    - In `complete_task` and `delete_task`, you have repeated logic for finding
#      a task by its ID.
#    - Create a helper function `_find_task_by_id(tasks, task_id)` that returns
#      the task dictionary or raises `TaskNotFoundError`. The underscore `_` prefix
#      is a convention for "internal" helper functions.
#    - Refactor `complete_task` and `delete_task` to use this new helper function.

# 3. Reflect on Ruff's impact:
#    - Look at the `git diff` of your files before and after running Ruff.
#    - What kind of changes did it make automatically?
#    - How does having an automated tool for this change the way you think about
#      code style while you are actively programming?

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- Iterating on a project by adding new features is a core part of software development.
- Code quality tools like Ruff are not just for a final cleanup; they are best
  used continuously to maintain a high standard throughout the development process.
- Automating formatting and linting frees you to focus on the logic and functionality
  of your application, knowing that the style will be handled for you.

This concludes Week 3! You've tackled robust error handling, professional logging,
and how to maintain excellent code quality.

Next up: Week 4 - Object-Oriented Programming and other modern Python features.
"""
