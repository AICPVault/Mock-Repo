"""
WEEK 1 PYTHON FOUNDATIONS - KNOWLEDGE TEST
==========================================
Complete all sections below. Test your knowledge without looking up answers!

INSTRUCTIONS:
- Write your answers directly in this file
- Run the code to check some answers automatically
- Some questions require written responses in comments
"""
from audioop import reverse

from day_wise_learning.day10_advanced_data_structures import dict2

# ============================================================================
# SECTION 1: SETUP & MODERN PYTHON (Day 1)
# ============================================================================

# Q1.1: What Python version features are you using? (Write answer as comment)
# Answer: 3.12.7

# Q1.2: What is the main advantage of uv over pip?
# Answer: 

# Q1.3: What does the Ruff extension do in VS Code?
# Answer: 


# ============================================================================
# SECTION 2: VARIABLES & TYPE HINTS (Day 2)
# ============================================================================

# Q2.1: Add modern type hints (Python 3.12+ syntax) to these variables
name = "Alice"
age = 25
scores = [95, 87, 92]
user_data = {"id": 1, "active": True}

name: str = "Alice"
age: int = 25
scores: list[int] = [95, 87, 92]
user_data: dict[str,int|bool] = {"id": 1, "active": True}


# Q2.2: Which of these are MUTABLE? Write True or False
# list_is_mutable = True
# tuple_is_mutable = False
# dict_is_mutable = True
# str_is_mutable = True
# set_is_mutable = False

# Q2.3: Fix this code - explain what's wrong in a comment
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list
#Nothing is wrong in this function, in the second argument instead of empty paranthesis it can also be given as None.

# Q2.4: Use Python 3.12+ generics syntax to type hint this function
def get_first_item(items):
    return items[0] if items else None


# ============================================================================
# SECTION 3: STRINGS (Day 3)
# ============================================================================

text = "Python Programming"

# Q3.1: Extract "Program" using slicing
words: list[str] = text.split(' ')
print(words)
final_word = words[1]
print(final_word)
result_3_1 = final_word[0:7]
print(result_3_1)

# Q3.2: Convert to "PYTHON programming" using methods
result_3_2 = None

# Q3.3: Create an f-string that outputs: "Language: Python, Length: 18"
text = "Python Programming"
language = text[0:6]
text_len = len(text)
result_3_3 = f"Language: {language}, Length: {text_len}"
print(result_3_3)

# Q3.4: Use a template string for: "Hello, {name}! You have {count} messages."
from string import Template
# Create template and substitute name="Bob", count=5
from string import Template
result_3_4 = None

# Q3.5: Split this into words and join with hyphens
sentence = "Learn Python every day"
words: list[str] = sentence.split(" ")
final_string = ''
for index,item in enumerate(words):
    if index == 0:
        final_string = item
    else:
        final_string = final_string + "-" + item
print(final_string)
result_3_5 = final_string



# ============================================================================
# SECTION 4: COLLECTIONS I - Lists & Tuples (Day 4)
# ============================================================================

numbers = [10, 20, 30, 40, 50]
nested = [[1, 2], [3, 4], [5, 6]]

# Q4.1: Get the last 3 numbers using slicing
result_4_1 = numbers[-3:]
print(result_4_1)

# Q4.2: Reverse the list using slicing
result_4_2 = None
print(result_4_2)

# Q4.3: Get every second element
result_4_3 = numbers[0:5:2]
print(result_4_3)

# Q4.4: Access the number 4 from nested list
result_4_4 = nested[1][1]

# Q4.5: Create a tuple with values 100, 200, 300 and try to change the first element
# What happens? Write your answer as a comment
my_tuple: tuple[int] = (100,200,300)
my_tuple(0) = 500
# Answer: SyntaxError: cannot assign to function call here

# Q4.6: Unpack this tuple into three variables a, b, c
coordinates = (10, 20, 30)
# Your code here
a=coordinates[0]
b=coordinates[1]
c=coordinates[2]

print(a)
print(b)
print(c)

# ============================================================================
# SECTION 5: COLLECTIONS II - Dicts & Sets (Day 5)
# ============================================================================

# Q5.1: Create a dictionary with keys: 'name', 'age', 'city' 
# Values: 'Emma', 28, 'Paris'
person: dict[str,int|str] = {'name' : 'Emma', 'age' : 28, 'city' : 'Paris'}
print(person)

# Q5.2: Add a new key 'country' with value 'France'
# Your code here
person.__setitem__('country','France')
print(person)

# Q5.3: Get 'email' with a default value 'no-email@example.com' if it doesn't exist
result_5_3 = person.__getitem__("email")
print(person)

# Q5.4: Merge these two dictionaries (Python 3.9+ syntax)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
result_5_4 = dict1 + dict2

# Q5.5: Create two sets and find their intersection
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
result_5_5 = set_a.intersection(set_b)

# Q5.6: Remove duplicates from this list using a set, keep order
numbers_with_dupes = [1, 2, 2, 3, 4, 4, 5, 1]
result_5_6 = None


# ============================================================================
# SECTION 6: CONTROL FLOW (Day 6)
# ============================================================================

# Q6.1: Write an if/elif/else that categorizes a score (0-100)
# 90-100: 'A', 80-89: 'B', 70-79: 'C', 60-69: 'D', below 60: 'F'
def get_grade(score: int) -> str:
    pass  # Your code here

# Q6.2: Use match/case (Python 3.10+) to handle these HTTP status codes
# 200: 'Success', 404: 'Not Found', 500: 'Server Error', default: 'Unknown'
def describe_status(code: int) -> str:
    pass  # Your code here

# Q6.3: Use a ternary expression to return "Even" or "Odd"
def check_parity(num: int) -> str:
    pass  # Your code here

# Q6.4: Write match/case with guard clauses
# If number is positive and even: 'Positive Even'
# If number is positive and odd: 'Positive Odd'
# If number is negative: 'Negative'
# If number is zero: 'Zero'
def classify_number(num: int) -> str:
    pass  # Your code here


# ============================================================================
# SECTION 7: LOOPS (Day 7)
# ============================================================================

# Q7.1: Use enumerate to print index and value
fruits = ['apple', 'banana', 'cherry']
# Write loop here that prints: "0: apple", "1: banana", "2: cherry"
for index,item in fruits:
    print(f"{index}: {item}")


# Q7.2: Use zip to combine these lists into tuples
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
# Create list of tuples: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
result_7_2 = zip(names,ages)

# Q7.3: Use a for loop with break to find first number > 50
numbers_7_3 = [10, 25, 30, 55, 60, 75]
# Your code here
for i in numbers_7_3:
    if i > 50:
        break
    else:
        continue

# Q7.4: Use continue to print only odd numbers
numbers_7_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Your code here
for i in numbers_7_4:
    if i % 3 == 0:
        print(f"{i} is a odd number")
    else:
        continue

# Q7.5: Use while loop to find first power of 2 greater than 1000
# Your code here
i = 1
number = 0
while (i <= 1000):
    if ((2 ** i) > 1000):
        number = 2 ** i
        break
    else:
        i += 1
print(number)

# Q7.6: Create a dictionary from two lists using zip
keys = ['name', 'age', 'city']
values = ['David', 32, 'London']
result_7_6 = zip(keys,values)


# ============================================================================
# BONUS CHALLENGES
# ============================================================================

# B1: Write a function that takes a list of integers and returns a dictionary
# with 'even' and 'odd' keys containing lists of even and odd numbers
def separate_even_odd(numbers: list[int]) -> dict[str, list[int]]:
    pass

# B2: Use list comprehension to create a list of squares for even numbers only
numbers_b2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_b2 = None

# B3: Create a nested dictionary representing a school with 2 classes,
# each class having 2 students with name and grade
school = None


# ============================================================================
# AUTO-CHECK SECTION (Run this to check some answers)
# ============================================================================

def check_answers():
    """Run this to verify some of your answers"""
    print("🔍 Checking your answers...\n")
    
    # Check Q3.1
    if 'result_3_1' in globals() and result_3_1 == "Program":
        print("✅ Q3.1 Correct!")
    else:
        print("❌ Q3.1 Incorrect")
    
    # Check Q4.1
    if 'result_4_1' in globals() and result_4_1 == [30, 40, 50]:
        print("✅ Q4.1 Correct!")
    else:
        print("❌ Q4.1 Incorrect")
    
    # Check Q5.5
    if 'result_5_5' in globals() and result_5_5 == {4, 5}:
        print("✅ Q5.5 Correct!")
    else:
        print("❌ Q5.5 Incorrect")
    
    # Check Q6.3
    if 'check_parity' in globals():
        if check_parity(4) == "Even" and check_parity(7) == "Odd":
            print("✅ Q6.3 Correct!")
        else:
            print("❌ Q6.3 Incorrect")
    
    print("\n📝 Check your other answers manually!")

# Uncomment to run checks:
# check_answers()