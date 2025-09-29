"""
COMPREHENSIVE GUIDE TO PYTHON LISTS
====================================

This file covers everything you need to know about Python lists:
- What are lists
- How to create lists
- List methods and functions
- Practical examples
- Best practices
"""

print("=" * 80)
print("COMPREHENSIVE GUIDE TO PYTHON LISTS")
print("=" * 80)

# =============================================================================
# 1. WHAT ARE LISTS?
# =============================================================================

print("\n1. WHAT ARE LISTS?")
print("-" * 50)
print("""
Lists are ordered, mutable (changeable) collections of items.
- Ordered: Items have a defined order that won't change
- Mutable: You can change, add, and remove items after creation
- Allow duplicates: Can have items with the same value
- Indexed: Access items by their position (starting from 0)
- Heterogeneous: Can contain different data types
""")

# =============================================================================
# 2. CREATING LISTS
# =============================================================================

print("\n2. CREATING LISTS")
print("-" * 50)

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with values
fruits = ["apple", "banana", "cherry"]
print(f"Fruits list: {fruits}")

# List with different data types
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
print(f"Mixed data types: {mixed_list}")

# Using list() constructor
numbers = list([1, 2, 3, 4, 5])
print(f"Using list() constructor: {numbers}")

# List from range
range_list = list(range(1, 6))
print(f"List from range: {range_list}")

# List comprehension (advanced)
squares = [x**2 for x in range(1, 6)]
print(f"List comprehension (squares): {squares}")

# =============================================================================
# 3. ACCESSING LIST ELEMENTS
# =============================================================================

print("\n3. ACCESSING LIST ELEMENTS")
print("-" * 50)

colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Original list: {colors}")

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
# 4. LIST METHODS - ADDING ELEMENTS
# =============================================================================

print("\n4. LIST METHODS - ADDING ELEMENTS")
print("-" * 50)

# append() - Add single element to end
numbers = [1, 2, 3]
print(f"Before append: {numbers}")
numbers.append(4)
print(f"After append(4): {numbers}")

# extend() - Add multiple elements
numbers.extend([5, 6, 7])
print(f"After extend([5, 6, 7]): {numbers}")

# insert() - Add element at specific position
numbers.insert(0, 0)
print(f"After insert(0, 0): {numbers}")

# + operator (creates new list)
new_numbers = numbers + [8, 9]
print(f"Using + operator: {new_numbers}")

# =============================================================================
# 5. LIST METHODS - REMOVING ELEMENTS
# =============================================================================

print("\n5. LIST METHODS - REMOVING ELEMENTS")
print("-" * 50)

items = ["apple", "banana", "cherry", "apple", "date"]
print(f"Original list: {items}")

# remove() - Remove first occurrence of value
items.remove("apple")
print(f"After remove('apple'): {items}")

# pop() - Remove and return element at index
popped = items.pop(1)
print(f"After pop(1): {items}, popped: {popped}")

# pop() without index - Remove and return last element
last = items.pop()
print(f"After pop(): {items}, popped: {last}")

# del statement - Remove element by index
del items[0]
print(f"After del items[0]: {items}")

# clear() - Remove all elements
items.clear()
print(f"After clear(): {items}")

# =============================================================================
# 6. LIST METHODS - SEARCHING AND COUNTING
# =============================================================================

print("\n6. LIST METHODS - SEARCHING AND COUNTING")
print("-" * 50)

data = [1, 2, 3, 2, 4, 2, 5]
print(f"Data list: {data}")

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
# 7. LIST METHODS - SORTING AND REVERSING
# =============================================================================

print("\n7. LIST METHODS - SORTING AND REVERSING")
print("-" * 50)

# sort() - Sort in place
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")
numbers.sort()
print(f"After sort(): {numbers}")

# sort() with reverse=True
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# reverse() - Reverse the list
numbers.reverse()
print(f"After reverse(): {numbers}")

# sorted() function (creates new list)
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(f"Original: {original}")
print(f"Sorted copy: {sorted_list}")

# =============================================================================
# 8. LIST METHODS - COPYING
# =============================================================================

print("\n8. LIST METHODS - COPYING")
print("-" * 50)

original = [1, 2, 3, 4, 5]
print(f"Original: {original}")

# Shallow copy methods
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

print(f"copy(): {copy1}")
print(f"Slice [:]: {copy2}")
print(f"list(): {copy3}")

# Modifying copy doesn't affect original
copy1.append(6)
print(f"After modifying copy: original={original}, copy={copy1}")

# =============================================================================
# 9. BUILT-IN FUNCTIONS WITH LISTS
# =============================================================================

print("\n9. BUILT-IN FUNCTIONS WITH LISTS")
print("-" * 50)

numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# len() - Get length
print(f"Length: {len(numbers)}")

# max() and min() - Maximum and minimum values
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

# sum() - Sum of all elements
print(f"Sum: {sum(numbers)}")

# any() and all() - Boolean checks
bool_list = [True, False, True]
print(f"Any true: {any(bool_list)}")
print(f"All true: {all(bool_list)}")

# enumerate() - Get index and value
print("Enumerate:")
for index, value in enumerate(numbers):
    print(f"  Index {index}: {value}")

# zip() - Combine multiple lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(f"Zip result: {list(zip(list1, list2))}")

# =============================================================================
# 10. LIST COMPREHENSIONS
# =============================================================================

print("\n10. LIST COMPREHENSIONS")
print("-" * 50)

# Basic list comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# String manipulation
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Upper words: {upper_words}")

# =============================================================================
# 11. PRACTICAL EXAMPLES
# =============================================================================

print("\n11. PRACTICAL EXAMPLES")
print("-" * 50)

# Example 1: Student grades
grades = [85, 92, 78, 96, 88, 91]
print(f"Grades: {grades}")
print(f"Average grade: {sum(grades) / len(grades):.2f}")
print(f"Highest grade: {max(grades)}")
print(f"Lowest grade: {min(grades)}")

# Example 2: Shopping list
shopping_list = ["milk", "bread", "eggs", "butter"]
print(f"Shopping list: {shopping_list}")

# Add items
shopping_list.append("cheese")
shopping_list.insert(1, "apples")
print(f"Updated list: {shopping_list}")

# Remove item
shopping_list.remove("bread")
print(f"After removing bread: {shopping_list}")

# Example 3: Data processing
temperatures = [22.5, 23.1, 21.8, 24.3, 22.9, 23.7]
print(f"Temperatures: {temperatures}")

# Filter temperatures above 23
hot_days = [temp for temp in temperatures if temp > 23]
print(f"Hot days (>23°C): {hot_days}")

# Convert to Fahrenheit
fahrenheit = [(temp * 9/5) + 32 for temp in temperatures]
print(f"Fahrenheit: {fahrenheit}")

# Example 4: Matrix operations
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
print(f"Matrix A: {matrix_a}")
print(f"Matrix B: {matrix_b}")

# =============================================================================
# 12. COMMON LIST OPERATIONS
# =============================================================================

print("\n12. COMMON LIST OPERATIONS")
print("-" * 50)

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"Concatenation: {combined}")

# Repetition
repeated = [1, 2] * 3
print(f"Repetition: {repeated}")

# Membership testing
test_list = [1, 2, 3, 4, 5]
print(f"Is 3 in list? {3 in test_list}")
print(f"Is 6 in list? {6 in test_list}")

# Comparison
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = [1, 2, 4]
print(f"list_a == list_b: {list_a == list_b}")
print(f"list_a == list_c: {list_a == list_c}")

# =============================================================================
# 13. NESTED LISTS (2D LISTS)
# =============================================================================

print("\n13. NESTED LISTS (2D LISTS)")
print("-" * 50)

# Creating a 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"2D Matrix: {matrix}")

# Accessing elements
print(f"Element at [1][2]: {matrix[1][2]}")
print(f"Second row: {matrix[1]}")

# Modifying elements
matrix[0][0] = 10
print(f"After modification: {matrix}")

# Adding rows
matrix.append([10, 11, 12])
print(f"After adding row: {matrix}")

# =============================================================================
# 14. BEST PRACTICES AND TIPS
# =============================================================================

print("\n14. BEST PRACTICES AND TIPS")
print("-" * 50)

print("""
BEST PRACTICES:
1. Use list comprehensions for simple transformations
2. Use .append() for single items, .extend() for multiple
3. Use .copy() or [:] for shallow copies
4. Use 'in' operator for membership testing
5. Use enumerate() when you need both index and value
6. Use zip() to combine multiple lists
7. Use sorted() when you need a sorted copy
8. Use .sort() when you want to sort in place

COMMON MISTAKES TO AVOID:
1. Don't use '==' to compare with None, use 'is'
2. Don't modify a list while iterating over it
3. Don't use list() constructor unnecessarily
4. Remember that some methods modify the original list
5. Be careful with mutable default arguments
""")

# =============================================================================
# 15. PERFORMANCE CONSIDERATIONS
# =============================================================================

print("\n15. PERFORMANCE CONSIDERATIONS")
print("-" * 50)

print("""
TIME COMPLEXITY:
- Access by index: O(1)
- Search by value: O(n)
- Append: O(1) amortized
- Insert at beginning: O(n)
- Remove by value: O(n)
- Remove by index: O(n)

SPACE COMPLEXITY:
- Lists use more memory than tuples
- Each element has overhead
- Consider using arrays for large numeric data
""")

print("\n" + "=" * 80)
print("END OF PYTHON LISTS TUTORIAL")
print("=" * 80)

