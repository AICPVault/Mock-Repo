"""
Day 1: Python Basics - Variables, Data Types, and Fundamentals
==============================================================

Welcome to your Python learning journey! This tutorial covers the essential
foundations of Python programming.

Learning Objectives:
- Understand what Python is and why it's popular
- Learn about variables and how to use them
- Explore Python's built-in data types
- Practice basic operations and assignments
- Understand Python syntax and indentation

Let's start coding!
"""

print("🐍 Welcome to Day 1: Python Basics!")
print("=" * 50)

# =============================================================================
# 1. WHAT IS PYTHON?
# =============================================================================

print("\n📚 WHAT IS PYTHON?")
print("-" * 20)

"""
Python is a high-level, interpreted programming language known for:
- Simple and readable syntax
- Versatility (web development, data science, AI, automation)
- Large community and extensive libraries
- Cross-platform compatibility
- Beginner-friendly yet powerful
"""

# =============================================================================
# 2. VARIABLES - STORING DATA
# =============================================================================

print("\n📦 VARIABLES - STORING DATA")
print("-" * 30)

# Variables are containers that store data
name = "Alice"
age = 25
height = 5.6
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is Student: {is_student}")

# Variables can be reassigned
age = 26
print(f"Updated age: {age}")

# Variables can change type (Python is dynamically typed)
my_variable = 42
print(f"my_variable: {my_variable} (type: {type(my_variable)})")

my_variable = "Hello World"
print(f"my_variable: {my_variable} (type: {type(my_variable)})")

# =============================================================================
# 3. DATA TYPES IN PYTHON
# =============================================================================

print("\n🔢 DATA TYPES IN PYTHON")
print("-" * 25)

# Numeric Types
integer_number = 42
float_number = 3.14
complex_number = 3 + 4j

print("Numeric Types:")
print(f"Integer: {integer_number} (type: {type(integer_number)})")
print(f"Float: {float_number} (type: {type(float_number)})")
print(f"Complex: {complex_number} (type: {type(complex_number)})")

# String Type
single_quote = 'Hello'
double_quote = "World"
triple_quote = """This is a
multiline string"""

print("\nString Types:")
print(f"Single quote: {single_quote}")
print(f"Double quote: {double_quote}")
print(f"Triple quote: {triple_quote}")

# Boolean Type
is_true = True
is_false = False

print("\nBoolean Types:")
print(f"True: {is_true} (type: {type(is_true)})")
print(f"False: {is_false} (type: {type(is_false)})")

# None Type
empty_value = None
print(f"None: {empty_value} (type: {type(empty_value)})")

# =============================================================================
# 4. BASIC OPERATIONS
# =============================================================================

print("\n➕ BASIC OPERATIONS")
print("-" * 20)

# Arithmetic Operations
a = 10
b = 3

print("Arithmetic Operations:")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# String Operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"\nString Operations:")
print(f"Full name: {full_name}")
print(f"Name length: {len(full_name)}")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")

# =============================================================================
# 5. VARIABLE NAMING RULES
# =============================================================================

print("\n📝 VARIABLE NAMING RULES")
print("-" * 28)

# Good variable names
user_name = "Alice"
user_age = 25
total_score = 100
is_logged_in = True

# Constants (convention: UPPER_CASE)
PI = 3.14159
MAX_SIZE = 100

print("Good variable names:")
print(f"user_name: {user_name}")
print(f"user_age: {user_age}")
print(f"total_score: {total_score}")
print(f"is_logged_in: {is_logged_in}")
print(f"Constants: PI = {PI}, MAX_SIZE = {MAX_SIZE}")

# Naming conventions
# snake_case for variables (recommended)
first_name = "Alice"
last_name = "Smith"

# camelCase (not recommended in Python)
firstName = "Bob"  # Avoid this in Python

print(f"\nNaming conventions:")
print(f"snake_case: {first_name} {last_name}")

# =============================================================================
# 6. TYPE CONVERSION
# =============================================================================

print("\n🔄 TYPE CONVERSION")
print("-" * 20)

# Implicit conversion (automatic)
int_num = 5
float_num = 3.14
result = int_num + float_num  # int + float = float
print(f"Implicit conversion: {int_num} + {float_num} = {result} (type: {type(result)})")

# Explicit conversion (manual)
str_num = "123"
converted_int = int(str_num)
converted_float = float(str_num)
converted_str = str(456)

print(f"\nExplicit conversion:")
print(f"String '123' to int: {converted_int} (type: {type(converted_int)})")
print(f"String '123' to float: {converted_float} (type: {type(converted_float)})")
print(f"Int 456 to string: {converted_str} (type: {type(converted_str)})")

# Boolean conversion
print(f"\nBoolean conversion:")
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool(''): {bool('')}")

# =============================================================================
# 7. PRACTICAL EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL EXAMPLES")
print("-" * 22)

# Example 1: Student Information
def student_info_example():
    """Example of storing student information."""
    student_name = "Alice Johnson"
    student_id = "S12345"
    grade = 85.5
    is_passing = grade >= 60
    
    print(f"Student Information:")
    print(f"  Name: {student_name}")
    print(f"  ID: {student_id}")
    print(f"  Grade: {grade}")
    print(f"  Passing: {is_passing}")

student_info_example()

# Example 2: Simple Calculator
def simple_calculator():
    """Example of basic calculations."""
    num1 = 15
    num2 = 4
    
    print(f"\nSimple Calculator:")
    print(f"  Numbers: {num1} and {num2}")
    print(f"  Sum: {num1 + num2}")
    print(f"  Difference: {num1 - num2}")
    print(f"  Product: {num1 * num2}")
    print(f"  Quotient: {num1 / num2}")
    print(f"  Remainder: {num1 % num2}")

simple_calculator()

# Example 3: Temperature Converter
def temperature_converter():
    """Example of temperature conversion."""
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    
    print(f"\nTemperature Converter:")
    print(f"  Celsius: {celsius}°C")
    print(f"  Fahrenheit: {fahrenheit}°F")

temperature_converter()

# =============================================================================
# 8. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice what you've learned:

Exercise 1: Create variables for a person's information
- Name, age, city, and occupation
- Display the information in a formatted way

Exercise 2: Create a simple shopping calculator
- Store item name, price, and quantity
- Calculate total cost
- Display the receipt

Exercise 3: Create a basic profile system
- Store username, email, and age
- Check if the user is an adult (18+)
- Display a welcome message

Exercise 4: Practice type conversion
- Convert a string number to integer
- Convert an integer to string
- Perform calculations with converted values

Exercise 5: Create a simple text processor
- Store a sentence
- Count the number of characters
- Convert to uppercase and lowercase
- Display all variations
""")

# =============================================================================
# 9. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ Variables are containers that store data
✅ Python is dynamically typed (variables can change type)
✅ Python has several built-in data types (int, float, str, bool, None)
✅ Variables follow naming conventions (snake_case)
✅ Type conversion allows changing data types
✅ Python syntax is clean and readable
✅ Practice with real examples helps understanding

Next Steps:
- Day 2: Operators, Conditionals, and Input/Output
- Day 3: Loops and Iteration
- Day 4: Functions and Scope
- Day 5: Data Structures (Lists, Tuples, Sets, Dictionaries)
""")

# =============================================================================
# 10. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 1 of your Python journey!

You now understand:
- How to create and use variables
- Python's basic data types
- Simple operations and calculations
- Variable naming conventions
- Type conversion

Keep practicing and experimenting with the code.
The more you code, the better you'll become!

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 1: Python Basics Tutorial")
    print("Run this file to see all examples in action!")
