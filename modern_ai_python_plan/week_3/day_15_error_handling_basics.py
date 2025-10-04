"""
Day 15: Error Handling I - The Basics
======================================

Even in the best-written code, errors can happen. Robust programs anticipate
and handle these errors gracefully. Today, we'll cover the fundamental tools
Python provides for error handling.

Learning Objectives:
1.  Understand the difference between syntax errors and exceptions.
2.  Use the `try...except` block to catch and handle exceptions.
3.  Utilize the `else` and `finally` clauses for more complex control flow.
4.  Understand Python's built-in exception hierarchy.
"""

# =============================================================================
# 1. SYNTAX ERRORS VS. EXCEPTIONS
# =============================================================================

# --- Syntax Error ---
# This is an error in the code's structure that Python's parser detects before
# the program even starts running. You must fix these before execution.
# Example (uncomment to see the error):
# print("Hello"

# --- Exception ---
# An exception occurs during the execution of the program. It happens when the
# syntax is correct, but something goes wrong during the operation.
# Example: Trying to divide by zero.
# 10 / 0  # This raises a ZeroDivisionError


# =============================================================================
# 2. THE `try...except` BLOCK
# =============================================================================

# This is the core mechanism for handling exceptions.
# - The code that might raise an exception is placed in the `try` block.
# - The code to handle the exception is placed in the `except` block.

def safe_divide(a: float, b: float) -> float | str:
    """A function that safely handles division by zero."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")


# --- Catching Specific Exceptions ---
# It's best practice to catch the most specific exception you expect.
user_input = "hello"
try:
    number = int(user_input)
    print(f"Successfully converted to integer: {number}")
except ValueError:
    print(f"Error: Could not convert '{user_input}' to an integer.")

# --- Catching Multiple Exceptions ---
# You can catch multiple exceptions in a single `except` block using a tuple.
def process_data(data: dict, key: str):
    try:
        value = data[key]
        result = 100 / value
        print(f"Result is {result}")
    except (KeyError, ZeroDivisionError, TypeError) as e:
        # The `as e` part captures the exception object itself.
        print(f"An error occurred: {e}")
        print(f"The type of the error was: {type(e).__name__}")

process_data({"value": 5}, "value")      # Works fine
process_data({"value": 0}, "value")      # ZeroDivisionError
process_data({"data": 5}, "value")       # KeyError
process_data({"value": "text"}, "value") # TypeError


# =============================================================================
# 3. THE `else` AND `finally` CLAUSES
# =============================================================================

# --- The `else` Block ---
# The `else` block executes only if the `try` block completes successfully
# (i.e., no exceptions were raised). It's useful for code that should only run
# when the main operation succeeds.

print("\n--- Example with `else` ---")
try:
    num = int("123")
except ValueError:
    print("Conversion failed.")
else:
    # This runs because the `try` block was successful.
    print(f"Conversion successful. The number is {num}.")

# --- The `finally` Block ---
# The `finally` block executes no matter what. It runs whether an exception
# was raised, handled, or not. It is essential for cleanup actions, like
- closing files or releasing network connections.

print("\n--- Example with `finally` ---")
f = None # Initialize f outside the try block
try:
    f = open("temp_file.txt", "w")
    f.write("Hello!")
    # Uncomment the next line to simulate an error
    # 10 / 0
    print("File write successful.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # This cleanup code runs regardless of an error.
    if f:
        f.close()
        print("File closed.")
        import os
        os.remove("temp_file.txt") # Clean up the created file


# =============================================================================
# EXERCISES
# =============================================================================

# 1. Safe Dictionary Access:
#    - Write a function `get_value(my_dict, key)` that attempts to access `my_dict[key]`.
#    - Use a `try...except` block to handle the `KeyError` that occurs if the key
#      is not in the dictionary. The function should return `None` in that case.

# 2. Number Input Validator:
#    - Write a loop that prompts the user to enter an integer.
#    - Use a `try...except ValueError` block to handle cases where the user enters
#      non-numeric input.
#    - The loop should continue until the user successfully enters a valid integer.
#    - Use an `else` block to print a "Thank you" message and then `break` the loop.

# 3. File Processor with Cleanup:
#    - Write a script that opens a file for writing, writes a line of text, and then
#      intentionally tries to perform an invalid operation (e.g., add a string to a number).
#    - Use `try...except...finally` to ensure that the file is always closed,
#      even after the error occurs.

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- `try`: Code that might fail.
- `except`: Code that runs if an error occurs. Catch specific exceptions.
- `else`: Code that runs only if the `try` block succeeds.
- `finally`: Code that runs no matter what. Essential for cleanup.
- Handling exceptions is key to building robust, production-ready applications.

Next up: Day 16 - Advanced error handling with custom exceptions and context managers.
"""
