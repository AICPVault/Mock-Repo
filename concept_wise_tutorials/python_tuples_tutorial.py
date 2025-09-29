"""
COMPREHENSIVE GUIDE TO PYTHON TUPLES
====================================

This file covers everything you need to know about Python tuples:
- What are tuples
- How to create tuples
- Tuple methods and functions
- Practical examples
- Best practices
- Tuples vs Lists comparison
"""

print("=" * 80)
print("COMPREHENSIVE GUIDE TO PYTHON TUPLES")
print("=" * 80)

# =============================================================================
# 1. WHAT ARE TUPLES?
# =============================================================================

print("\n1. WHAT ARE TUPLES?")
print("-" * 50)
print("""
Tuples are ordered, immutable (unchangeable) collections of items.
- Ordered: Items have a defined order that won't change
- Immutable: You CANNOT change, add, or remove items after creation
- Allow duplicates: Can have items with the same value
- Indexed: Access items by their position (starting from 0)
- Heterogeneous: Can contain different data types
- Faster than lists: More memory efficient and faster access
- Hashable: Can be used as dictionary keys
""")

# =============================================================================
# 2. CREATING TUPLES
# =============================================================================

print("\n2. CREATING TUPLES")
print("-" * 50)

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Tuple with values
fruits = ("apple", "banana", "cherry")
print(f"Fruits tuple: {fruits}")

# Tuple with different data types
mixed_tuple = (1, "hello", 3.14, True, [1, 2, 3])
print(f"Mixed data types: {mixed_tuple}")

# Using tuple() constructor
numbers = tuple([1, 2, 3, 4, 5])
print(f"Using tuple() constructor: {numbers}")

# Tuple from range
range_tuple = tuple(range(1, 6))
print(f"Tuple from range: {range_tuple}")

# Single element tuple (note the comma!)
single = (42,)  # Comma is required!
print(f"Single element tuple: {single}")
print(f"Type: {type(single)}")

# Without comma (not a tuple!)
not_tuple = (42)
print(f"Without comma: {not_tuple}, Type: {type(not_tuple)}")

# Tuple unpacking
coordinates = (10, 20)
x, y = coordinates
print(f"Coordinates: {coordinates}, x={x}, y={y}")

# =============================================================================
# 3. ACCESSING TUPLE ELEMENTS
# =============================================================================

print("\n3. ACCESSING TUPLE ELEMENTS")
print("-" * 50)

colors = ("red", "green", "blue", "yellow", "purple")
print(f"Original tuple: {colors}")

# Access by index (positive indexing)
print(f"First element (index 0): {colors[0]}")
print(f"Second element (index 1): {colors[1]}")
print(f"Last element (index -1): {colors[-1]}")

# Negative indexing
print(f"Second to last (index -2): {colors[-2]}")

# Slicing
print(f"First 3 elements: {colors[0:3]}")
print(f"From index 2 to end: {colors[2:]}")
print(f"Last 3 elements: {colors[-3:]}")
print(f"Every second element: {colors[::2]}")

# =============================================================================
# 4. TUPLE METHODS - SEARCHING AND COUNTING
# =============================================================================

print("\n4. TUPLE METHODS - SEARCHING AND COUNTING")
print("-" * 50)

data = (1, 2, 3, 2, 4, 2, 5)
print(f"Data tuple: {data}")

# index() - Find index of first occurrence
try:
    index = data.index(2)
    print(f"Index of first 2: {index}")
except ValueError:
    print("Value not found")

# count() - Count occurrences
count = data.count(2)
print(f"Count of 2: {count}")

# in operator - Check if element exists
exists = 3 in data
print(f"Is 3 in data? {exists}")

# not in operator
not_exists = 10 not in data
print(f"Is 10 not in data? {not_exists}")

# =============================================================================
# 5. BUILT-IN FUNCTIONS WITH TUPLES
# =============================================================================

print("\n5. BUILT-IN FUNCTIONS WITH TUPLES")
print("-" * 50)

numbers = (1, 2, 3, 4, 5)
print(f"Numbers: {numbers}")

# len() - Get length
print(f"Length: {len(numbers)}")

# max() and min() - Maximum and minimum values
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

# sum() - Sum of all elements
print(f"Sum: {sum(numbers)}")

# any() and all() - Boolean checks
bool_tuple = (True, False, True)
print(f"Any true: {any(bool_tuple)}")
print(f"All true: {all(bool_tuple)}")

# enumerate() - Get index and value
print("Enumerate:")
for index, value in enumerate(numbers):
    print(f"  Index {index}: {value}")

# zip() - Combine multiple tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
print(f"Zip result: {tuple(zip(tuple1, tuple2))}")

# sorted() - Create sorted list from tuple
unsorted = (3, 1, 4, 1, 5)
sorted_list = sorted(unsorted)
print(f"Original: {unsorted}")
print(f"Sorted list: {sorted_list}")

# =============================================================================
# 6. TUPLE OPERATIONS
# =============================================================================

print("\n6. TUPLE OPERATIONS")
print("-" * 50)

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Concatenation: {combined}")

# Repetition
repeated = (1, 2) * 3
print(f"Repetition: {repeated}")

# Membership testing
test_tuple = (1, 2, 3, 4, 5)
print(f"Is 3 in tuple? {3 in test_tuple}")
print(f"Is 6 in tuple? {6 in test_tuple}")

# Comparison
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 3)
tuple_c = (1, 2, 4)
print(f"tuple_a == tuple_b: {tuple_a == tuple_b}")
print(f"tuple_a == tuple_c: {tuple_a == tuple_c}")

# =============================================================================
# 7. TUPLE UNPACKING
# =============================================================================

print("\n7. TUPLE UNPACKING")
print("-" * 50)

# Basic unpacking
point = (10, 20)
x, y = point
print(f"Point: {point}, x={x}, y={y}")

# Multiple assignment
name, age, city = ("Alice", 25, "New York")
print(f"Name: {name}, Age: {age}, City: {city}")

# Unpacking with * (Python 3+)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Swapping variables
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # Tuple unpacking for swapping
print(f"After swap: a={a}, b={b}")

# Function returning multiple values
def get_name_age():
    return ("Bob", 30)

name, age = get_name_age()
print(f"Function result: name={name}, age={age}")

# =============================================================================
# 8. NESTED TUPLES
# =============================================================================

print("\n8. NESTED TUPLES")
print("-" * 50)

# Creating nested tuples
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(f"2D Matrix: {matrix}")

# Accessing elements
print(f"Element at [1][2]: {matrix[1][2]}")
print(f"Second row: {matrix[1]}")

# Tuple of tuples
coordinates = ((0, 0), (1, 1), (2, 2))
print(f"Coordinates: {coordinates}")

# =============================================================================
# 9. PRACTICAL EXAMPLES
# =============================================================================

print("\n9. PRACTICAL EXAMPLES")
print("-" * 50)

# Example 1: RGB Color values
red_color = (255, 0, 0)
green_color = (0, 255, 0)
blue_color = (0, 0, 255)
print(f"Red: {red_color}, Green: {green_color}, Blue: {blue_color}")

# Example 2: Database records
student_record = ("Alice", 20, "Computer Science", 3.8)
name, age, major, gpa = student_record
print(f"Student: {name}, Age: {age}, Major: {major}, GPA: {gpa}")

# Example 3: Configuration settings
config = ("localhost", 8080, True, "UTF-8")
host, port, debug, encoding = config
print(f"Host: {host}, Port: {port}, Debug: {debug}, Encoding: {encoding}")

# Example 4: Function returning multiple values
def get_stats(numbers):
    return (min(numbers), max(numbers), sum(numbers) / len(numbers))

data = (10, 20, 30, 40, 50)
min_val, max_val, avg_val = get_stats(data)
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val:.2f}")

# Example 5: Coordinates and distances
point1 = (0, 0)
point2 = (3, 4)
print(f"Point 1: {point1}, Point 2: {point2}")

# =============================================================================
# 10. TUPLES AS DICTIONARY KEYS
# =============================================================================

print("\n10. TUPLES AS DICTIONARY KEYS")
print("-" * 50)

# Tuples can be used as dictionary keys (lists cannot!)
coordinates_dict = {
    (0, 0): "origin",
    (1, 0): "east",
    (0, 1): "north",
    (1, 1): "northeast"
}

print(f"Coordinate dictionary: {coordinates_dict}")
print(f"Value at (1, 1): {coordinates_dict[(1, 1)]}")

# Nested tuples as keys
grid_positions = {
    ((0, 0), (1, 1)): "diagonal",
    ((0, 1), (1, 0)): "cross"
}
print(f"Grid positions: {grid_positions}")

# =============================================================================
# 11. TUPLE COMPREHENSIONS (GENERATOR EXPRESSIONS)
# =============================================================================

print("\n11. TUPLE COMPREHENSIONS (GENERATOR EXPRESSIONS)")
print("-" * 50)

# Tuple comprehensions create generator objects
squares_gen = (x**2 for x in range(1, 6))
print(f"Generator object: {squares_gen}")
print(f"Convert to tuple: {tuple(squares_gen)}")

# With condition
even_squares = tuple(x**2 for x in range(1, 11) if x % 2 == 0)
print(f"Even squares: {even_squares}")

# String manipulation
words = ("hello", "world", "python")
upper_words = tuple(word.upper() for word in words)
print(f"Upper words: {upper_words}")

# =============================================================================
# 12. TUPLES VS LISTS COMPARISON
# =============================================================================

print("\n12. TUPLES VS LISTS COMPARISON")
print("-" * 50)

print("""
CHARACTERISTICS COMPARISON:
┌─────────────────┬─────────────┬─────────────┐
│ Characteristic  │    Tuple    │    List     │
├─────────────────┼─────────────┼─────────────┤
│ Mutability       │ Immutable   │ Mutable     │
│ Memory Usage    │ Less        │ More        │
│ Performance     │ Faster      │ Slower      │
│ Dictionary Keys │ Yes         │ No          │
│ Methods         │ Few (2)     │ Many (11+)  │
│ Syntax          │ () or ,     │ []          │
└─────────────────┴─────────────┴─────────────┘

WHEN TO USE TUPLES:
✓ When data shouldn't change (coordinates, settings)
✓ As dictionary keys
✓ Function return values
✓ When you need hashable objects
✓ For better performance with large data

WHEN TO USE LISTS:
✓ When you need to modify the collection
✓ When you need many methods (append, remove, etc.)
✓ For dynamic data that changes frequently
✓ When you need to sort in place
""")

# =============================================================================
# 13. CONVERTING BETWEEN TUPLES AND LISTS
# =============================================================================

print("\n13. CONVERTING BETWEEN TUPLES AND LISTS")
print("-" * 50)

# List to tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(f"List: {my_list}")
print(f"Converted to tuple: {my_tuple}")

# Tuple to list
my_tuple = (6, 7, 8, 9, 10)
my_list = list(my_tuple)
print(f"Tuple: {my_tuple}")
print(f"Converted to list: {my_list}")

# String to tuple
text = "hello"
char_tuple = tuple(text)
print(f"String: {text}")
print(f"Converted to tuple: {char_tuple}")

# =============================================================================
# 14. ADVANCED TUPLE FEATURES
# =============================================================================

print("\n14. ADVANCED TUPLE FEATURES")
print("-" * 50)

# Named tuples (from collections module)
from collections import namedtuple

# Create a named tuple
Person = namedtuple('Person', ['name', 'age', 'city'])
person1 = Person("Alice", 25, "New York")
print(f"Named tuple: {person1}")
print(f"Name: {person1.name}, Age: {person1.age}")

# Access by index or name
print(f"By index: {person1[0]}")
print(f"By name: {person1.name}")

# Multiple named tuples
people = [
    Person("Alice", 25, "New York"),
    Person("Bob", 30, "Boston"),
    Person("Charlie", 35, "Chicago")
]
print(f"People: {people}")

# =============================================================================
# 15. BEST PRACTICES AND TIPS
# =============================================================================

print("\n15. BEST PRACTICES AND TIPS")
print("-" * 50)

print("""
BEST PRACTICES:
1. Use tuples for immutable data (coordinates, settings)
2. Use tuples as dictionary keys
3. Use tuple unpacking for multiple assignments
4. Use tuples for function return values
5. Use named tuples for structured data
6. Remember the comma for single-element tuples
7. Use tuples when you need hashable objects

COMMON MISTAKES TO AVOID:
1. Forgetting the comma in single-element tuples
2. Trying to modify tuple elements (they're immutable!)
3. Using lists when tuples would be more appropriate
4. Not using tuple unpacking when possible
5. Confusing tuple() constructor with tuple literals

PERFORMANCE TIPS:
1. Tuples are faster than lists for iteration
2. Tuples use less memory than lists
3. Use tuples for large, unchanging datasets
4. Consider tuples for function parameters that won't change
""")

# =============================================================================
# 16. REAL-WORLD APPLICATIONS
# =============================================================================

print("\n16. REAL-WORLD APPLICATIONS")
print("-" * 50)

# Example 1: Database records
print("Database Records:")
records = [
    ("user1", "John", "Doe", "john@email.com"),
    ("user2", "Jane", "Smith", "jane@email.com"),
    ("user3", "Bob", "Johnson", "bob@email.com")
]

for user_id, first, last, email in records:
    print(f"  {user_id}: {first} {last} ({email})")

# Example 2: API responses
print("\nAPI Response Format:")
api_response = ("success", 200, {"data": "example"}, "application/json")
status, code, data, content_type = api_response
print(f"  Status: {status}, Code: {code}, Type: {content_type}")

# Example 3: Game coordinates
print("\nGame Coordinates:")
player_positions = {
    "player1": (100, 200),
    "player2": (150, 250),
    "player3": (200, 300)
}

for player, (x, y) in player_positions.items():
    print(f"  {player}: ({x}, {y})")

# Example 4: Configuration tuples
print("\nConfiguration Settings:")
settings = (
    ("database_host", "localhost"),
    ("database_port", 5432),
    ("debug_mode", True),
    ("max_connections", 100)
)

for key, value in settings:
    print(f"  {key}: {value}")

print("\n" + "=" * 80)
print("END OF PYTHON TUPLES TUTORIAL")
print("=" * 80)



