"""
Day 4: Collections I - Lists and Tuples
=========================================

Collections are data types used to store multiple items. Today we'll cover
the two most common sequence collections: lists and tuples.

Learning Objectives:
1.  Create and manipulate lists (mutable).
2.  Understand list indexing, slicing, and methods.
3.  Create and use tuples (immutable).
4.  Recognize the key differences and use cases for lists vs. tuples.
5.  Work with nested collections.
"""

# =============================================================================
# 1. LISTS - MUTABLE SEQUENCES
# =============================================================================

# A list is an ordered and changeable collection. It allows duplicate members.
# Created with square brackets `[]`.

# An empty list
empty_list: list = []

# A list of strings
languages: list[str] = ["Python", "Rust", "Go"]
print(f"Programming languages: {languages}")

# Lists can contain items of different types
mixed_list: list = ["Hello", 42, 3.14, True]
print(f"Mixed-type list: {mixed_list}")

# --- Accessing items (Indexing) ---
# Same 0-based indexing as strings
print(f"First language: {languages[0]}")
print(f"Last language: {languages[-1]}")

# --- Modifying a list (it's mutable!) ---
languages[1] = "JavaScript"  # Change the item at index 1
print(f"After modification: {languages}")

# --- List Methods ---
# Add an item to the end
languages.append("Rust")
print(f"After append: {languages}")

# Insert an item at a specific position
languages.insert(1, "TypeScript")
print(f"After insert: {languages}")

# Remove and return the last item
last_item = languages.pop()
print(f"Popped item: {last_item}, List is now: {languages}")

# Remove a specific item by value
languages.remove("JavaScript")
print(f"After removing 'JavaScript': {languages}")

# Sorting
numbers: list[int] = [5, 2, 8, 1, 9]
numbers.sort()  # Sorts the list in-place
print(f"Sorted numbers: {numbers}")
numbers.sort(reverse=True)  # Sort in descending order
print(f"Reverse sorted numbers: {numbers}")

# --- Slicing ---
# Works just like with strings, creating a *new* list (a shallow copy).
first_two_langs = languages[0:2]
print(f"First two languages: {first_two_langs}")


# =============================================================================
# 2. TUPLES - IMMUTABLE SEQUENCES
# =============================================================================

# A tuple is an ordered and UNCHANGEABLE collection. Allows duplicate members.
# Created with parentheses `()`.

# An empty tuple
empty_tuple: tuple = ()

# A tuple of coordinates
coordinates: tuple[int, int] = (10, 20)
print(f"Coordinates: {coordinates}")

# A tuple with one item needs a trailing comma to distinguish it from a grouping parenthesis.
single_item_tuple: tuple[str] = ("hello",)
not_a_tuple = ("hello") # This is just a string
print(f"This is a tuple: {type(single_item_tuple)}")
print(f"This is not: {type(not_a_tuple)}")

# --- Accessing items ---
# Same as lists
print(f"X coordinate: {coordinates[0]}")

# --- Immutability in action ---
try:
    coordinates[0] = 15  # This will raise a TypeError
except TypeError as e:
    print(f"\nError trying to change a tuple: {e}")

# You can't change a tuple, but you can create a new one from existing ones.
new_coordinates = coordinates + (30,)
print(f"New tuple created by concatenation: {new_coordinates}")


# =============================================================================
# 3. LISTS VS TUPLES - WHEN TO USE WHICH?
# =============================================================================

"""
Use a LIST when:
- You have a collection of items that may need to change (add, remove, update).
- The order matters and you might need to sort it.
- E.g., a list of users, a to-do list, a list of scores.

Use a TUPLE when:
- You have a collection of items that should NOT change.
- The data represents a single, coherent "thing" or record.
- You want a slight performance boost (tuples are slightly faster to create and access).
- You need a key in a dictionary (lists can't be dict keys because they are mutable).
- E.g., RGB color values (255, 99, 71), geographic coordinates, a function returning multiple fixed values.
"""

# Example: Function returning multiple values
def get_user_info() -> tuple[str, int]:
    return ("Alice", 30)  # Returning a tuple is common practice

user_name, user_age = get_user_info() # This is called "unpacking"
print(f"Unpacked values: Name={user_name}, Age={user_age}")


# =============================================================================
# 4. NESTED COLLECTIONS
# =============================================================================

# You can have lists of lists, lists of tuples, etc.
# This is how you represent 2D grids, matrices, or structured data.

tic_tac_toe_board: list[list[str]] = [
    ["X", "O", "X"],
    ["O", "X", ""],
    ["O", "", "O"],
]

# Accessing a nested item: board[row][column]
middle_square = tic_tac_toe_board[1][1]
print(f"\nTic-tac-toe middle square: {middle_square}")

# Change an item
tic_tac_toe_board[1][2] = "X"
print(f"Updated board: {tic_tac_toe_board}")


# =============================================================================
# EXERCISES
# =============================================================================

# 1. To-Do List Manager:
#    - Create an empty list called `todos`.
#    - Add three to-do items (strings) to it using `append()`.
#    - Print the list.
#    - Mark the second item as done by modifying it (e.g., add "[DONE]" to the string).
#    - Remove the first item from the list.
#    - Print the final list.

# 2. Immutable Records:
#    - You are storing book information as tuples: `(title, author, year)`.
#    - Create a list of these book tuples for at least two books.
#    - Try to change the year of the first book. What happens?
#    - Print the author of the second book.

# 3. Unpacking:
#    - A tuple is defined as `user = ("JohnDoe", "john.doe@email.com", 25)`.
#    - Use tuple unpacking to assign the values to three variables: `username`, `email`, and `age`.
#    - Print the variables.

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- **Lists** (`[]`) are ordered, **mutable** collections. Your go-to for dynamic sequences.
- **Tuples** (`()`) are ordered, **immutable** collections. Ideal for fixed data records.
- Indexing and slicing work similarly for both, but modification only works on lists.
- Unpacking is a powerful feature for assigning collection items to variables.

Next up: Day 5 - Collections Part II: Dictionaries and Sets.
"""
