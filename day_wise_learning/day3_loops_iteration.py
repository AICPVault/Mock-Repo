"""
Day 3: Loops and Iteration
=========================

Today we'll learn about loops - one of the most powerful concepts in programming.
Loops allow us to repeat code multiple times, making our programs more efficient
and capable of handling repetitive tasks.

Learning Objectives:
- Understand the concept of loops and iteration
- Master for loops and while loops
- Learn about loop control (break, continue, pass)
- Practice nested loops
- Build programs that can handle repetitive tasks
- Understand when to use each type of loop

Let's dive into the world of loops!
"""

print("🐍 Welcome to Day 3: Loops and Iteration!")
print("=" * 50)

# =============================================================================
# 1. WHAT ARE LOOPS?
# =============================================================================

print("\n🔄 WHAT ARE LOOPS?")
print("-" * 20)

"""
Loops are programming constructs that allow us to:
- Repeat code multiple times
- Process collections of data
- Automate repetitive tasks
- Make programs more efficient
- Handle dynamic data processing

Types of loops in Python:
- for loops: iterate over sequences
- while loops: repeat while condition is true
"""

# =============================================================================
# 2. FOR LOOPS
# =============================================================================

print("\n🔄 FOR LOOPS")
print("-" * 15)

# Basic for loop with range()
print("Basic for loop with range():")
for i in range(5):
    print(f"  Iteration {i}")

# For loop with range(start, stop, step)
print("\nFor loop with range(1, 10, 2):")
for i in range(1, 10, 2):
    print(f"  Odd number: {i}")

# For loop with strings
print("\nFor loop with string:")
word = "Python"
for letter in word:
    print(f"  Letter: {letter}")

# For loop with lists
print("\nFor loop with list:")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"  Fruit: {fruit}")

# For loop with enumerate() - get both index and value
print("\nFor loop with enumerate():")
for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

# =============================================================================
# 3. WHILE LOOPS
# =============================================================================

print("\n🔄 WHILE LOOPS")
print("-" * 16)

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

# While loop with break
print("\nWhile loop with break:")
count = 0
while True:  # Infinite loop
    count += 1
    print(f"  Count: {count}")
    if count >= 3:
        break  # Exit the loop

# =============================================================================
# 4. LOOP CONTROL STATEMENTS
# =============================================================================

print("\n🎛️ LOOP CONTROL STATEMENTS")
print("-" * 30)

# break - exit the loop completely
print("Break statement:")
for i in range(10):
    if i == 5:
        print(f"  Breaking at {i}")
        break
    print(f"  i = {i}")

# continue - skip current iteration
print("\nContinue statement:")
for i in range(5):
    if i == 2:
        print(f"  Skipping {i}")
        continue
    print(f"  i = {i}")

# pass - do nothing (placeholder)
print("\nPass statement:")
for i in range(3):
    if i == 1:
        pass  # Do nothing
    else:
        print(f"  i = {i}")

# =============================================================================
# 5. NESTED LOOPS
# =============================================================================

print("\n🔄 NESTED LOOPS")
print("-" * 18)

# Nested for loops
print("Nested for loops - multiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"  {i} x {j} = {result}")

# Nested loops with different data types
print("\nNested loops with lists:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(f"  Element: {element}")

# =============================================================================
# 6. PRACTICAL EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL EXAMPLES")
print("-" * 22)

# Example 1: Number Guessing Game
def number_guessing_game():
    """Simulate a number guessing game."""
    import random
    
    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 3
    
    print(f"Number Guessing Game:")
    print(f"Guess a number between 1 and 10 (max {max_attempts} attempts)")
    
    # Simulate guesses
    guesses = [3, 7, 5]  # Simulated user guesses
    
    for guess in guesses:
        attempts += 1
        print(f"  Attempt {attempts}: Guessing {guess}")
        
        if guess == secret_number:
            print(f"  🎉 Correct! The number was {secret_number}")
            break
        elif guess < secret_number:
            print(f"  Too low!")
        else:
            print(f"  Too high!")
        
        if attempts >= max_attempts:
            print(f"  Game over! The number was {secret_number}")

number_guessing_game()

# Example 2: Shopping Cart Total
def shopping_cart_total():
    """Calculate total for shopping cart."""
    items = [
        {"name": "Apple", "price": 1.50, "quantity": 3},
        {"name": "Banana", "price": 0.75, "quantity": 5},
        {"name": "Orange", "price": 2.00, "quantity": 2}
    ]
    
    print(f"\nShopping Cart:")
    total = 0
    
    for item in items:
        item_total = item["price"] * item["quantity"]
        total += item_total
        print(f"  {item['name']}: ${item['price']} x {item['quantity']} = ${item_total:.2f}")
    
    print(f"  Total: ${total:.2f}")

shopping_cart_total()

# Example 3: Student Grade Analysis
def student_grade_analysis():
    """Analyze student grades."""
    students = [
        {"name": "Alice", "grades": [85, 90, 78, 92]},
        {"name": "Bob", "grades": [76, 82, 88, 85]},
        {"name": "Charlie", "grades": [92, 95, 89, 91]}
    ]
    
    print(f"\nStudent Grade Analysis:")
    
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = sum(grades) / len(grades)
        
        print(f"  {name}:")
        print(f"    Grades: {grades}")
        print(f"    Average: {average:.1f}")
        
        if average >= 90:
            print(f"    Status: Excellent!")
        elif average >= 80:
            print(f"    Status: Good!")
        elif average >= 70:
            print(f"    Status: Satisfactory!")
        else:
            print(f"    Status: Needs improvement!")

student_grade_analysis()

# Example 4: Pattern Printing
def pattern_printing():
    """Print various patterns using loops."""
    print(f"\nPattern Printing:")
    
    # Triangle pattern
    print("  Triangle:")
    for i in range(1, 6):
        print("  " + "*" * i)
    
    # Number pattern
    print("\n  Number pattern:")
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(f"  {j}", end="")
        print()
    
    # Diamond pattern
    print("\n  Diamond:")
    size = 3
    for i in range(size):
        print("  " + " " * (size - i - 1) + "*" * (2 * i + 1))
    for i in range(size - 2, -1, -1):
        print("  " + " " * (size - i - 1) + "*" * (2 * i + 1))

pattern_printing()

# =============================================================================
# 7. LOOP BEST PRACTICES
# =============================================================================

print("\n💡 LOOP BEST PRACTICES")
print("-" * 25)

print("""
Best practices for writing loops:

1. Use for loops when you know the number of iterations
2. Use while loops when you need to repeat until a condition is met
3. Always ensure your while loop has a way to terminate
4. Use meaningful variable names for loop counters
5. Avoid infinite loops unless absolutely necessary
6. Use break and continue judiciously
7. Consider using enumerate() when you need both index and value
8. Use list comprehensions for simple transformations (Day 5)
9. Keep loop bodies simple and readable
10. Test your loops with edge cases (empty lists, zero iterations)
""")

# =============================================================================
# 8. COMMON LOOP PATTERNS
# =============================================================================

print("\n🔄 COMMON LOOP PATTERNS")
print("-" * 25)

# Pattern 1: Accumulator
print("Pattern 1: Accumulator (summing values)")
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"  Sum of {numbers}: {total}")

# Pattern 2: Counter
print("\nPattern 2: Counter (counting occurrences)")
text = "hello world"
vowel_count = 0
vowels = "aeiou"
for char in text:
    if char.lower() in vowels:
        vowel_count += 1
print(f"  Vowels in '{text}': {vowel_count}")

# Pattern 3: Search
print("\nPattern 3: Search (finding items)")
fruits = ["apple", "banana", "orange", "grape"]
target = "banana"
found = False
for fruit in fruits:
    if fruit == target:
        found = True
        break
print(f"  Found '{target}': {found}")

# Pattern 4: Filter
print("\nPattern 4: Filter (collecting items)")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"  Even numbers: {even_numbers}")

# =============================================================================
# 9. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice what you've learned:

Exercise 1: Create a multiplication table
- Ask for a number
- Print its multiplication table from 1 to 10

Exercise 2: Build a simple calculator with loop
- Keep asking for numbers and operations
- Continue until user types 'quit'
- Display running total

Exercise 3: Create a password generator
- Ask for password length
- Generate random password with letters and numbers
- Display the password

Exercise 4: Build a number guessing game
- Generate random number
- Let user guess with hints
- Count attempts and display result

Exercise 5: Create a text analyzer
- Ask for a sentence
- Count words, characters, vowels
- Display statistics

Exercise 6: Build a simple menu system
- Display menu options
- Keep asking for choice until 'exit'
- Perform different actions based on choice
""")

# =============================================================================
# 10. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common loop mistakes and how to avoid them:

1. Infinite loops
   ❌ while True:  # No exit condition
   ✅ while condition:  # Always have an exit condition

2. Off-by-one errors
   ❌ for i in range(1, 5):  # Might miss the last element
   ✅ for i in range(1, 6):  # Check your range carefully

3. Modifying list while iterating
   ❌ for item in my_list:
         my_list.remove(item)  # Dangerous!
   ✅ for item in my_list.copy():  # Use a copy

4. Not initializing variables
   ❌ for i in range(5):
         total += i  # total not initialized
   ✅ total = 0
       for i in range(5):
           total += i

5. Using break/continue incorrectly
   ❌ if condition:
         break  # break only works in loops
   ✅ for item in items:
         if condition:
             break
""")

# =============================================================================
# 11. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ For loops iterate over sequences
✅ While loops repeat while condition is true
✅ Break exits loops, continue skips iterations
✅ Nested loops handle complex data structures
✅ Loops make programs more efficient
✅ Common patterns: accumulator, counter, search, filter
✅ Best practices for writing clean loops
✅ How to avoid common loop mistakes

Next Steps:
- Day 4: Functions and Scope
- Day 5: Data Structures (Lists, Tuples, Sets, Dictionaries)
""")

# =============================================================================
# 12. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 3 of your Python journey!

You now understand:
- How to use for and while loops effectively
- How to control loop execution with break and continue
- How to work with nested loops
- Common loop patterns and best practices
- How to avoid common loop mistakes

Loops are fundamental to programming!
Practice with the exercises to master this concept.

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 3: Loops and Iteration Tutorial")
    print("Run this file to see all examples in action!")
