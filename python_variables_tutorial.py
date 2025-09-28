"""
Python Variables Tutorial
=========================

This tutorial covers Python variables from basic concepts to advanced usage.
Variables are containers that store data values in memory.

Table of Contents:
1. What are Variables?
2. Variable Declaration and Assignment
3. Variable Naming Rules and Conventions
4. Data Types in Python
5. Type Conversion
6. Multiple Assignment
7. Variable Scope (Local vs Global)
8. Memory Management
9. Constants and Best Practices
10. Advanced Variable Concepts
11. Practical Examples
12. Common Mistakes and How to Avoid Them
13. Exercises

Let's start learning!
"""

# =============================================================================
# 1. WHAT ARE VARIABLES?
# =============================================================================

"""
Variables are:
- Named containers that store data values
- References to memory locations
- Dynamic (can change type and value)
- Essential for programming and data manipulation

Think of variables as labeled boxes that hold different types of information.
"""

# =============================================================================
# 2. VARIABLE DECLARATION AND ASSIGNMENT
# =============================================================================

print("=== VARIABLE DECLARATION AND ASSIGNMENT ===")

# Basic variable assignment
name = "Alice"
age = 25
height = 5.6
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# Variables can be reassigned
age = 26  # Changing the value
print(f"Updated age: {age}")

# Variables can change type (Python is dynamically typed)
my_variable = 42
print(f"my_variable is: {my_variable} (type: {type(my_variable)})")

my_variable = "Hello World"
print(f"my_variable is now: {my_variable} (type: {type(my_variable)})")

# =============================================================================
# 3. VARIABLE NAMING RULES AND CONVENTIONS
# =============================================================================

print("\n=== VARIABLE NAMING RULES AND CONVENTIONS ===")

# Valid variable names
user_name = "John"
userAge = 30
user2 = "Jane"
_private_var = "private"
__very_private = "very private"

# Invalid variable names (commented out to avoid syntax errors)
# 2user = "invalid"  # Cannot start with number
# user-name = "invalid"  # Cannot contain hyphens
# class = "invalid"  # Cannot use reserved keywords

print("Valid variable names:")
print(f"user_name: {user_name}")
print(f"userAge: {userAge}")
print(f"user2: {user2}")

# Naming conventions
# snake_case (recommended for Python)
first_name = "Alice"
last_name = "Smith"
phone_number = "123-456-7890"

# camelCase (common in other languages, but not Python convention)
firstName = "Bob"  # Not recommended in Python
lastName = "Johnson"

# UPPER_CASE for constants
PI = 3.14159
MAX_SIZE = 100
API_KEY = "abc123"

print(f"Snake case: {first_name} {last_name}")
print(f"Constants: PI = {PI}, MAX_SIZE = {MAX_SIZE}")

# =============================================================================
# 4. DATA TYPES IN PYTHON
# =============================================================================

print("\n=== DATA TYPES IN PYTHON ===")

# Numeric types
integer_var = 42
float_var = 3.14
complex_var = 3 + 4j

print(f"Integer: {integer_var} (type: {type(integer_var)})")
print(f"Float: {float_var} (type: {type(float_var)})")
print(f"Complex: {complex_var} (type: {type(complex_var)})")

# String type
string_var = "Hello, Python!"
multiline_string = """This is a
multiline string"""

print(f"String: {string_var}")
print(f"Multiline: {multiline_string}")

# Boolean type
true_var = True
false_var = False

print(f"Boolean True: {true_var} (type: {type(true_var)})")
print(f"Boolean False: {false_var} (type: {type(false_var)})")

# Collection types
list_var = [1, 2, 3, "hello"]
tuple_var = (1, 2, 3, "world")
set_var = {1, 2, 3, 4, 5}
dict_var = {"name": "Alice", "age": 25, "city": "New York"}

print(f"List: {list_var} (type: {type(list_var)})")
print(f"Tuple: {tuple_var} (type: {type(tuple_var)})")
print(f"Set: {set_var} (type: {type(set_var)})")
print(f"Dictionary: {dict_var} (type: {type(dict_var)})")

# None type
none_var = None
print(f"None: {none_var} (type: {type(none_var)})")

# =============================================================================
# 5. TYPE CONVERSION
# =============================================================================

print("\n=== TYPE CONVERSION ===")

# Implicit type conversion (automatic)
int_num = 5
float_num = 3.14
result = int_num + float_num  # int + float = float
print(f"5 + 3.14 = {result} (type: {type(result)})")

# Explicit type conversion (manual)
str_num = "123"
converted_int = int(str_num)
converted_float = float(str_num)
converted_str = str(456)

print(f"String '123' to int: {converted_int} (type: {type(converted_int)})")
print(f"String '123' to float: {converted_float} (type: {type(converted_float)})")
print(f"Int 456 to string: {converted_str} (type: {type(converted_str)})")

# Boolean conversion
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool(''): {bool('')}")
print(f"bool([]): {bool([])}")
print(f"bool([1, 2, 3]): {bool([1, 2, 3])}")

# List and tuple conversion
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
my_set = set(my_list)

print(f"List to tuple: {my_tuple} (type: {type(my_tuple)})")
print(f"List to set: {my_set} (type: {type(my_set)})")

# =============================================================================
# 6. MULTIPLE ASSIGNMENT
# =============================================================================

print("\n=== MULTIPLE ASSIGNMENT ===")

# Multiple variables, same value
a = b = c = 10
print(f"a = {a}, b = {b}, c = {c}")

# Multiple variables, different values
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")

# Swapping variables
a, b = 5, 10
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a  # Pythonic way to swap
print(f"After swap: a = {a}, b = {b}")

# Unpacking sequences
coordinates = (3, 4)
x, y = coordinates
print(f"Coordinates: x = {x}, y = {y}")

# Unpacking with rest
numbers = [1, 2, 3, 4, 5]
first, *rest = numbers
print(f"First: {first}, Rest: {rest}")

# =============================================================================
# 7. VARIABLE SCOPE (LOCAL VS GLOBAL)
# =============================================================================

print("\n=== VARIABLE SCOPE ===")

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

outer_function()

# =============================================================================
# 8. MEMORY MANAGEMENT
# =============================================================================

print("\n=== MEMORY MANAGEMENT ===")

# Object identity and memory
a = [1, 2, 3]
b = a  # Same reference
c = [1, 2, 3]  # Different object

print(f"a is b: {a is b}")  # True - same object
print(f"a is c: {a is c}")  # False - different objects
print(f"a == c: {a == c}")  # True - same content

# Modifying shared reference
a.append(4)
print(f"After modifying a: a = {a}, b = {b}")

# Creating independent copies
original = [1, 2, 3]
shallow_copy = original.copy()  # or list(original)
deep_copy = original[:]  # slice copy

original.append(4)
print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")

# Garbage collection example
import sys

def memory_example():
    """Demonstrate memory usage."""
    large_list = list(range(1000))
    print(f"Memory usage: {sys.getsizeof(large_list)} bytes")
    return large_list

# Variables are automatically cleaned up when out of scope
result = memory_example()
print(f"Result length: {len(result)}")

# =============================================================================
# 9. CONSTANTS AND BEST PRACTICES
# =============================================================================

print("\n=== CONSTANTS AND BEST PRACTICES ===")

# Constants (convention: UPPER_CASE)
PI = 3.14159
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30

# Good variable names
user_count = 0
is_logged_in = False
file_path = "/path/to/file.txt"

# Avoid these practices:
# 1. Single letter variables (except in loops)
# 2. Abbreviations that aren't clear
# 3. Names that don't describe purpose

# Good examples:
total_score = 0
average_grade = 85.5
student_names = ["Alice", "Bob", "Charlie"]

# Avoid:
# t = 0  # What does 't' mean?
# avg = 85.5  # 'avg' is okay, but 'average_grade' is clearer
# names = [...]  # 'names' is okay, but 'student_names' is more specific

print(f"Constants: PI = {PI}, MAX_CONNECTIONS = {MAX_CONNECTIONS}")
print(f"Good variables: total_score = {total_score}, average_grade = {average_grade}")

# =============================================================================
# 10. ADVANCED VARIABLE CONCEPTS
# =============================================================================

print("\n=== ADVANCED VARIABLE CONCEPTS ===")

# Variable annotations (Python 3.6+)
name: str = "Alice"
age: int = 25
scores: list[float] = [85.5, 92.0, 78.5]

print(f"Annotated variables:")
print(f"name: {name} (type: {type(name)})")
print(f"age: {age} (type: {type(age)})")
print(f"scores: {scores} (type: {type(scores)})")

# Class variables vs instance variables
class Person:
    """Example class with class and instance variables."""
    species = "Homo sapiens"  # Class variable (shared by all instances)
    
    def __init__(self, name, age):
        self.name = name  # Instance variable (unique to each instance)
        self.age = age

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(f"Person1: {person1.name}, {person1.age}, species: {person1.species}")
print(f"Person2: {person2.name}, {person2.age}, species: {person2.species}")

# Modifying class variable affects all instances
Person.species = "Homo sapiens sapiens"
print(f"Updated species for all: {person1.species}")

# Private variables (convention: single underscore)
class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance  # Protected variable
    
    def get_balance(self):
        return self._balance

account = BankAccount(1000)
print(f"Account balance: {account.get_balance()}")

# =============================================================================
# 11. PRACTICAL EXAMPLES
# =============================================================================

print("\n=== PRACTICAL EXAMPLES ===")

# Example 1: User registration system
def create_user_profile():
    """Create a user profile with various data types."""
    # User information
    username = "alice_smith"
    email = "alice@example.com"
    age = 28
    is_premium = True
    subscription_months = 12
    
    # Preferences
    favorite_colors = ["blue", "green", "purple"]
    settings = {
        "notifications": True,
        "theme": "dark",
        "language": "en"
    }
    
    # Calculate derived values
    days_since_registration = subscription_months * 30
    user_tier = "Premium" if is_premium else "Free"
    
    print(f"User Profile:")
    print(f"  Username: {username}")
    print(f"  Email: {email}")
    print(f"  Age: {age}")
    print(f"  Tier: {user_tier}")
    print(f"  Days since registration: {days_since_registration}")
    print(f"  Favorite colors: {favorite_colors}")
    print(f"  Settings: {settings}")

create_user_profile()

# Example 2: Shopping cart system
def shopping_cart_example():
    """Demonstrate variables in a shopping context."""
    # Product information
    product_name = "Laptop"
    product_price = 999.99
    quantity = 2
    tax_rate = 0.08
    
    # Calculations
    subtotal = product_price * quantity
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    
    # Customer information
    customer_name = "John Doe"
    customer_email = "john@example.com"
    is_vip = True
    
    # Apply VIP discount
    if is_vip:
        discount_rate = 0.10
        discount_amount = subtotal * discount_rate
        total = total - discount_amount
    
    print(f"\nShopping Cart:")
    print(f"  Product: {product_name}")
    print(f"  Price per unit: ${product_price}")
    print(f"  Quantity: {quantity}")
    print(f"  Subtotal: ${subtotal:.2f}")
    if is_vip:
        print(f"  VIP Discount: ${discount_amount:.2f}")
    print(f"  Tax: ${tax_amount:.2f}")
    print(f"  Total: ${total:.2f}")

shopping_cart_example()

# Example 3: Data analysis
def data_analysis_example():
    """Demonstrate variables in data analysis."""
    # Sample data
    temperatures = [72, 75, 78, 80, 82, 79, 76, 74]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego"]
    
    # Calculate statistics
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    avg_temp = sum(temperatures) / len(temperatures)
    
    # Find hottest and coldest cities
    max_index = temperatures.index(max_temp)
    min_index = temperatures.index(min_temp)
    hottest_city = cities[max_index]
    coldest_city = cities[min_index]
    
    print(f"\nWeather Analysis:")
    print(f"  Average temperature: {avg_temp:.1f}°F")
    print(f"  Highest temperature: {max_temp}°F in {hottest_city}")
    print(f"  Lowest temperature: {min_temp}°F in {coldest_city}")
    print(f"  Temperature range: {max_temp - min_temp}°F")

data_analysis_example()

# =============================================================================
# 12. COMMON MISTAKES AND HOW TO AVOID THEM
# =============================================================================

print("\n=== COMMON MISTAKES AND HOW TO AVOID THEM ===")

# Mistake 1: Using reserved keywords
# class = "MyClass"  # Don't do this!
# Solution: Use descriptive names
class_name = "MyClass"

# Mistake 2: Not initializing variables
# print(undefined_variable)  # NameError!
# Solution: Always initialize variables
undefined_variable = None
print(f"Initialized variable: {undefined_variable}")

# Mistake 3: Confusing assignment with comparison
x = 5
if x == 5:  # Correct: comparison
    print("x equals 5")
# if x = 5:  # Wrong: assignment in condition

# Mistake 4: Modifying immutable objects
# Strings are immutable
original_string = "Hello"
new_string = original_string + " World"
print(f"Original: {original_string}")
print(f"New: {new_string}")

# Mistake 5: Not understanding variable scope
def scope_mistake():
    # local_var = "I'm local"
    pass

# print(local_var)  # NameError! Variable not in scope
# Solution: Return values or use global variables properly

print("Common mistakes avoided!")

# =============================================================================
# 13. EXERCISES
# =============================================================================

print("\n=== EXERCISES ===")
print("Try these exercises to practice your variable skills:")

"""
Exercise 1: Create variables for a student record:
- Name, age, grade, subjects (list), and GPA
- Calculate and display average grade

Exercise 2: Create a simple calculator using variables:
- Store two numbers and an operation
- Perform the calculation and store the result
- Display the calculation

Exercise 3: Create a temperature converter:
- Store temperature in Celsius
- Convert to Fahrenheit and Kelvin
- Display all three values

Exercise 4: Create a simple bank account system:
- Store account balance, interest rate, and years
- Calculate compound interest
- Display final balance

Exercise 5: Create a text analyzer:
- Store a sentence
- Count words, characters, and vowels
- Display statistics
"""

# =============================================================================
# BONUS: VARIABLE TRICKS AND TIPS
# =============================================================================

print("\n=== BONUS: VARIABLE TRICKS AND TIPS ===")

# Chained assignment
a = b = c = 0
print(f"Chained assignment: a={a}, b={b}, c={c}")

# Multiple return values
def get_coordinates():
    return 10, 20, 30

x, y, z = get_coordinates()
print(f"Coordinates: x={x}, y={y}, z={z}")

# Conditional assignment
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(f"Score: {score}, Grade: {grade}")

# Variable unpacking with *
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Dictionary unpacking
person_info = {"name": "Alice", "age": 25, "city": "NYC"}
name, age, city = person_info.values()
print(f"Unpacked: {name}, {age}, {city}")

# =============================================================================
# CONCLUSION
# =============================================================================

print("\n=== CONCLUSION ===")
print("""
Congratulations! You've learned about Python variables:

Key Takeaways:
1. Variables are containers that store data values
2. Python is dynamically typed (variables can change type)
3. Follow naming conventions (snake_case for variables, UPPER_CASE for constants)
4. Understand scope (local vs global variables)
5. Use meaningful variable names
6. Initialize variables before using them
7. Be aware of object references and memory management
8. Practice with real examples to master variable usage

Remember:
- Variables make your code readable and maintainable
- Good variable names are self-documenting
- Scope determines where variables can be accessed
- Type conversion helps when working with different data types
- Practice with exercises to reinforce learning

Keep coding and experimenting with variables!
""")

# Run the tutorial
if __name__ == "__main__":
    print("Python Variables Tutorial")
    print("=" * 50)
    print("This tutorial demonstrates various aspects of Python variables.")
    print("Run this file to see all examples in action!")
