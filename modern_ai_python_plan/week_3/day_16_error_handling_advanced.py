"""
Day 16: Error Handling II - Advanced Concepts
==============================================

Building on yesterday's basics, we'll now explore how to create our own
custom exceptions for more specific error reporting and how to use context
managers to handle resources like files more elegantly and safely.

Learning Objectives:
1.  Create and raise custom exception classes.
2.  Understand the benefits of application-specific exceptions.
3.  Use the `with` statement (context managers) for resource management.
4.  Briefly understand how to create your own context manager (optional).
"""

# =============================================================================
# 1. CUSTOM EXCEPTIONS
# =============================================================================

# While Python's built-in exceptions are useful, sometimes you need to represent
# an error that is specific to your application's logic.

# --- Creating a Custom Exception ---
# It's as simple as inheriting from the base `Exception` class.
# It's good practice to create a base exception for your application.
class AppError(Exception):
    """Base exception for this application."""
    pass

class UserNotFoundError(AppError):
    """Raised when a user is not found in the database."""
    pass

class InsufficientPermissionsError(AppError):
    """Raised when a user attempts an action they are not authorized for."""
    def __init__(self, user, action):
        self.user = user
        self.action = action
        message = f"User '{self.user}' does not have permission to '{self.action}'."
        super().__init__(message)

# --- Raising a Custom Exception ---
# The `raise` keyword is used to trigger an exception.
def get_user(user_id: int) -> dict:
    # A mock database
    users_db = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    if user_id not in users_db:
        raise UserNotFoundError(f"User with ID {user_id} does not exist.")
    return users_db[user_id]

def delete_post(user_role: str):
    if user_role != "admin":
        raise InsufficientPermissionsError(user=user_role, action="delete post")
    print("Post deleted successfully.")


# --- Handling Custom Exceptions ---
# You catch them just like built-in exceptions.
try:
    get_user(3)
except UserNotFoundError as e:
    print(f"Caught a custom error: {e}")

try:
    delete_post(user_role="editor")
except InsufficientPermissionsError as e:
    print(f"Caught a permission error: {e}")


# =============================================================================
# 2. CONTEXT MANAGERS (THE `with` STATEMENT)
# =============================================================================

"""
A context manager is an object that defines a temporary context for a block of code.
The `with` statement ensures that setup and cleanup operations are always performed.

You've already been using it for files!
`with open(...) as f:` is a context manager.
- Setup: It opens the file and returns a file object.
- Cleanup: It automatically closes the file, even if errors occur inside the block.
"""

# The `with` statement makes the `try...finally` pattern for cleanup obsolete.
# It's cleaner, more readable, and less error-prone.

# --- Old way (from yesterday) ---
f = None
try:
    f = open("old_way.txt", "w")
    f.write("messy")
finally:
    if f:
        f.close()

# --- Modern, correct way ---
try:
    with open("modern_way.txt", "w") as f:
        f.write("clean and safe")
    # The file is guaranteed to be closed here.
except IOError as e:
    print(f"File error: {e}")

# Clean up our example files
import os
os.remove("old_way.txt")
os.remove("modern_way.txt")

# The `with` statement can be used for many other resources, like:
# - Database connections
# - Network sockets
# - Locks in multithreading


# =============================================================================
# EXERCISES
# =============================================================================

# 1. Custom API Error:
#    - Create a custom exception called `APIRequestError`.
#    - Write a mock function `fetch_data_from_api(url: str)` that simulates
#      fetching data.
#    - Inside the function, if the `url` does not start with "https://", `raise`
#      the `APIRequestError` with a helpful message.
#    - Call this function with both a valid and an invalid URL, and wrap the
#      calls in a `try...except` block to handle the custom error.

# 2. Insufficient Funds:
#    - Create a custom exception `InsufficientFundsError`.
#    - Write a simple `BankAccount` class with an `__init__` method that sets a
#      `balance` and a `withdraw(amount)` method.
#    - In the `withdraw` method, if the `amount` is greater than the `balance`,
#      `raise` the `InsufficientFundsError`. Otherwise, reduce the balance.
#    - Create an instance of the bank account and test the withdrawal logic,
#      handling the exception gracefully.

# 3. Refactor to `with`:
#    - Imagine you have code that manually acquires and releases a lock for
#      threading (even if you don't know threading, the pattern is the key).
#      ```python
#      import threading
#      lock = threading.Lock()
#      lock.acquire()
#      try:
#          # do some critical work...
#          print("Doing critical work while holding the lock.")
#      finally:
#          lock.release()
#      ```
#    - The `threading.Lock` object is also a context manager. Refactor the
#      above code to use a `with` statement, which is the standard practice.

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- Custom exceptions make your application's error-handling more specific and meaningful.
- The `with` statement is the superior, modern way to manage resources that require
  setup and cleanup, ensuring that cleanup code always runs.
- Always prefer `with` for files, locks, database connections, and other similar resources.

Next up: Day 17 - Ensuring code quality from the start with Ruff.
"""
