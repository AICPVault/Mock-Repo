"""
Day 9: Functions II - Advanced Features
=======================================

Today we build on our knowledge of functions, exploring modern type annotation
syntax and advanced parameter handling that gives you precise control over
how your functions can be called.

Learning Objectives:
1.  Use modern syntax for type annotations in functions.
2.  Understand and use positional-only (`/`) and keyword-only (`*`) parameters.
3.  Grasp the concept of function scope (local vs. global).
4.  Write clear and robust function signatures.
"""
from typing import Sequence # Using typing for more complex hints

# =============================================================================
# 1. TYPE ANNOTATIONS FOR FUNCTIONS (MODERN SYNTAX)
# =============================================================================

# Type annotations make function signatures much clearer.
# Syntax: `def func(param: type) -> return_type:`

def calculate_total(prices: list[float], tax_rate: float) -> float:
    """Calculates the total cost including tax."""
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)

# Using more complex types from the `typing` module
# `Sequence` is a generic type that includes lists, tuples, strings, etc.
def find_longest_word(words: Sequence[str]) -> str | None:
    """Finds the longest word in a sequence of words."""
    if not words:
        return None
    return max(words, key=len)

# You can use `|` for union types (e.g., can accept an int or a float).
def process_id(user_id: int | str) -> None:
    print(f"Processing user ID: {user_id} of type {type(user_id)}")

process_id(123)
process_id("user-abc-456")


# =============================================================================
# 2. POSITIONAL-ONLY AND KEYWORD-ONLY PARAMETERS
# =============================================================================

"""
Python 3.8+ introduced syntax for enforcing how arguments can be passed to a function.
This makes APIs less ambiguous and more maintainable.

- Positional-Only (`/`): Everything before the `/` MUST be passed by position.
- Keyword-Only (`*`): Everything after the `*` MUST be passed by keyword.
- You can use both together.
"""

# --- Positional-Only Example (`/`) ---
# Useful for simple parameters where the name doesn't add much clarity, like in math functions.
def add(a: int, b: int, /) -> int:
    """This function only accepts positional arguments."""
    return a + b

print(f"Positional-only call (correct): {add(10, 20)}")
try:
    add(a=10, b=20) # This will raise a TypeError
except TypeError as e:
    print(f"Positional-only call (incorrect): {e}")


# --- Keyword-Only Example (`*`) ---
# Useful when you want to force callers to be explicit, which improves readability.
def send_email(*, recipient: str, subject: str, body: str) -> None:
    """This function only accepts keyword arguments."""
    print(f"\nSending email to: {recipient}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")

send_email(recipient="test@example.com", subject="Hello", body="This is a test.")
try:
    # This will raise a TypeError because the arguments are not passed by keyword.
    send_email("test@example.com", "Hello", "This is a test.")
except TypeError as e:
    print(f"\nKeyword-only call (incorrect): {e}")

# --- Combining All Three ---
def create_user(name: str, /, *, age: int, is_active: bool = True) -> dict:
    """
    `name` is positional-only.
    `age` and `is_active` are keyword-only.
    """
    return {"name": name, "age": age, "is_active": is_active}

# Correct usage
user = create_user("Alice", age=30)
print(f"\nCorrect combined call: {user}")

# Incorrect usage
try:
    # `name` passed as keyword, `age` passed as positional
    create_user(name="Bob", 35)
except TypeError as e:
    print(f"Incorrect combined call: {e}")


# =============================================================================
# 3. FUNCTION SCOPE
# =============================================================================

# Scope determines the visibility of a variable.

# Global variable
global_var: str = "I am global"

def scope_test():
    # Local variable - it only exists inside this function
    local_var: str = "I am local"
    print(f"Inside function: Can access local_var -> '{local_var}'")
    print(f"Inside function: Can access global_var -> '{global_var}'")

scope_test()

print(f"\nOutside function: Can access global_var -> '{global_var}'")
try:
    # This will raise a NameError because local_var is out of scope
    print(local_var)
except NameError as e:
    print(f"Outside function: Cannot access local_var -> {e}")


# =============================================================================
# EXERCISES
# =============================================================================

# 1. Type-Annotated Formatter:
#    - Write a function `format_user_data` that takes a list of dictionaries and a boolean `short_format`.
#    - Add type annotations for all parameters and the return value (it should return a list of strings).
#    - Inside the function, format the data based on the boolean flag.

# 2. Enforce API Clarity:
#    - Design a function `create_report(title, /, *, data: list, author: str)`.
#    - `title` should be a positional-only argument.
#    - `data` and `author` should be keyword-only arguments.
#    - The function should print a confirmation that the report is being generated.
#    - Call the function correctly.
#    - Try to call it incorrectly (e.g., `create_report(title="My Report", ...)` and observe the error.

# 3. Scope Experiment:
#    - Define a global variable `counter = 0`.
#    - Write a function `increment()` that tries to increase the counter.
#    - What happens when you run it? (It will raise an UnboundLocalError).
#    - Fix it by using the `global` keyword inside the function (`global counter`).
#      (Note: Modifying global state is generally discouraged, but this is a key concept to understand).

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- Type annotations are crucial for writing modern, maintainable Python.
- Positional-only (`/`) and keyword-only (`*`) syntax gives you fine-grained control
  over your function's API, making it more robust and readable.
- Understanding variable scope (local vs. global) is essential for avoiding bugs.

Next up: Day 10 - A very "Pythonic" feature: Comprehensions.
"""
