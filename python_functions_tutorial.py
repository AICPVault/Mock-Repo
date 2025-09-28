"""
Python Functions Tutorial
========================

This tutorial covers Python functions from basic concepts to advanced usage.
Functions are reusable blocks of code that perform specific tasks.

Table of Contents:
1. What are Functions?
2. Basic Function Syntax
3. Parameters and Arguments
4. Return Values
5. Default Parameters
6. Keyword Arguments
7. Variable Arguments (*args and **kwargs)
8. Local vs Global Scope
9. Lambda Functions
10. Function Documentation
11. Practical Examples
12. Exercises

Let's start learning!
"""

# =============================================================================
# 1. WHAT ARE FUNCTIONS?
# =============================================================================

"""
Functions are blocks of reusable code that:
- Perform a specific task
- Can accept input (parameters)
- Can return output (return values)
- Help organize and modularize code
- Make code more readable and maintainable

Think of functions as mini-programs within your program.
"""

# =============================================================================
# 2. BASIC FUNCTION SYNTAX
# =============================================================================

print("=== BASIC FUNCTION SYNTAX ===")

# Simple function without parameters
def greet():
    """A simple function that prints a greeting."""
    print("Hello, World!")

# Calling the function
greet()

# Function with parameters
def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}!")

# Calling with argument
greet_person("Alice")
greet_person("Bob")

# =============================================================================
# 3. PARAMETERS AND ARGUMENTS
# =============================================================================

print("\n=== PARAMETERS AND ARGUMENTS ===")

# Multiple parameters
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

# Using the function with positional arguments
rectangle_area = calculate_area(5, 3)
print(f"Area of rectangle: {rectangle_area}")

# Different data types as parameters
def describe_pet(name, age, species="dog"):
    """Describe a pet with name, age, and species."""
    print(f"{name} is a {age}-year-old {species}.")

describe_pet("Buddy", 3, "cat")
describe_pet("Max", 5)  # Uses default species

# =============================================================================
# 4. RETURN VALUES
# =============================================================================

print("\n=== RETURN VALUES ===")

# Function that returns a value
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add_numbers(10, 20)
print(f"Sum: {result}")

# Function that returns multiple values
def get_name_parts(full_name):
    """Split a full name into first and last name."""
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1] if len(parts) > 1 else ""
    return first_name, last_name

first, last = get_name_parts("John Doe")
print(f"First: {first}, Last: {last}")

# Function that returns different types
def process_number(num):
    """Process a number and return different information."""
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

print(process_number(5))
print(process_number(-3))
print(process_number(0))

# =============================================================================
# 5. DEFAULT PARAMETERS
# =============================================================================

print("\n=== DEFAULT PARAMETERS ===")

def create_profile(name, age=25, city="Unknown"):
    """Create a user profile with default values."""
    print(f"Name: {name}, Age: {age}, City: {city}")

# Using default values
create_profile("Alice")
create_profile("Bob", 30)
create_profile("Charlie", 35, "New York")

# =============================================================================
# 6. KEYWORD ARGUMENTS
# =============================================================================

print("\n=== KEYWORD ARGUMENTS ===")

def create_rectangle(length, width, color="blue", border=True):
    """Create a rectangle with specified properties."""
    print(f"Rectangle: {length}x{width}, Color: {color}, Border: {border}")

# Using keyword arguments (order doesn't matter)
create_rectangle(width=10, length=5, color="red")
create_rectangle(8, 6, border=False)

# Mix of positional and keyword arguments
create_rectangle(12, 8, color="green")

# =============================================================================
# 7. VARIABLE ARGUMENTS (*args and **kwargs)
# =============================================================================

print("\n=== VARIABLE ARGUMENTS ===")

# *args - variable number of positional arguments
def sum_all(*numbers):
    """Sum all provided numbers."""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1,2,3: {sum_all(1, 2, 3)}")
print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - variable number of keyword arguments
def create_student(name, **details):
    """Create a student profile with additional details."""
    print(f"Student: {name}")
    for key, value in details.items():
        print(f"  {key}: {value}")

create_student("Alice", age=20, major="Computer Science", gpa=3.8)
create_student("Bob", grade="A", attendance=95)

# Combining *args and **kwargs
def flexible_function(*args, **kwargs):
    """Function that accepts any number of arguments."""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=25)

# =============================================================================
# 8. LOCAL VS GLOBAL SCOPE
# =============================================================================

print("\n=== LOCAL VS GLOBAL SCOPE ===")

# Global variable
global_counter = 0

def increment_local():
    """Demonstrate local scope."""
    local_counter = 0  # Local variable
    local_counter += 1
    print(f"Local counter: {local_counter}")

def increment_global():
    """Demonstrate global scope."""
    global global_counter  # Access global variable
    global_counter += 1
    print(f"Global counter: {global_counter}")

# Demonstrate scope
increment_local()
increment_local()
increment_global()
increment_global()

# =============================================================================
# 9. LAMBDA FUNCTIONS
# =============================================================================

print("\n=== LAMBDA FUNCTIONS ===")

# Regular function
def square(x):
    return x ** 2

# Lambda function (anonymous function)
square_lambda = lambda x: x ** 2

print(f"Square of 5 (regular): {square(5)}")
print(f"Square of 5 (lambda): {square_lambda(5)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")

# Filter with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# =============================================================================
# 10. FUNCTION DOCUMENTATION
# =============================================================================

print("\n=== FUNCTION DOCUMENTATION ===")

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    
    Parameters:
    radius (float): The radius of the circle
    
    Returns:
    float: The area of the circle
    
    Raises:
    ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 3.14159 * radius ** 2

# Accessing function documentation
print("Function documentation:")
print(calculate_circle_area.__doc__)

# =============================================================================
# 11. PRACTICAL EXAMPLES
# =============================================================================

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: Calculator functions
def calculator(operation, a, b):
    """Simple calculator function."""
    operations = {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b if b != 0 else "Cannot divide by zero"
    }
    return operations.get(operation, "Invalid operation")

print(f"5 + 3 = {calculator('add', 5, 3)}")
print(f"10 - 4 = {calculator('subtract', 10, 4)}")
print(f"6 * 7 = {calculator('multiply', 6, 7)}")
print(f"15 / 3 = {calculator('divide', 15, 3)}")

# Example 2: Text processing
def process_text(text, operation="count"):
    """Process text with different operations."""
    if operation == "count":
        return len(text)
    elif operation == "upper":
        return text.upper()
    elif operation == "lower":
        return text.lower()
    elif operation == "reverse":
        return text[::-1]
    else:
        return "Invalid operation"

sample_text = "Hello, Python!"
print(f"Text length: {process_text(sample_text)}")
print(f"Uppercase: {process_text(sample_text, 'upper')}")
print(f"Reversed: {process_text(sample_text, 'reverse')}")

# Example 3: Data validation
def validate_email(email):
    """Simple email validation."""
    if "@" in email and "." in email:
        return True, "Valid email"
    else:
        return False, "Invalid email"

email1 = "user@example.com"
email2 = "invalid-email"
print(f"{email1}: {validate_email(email1)}")
print(f"{email2}: {validate_email(email2)}")

# =============================================================================
# 12. EXERCISES
# =============================================================================

print("\n=== EXERCISES ===")
print("Try these exercises to practice your function skills:")

"""
Exercise 1: Create a function that takes a list of numbers and returns:
- The sum of all numbers
- The average of all numbers
- The maximum number
- The minimum number

Exercise 2: Write a function that checks if a word is a palindrome
(reads the same forwards and backwards)

Exercise 3: Create a function that generates a password with:
- Specified length
- Mix of uppercase, lowercase, numbers, and symbols
- Optional parameters for character types

Exercise 4: Write a function that sorts a list of dictionaries by a specified key

Exercise 5: Create a function that finds the factorial of a number using recursion
"""

# =============================================================================
# BONUS: RECURSION EXAMPLE
# =============================================================================

print("\n=== RECURSION EXAMPLE ===")

def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

def fibonacci(n):
    """Calculate Fibonacci number using recursion."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci sequence (first 10 numbers):")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")

# =============================================================================
# CONCLUSION
# =============================================================================

print("\n=== CONCLUSION ===")
print("""
Congratulations! You've learned about Python functions:

Key Takeaways:
1. Functions help organize and reuse code
2. Parameters make functions flexible
3. Return values allow functions to provide results
4. Default parameters make functions more convenient
5. Keyword arguments improve readability
6. *args and **kwargs handle variable arguments
7. Scope determines variable accessibility
8. Lambda functions are useful for simple operations
9. Documentation makes code more maintainable
10. Practice with real examples improves understanding

Keep practicing and building projects to master functions!
""")

# Run the tutorial
if __name__ == "__main__":
    print("Python Functions Tutorial")
    print("=" * 50)
    print("This tutorial demonstrates various aspects of Python functions.")
    print("Run this file to see all examples in action!")
