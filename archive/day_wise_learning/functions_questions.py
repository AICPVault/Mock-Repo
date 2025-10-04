"""
PYTHON FUNCTIONS - COMPREHENSIVE KNOWLEDGE TEST
================================================
Test your knowledge of Python functions (excluding lambda)

INSTRUCTIONS:
- Complete all sections
- Write actual working code, not pseudocode
- Test your functions by uncommenting the test cases
- Some questions require written explanations in comments
"""


# ============================================================================
# SECTION 1: FUNCTION BASICS
# ============================================================================

# Q1.1: Create a function that takes two numbers and returns their sum
# Add proper type hints
def add_numbers(a:int, b:int) -> int:
    return a + b

i = 5
j = 3
print(f"The sum of two numbers {i}  and {j} is  {add_numbers(i,j)}")

# Test:
# print(add_numbers(5, 3))  # Should print: 8


# Q1.2: Create a function that takes a name and returns a greeting
# If no name is provided, it should greet "Guest"
def greet(name: str = "Guest") -> str:
    return f"Hello {name}"
print(greet("Alice"))
print(greet())
# Test:
# print(greet("Alice"))  # Should print: Hello, Alice!
# print(greet())         # Should print: Hello, Guest!


# Q1.3: Create a function that returns multiple values:
# the sum and product of two numbers
def sum_and_product(a: int,b:int) -> tuple[int,int]:
    return a+b,a*b

s, p = sum_and_product(4, 5)
print(f"Sum: {s}, Product: {p}")

# Test:
# s, p = sum_and_product(4, 5)
# print(f"Sum: {s}, Product: {p}")  # Should print: Sum: 9, Product: 20


# ============================================================================
# SECTION 2: PARAMETERS & ARGUMENTS
# ============================================================================

# Q2.1: Create a function that accepts any number of integers
# and returns their sum using *args
def sum_all():
    pass


# Test:
# print(sum_all(1, 2, 3))        # 6
# print(sum_all(10, 20, 30, 40)) # 100


# Q2.2: Create a function that accepts any keyword arguments
# and returns them as a formatted string using **kwargs
# Format: "key1: value1, key2: value2"
def format_info():
    pass


# Test:
# print(format_info(name="Alice", age=25, city="Paris"))
# Should print: "name: Alice, age: 25, city: Paris"


# Q2.3: Create a function with ALL parameter types in correct order:
# positional, *args, keyword-only (after *), **kwargs
# The function should return a dictionary with all the received values
def complex_params():
    pass


# Test:
# result = complex_params(1, 2, 3, 4, required_kw="test", a=10, b=20)
# print(result)


# Q2.4: Fix this function - what's wrong with the parameter order?
def broken_function(name, *args, age=25, **kwargs, city):
    return f"{name}, {age}, {city}"


# Write your explanation here:
# Problem:
# Fixed version below:


# Q2.5: Create a function that only accepts keyword arguments (no positional)
# It should take 'width' and 'height' and return area
def calculate_area():
    pass


# Test:
# print(calculate_area(width=5, height=10))  # 50
# print(calculate_area(5, 10))  # Should raise TypeError


# ============================================================================
# SECTION 3: RETURN VALUES & None
# ============================================================================

# Q3.1: What does this function return? Write your answer as a comment
def mystery_function(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"


# Answer for mystery_function(0):


# Q3.2: Create a function that returns early if input is invalid
# If number is negative, return None immediately
# Otherwise, return the square root (use: number ** 0.5)
def safe_sqrt():
    pass


# Test:
# print(safe_sqrt(16))   # 4.0
# print(safe_sqrt(-5))   # None


# Q3.3: Create a function that returns different types based on input
# If input is a string, return its length (int)
# If input is a list, return its first element (any type)
# If input is a number, return its double (float)
# Use proper type hints with Union/| for return type
def flexible_return():
    pass


# ============================================================================
# SECTION 4: SCOPE & CLOSURES
# ============================================================================

# Q4.1: Fix this function - it should increment the counter
counter = 0


def increment():
    counter = counter + 1
    return counter


# Explain the problem and fix it:
# Problem:
# Fixed version:


# Q4.2: What will this print? Write your answer before running
x = 10


def outer():
    x = 20

    def inner():
        x = 30
        print(f"Inner: {x}")

    inner()
    print(f"Outer: {x}")


outer()
print(f"Global: {x}")

# Your prediction:
# Inner:
# Outer:
# Global:


# Q4.3: Create a function that demonstrates the LEGB rule
# It should access variables from all four scopes
builtin_test = len  # Using a builtin

global_var = "global"


def demonstrate_legb():
    enclosing_var = "enclosing"

    def inner():
        local_var = "local"
        # Print all four: builtin (len), global, enclosing, local
        pass

    inner()


# Q4.4: Create a counter function using closures (not classes!)
# It should return a function that increments and returns a count
def make_counter():
    pass


# Test:
# counter1 = make_counter()
# print(counter1())  # 1
# print(counter1())  # 2
# counter2 = make_counter()
# print(counter2())  # 1 (independent counter)


# ============================================================================
# SECTION 5: DECORATORS (Function Basics)
# ============================================================================

# Q5.1: Create a simple decorator that prints "Before" and "After"
# when a function is called
def log_wrapper():
    pass


# Test:
# @log_wrapper
# def say_hello():
#     print("Hello!")
#
# say_hello()
# Should print:
# Before
# Hello!
# After


# Q5.2: Create a decorator that measures execution time
# Use time.time() before and after
import time


def timer():
    pass


# Test:
# @timer
# def slow_function():
#     time.sleep(0.1)
#     return "Done"
#
# slow_function()


# Q5.3: What's wrong with this decorator? Fix it and explain.
def broken_decorator(func):
    def wrapper():
        print("Calling function")
        return func()

    return wrapper


@broken_decorator
def greet_person(name):
    return f"Hello, {name}"


# greet_person("Alice")  # This will fail - why?
# Problem:
# Fixed version:


# ============================================================================
# SECTION 6: RECURSION
# ============================================================================

# Q6.1: Create a recursive function to calculate factorial
# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
# Include base case and recursive case
def factorial():
    pass


# Test:
# print(factorial(5))   # 120
# print(factorial(0))   # 1


# Q6.2: Create a recursive function to calculate Fibonacci number
# fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2)
def fibonacci():
    pass


# Test:
# print(fibonacci(6))  # 8 (sequence: 0,1,1,2,3,5,8)


# Q6.3: Create a recursive function to sum all numbers in a nested list
# Example: [1, [2, 3], [4, [5, 6]]] -> 21
def sum_nested():
    pass


# Test:
# print(sum_nested([1, [2, 3], [4, [5, 6]]]))  # 21


# Q6.4: Explain why this recursive function is dangerous:
def dangerous_recursion(n):
    return dangerous_recursion(n - 1) + 1


# Problem:
# How to fix:


# ============================================================================
# SECTION 7: DOCSTRINGS & ANNOTATIONS
# ============================================================================

# Q7.1: Add a proper docstring (Google or NumPy style) to this function
def calculate_bmi(weight, height):
    return weight / (height ** 2)


# Q7.2: Add complete type hints to this function including return type
def process_data(items, multiplier, include_negative):
    result = []
    for item in items:
        value = item * multiplier
        if include_negative or value >= 0:
            result.append(value)
    return result


# Q7.3: Create a function with a complex return type hint
# It should take a list of strings and return a dict where:
# - keys are string lengths (int)
# - values are lists of strings with that length
def group_by_length():
    pass


# Test:
# print(group_by_length(["a", "bb", "ccc", "dd", "e"]))
# Should return: {1: ['a', 'e'], 2: ['bb', 'dd'], 3: ['ccc']}


# ============================================================================
# SECTION 8: ADVANCED CONCEPTS
# ============================================================================

# Q8.1: Create a function that accepts another function as a parameter
# Apply that function to each element in a list
def apply_to_list():
    pass


# Test:
# def square(x): return x ** 2
# print(apply_to_list([1, 2, 3, 4], square))  # [1, 4, 9, 16]


# Q8.2: Create a function that returns another function
# The returned function should add a specific value to its input
def make_adder():
    pass


# Test:
# add_5 = make_adder(5)
# print(add_5(10))  # 15
# add_10 = make_adder(10)
# print(add_10(10))  # 20


# Q8.3: Implement a function cache using a dictionary
# The function should remember previous results
def memoize():
    cache = {}
    # Your code here
    pass


# @memoize
# def expensive_function(n):
#     print(f"Computing for {n}")
#     time.sleep(1)
#     return n ** 2


# Q8.4: Create a function with a generator expression (not generator function!)
# It should return a generator that yields squares of numbers
def get_squares_generator():
    pass


# Test:
# gen = get_squares_generator(5)
# print(list(gen))  # [0, 1, 4, 9, 16]


# ============================================================================
# SECTION 9: BEST PRACTICES & COMMON MISTAKES
# ============================================================================

# Q9.1: Fix this function - it has a mutable default argument problem
def add_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list


# Problem:
# Fixed version:


# Q9.2: What's wrong with this function? Explain and fix.
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


# Try: calculate_average([])
# Problem:
# Fixed version:


# Q9.3: Improve this function using early returns
def check_age(age):
    if age >= 0:
        if age < 18:
            return "Minor"
        else:
            if age < 65:
                return "Adult"
            else:
                return "Senior"
    else:
        return "Invalid"


# Improved version:


# Q9.4: Add proper error handling to this function
def divide_numbers(a, b):
    return a / b


# Improved version with try/except:


# ============================================================================
# SECTION 10: PRACTICAL CHALLENGES
# ============================================================================

# Q10.1: Create a function that validates email format
# Rules: must contain @ and a dot after @
# Return True/False
def is_valid_email():
    pass


# Q10.2: Create a function that takes a list of numbers
# Returns a dict with 'min', 'max', 'avg', 'sum'
def analyze_numbers():
    pass


# Q10.3: Create a retry decorator that tries a function up to 3 times
# If it fails all 3 times, raise the exception
def retry():
    pass


# Q10.4: Create a function that flattens a nested dictionary
# Example: {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
# Becomes: {'a': 1, 'b.c': 2, 'b.d.e': 3}
def flatten_dict():
    pass


# ============================================================================
# REFLECTION QUESTIONS (Answer in comments)
# ============================================================================

"""
R1: What's the difference between arguments and parameters?
Answer: 

R2: When would you use *args vs **kwargs?
Answer: 

R3: What is the difference between 'return' and 'print'?
Answer: 

R4: Why are closures useful?
Answer: 

R5: What happens if a function doesn't have a return statement?
Answer: 
"""


# ============================================================================
# BONUS: CODE REVIEW
# ============================================================================

# Find and fix ALL the issues in this function:
def process_user_data(name, age, hobbies=[], is_active=True, **extra):
    if age:
        user = {
            'name': name.upper(),
            'age': age,
            'hobbies': hobbies,
            'active': is_active
        }
        hobbies.append('reading')
        for key, value in extra:
            user[key] = value
        return user


# List all issues:
# 1.
# 2.
# 3.
# 4.

# Fixed version:


print("\n" + "=" * 60)
print("Test complete! Review your answers.")
print("=" * 60)