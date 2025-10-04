"""
Day 4: Functions and Scope
==============================

Today we'll learn about functions - one of the most important concepts in programming.
Functions allow us to organize code, avoid repetition, and create reusable components.
We'll also explore variable scope and how data is accessed in different parts of our code.

Learning Objectives:
- Understand what functions are and why they're important
- Learn how to define and call functions
- Master function parameters and return values
- Understand variable scope (local vs global)
- Learn about function documentation and best practices
- Build modular and reusable code

Let's dive into the world of functions!
"""

print("🐍 Welcome to Day 4: Functions and Scope!")
print("=" * 50)

# =============================================================================
# 1. WHAT ARE FUNCTIONS?
# =============================================================================

print("\n🔧 WHAT ARE FUNCTIONS?")
print("-" * 25)

"""
Functions are:
- Reusable blocks of code that perform specific tasks
- Named containers for code that can be called multiple times
- Essential for organizing and modularizing code
- Help avoid code duplication
- Make programs easier to read, test, and maintain

Think of functions as mini-programs within your program!
"""

# =============================================================================
# 2. BASIC FUNCTION SYNTAX
# =============================================================================

print("\n📝 BASIC FUNCTION SYNTAX")
print("-" * 28)

# Simple function without parameters
def greet():
    """A simple function that prints a greeting."""
    print("Hello, World!")

# Calling the function
print("Calling greet():")
greet()

# Function with parameters
def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}!")

# Calling with argument
print("\nCalling greet_person('Alice'):")
greet_person("Alice")

# Function with multiple parameters
def introduce(name, age, city):
    """Introduce a person with their details."""
    print(f"Hi! I'm {name}, {age} years old, from {city}.")

print("\nCalling introduce():")
introduce("Bob", 25, "New York")

# =============================================================================
# 3. RETURN VALUES
# =============================================================================

print("\n🔄 RETURN VALUES")
print("-" * 18)

# Function that returns a value
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add_numbers(5, 3)
print(f"add_numbers(5, 3) = {result}")

# Function that returns multiple values
def get_name_parts(full_name):
    """Split a full name into first and last name."""
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1] if len(parts) > 1 else ""
    return first_name, last_name

first, last = get_name_parts("John Doe")
print(f"First name: {first}, Last name: {last}")

# Function that returns different types based on input
def process_number(num):
    """Process a number and return information about it."""
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

print(f"process_number(5): {process_number(5)}")
print(f"process_number(-3): {process_number(-3)}")
print(f"process_number(0): {process_number(0)}")

# =============================================================================
# 4. DEFAULT PARAMETERS
# =============================================================================

print("\n⚙️ DEFAULT PARAMETERS")
print("-" * 25)

# Function with default parameters
def create_profile(name, age=25, city="Unknown"):
    """Create a user profile with default values."""
    print(f"Name: {name}, Age: {age}, City: {city}")

print("Using default parameters:")
create_profile("Alice")
create_profile("Bob", 30)
create_profile("Charlie", 35, "Los Angeles")

# Function with mixed default and required parameters
def calculate_area(length, width=1):
    """Calculate area with default width."""
    return length * width

print(f"\ncalculate_area(5): {calculate_area(5)}")
print(f"calculate_area(5, 3): {calculate_area(5, 3)}")

# =============================================================================
# 5. KEYWORD ARGUMENTS
# =============================================================================

print("\n🔑 KEYWORD ARGUMENTS")
print("-" * 25)

def create_rectangle(length, width, color="blue", border=True):
    """Create a rectangle with specified properties."""
    print(f"Rectangle: {length}x{width}, Color: {color}, Border: {border}")

print("Using keyword arguments:")
create_rectangle(width=10, length=5, color="red")
create_rectangle(8, 6, border=False)
create_rectangle(12, 8, color="green")

# =============================================================================
# 6. VARIABLE SCOPE
# =============================================================================

print("\n🌍 VARIABLE SCOPE")
print("-" * 18)

# Global variable
global_var = "I'm global"

def demonstrate_scope():
    """Demonstrate local and global scope."""
    # Local variable
    local_var = "I'm local"
    print(f"Inside function - Local: {local_var}")
    print(f"Inside function - Global: {global_var}")
    
    # Modifying global variable
    global global_var
    global_var = "I'm modified global"

# Before function call
print(f"Before function - Global: {global_var}")

# Call function
demonstrate_scope()

# After function call
print(f"After function - Global: {global_var}")

# Nested scope example
def outer_function():
    """Outer function with nested scope."""
    outer_var = "I'm in outer function"
    
    def inner_function():
        """Inner function accessing outer scope."""
        nonlocal outer_var  # Access outer function's variable
        outer_var = "Modified in inner function"
        print(f"Inner function: {outer_var}")
    
    print(f"Before inner: {outer_var}")
    inner_function()
    print(f"After inner: {outer_var}")

print("\nNested scope example:")
outer_function()

# =============================================================================
# 7. PRACTICAL EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL EXAMPLES")
print("-" * 22)

# Example 1: Calculator Functions
def calculator(operation, a, b):
    """Simple calculator function."""
    operations = {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b if b != 0 else "Cannot divide by zero"
    }
    return operations.get(operation, "Invalid operation")

print("Calculator Functions:")
print(f"5 + 3 = {calculator('add', 5, 3)}")
print(f"10 - 4 = {calculator('subtract', 10, 4)}")
print(f"6 * 7 = {calculator('multiply', 6, 7)}")
print(f"15 / 3 = {calculator('divide', 15, 3)}")

# Example 2: Text Processing Functions
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
print(f"\nText Processing:")
print(f"Text: {sample_text}")
print(f"Length: {process_text(sample_text)}")
print(f"Uppercase: {process_text(sample_text, 'upper')}")
print(f"Reversed: {process_text(sample_text, 'reverse')}")

# Example 3: Data Validation Functions
def validate_email(email):
    """Simple email validation."""
    if "@" in email and "." in email:
        return True, "Valid email"
    else:
        return False, "Invalid email"

def validate_age(age):
    """Validate age range."""
    if age < 0:
        return False, "Age cannot be negative"
    elif age > 150:
        return False, "Age seems unrealistic"
    else:
        return True, "Valid age"

print(f"\nData Validation:")
email1 = "user@example.com"
email2 = "invalid-email"
print(f"{email1}: {validate_email(email1)}")
print(f"{email2}: {validate_email(email2)}")
print(f"Age 25: {validate_age(25)}")
print(f"Age -5: {validate_age(-5)}")

# =============================================================================
# 8. FUNCTION DOCUMENTATION
# =============================================================================

print("\n📚 FUNCTION DOCUMENTATION")
print("-" * 30)

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

# Using the function
try:
    area = calculate_circle_area(5)
    print(f"Area of circle with radius 5: {area:.2f}")
except ValueError as e:
    print(f"Error: {e}")

# =============================================================================
# 9. LAMBDA FUNCTIONS
# =============================================================================

print("\nλ LAMBDA FUNCTIONS")
print("-" * 20)

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
# 10. RECURSION
# =============================================================================

print("\n🔄 RECURSION")
print("-" * 15)

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
# 11. FUNCTION BEST PRACTICES
# =============================================================================

print("\n💡 FUNCTION BEST PRACTICES")
print("-" * 30)

print("""
Best practices for writing functions:

1. Use descriptive function names
   ✅ def calculate_total_price():
   ❌ def calc():

2. Keep functions small and focused
   ✅ One function, one responsibility
   ❌ One function doing everything

3. Use meaningful parameter names
   ✅ def greet_person(name):
   ❌ def greet(x):

4. Document your functions
   ✅ Use docstrings to explain purpose
   ❌ Leave functions undocumented

5. Return values instead of printing
   ✅ return result
   ❌ print(result)  # Unless it's a display function

6. Use default parameters wisely
   ✅ def create_user(name, age=18):
   ❌ def create_user(name, age, city, country, ...):

7. Handle errors gracefully
   ✅ Use try-except blocks
   ❌ Let errors crash the program

8. Test your functions
   ✅ Write test cases
   ❌ Assume functions work correctly
""")

# =============================================================================
# 12. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice what you've learned:

Exercise 1: Create a function library
- Write functions for basic math operations
- Create a function to check if a number is prime
- Build a function to find the maximum in a list

Exercise 2: Build a text processing toolkit
- Function to count words in a sentence
- Function to capitalize first letter of each word
- Function to remove vowels from a string

Exercise 3: Create a simple banking system
- Function to deposit money
- Function to withdraw money
- Function to check balance
- Function to transfer money between accounts

Exercise 4: Build a student grade manager
- Function to add a student
- Function to add grades for a student
- Function to calculate average grade
- Function to find top student

Exercise 5: Create a password manager
- Function to generate random password
- Function to check password strength
- Function to validate password requirements
- Function to encrypt/decrypt passwords
""")

# =============================================================================
# 13. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common function mistakes and how to avoid them:

1. Not using return statements
   ❌ def add(a, b):
         a + b  # This doesn't return anything
   ✅ def add(a, b):
         return a + b

2. Modifying global variables without global keyword
   ❌ global_var = 5
       def modify():
           global_var = 10  # Creates local variable
   ✅ global_var = 5
       def modify():
           global global_var
           global_var = 10

3. Using mutable default arguments
   ❌ def append_to_list(item, my_list=[]):
         my_list.append(item)
         return my_list
   ✅ def append_to_list(item, my_list=None):
         if my_list is None:
             my_list = []
         my_list.append(item)
         return my_list

4. Not handling errors
   ❌ def divide(a, b):
         return a / b  # Crashes if b is 0
   ✅ def divide(a, b):
         if b == 0:
             return "Cannot divide by zero"
         return a / b

5. Functions that are too long
   ❌ def do_everything():  # 100+ lines
   ✅ def do_specific_thing():  # 10-20 lines
""")

# =============================================================================
# 14. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ Functions are reusable blocks of code
✅ Functions help organize and modularize code
✅ Parameters make functions flexible
✅ Return values allow functions to provide results
✅ Scope determines variable accessibility
✅ Documentation makes code maintainable
✅ Lambda functions are useful for simple operations
✅ Recursion allows functions to call themselves
✅ Best practices lead to better code

Next Steps:
- Day 5: Data Structures (Lists, Tuples, Sets, Dictionaries)
""")

# =============================================================================
# 15. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 4 of your Python journey!

You now understand:
- How to create and use functions effectively
- How to handle parameters and return values
- How variable scope works in Python
- How to write clean, documented functions
- How to use lambda functions and recursion
- Best practices for function design

Functions are the building blocks of good programming!
Practice with the exercises to master this essential concept.

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 4: Functions and Scope Tutorial")
    print("Run this file to see all examples in action!")
