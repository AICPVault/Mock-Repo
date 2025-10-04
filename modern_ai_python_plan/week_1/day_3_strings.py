"""
Day 3: Strings
==============

Strings are one of the most common data types you'll work with.
Today, we'll explore how to manipulate them effectively using slicing,
methods, and modern formatting techniques.

Learning Objectives:
1.  Understand string creation and indexing.
2.  Master string slicing to extract substrings.
3.  Use common and useful string methods.
4.  Learn modern string formatting with f-strings and template strings.
"""

# =============================================================================
# 1. STRING BASICS & INDEXING
# =============================================================================

# Strings can be created with single, double, or triple quotes.
s1: str = 'Hello, Python!'
s2: str = "Working with strings."
s3: str = """
This is a multi-line string.
It preserves the line breaks.
"""

# Indexing: Accessing individual characters
# Python uses 0-based indexing.
greeting: str = "Hello"
# H e l l o
# 0 1 2 3 4
#-5-4-3-2-1  (Negative indexing from the end)

print(f"First character: {greeting[0]}")  # 'H'
print(f"Third character: {greeting[2]}")  # 'l'
print(f"Last character: {greeting[-1]}")   # 'o'


# =============================================================================
# 2. STRING SLICING
# =============================================================================

# Slicing extracts a portion of the string.
# Syntax: `string[start:stop:step]`
# - `start`: The index to begin the slice (inclusive). Defaults to 0.
# - `stop`: The index to end the slice (exclusive). Defaults to the end.
# - `step`: The amount to jump between characters. Defaults to 1.

data: str = "0123456789"

# Get a substring from index 2 up to (but not including) index 5
print(f"Slice [2:5]: {data[2:5]}")  # "234"

# Get a substring from the beginning up to index 4
print(f"Slice [:4]: {data[:4]}")  # "0123"

# Get a substring from index 5 to the end
print(f"Slice [5:]: {data[5:]}")  # "56789"

# Get every second character
print(f"Slice [::2]: {data[::2]}")  # "02468"

# Reverse a string with a negative step!
print(f"Reversed with slice [::-1]: {data[::-1]}")  # "9876543210"


# =============================================================================
# 3. COMMON STRING METHODS
# =============================================================================

# String methods are functions that run on a string object.
# They are immutable operations - they return a *new* string.

text: str = "  Modern Python is FAST and Readable!  "

# Case manipulation
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")

# Whitespace removal
print(f"Stripped: '{text.strip()}'")  # Removes leading/trailing whitespace
print(f"Left stripped: '{text.lstrip()}'")
print(f"Right stripped: '{text.rstrip()}'")

# Find and replace
print(f"Replace 'FAST' with 'Powerful': {text.replace('FAST', 'Powerful')}")

# Checking content
print(f"Starts with '  Modern': {text.startswith('  Modern')}")  # True
print(f"Ends with '!': {text.endswith('!')}")              # False (due to whitespace)
print(f"Ends with '!  ': {text.endswith('!  ')}")          # True

# Splitting and joining
words: list[str] = text.strip().split(" ")
print(f"Split into words: {words}")

sentence: str = " ".join(words)
print(f"Joined back together: '{sentence}'")


# =============================================================================
# 4. MODERN STRING FORMATTING
# =============================================================================

# --- f-strings (Formatted String Literals) - The standard choice ---
# Introduced in Python 3.6, they are the most common, readable, and performant way.
# Prefix the string with `f` or `F`.

name: str = "Ada"
age: int = 35
pi: float = 3.14159265

# Embed expressions directly inside curly braces `{}`
print(f"User: {name}, Age: {age}")
print(f"Math expression: 5 * 5 = {5*5}")

# You can also control formatting
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Age padded with zeros: {age:04}")  # Pad to 4 digits

# --- Template Strings - For user-supplied templates ---
# Safer for templates that come from user input, as they don't execute arbitrary expressions.
from string import Template

template = Template("Hello, $name! Your ticket number is $ticket.")
formatted_string = template.substitute(name="Bob", ticket=123)
print(formatted_string)

# =============================================================================
# EXERCISES
# =============================================================================

# 1. Filename Extractor:
#    - Given a filename string like `document.pdf` or `image.png`.
#    - Use slicing or a string method to extract and print just the extension (e.g., "pdf", "png").
#    - Hint: `rsplit()` or negative slicing might be useful.

# 2. Formatted User Profile:
#    - Create variables for a user's `first_name`, `last_name`, and `birth_year`.
#    - Calculate their approximate `age`.
#    - Use an f-string to print a message like:
#      "Profile for Smith, John. Age: 34."

# 3. Clean and Normalize Data:
#    - You are given a messy string: `  uSeR_iD | 12345 \n`
#    - Write a chain of string methods to clean it up into `user_id | 12345`.
#    - Steps: remove leading/trailing whitespace, convert to lowercase, replace `_` with a space.

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- Strings are immutable sequences of characters.
- Slicing (`[start:stop:step]`) is a powerful mini-language for extracting substrings.
- String methods (`.upper()`, `.strip()`, `.replace()`, `.split()`) are your tools for manipulation.
- f-strings are the modern, go-to solution for embedding variables and expressions into strings.

Next up: Day 4 - Collections Part I: Lists and Tuples.
"""
