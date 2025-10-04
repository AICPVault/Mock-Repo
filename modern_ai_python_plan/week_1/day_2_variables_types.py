"""
Day 2: Variables, Modern Type Hints, and Mutability
=====================================================

Today we'll dive into the core concepts of storing data: variables,
how to annotate them with modern type hints, and the crucial difference
between mutable and immutable types.

Learning Objectives:
1.  Understand and declare variables.
2.  Use Python 3.12+'s modern generic syntax for type hints.
3.  Differentiate between mutable (e.g., list) and immutable (e.g., string) types.
4.  Learn about Python's built-in data types.
"""

# =============================================================================
# 1. VARIABLES
# =============================================================================

# A variable is a name that refers to a value.
# You can think of it as a label for a piece of data.
# The assignment operator `=` is used to assign a value to a variable.

project_name = "AI Learning Plan"
day_number = 2
is_beginner_friendly = True
learning_progress = 0.05

print(f"Project: {project_name}")
print(f"Day: {day_number}")
print(f"Progress: {learning_progress * 100}%")

# Python is dynamically typed, meaning you don't have to declare the type of a variable.
# The type is inferred at runtime. The same variable name can even be reassigned to a different type.
a_variable = 100
print(f"Variable is: {a_variable}, type is: {type(a_variable)}")

a_variable = "Now I'm a string"
print(f"Variable is: {a_variable}, type is: {type(a_variable)}")


# =============================================================================
# 2. MODERN TYPE HINTS (PYTHON 3.9+)
# =============================================================================

"""
What are Type Hints?
- They are optional annotations that indicate the expected type of a variable or function parameter.
- They do NOT enforce types (Python remains dynamically typed), but they are used by tools
  like linters (Ruff) and IDEs (VS Code) to help you catch bugs before you run the code.
- They make code much easier to read and understand.

Modern Syntax (PEP 585 & PEP 604):
- Use built-in collection types directly (e.g., `list`, `dict`, `set`).
- Use `|` for unions (e.g., `int | float`).
"""

# Variable with a simple type hint
user_name: str = "Alice"

# Variable with a more complex type hint (a list of integers)
user_scores: list[int] = [98, 100, 95]

# A dictionary mapping string keys to float values
product_prices: dict[str, float] = {"laptop": 1200.50, "mouse": 25.00}

# A variable that can be either an integer or a string
user_id: int | str = 12345
user_id = "uid-abc-123"  # This is also valid according to the hint

# The `None` type can be used for optional values
winner: str | None = None
print(f"Winner: {winner}")
winner = "Bob"
print(f"Winner: {winner}")


# =============================================================================
# 3. MUTABLE VS IMMUTABLE TYPES
# =============================================================================

"""
This is a FUNDAMENTAL concept in Python.

Immutable Types:
- Their value CANNOT be changed after they are created.
- If you "change" them, you are actually creating a new object in memory.
- Examples: int, float, str, tuple, bool, None

Mutable Types:
- Their value CAN be changed in-place after they are created.
- You can modify them without creating a new object.
- Examples: list, dict, set
"""

# --- IMMUTABLE EXAMPLE (string) ---
my_string: str = "hello"
print(f"Original string: '{my_string}' at memory ID: {id(my_string)}")

# This does not change the original string. It creates a NEW string.
my_string = my_string + " world"
print(f"New string: '{my_string}' at memory ID: {id(my_string)}")
# Note that the memory ID has changed!

# --- MUTABLE EXAMPLE (list) ---
my_list: list[int] = [1, 2, 3]
print(f"Original list: {my_list} at memory ID: {id(my_list)}")

# We are modifying the list in-place.
my_list.append(4)
print(f"Modified list: {my_list} at memory ID: {id(my_list)}")
# Note that the memory ID is the SAME!

# Why does this matter?
# Understanding this is crucial for avoiding bugs, especially when passing data to functions.
# If you pass a mutable object to a function, that function can change it!

# =============================================================================
# EXERCISES
# =============================================================================

# 1. Declare variables for a user profile:
#    - `username` (string)
#    - `user_age` (integer)
#    - `favorite_languages` (a list of strings)
#    - `is_active` (boolean)
#    - Add modern type hints to all of them.
#    - Print each variable with a descriptive label.

# 2. Predict the output and the memory IDs:
#    - Before running the code, guess if the ID of `a` will change.
a: tuple[int, ...] = (1, 2, 3)
print(f"Initial tuple `a`: {a}, ID: {id(a)}")
a = a + (4,)  # Note: adding a tuple to a tuple creates a new one
print(f"Final tuple `a`: {a}, ID: {id(a)}")

# 3. Modify a mutable object:
#    - Create a dictionary representing a car with keys "brand", "model", and "year".
#    - Add a new key "color" with a value.
#    - Update the "year" to the current year.
#    - Print the final dictionary.

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- Variables are labels for data.
- Modern type hints (`list[int]`, `str | None`) make your code robust and readable.
- The distinction between mutable (changable, e.g., list) and immutable (unchangable, e.g., str)
  objects is critical for understanding how Python manages data.

Next up: Day 3 - A deep dive into strings.
"""
