# Day 1: Python Basics - Variables and Data Types

# 1. Basic Variables and Data Types
# -------------------------------
# Numbers
my_integer = 10              # Whole number
my_float = 3.14             # Decimal number
my_complex = 1 + 2j         # Complex number

# Text (String)
my_string = "Hello Python"   # String variable

# Boolean (True/False)
is_learning = True          # Boolean variable

# 2. Print Statements
# -------------------------------
print("Basic printing:")
print(my_integer)           # Prints: 10
print(my_float)             # Prints: 3.14
print(my_string)            # Prints: Hello Python

# 3. String Formatting (3 ways)
# -------------------------------
name = "Alice"
age = 25

# Way 1: Using + (Old way)
print("My name is " + name + " and I am " + str(age) + " years old")

# Way 2: Using .format() (Better way)
print("My name is {} and I am {} years old".format(name, age))

# Way 3: Using f-strings (Modern way - Python 3.6+)
print(f"My name is {name} and I am {age} years old")

# 4. Simple Variable Operations
# -------------------------------
# Numbers
x = 5
y = 2
sum_result = x + y
print(f"Sum of {x} and {y} is: {sum_result}")


# Strings
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# 5. Checking Variable Types
# -------------------------------
print(f"Type of my_integer: {type(my_integer)}")
print(f"Type of my_float: {type(my_float)}")
print(f"Type of my_string: {type(my_string)}")
print(f"Type of is_learning: {type(is_learning)}")

# Practice Exercise:
# Try changing the values of these variables and see what happens!

