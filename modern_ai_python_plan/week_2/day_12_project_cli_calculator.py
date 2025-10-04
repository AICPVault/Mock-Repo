"""
Day 11: Lambdas and Built-in Functions
=======================================

Today we'll learn about lambda functions, which are small, anonymous functions,
and how they are commonly used with Python's powerful built-in functions
like `map`, `filter`, and `sorted`.

Learning Objectives:
1.  Understand and create lambda functions.
2.  Use `map()` to apply a function to every item of an iterable.
3.  Use `filter()` to select items from an iterable based on a condition.
4.  Use `sorted()` with a custom key for advanced sorting.
5.  Understand the functional helpers `any()` and `all()`.
"""

# =============================================================================
# 1. LAMBDA FUNCTIONS
# =============================================================================

# A lambda function is a small, anonymous function defined with the `lambda` keyword.
# Syntax: `lambda arguments: expression`
# - They can have any number of arguments but only one expression.
# - The expression is evaluated and returned.
# - They are syntactically restricted and cannot contain statements like `if`, `for`, etc.

# --- Regular function definition ---
def add(x: int, y: int) -> int:
    return x + y

# --- Equivalent lambda function ---
add_lambda = lambda x, y: x + y

print(f"Result from regular function: {add(5, 3)}")
print(f"Result from lambda function: {add_lambda(5, 3)}")

# Lambdas are most useful when you need a small, one-off function for a short period,
# especially as an argument to a higher-order function (a function that takes another function).


# =============================================================================
# 2. `map()` - APPLYING A FUNCTION TO A SEQUENCE
# =============================================================================

# `map(function, iterable)` applies `function` to every item of `iterable` and returns a map object (an iterator).

numbers: list[int] = [1, 2, 3, 4, 5]

# Using a lambda with map to square each number
squared_numbers_iterator = map(lambda x: x * x, numbers)
squared_numbers_list: list[int] = list(squared_numbers_iterator) # Convert iterator to list
print(f"Squared numbers with map: {squared_numbers_list}")

# For simple cases like this, a list comprehension is often considered more "Pythonic" and readable.
squared_comp: list[int] = [x * x for x in numbers]
print(f"Squared numbers with comprehension: {squared_comp}")


# =============================================================================
# 3. `filter()` - SELECTING ITEMS FROM A SEQUENCE
# =============================================================================

# `filter(function, iterable)` constructs an iterator from elements of `iterable` for which `function` returns `True`.

# Using a lambda with filter to get only the even numbers
even_numbers_iterator = filter(lambda x: x % 2 == 0, numbers)
even_numbers_list: list[int] = list(even_numbers_iterator)
print(f"\nEven numbers with filter: {even_numbers_list}")

# Again, a list comprehension can achieve the same result and is often preferred.
even_comp: list[int] = [x for x in numbers if x % 2 == 0]
print(f"Even numbers with comprehension: {even_comp}")


# =============================================================================
# 4. `sorted()` - CUSTOM SORTING
# =============================================================================

# `sorted(iterable, key=function)` is where lambdas truly shine.
# The `key` parameter specifies a function to be called on each list element
# prior to making comparisons.

# Sort a list of strings by their length
words: list[str] = ["apple", "banana", "cherry", "date"]
sorted_by_length: list[str] = sorted(words, key=lambda word: len(word))
print(f"\nWords sorted by length: {sorted_by_length}")

# Sort a list of dictionaries by a specific key
users: list[dict] = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]
sorted_by_age: list[dict] = sorted(users, key=lambda user: user["age"])
print(f"Users sorted by age: {sorted_by_age}")


# =============================================================================
# 5. `any()` AND `all()`
# =============================================================================

# These are useful built-in functions for checking conditions across an iterable.

# `all(iterable)`: Returns `True` if all elements of the iterable are truthy.
# `any(iterable)`: Returns `True` if any element of the iterable is truthy.

bools_all_true: list[bool] = [True, True, True]
bools_mixed: list[bool] = [True, False, True]
bools_all_false: list[bool] = [False, False, False]

print(f"\nall(bools_all_true): {all(bools_all_true)}")   # True
print(f"all(bools_mixed): {all(bools_mixed)}")       # False

print(f"any(bools_mixed): {any(bools_mixed)}")       # True
print(f"any(bools_all_false): {any(bools_all_false)}") # False

# Practical example: Check if there are any negative numbers in a list.
nums = [10, 20, -5, 40]
has_negative = any(n < 0 for n in nums) # Using a generator expression (more memory efficient than a list comprehension)
print(f"Does the list have any negative numbers? {has_negative}")


# =============================================================================
# EXERCISES
# =============================================================================

# 1. Convert to Uppercase:
#    - You have a list of names: `names = ["alice", "bob", "charlie"]`.
#    - Use `map` and a `lambda` function to create a new list where all names are uppercase.

# 2. Filter by Grade:
#    - You have a list of student scores: `scores = [88, 92, 75, 64, 97]`.
#    - Use `filter` and a `lambda` to create a new list containing only the "A" grades (scores >= 90).

# 3. Sort by Last Character:
#    - You have a list of words: `words = ["banana", "pie", "apple", "fig"]`.
#    - Use `sorted` and a `lambda` to sort the list based on the last character of each word.

# 4. Check for Empty Strings:
#    - You have a list of strings: `data = ["info", "", "more info"]`.
#    - Use `any()` to check if there is at least one empty string in the list.
#    - Use `all()` to check if all strings in the list are non-empty.

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- Lambda functions (`lambda args: expr`) are for creating small, single-expression anonymous functions.
- They are most powerful when used as arguments to higher-order functions.
- `map()` and `filter()` are functional tools for applying operations to iterables, though
  comprehensions are often preferred for readability.
- `sorted(iterable, key=...)` is the perfect use case for lambdas to define custom sort orders.
- `any()` and `all()` are efficient for logical checks on entire iterables.

Next up: Day 12 - Project Day! We'll build a command-line calculator.
"""
