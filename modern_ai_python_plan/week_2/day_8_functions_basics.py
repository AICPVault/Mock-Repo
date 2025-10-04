"""
Day 8: Functions I - The Basics
===============================

Functions are reusable blocks of code that perform a specific task. They are
the cornerstone of organized, efficient, and readable programming.

Learning Objectives:
1.  Define and call functions using `def`.
2.  Understand parameters and arguments.
3.  Use the `return` statement to send back values.
4.  Learn to capture a variable number of arguments with `*args` and `**kwargs`.
5.  Write effective docstrings to document your functions.
"""

# =============================================================================
# 1. DEFINING AND CALLING A FUNCTION
# =============================================================================

# The `def` keyword is used to define a function.
# The function body is indented, just like with loops and conditionals.

def greet():
    """This is a simple function that prints a greeting."""
    print("Hello, welcome to Week 2!")

# To run the code inside a function, you "call" it.
greet()


# =============================================================================
# 2. PARAMETERS AND ARGUMENTS
# =============================================================================

# Parameters are the names listed in the function definition.
# Arguments are the actual values passed to the function when it is called.

def greet_user(name: str):  # `name` is a parameter
    """Greets a specific user."""
    print(f"Hello, {name}!")

greet_user("Alice")  # "Alice" is an argument

# --- Default Arguments ---
# You can provide a default value for a parameter.
def greet_with_default(name: str = "Guest"):
    """Greets a user, with a default name if none is provided."""
    print(f"Hello, {name}!")

greet_with_default("Bob")
greet_with_default() # Will use the default value "Guest"


# =============================================================================
# 3. THE `return` STATEMENT
# =============================================================================

# Functions can process data and send a result back to the caller using `return`.
# When `return` is executed, the function immediately exits.

def add(a: int, b: int) -> int:  # `-> int` is a type hint for the return value
    """Adds two numbers and returns the result."""
    return a + b

sum_result = add(5, 3)
print(f"The sum is: {sum_result}")

# A function can return multiple values (as a tuple).
def get_user_details() -> tuple[str, int]:
    """Returns a user's name and age."""
    return "Charlie", 30

user_name, user_age = get_user_details() # Unpacking the returned tuple
print(f"User: {user_name}, Age: {user_age}")


# =============================================================================
# 4. VARIABLE ARGUMENTS: `*args` and `**kwargs`
# =============================================================================

# This is a powerful feature for when you don't know how many arguments will be passed.

# --- `*args` (Arbitrary Positional Arguments) ---
# `*args` collects any number of positional arguments into a tuple.
def sum_all(*numbers: int) -> int:
    """Calculates the sum of an arbitrary number of integers."""
    print(f"Received numbers as a tuple: {numbers}")
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 10, 20, 30, 40, 50: {sum_all(10, 20, 30, 40, 50)}")

# --- `**kwargs` (Arbitrary Keyword Arguments) ---
# `**kwargs` collects any number of keyword arguments into a dictionary.
def display_user_profile(**details: str | int):
    """Displays user profile details from keyword arguments."""
    print("\n--- User Profile ---")
    for key, value in details.items():
        print(f"{key.title()}: {value}")

display_user_profile(name="Eve", age=28, city="New York")
display_user_profile(username="frank_dev", status="active")


# =============================================================================
# 5. DOCSTRINGS
# =============================================================================

"""
A docstring is a string literal that occurs as the first statement in a module,
function, class, or method definition. It is used to document what the code does.

- It's enclosed in triple quotes `"""..."""`.
- It becomes the `__doc__` attribute of the object.
- Tools like VS Code and help() use it to provide information about the function.
- A good docstring explains the function's purpose, arguments, and what it returns.
"""

def complex_function(param1: int, param2: str) -> bool:
    """
    Performs a complex operation.

    This docstring follows a common convention (Google style).

    Args:
        param1: The first parameter, representing a count.
        param2: The second parameter, a descriptive string.

    Returns:
        True if the operation was successful, False otherwise.
    """
    # ... function logic ...
    return True

# You can view the docstring using help()
help(complex_function)


# =============================================================================
# EXERCISES
# =============================================================================

# 1. Area Calculator:
#    - Write a function `calculate_rectangle_area(width: float, height: float) -> float`.
#    - It should take width and height as arguments and return the calculated area.
#    - Call it with some values and print the result.

# 2. Greeter with Default Message:
#    - Create a function `greet(name: str, message: str = "Welcome")`.
#    - It should print a formatted string like "{message}, {name}!".
#    - Call it once with just a name, and once with a name and a custom message.

# 3. Average Calculator with `*args`:
#    - Write a function `calculate_average(*numbers: float) -> float`.
#    - It should accept any number of numerical arguments.
#    - It should return their average. If no numbers are passed, it should return 0.0.

# 4. Build a Configuration Dictionary with `**kwargs`:
#    - Write a function `create_config(**settings) -> dict`.
#    - It should accept any number of keyword arguments and return them as a dictionary.
#    - Call it with settings like `theme="dark"`, `version=2`, `auto_save=True` and print the resulting dict.

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- Functions (`def`) are the building blocks of modular code.
- Parameters are placeholders; arguments are the actual values you pass in.
- `return` allows functions to produce output.
- `*args` and `**kwargs` provide flexibility for handling a variable number of arguments.
- Docstrings are essential for writing understandable and maintainable code.

Next up: Day 9 - Advanced function features and modern type annotations.
"""
