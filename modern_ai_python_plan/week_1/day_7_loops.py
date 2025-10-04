"""
Day 7: Loops
============

Loops are used to execute a block of code repeatedly. Python offers
`for` loops for iterating over sequences and `while` loops for repeating
based on a condition.

Learning Objectives:
1.  Use `for` loops to iterate over lists, strings, and other iterables.
2.  Use the `range()` function to generate sequences of numbers.
3.  Combine `for` loops with `enumerate()` and `zip()` for more powerful iteration.
4.  Use `while` loops for conditions of unknown duration.
5.  Control loop execution with `break` and `continue`.
"""

# =============================================================================
# 1. THE `for` LOOP - ITERATING OVER SEQUENCES
# =============================================================================

# A `for` loop executes a block of code for each item in a sequence (like a list, tuple, or string).

# --- Looping over a list ---
fruits: list[str] = ["apple", "banana", "cherry"]
print("--- Looping over a list ---")
for fruit in fruits:
    print(f"Current fruit: {fruit}")

# --- Looping over a string ---
print("\n--- Looping over a string ---")
for char in "Python":
    print(char, end=" ") # `end=" "` prints a space instead of a newline
print()

# --- The `range()` function ---
# `range()` generates a sequence of numbers, which is very useful for looping a specific number of times.
# `range(stop)`: Goes from 0 up to (but not including) `stop`.
print("\n--- Looping with range(5) ---")
for i in range(5):
    print(f"Iteration {i}")

# `range(start, stop, step)`
print("\n--- Looping with range(2, 10, 2) ---")
for i in range(2, 10, 2):
    print(f"Even number: {i}")


# =============================================================================
# 2. ENHANCING `for` LOOPS WITH `enumerate` AND `zip`
# =============================================================================

# --- `enumerate()` - Getting both index and value ---
# When you need the index of the item you're looping over.
print("\n--- Looping with enumerate ---")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# --- `zip()` - Looping over multiple sequences at once ---
# `zip` pairs up elements from two or more iterables. It stops when the shortest iterable is exhausted.
print("\n--- Looping with zip ---")
students: list[str] = ["Alice", "Bob", "Charlie"]
scores: list[int] = [95, 88, 92]

for student, score in zip(students, scores):
    print(f"{student} scored {score}")


# =============================================================================
# 3. THE `while` LOOP - LOOPING BASED ON A CONDITION
# =============================================================================

# A `while` loop executes a block of code as long as a condition is `True`.
# It's useful when you don't know in advance how many times you need to loop.

print("\n--- A simple while loop ---")
count: int = 0
while count < 5:
    print(f"Count is {count}")
    count += 1  # IMPORTANT: You must change the condition variable inside the loop, or you'll get an infinite loop!

print("While loop finished.")


# =============================================================================
# 4. CONTROLLING LOOPS WITH `break` AND `continue`
# =============================================================================

# --- `break` - Exiting a loop early ---
# The `break` statement immediately terminates the loop.
print("\n--- Loop with break ---")
for number in range(10):
    if number == 5:
        print("Found the number 5! Breaking the loop.")
        break  # Exit the loop now
    print(f"Checking number {number}")

# --- `continue` - Skipping the current iteration ---
# The `continue` statement skips the rest of the code inside the loop for the current iteration
# and proceeds to the next one.
print("\n--- Loop with continue ---")
for number in range(10):
    if number % 2 == 0:  # If the number is even...
        continue  # ...skip the print statement and go to the next number
    print(f"Found an odd number: {number}")


# =============================================================================
# EXERCISES
# =============================================================================

# 1. Sum of Evens:
#    - Use a `for` loop with `range()` to iterate from 1 to 100.
#    - Calculate the sum of all the even numbers in that range and print the result.
#    - Hint: Use the modulus operator `%` to check for evenness.

# 2. User Input Validator:
#    - Write a `while` loop that asks the user to enter a password.
#    - The loop should continue asking until the user enters "python123".
#    - Once they enter the correct password, print "Access granted" and exit the loop.

# 3. Find First Admin:
#    - You have a list of user roles: `roles = ["viewer", "editor", "viewer", "admin", "editor"]`.
#    - Use a `for` loop to iterate through the list.
#    - The first time you encounter the "admin", print "Admin found!" and use `break` to stop searching.

# 4. Process Orders with `zip`:
#    - You have two lists:
#      `order_ids = [101, 102, 103, 104]`
#      `order_statuses = ["shipped", "processing", "shipped", "delivered"]`
#    - Use `zip` to loop through both lists simultaneously.
#    - Print a formatted string for each order, like "Order 101 has status: shipped".

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- **`for` loops** are for iterating over a known sequence of items.
- **`while` loops** are for repeating a task until a specific condition becomes false.
- `enumerate()` and `zip()` are powerful tools to make your `for` loops more efficient.
- `break` and `continue` give you fine-grained control over your loop's execution.

This concludes Week 1! You've built a solid foundation in Python's basic syntax,
data types, collections, and control flow.

Next up: Week 2, where we'll dive into Functions and build our first project.
"""
