"""
Day 9: Modules and Packages
============================

Today we'll learn about Python modules and packages - how to organize code,
create reusable components, and build larger applications. We'll explore
importing, creating modules, and managing packages.

Learning Objectives:
- Understand what modules and packages are
- Learn how to import and use modules
- Create your own modules and packages
- Master different import techniques
- Understand the Python path and module search
- Build organized, maintainable code

Let's explore modules and packages!
"""

print("🐍 Welcome to Day 9: Modules and Packages!")
print("=" * 50)

# =============================================================================
# 1. WHAT ARE MODULES AND PACKAGES?
# =============================================================================

print("\n📦 WHAT ARE MODULES AND PACKAGES?")
print("-" * 35)

"""
Modules and Packages are ways to organize Python code:

MODULES:
- Single Python files (.py)
- Contain functions, classes, and variables
- Can be imported and used in other files
- Examples: math, random, datetime

PACKAGES:
- Directories containing multiple modules
- Must have __init__.py file
- Organize related modules together
- Examples: os, sys, collections

Benefits:
- Code reusability and organization
- Namespace management
- Easier maintenance and testing
- Modular application development
"""

# =============================================================================
# 2. USING BUILT-IN MODULES
# =============================================================================

print("\n🔧 USING BUILT-IN MODULES")
print("-" * 30)

# Import entire module
import math
print(f"Math module - Square root of 16: {math.sqrt(16)}")
print(f"Math module - Pi: {math.pi}")
print(f"Math module - Sine of 90 degrees: {math.sin(math.radians(90))}")

# Import specific functions
from random import randint, choice
print(f"Random integer (1-10): {randint(1, 10)}")
print(f"Random choice from list: {choice(['apple', 'banana', 'orange'])}")

# Import with alias
import datetime as dt
current_time = dt.datetime.now()
print(f"Current time: {current_time}")

# Import specific items with alias
from collections import Counter as Count
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Count(data)
print(f"Item counts: {counter}")

# =============================================================================
# 3. CREATING YOUR OWN MODULES
# =============================================================================

print("\n🏗️ CREATING YOUR OWN MODULES")
print("-" * 35)

# Let's create a simple module (in real scenario, this would be a separate file)
# For demonstration, we'll define functions that would be in a module

def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def calculate_triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

# These functions would be saved in a file called 'geometry.py'
# Then imported like: from geometry import calculate_circle_area

print("Custom module functions:")
print(f"Circle area (radius 5): {calculate_circle_area(5):.2f}")
print(f"Rectangle area (4x6): {calculate_rectangle_area(4, 6)}")
print(f"Triangle area (base 8, height 5): {calculate_triangle_area(8, 5)}")

# =============================================================================
# 4. MODULE ATTRIBUTES
# =============================================================================

print("\n📋 MODULE ATTRIBUTES")
print("-" * 22)

def demonstrate_module_attributes():
    """Demonstrate module attributes."""
    print("Module attributes:")
    print(f"Module name: {__name__}")
    print(f"Module file: {__file__}")
    print(f"Module docstring: {__doc__}")
    
    # Get all attributes of math module
    math_attributes = [attr for attr in dir(math) if not attr.startswith('_')]
    print(f"Math module attributes (first 10): {math_attributes[:10]}")

demonstrate_module_attributes()

# =============================================================================
# 5. PACKAGE CREATION
# =============================================================================

print("\n📁 PACKAGE CREATION")
print("-" * 22)

"""
To create a package, you need:

1. Create a directory (e.g., 'mypackage')
2. Add __init__.py file (can be empty)
3. Add modules to the directory
4. Import using package.module syntax

Example structure:
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
"""

# Simulate package structure
class PackageSimulator:
    """Simulate package structure for demonstration."""
    
    def __init__(self):
        self.name = "mypackage"
        self.modules = ["module1", "module2", "subpackage.module3"]
    
    def show_structure(self):
        """Show package structure."""
        print(f"Package: {self.name}")
        print("Structure:")
        print("├── __init__.py")
        print("├── module1.py")
        print("├── module2.py")
        print("└── subpackage/")
        print("    ├── __init__.py")
        print("    └── module3.py")
        
        print(f"\nImport examples:")
        print("from mypackage import module1")
        print("from mypackage.module2 import function_name")
        print("from mypackage.subpackage import module3")

package_sim = PackageSimulator()
package_sim.show_structure()

# =============================================================================
# 6. IMPORT TECHNIQUES
# =============================================================================

print("\n📥 IMPORT TECHNIQUES")
print("-" * 22)

# Different import techniques
print("Import Techniques:")

# 1. Import entire module
print("1. import module_name")
print("   Usage: module_name.function_name()")

# 2. Import specific items
print("2. from module import item")
print("   Usage: item()")

# 3. Import with alias
print("3. import module as alias")
print("   Usage: alias.function_name()")

# 4. Import all items
print("4. from module import *")
print("   Usage: function_name() (not recommended)")

# 5. Import from package
print("5. from package.module import item")
print("   Usage: item()")

# Demonstrate different imports
import sys
from os import path
import json as json_module

print(f"\nPractical examples:")
print(f"System platform: {sys.platform}")
print(f"Current working directory: {path.abspath('.')}")
print(f"JSON module: {json_module.__name__}")

# =============================================================================
# 7. PYTHON PATH AND MODULE SEARCH
# =============================================================================

print("\n🔍 PYTHON PATH AND MODULE SEARCH")
print("-" * 35)

def demonstrate_python_path():
    """Demonstrate Python path and module search."""
    print("Python searches for modules in this order:")
    
    # Current directory
    print("1. Current directory")
    print(f"   Current dir: {path.abspath('.')}")
    
    # PYTHONPATH environment variable
    print("2. PYTHONPATH environment variable")
    pythonpath = sys.path
    print(f"   Python path: {pythonpath[:3]}...")  # Show first 3 items
    
    # Standard library directories
    print("3. Standard library directories")
    print(f"   Standard lib: {sys.prefix}")
    
    # Site-packages directory
    print("4. Site-packages directory")
    print(f"   Site-packages: {sys.path[-1]}")

demonstrate_python_path()

# =============================================================================
# 8. RELATIVE AND ABSOLUTE IMPORTS
# =============================================================================

print("\n📂 RELATIVE AND ABSOLUTE IMPORTS")
print("-" * 40)

print("""
ABSOLUTE IMPORTS:
- Import from the top-level package
- Use full path from project root
- Recommended for most cases

Examples:
from mypackage.module import function
from mypackage.subpackage.module import class_name

RELATIVE IMPORTS:
- Import relative to current module
- Use dots (.) to indicate relative path
- Only work within packages

Examples:
from .module import function          # Same level
from ..parent_module import function  # Parent level
from ...grandparent import function   # Grandparent level
""")

# =============================================================================
# 9. PRACTICAL EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL EXAMPLES")
print("-" * 22)

# Example 1: Math Utilities Package
class MathUtils:
    """Simulate a math utilities module."""
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    @staticmethod
    def power(base, exponent):
        return base ** exponent

# Example 2: String Utilities Package
class StringUtils:
    """Simulate a string utilities module."""
    
    @staticmethod
    def reverse_string(text):
        return text[::-1]
    
    @staticmethod
    def count_vowels(text):
        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)
    
    @staticmethod
    def is_palindrome(text):
        cleaned = text.lower().replace(" ", "")
        return cleaned == cleaned[::-1]
    
    @staticmethod
    def capitalize_words(text):
        return " ".join(word.capitalize() for word in text.split())

# Example 3: Data Processing Package
class DataProcessor:
    """Simulate a data processing module."""
    
    @staticmethod
    def find_max(numbers):
        if not numbers:
            return None
        return max(numbers)
    
    @staticmethod
    def find_min(numbers):
        if not numbers:
            return None
        return min(numbers)
    
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return None
        return sum(numbers) / len(numbers)
    
    @staticmethod
    def remove_duplicates(items):
        return list(set(items))

# Demonstrate the modules
print("Math Utilities:")
print(f"Add: {MathUtils.add(5, 3)}")
print(f"Power: {MathUtils.power(2, 3)}")

print("\nString Utilities:")
text = "Hello World"
print(f"Reverse: {StringUtils.reverse_string(text)}")
print(f"Vowels: {StringUtils.count_vowels(text)}")
print(f"Palindrome: {StringUtils.is_palindrome('racecar')}")

print("\nData Processing:")
numbers = [1, 5, 3, 9, 2, 5, 8]
print(f"Numbers: {numbers}")
print(f"Max: {DataProcessor.find_max(numbers)}")
print(f"Min: {DataProcessor.find_min(numbers)}")
print(f"Average: {DataProcessor.calculate_average(numbers):.2f}")
print(f"Unique: {DataProcessor.remove_duplicates(numbers)}")

# =============================================================================
# 10. MODULE TESTING
# =============================================================================

print("\n🧪 MODULE TESTING")
print("-" * 20)

def test_math_utils():
    """Test MathUtils module."""
    print("Testing MathUtils:")
    
    # Test addition
    assert MathUtils.add(2, 3) == 5, "Addition test failed"
    print("✅ Addition test passed")
    
    # Test division
    assert MathUtils.divide(10, 2) == 5, "Division test failed"
    print("✅ Division test passed")
    
    # Test power
    assert MathUtils.power(2, 3) == 8, "Power test failed"
    print("✅ Power test passed")
    
    # Test error handling
    try:
        MathUtils.divide(10, 0)
        print("❌ Division by zero test failed")
    except ValueError:
        print("✅ Division by zero test passed")

def test_string_utils():
    """Test StringUtils module."""
    print("\nTesting StringUtils:")
    
    # Test reverse
    assert StringUtils.reverse_string("hello") == "olleh", "Reverse test failed"
    print("✅ Reverse test passed")
    
    # Test palindrome
    assert StringUtils.is_palindrome("racecar") == True, "Palindrome test failed"
    print("✅ Palindrome test passed")
    
    # Test vowel count
    assert StringUtils.count_vowels("hello") == 2, "Vowel count test failed"
    print("✅ Vowel count test passed")

# Run tests
test_math_utils()
test_string_utils()

# =============================================================================
# 11. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice modules and packages:

Exercise 1: Create a Calculator Module
- Create a calculator.py module
- Add functions for basic operations
- Import and use in another file
- Add error handling for division by zero

Exercise 2: Build a Text Processing Package
- Create a text_utils package
- Add modules for different text operations
- Include functions for formatting, validation
- Create a main module that uses all utilities

Exercise 3: Design a Data Analysis Package
- Create a data_analysis package
- Add modules for statistics, visualization
- Include functions for data cleaning
- Create example usage scripts

Exercise 4: Build a Configuration Manager
- Create a config module
- Handle different configuration formats
- Support environment variables
- Provide default values

Exercise 5: Create a Logging Package
- Build a custom logging package
- Support different log levels
- Include file and console output
- Add timestamp and formatting features
""")

# =============================================================================
# 12. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
Module and package best practices:

1. Use descriptive names
   ✅ user_authentication.py
   ❌ auth.py

2. Keep modules focused
   ✅ One responsibility per module
   ❌ Everything in one module

3. Use __init__.py effectively
   ✅ Control what gets imported
   ❌ Empty __init__.py files

4. Avoid circular imports
   ✅ Design clear dependencies
   ❌ Module A imports B, B imports A

5. Use absolute imports
   ✅ from mypackage.module import function
   ❌ from .module import function (unless necessary)

6. Document your modules
   ✅ """Module docstring"""
   ❌ No documentation

7. Use __all__ to control exports
   ✅ __all__ = ['function1', 'function2']
   ❌ Export everything with *

8. Organize related functionality
   ✅ Group related functions in modules
   ❌ Random function placement
""")

# =============================================================================
# 13. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common module and package mistakes:

1. Circular imports
   ❌ Module A imports B, B imports A
   ✅ Design clear dependency hierarchy

2. Using import * everywhere
   ❌ from module import *
   ✅ from module import specific_function

3. Not using __init__.py
   ❌ Package without __init__.py
   ✅ Always include __init__.py

4. Confusing relative and absolute imports
   ❌ from ..module import function (outside package)
   ✅ from package.module import function

5. Not handling import errors
   ❌ import module  # Can fail
   ✅ try: import module except ImportError: handle_error()

6. Creating too many small modules
   ❌ One function per module
   ✅ Group related functions together

7. Not using virtual environments
   ❌ Installing packages globally
   ✅ Use virtual environments for projects
""")

# =============================================================================
# 14. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ How to use built-in modules effectively
✅ How to create your own modules and packages
✅ Different import techniques and when to use them
✅ Python path and module search order
✅ Relative vs absolute imports
✅ Best practices for organizing code
✅ Common mistakes to avoid

Next Steps:
- Day 10: Advanced Data Structures
- Day 11: Regular Expressions
- Day 12: Working with APIs
""")

# =============================================================================
# 15. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 9 of your Python journey!

You now understand:
- How to organize code with modules and packages
- Different import techniques and their uses
- How to create reusable components
- Best practices for code organization
- How to avoid common mistakes

Modules and packages are essential for building large applications!
Practice with the exercises to master this important skill.

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 9: Modules and Packages Tutorial")
    print("Run this file to see all examples in action!")
