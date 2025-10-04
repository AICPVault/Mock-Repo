"""
Day 10: Comprehensions
======================

Comprehensions are a concise and readable way to create lists, dictionaries,
and sets from other iterables. They are a hallmark of idiomatic ("Pythonic") code.

Learning Objectives:
1.  Write list comprehensions to replace simple `for` loops.
2.  Add conditional logic to list comprehensions.
3.  Create dictionary and set comprehensions.
4.  Understand nested comprehensions for more complex data structures.
"""

# =============================================================================
# 1. LIST COMPREHENSIONS
# =============================================================================

# --- The "Classic" Way (with a for loop) ---
# Let's say we want a list of the squares of numbers from 0 to 9.
squares_loop: list[int] = []
for i in range(10):
    squares_loop.append(i * i)

print(f"Squares with a for loop: {squares_loop}")

# --- The "Pythonic" Way (with a list comprehension) ---
# Syntax: `[expression for item in iterable]`
squares_comp: list[int] = [i * i for i in range(10)]

print(f"Squares with comprehension: {squares_comp}")
# It's more concise and often faster.


# =============================================================================
# 2. CONDITIONAL LOGIC IN LIST COMPREHENSIONS
# =============================================================================

# You can add an `if` condition to filter items from the iterable.
# Syntax: `[expression for item in iterable if condition]`

# Get the squares of only the even numbers from 0 to 9.
even_squares: list[int] = [i * i for i in range(10) if i % 2 == 0]
print(f"\nSquares of even numbers: {even_squares}")

# --- Using a conditional expression (ternary operator) ---
# This changes the *expression* part based on a condition.
# Syntax: `[value_if_true if condition else value_if_false for item in iterable]`

# Create a list labeling numbers as "even" or "odd".
labels: list[str] = ["even" if i % 2 == 0 else "odd" for i in range(10)]
print(f"Even/Odd labels: {labels}")


# =============================================================================
# 3. DICTIONARY AND SET COMPREHENSIONS
# =============================================================================

# The same concept can be applied to create dictionaries and sets.

# --- Dictionary Comprehension ---
# Syntax: `{key_expression: value_expression for item in iterable}`
# Create a dictionary mapping numbers to their squares.
square_dict: dict[int, int] = {i: i * i for i in range(5)}
print(f"\nDictionary of squares: {square_dict}")

# Can also be used to transform existing dictionaries.
user_data = {"name": "alice", "city": "london", "role": "engineer"}
capitalized_user_data: dict[str, str] = {
    k.upper(): v.title() for k, v in user_data.items()
}
print(f"Capitalized user data: {capitalized_user_data}")

# --- Set Comprehension ---
# Syntax: `{expression for item in iterable}`
# Useful for creating sets from iterables, automatically handling uniqueness.
numbers: list[int] = [1, 2, 2, 3, 4, 4, 5, 1]
unique_squares: set[int] = {n * n for n in numbers}
print(f"Set of unique squares: {unique_squares}")


# =============================================================================
# 4. NESTED COMPREHENSIONS
# =============================================================================

# You can nest comprehensions, but be careful with readability.
# They are great for flattening lists of lists.

matrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Flatten the matrix into a single list.
flattened_list: list[int] = [item for row in matrix for item in row]
print(f"\nFlattened matrix: {flattened_list}")

# The for loop equivalent for clarity:
# flattened_loop = []
# for row in matrix:
#     for item in row:
#         flattened_loop.append(item)


# =============================================================================
# EXERCISES
# =============================================================================

# 1. Word Lengths:
#    - You have a list of words: `words = ["hello", "world", "in", "python"]`.
#    - Use a list comprehension to create a new list containing the length of each word.
#    - Expected output: `[5, 5, 2, 6]`

# 2. Filter Long Words:
#    - Using the same `words` list, use a list comprehension to create a new list
#      that only contains words with 4 or more characters.
#    - Expected output: `['hello', 'world', 'python']`

# 3. Character Counter Dictionary:
#    - You have a string: `sentence = "comprehensions are cool"`.
#    - Use a dictionary comprehension to create a dictionary mapping each character
#      to its count in the sentence. (Hint: you can use the `.count()` string method).
#    - Note: a `collections.Counter` is the "professional" way to do this, but it's a
#      great exercise for comprehensions.

# 4. Find Common Numbers:
#    - You have two lists: `list_a = [1, 2, 3, 4]` and `list_b = [2, 3, 4, 5]`.
#    - Use a set comprehension to find the numbers that are present in both lists.
#    - Hint: `... for n in list_a if n in list_b`

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- Comprehensions provide a powerful and elegant syntax for creating collections from iterables.
- They are often more readable and performant than the equivalent `for` loop.
- The basic structure is `[expression for item in iterable if condition]`.
- This concept extends to dictionaries `{key: val ...}` and sets `{item ...}`.
- Use them to make your code more "Pythonic", but avoid overly complex nested
  comprehensions that might harm readability.

Next up: Day 11 - Lambda functions and built-in functional tools like map and filter.
"""
