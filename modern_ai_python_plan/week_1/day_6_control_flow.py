"""
Day 6: Control Flow
===================

Control flow statements allow your program to make decisions and execute
different blocks of code based on conditions.

Learning Objectives:
1.  Use `if`, `elif`, and `else` for conditional logic.
2.  Understand truthiness and how non-boolean values are evaluated.
3.  Use the modern `match/case` statement for structural pattern matching (Python 3.10+).
4.  Write concise conditions with ternary expressions.
"""

# =============================================================================
# 1. IF / ELIF / ELSE
# =============================================================================

# This is the fundamental way to make decisions in code.
# The code block under the first `True` condition is executed.

# --- Simple `if` statement ---
temperature: float = 25.5
if temperature > 20:
    print("It's a warm day!")

# --- `if/else` statement ---
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# --- `if/elif/else` chain ---
# This is used for multiple exclusive conditions.
score: int = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(f"A score of {score} gets a grade of {grade}.")


# =============================================================================
# 2. TRUTHINESS
# =============================================================================

"""
In Python, values can be evaluated in a boolean context. This is "truthiness".

Values that are considered `False` (Falsy):
- The boolean `False`
- `None`
- Numeric zero (0, 0.0)
- Empty collections ([], (), {}, set())
- Empty strings ("")

Everything else is considered `True` (Truthy).
"""

my_list: list[int] = []

# Instead of `if len(my_list) > 0:`, we can just do:
if my_list:
    print("The list is not empty.")
else:
    print("The list is empty.") # This will be printed

user_name: str | None = None
if user_name:
    print(f"Hello, {user_name}")
else:
    print("Hello, guest!") # This will be printed


# =============================================================================
# 3. MATCH / CASE (STRUCTURAL PATTERN MATCHING)
# =============================================================================

"""
Introduced in Python 3.10, `match/case` is a powerful alternative to complex
`if/elif/else` chains, especially when you need to match the *structure* of data.
"""

# --- Simple value matching ---
http_status: int = 404

match http_status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:  # The wildcard `_` acts as a default/catch-all, like `else`.
        print("Unknown status")

# --- Matching with structure and conditions ---
# This is where `match/case` really shines.
command: tuple = ("move", 10, 25) # Represents a command tuple

match command:
    case ("quit",):
        print("Quitting the program.")
    case ("move", x, y):
        print(f"Moving to position ({x}, {y}).")
    case ("draw", shape, color) if color in ["red", "blue", "green"]:
        print(f"Drawing a {color} {shape}.")
    case ("draw", _, _):
        print("Invalid color specified for draw command.")
    case _:
        print("Unknown command.")


# =============================================================================
# 4. TERNARY EXPRESSIONS
# =============================================================================

# A concise, one-line way to write a simple `if/else` statement.
# Syntax: `value_if_true if condition else value_if_false`

age: int = 20

# Classic if/else
if age >= 18:
    access_level = "adult"
else:
    access_level = "minor"

# Ternary expression equivalent
access_level_ternary = "adult" if age >= 18 else "minor"

print(f"\nAccess level (classic): {access_level}")
print(f"Access level (ternary): {access_level_ternary}")

# It's great for simple assignments, but don't overuse it for complex logic
# as it can harm readability.


# =============================================================================
# EXERCISES
# =============================================================================

# 1. User Role Checker:
#    - Write a script that checks a user's role (`admin`, `editor`, `viewer`).
#    - Use an `if/elif/else` chain to print a different message for each role.
#    - For an unknown role, print "Invalid role".

# 2. Command Processor with `match/case`:
#    - You receive a command which is a list, e.g., `['post', 'This is my message']`
#      or `['delete', 123]`.
#    - Write a `match/case` block that handles the following commands:
#      - `['post', message]`: Print `Posting message: "{message}"`
#      - `['delete', post_id]`: Print `Deleting post with ID: {post_id}`
#      - `['like', post_id]`: Print `Liking post {post_id}`
#      - Any other command should print "Command not recognized."

# 3. Pluralizer with Ternary:
#    - You have a variable `num_items`.
#    - Use a ternary expression to create a string that says "1 item" if `num_items` is 1,
#      and "N items" otherwise (where N is the value of `num_items`).
#    - Test it with `num_items = 1` and `num_items = 5`.

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- `if/elif/else` is your standard tool for decision-making.
- Understanding "truthiness" allows you to write more concise and Pythonic code.
- `match/case` is the modern, powerful tool for handling complex conditional logic based on
  data structure, not just value.
- Ternary expressions are a compact way to handle simple assignments based on a condition.

Next up: Day 7 - Loops for iteration.
"""
