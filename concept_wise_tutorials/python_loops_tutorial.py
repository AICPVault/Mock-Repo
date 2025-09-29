"""
COMPREHENSIVE GUIDE TO PYTHON LOOPS
===================================

This file covers everything you need to know about Python loops:
- What are loops
- For loops and while loops
- Loop control statements (break, continue, pass)
- Nested loops
- Practical examples
- Best practices
"""

print("=" * 80)
print("COMPREHENSIVE GUIDE TO PYTHON LOOPS")
print("=" * 80)

# =============================================================================
# 1. WHAT ARE LOOPS?
# =============================================================================

print("\n1. WHAT ARE LOOPS?")
print("-" * 50)
print("""
Loops are control structures that allow you to execute a block of code repeatedly.
- Automate repetitive tasks
- Process collections of data
- Implement algorithms
- Create interactive programs

Types of loops in Python:
1. for loops - iterate over sequences
2. while loops - repeat while condition is true
3. Nested loops - loops inside other loops
""")

# =============================================================================
# 2. FOR LOOPS
# =============================================================================

print("\n2. FOR LOOPS")
print("-" * 50)

# Basic for loop with range()
print("Basic for loop with range():")
for i in range(5):
    print(f"  Iteration {i}")

# For loop with list
print("\nFor loop with list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  Fruit: {fruit}")

# For loop with string
print("\nFor loop with string:")
word = "Python"
for char in word:
    print(f"  Character: {char}")

# For loop with tuple
print("\nFor loop with tuple:")
coordinates = (10, 20, 30)
for coord in coordinates:
    print(f"  Coordinate: {coord}")

# =============================================================================
# 3. RANGE() FUNCTION
# =============================================================================

print("\n3. RANGE() FUNCTION")
print("-" * 50)

# range(stop)
print("range(5):")
for i in range(5):
    print(f"  {i}", end=" ")
print()

# range(start, stop)
print("\nrange(2, 7):")
for i in range(2, 7):
    print(f"  {i}", end=" ")
print()

# range(start, stop, step)
print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"  {i}", end=" ")
print()

# range with negative step
print("\nrange(10, 0, -1):")
for i in range(10, 0, -1):
    print(f"  {i}", end=" ")
print()

# =============================================================================
# 4. ENUMERATE() FUNCTION
# =============================================================================

print("\n4. ENUMERATE() FUNCTION")
print("-" * 50)

# Basic enumerate
colors = ["red", "green", "blue"]
print("Basic enumerate:")
for index, color in enumerate(colors):
    print(f"  Index {index}: {color}")

# Enumerate with start value
print("\nEnumerate with start=1:")
for index, color in enumerate(colors, start=1):
    print(f"  Position {index}: {color}")

# =============================================================================
# 5. ZIP() FUNCTION
# =============================================================================

print("\n5. ZIP() FUNCTION")
print("-" * 50)

# Basic zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
print("Basic zip:")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# Zip with different length lists
short_list = [1, 2]
long_list = [1, 2, 3, 4]
print("\nZip with different lengths:")
for a, b in zip(short_list, long_list):
    print(f"  {a}, {b}")

# =============================================================================
# 6. WHILE LOOPS
# =============================================================================

print("\n6. WHILE LOOPS")
print("-" * 50)

# Basic while loop
print("Basic while loop:")
count = 0
while count < 5:
    print(f"  Count: {count}")
    count += 1

# While loop with user input simulation
print("\nWhile loop with condition:")
number = 10
while number > 0:
    print(f"  Number: {number}")
    number -= 2

# =============================================================================
# 7. LOOP CONTROL STATEMENTS
# =============================================================================

print("\n7. LOOP CONTROL STATEMENTS")
print("-" * 50)

# break statement
print("break statement:")
for i in range(10):
    if i == 5:
        print(f"  Breaking at {i}")
        break
    print(f"  {i}", end=" ")
print()

# continue statement
print("\ncontinue statement:")
for i in range(5):
    if i == 2:
        print(f"  Skipping {i}")
        continue
    print(f"  {i}", end=" ")
print()

# pass statement
print("\npass statement:")
for i in range(3):
    if i == 1:
        pass  # Do nothing
    else:
        print(f"  {i}", end=" ")
print()

# =============================================================================
# 8. NESTED LOOPS
# =============================================================================

print("\n8. NESTED LOOPS")
print("-" * 50)

# Basic nested loops
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i * j}")

# Nested loops with different data types
print("\nNested loops with lists:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(f"  {element}", end=" ")
    print()

# =============================================================================
# 9. LIST COMPREHENSIONS (LOOP ALTERNATIVES)
# =============================================================================

print("\n9. LIST COMPREHENSIONS (LOOP ALTERNATIVES)")
print("-" * 50)

# Basic list comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# List comprehension with condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Dictionary comprehension
square_dict = {x: x**2 for x in range(1, 6)}
print(f"Square dictionary: {square_dict}")

# =============================================================================
# 10. PRACTICAL EXAMPLES
# =============================================================================

print("\n10. PRACTICAL EXAMPLES")
print("-" * 50)

# Example 1: Number guessing game simulation
print("Number guessing game simulation:")
import random
secret_number = random.randint(1, 10)
guesses = 0
max_guesses = 3

while guesses < max_guesses:
    guess = random.randint(1, 10)  # Simulated guess
    guesses += 1
    if guess == secret_number:
        print(f"  Correct! Secret number was {secret_number}")
        break
    else:
        print(f"  Guess {guesses}: {guess} (Wrong)")
else:
    print(f"  Game over! Secret number was {secret_number}")

# Example 2: Data processing
print("\nData processing example:")
temperatures = [22.5, 23.1, 21.8, 24.3, 22.9, 23.7]
print(f"Temperatures: {temperatures}")

# Find average
total = 0
for temp in temperatures:
    total += temp
average = total / len(temperatures)
print(f"Average temperature: {average:.2f}°C")

# Count days above average
above_average = 0
for temp in temperatures:
    if temp > average:
        above_average += 1
print(f"Days above average: {above_average}")

# Example 3: Text processing
print("\nText processing example:")
text = "Hello World Python Programming"
words = text.split()
print(f"Text: {text}")
print(f"Words: {words}")

# Count word lengths
word_lengths = []
for word in words:
    word_lengths.append(len(word))
print(f"Word lengths: {word_lengths}")

# Find longest word
longest_word = ""
max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word
print(f"Longest word: '{longest_word}' ({max_length} characters)")

# =============================================================================
# 11. ADVANCED LOOP PATTERNS
# =============================================================================

print("\n11. ADVANCED LOOP PATTERNS")
print("-" * 50)

# Pattern 1: Accumulator pattern
print("Accumulator pattern:")
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum of {numbers}: {total}")

# Pattern 2: Search pattern
print("\nSearch pattern:")
target = 4
found = False
for num in numbers:
    if num == target:
        found = True
        break
print(f"Target {target} found: {found}")

# Pattern 3: Filter pattern
print("\nFilter pattern:")
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers: {even_numbers}")

# Pattern 4: Transformation pattern
print("\nTransformation pattern:")
doubled_numbers = []
for num in numbers:
    doubled_numbers.append(num * 2)
print(f"Doubled numbers: {doubled_numbers}")

# =============================================================================
# 12. LOOPING WITH DICTIONARIES
# =============================================================================

print("\n12. LOOPING WITH DICTIONARIES")
print("-" * 50)

student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 96
}

# Loop through keys
print("Loop through keys:")
for student in student_grades:
    print(f"  Student: {student}")

# Loop through values
print("\nLoop through values:")
for grade in student_grades.values():
    print(f"  Grade: {grade}")

# Loop through items (key-value pairs)
print("\nLoop through items:")
for student, grade in student_grades.items():
    print(f"  {student}: {grade}")

# =============================================================================
# 13. LOOPING WITH FILES
# =============================================================================

print("\n13. LOOPING WITH FILES")
print("-" * 50)

# Simulate file reading
file_content = ["Line 1: Hello", "Line 2: World", "Line 3: Python"]
print("Simulated file reading:")
for line_num, line in enumerate(file_content, 1):
    print(f"  Line {line_num}: {line}")

# =============================================================================
# 14. ERROR HANDLING IN LOOPS
# =============================================================================

print("\n14. ERROR HANDLING IN LOOPS")
print("-" * 50)

# Try-except in loops
data = [1, 2, "three", 4, "five", 6]
print("Error handling in loops:")
for item in data:
    try:
        result = item * 2
        print(f"  {item} * 2 = {result}")
    except TypeError:
        print(f"  Cannot multiply '{item}' by 2")

# =============================================================================
# 15. PERFORMANCE CONSIDERATIONS
# =============================================================================

print("\n15. PERFORMANCE CONSIDERATIONS")
print("-" * 50)

print("""
PERFORMANCE TIPS:
1. Use list comprehensions for simple transformations
2. Avoid unnecessary nested loops
3. Use enumerate() instead of range(len())
4. Use zip() for parallel iteration
5. Consider using built-in functions (sum, max, min)
6. Use generators for large datasets
7. Break early when possible

COMMON MISTAKES:
1. Modifying list while iterating
2. Infinite while loops
3. Not updating loop variables
4. Using loops when built-in functions would work
5. Not handling exceptions in loops
""")

# =============================================================================
# 16. REAL-WORLD APPLICATIONS
# =============================================================================

print("\n16. REAL-WORLD APPLICATIONS")
print("-" * 50)

# Example 1: Data analysis
print("Data analysis example:")
sales_data = [100, 150, 200, 175, 300, 250, 180]
print(f"Sales data: {sales_data}")

# Calculate statistics
total_sales = sum(sales_data)
average_sales = total_sales / len(sales_data)
print(f"Total sales: ${total_sales}")
print(f"Average sales: ${average_sales:.2f}")

# Find best and worst days
best_day = max(sales_data)
worst_day = min(sales_data)
print(f"Best day: ${best_day}")
print(f"Worst day: ${worst_day}")

# Example 2: Menu system simulation
print("\nMenu system simulation:")
menu_items = ["1. View Profile", "2. Edit Settings", "3. Logout"]
print("Menu:")
for item in menu_items:
    print(f"  {item}")

# Example 3: Game loop simulation
print("\nGame loop simulation:")
player_health = 100
enemies = ["Goblin", "Orc", "Dragon"]
print(f"Player health: {player_health}")

for enemy in enemies:
    damage = random.randint(10, 30)
    player_health -= damage
    print(f"  Fought {enemy}, took {damage} damage, health: {player_health}")
    if player_health <= 0:
        print("  Game Over!")
        break
else:
    print("  Victory! All enemies defeated!")

# =============================================================================
# 17. LOOP BEST PRACTICES
# =============================================================================

print("\n17. LOOP BEST PRACTICES")
print("-" * 50)

print("""
BEST PRACTICES:
1. Use descriptive variable names
2. Keep loops simple and focused
3. Use appropriate loop type (for vs while)
4. Handle edge cases and errors
5. Use break and continue judiciously
6. Consider readability over cleverness
7. Test with different data sizes
8. Document complex loop logic

COMMON PATTERNS:
1. Accumulator: sum, count, product
2. Search: find, contains, exists
3. Filter: select, remove, keep
4. Transform: map, convert, modify
5. Validation: check, verify, test
""")

print("\n" + "=" * 80)
print("END OF PYTHON LOOPS TUTORIAL")
print("=" * 80)


