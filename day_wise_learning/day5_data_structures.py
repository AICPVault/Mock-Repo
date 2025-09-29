"""
Day 5: Data Structures - Lists, Tuples, Sets, and Dictionaries
==============================================================

Today we'll explore Python's powerful data structures. These are essential
for organizing and manipulating data in your programs. We'll learn about
lists, tuples, sets, and dictionaries - each with their unique characteristics
and use cases.

Learning Objectives:
- Master Python lists and their operations
- Understand tuples and their immutability
- Learn about sets and set operations
- Explore dictionaries and key-value pairs
- Practice working with nested data structures
- Build programs that handle complex data

Let's dive into the world of data structures!
"""

print("🐍 Welcome to Day 5: Data Structures!")
print("=" * 50)

# =============================================================================
# 1. WHAT ARE DATA STRUCTURES?
# =============================================================================

print("\n📊 WHAT ARE DATA STRUCTURES?")
print("-" * 30)

"""
Data structures are ways of organizing and storing data in a computer
so that it can be accessed and modified efficiently.

Python's main data structures:
- Lists: Ordered, mutable collections
- Tuples: Ordered, immutable collections
- Sets: Unordered, unique collections
- Dictionaries: Key-value pairs

Each has its own characteristics and use cases!
"""

# =============================================================================
# 2. LISTS - ORDERED AND MUTABLE
# =============================================================================

print("\n📋 LISTS - ORDERED AND MUTABLE")
print("-" * 35)

# Creating lists
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")

# List operations
print(f"\nList Operations:")
print(f"Length: {len(fruits)}")
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")

# Modifying lists
fruits.append("kiwi")
print(f"After append('kiwi'): {fruits}")

fruits.insert(1, "mango")
print(f"After insert(1, 'mango'): {fruits}")

fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

popped = fruits.pop()
print(f"After pop(): {fruits}, popped: {popped}")

# List methods
print(f"\nList Methods:")
print(f"Index of 'orange': {fruits.index('orange')}")
print(f"Count of 'apple': {fruits.count('apple')}")
fruits.sort()
print(f"Sorted: {fruits}")
fruits.reverse()
print(f"Reversed: {fruits}")

# =============================================================================
# 3. TUPLES - ORDERED AND IMMUTABLE
# =============================================================================

print("\n📌 TUPLES - ORDERED AND IMMUTABLE")
print("-" * 35)

# Creating tuples
coordinates = (3, 4)
colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma for single-item tuple

print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"Single item: {single_item}")

# Tuple operations
print(f"\nTuple Operations:")
print(f"Length: {len(coordinates)}")
print(f"First item: {coordinates[0]}")
print(f"Last item: {coordinates[-1]}")
print(f"Slice [0:2]: {coordinates[0:2]}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked: x = {x}, y = {y}")

# Tuple methods
print(f"\nTuple Methods:")
print(f"Index of 'green': {colors.index('green')}")
print(f"Count of 'red': {colors.count('red')}")

# Tuples are immutable
# coordinates[0] = 5  # This would cause an error
print("Tuples are immutable - cannot modify after creation")

# =============================================================================
# 4. SETS - UNORDERED AND UNIQUE
# =============================================================================

print("\n🔢 SETS - UNORDERED AND UNIQUE")
print("-" * 30)

# Creating sets
numbers = {1, 2, 3, 4, 5}
colors = {"red", "green", "blue"}
mixed = {1, "hello", 3.14, True}

print(f"Numbers: {numbers}")
print(f"Colors: {colors}")
print(f"Mixed: {mixed}")

# Set operations
print(f"\nSet Operations:")
print(f"Length: {len(numbers)}")
print(f"Contains 3: {3 in numbers}")
print(f"Contains 6: {6 in numbers}")

# Adding and removing elements
numbers.add(6)
print(f"After add(6): {numbers}")

numbers.remove(1)
print(f"After remove(1): {numbers}")

numbers.discard(10)  # Safe remove (no error if not found)
print(f"After discard(10): {numbers}")

# Set methods
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nSet Methods:")
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Difference: {set1.difference(set2)}")
print(f"Symmetric difference: {set1.symmetric_difference(set2)}")

# =============================================================================
# 5. DICTIONARIES - KEY-VALUE PAIRS
# =============================================================================

print("\n📚 DICTIONARIES - KEY-VALUE PAIRS")
print("-" * 35)

# Creating dictionaries
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "is_student": True
}

scores = {"math": 95, "science": 87, "english": 92}

print(f"Person: {person}")
print(f"Scores: {scores}")

# Dictionary operations
print(f"\nDictionary Operations:")
print(f"Length: {len(person)}")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Modifying dictionaries
person["age"] = 26
person["occupation"] = "Engineer"
print(f"After modifications: {person}")

# Dictionary methods
print(f"\nDictionary Methods:")
print(f"Get age: {person.get('age')}")
print(f"Get height (default): {person.get('height', 'Unknown')}")
print(f"Pop age: {person.pop('age')}")
print(f"After pop: {person}")

# =============================================================================
# 6. NESTED DATA STRUCTURES
# =============================================================================

print("\n🔄 NESTED DATA STRUCTURES")
print("-" * 30)

# List of dictionaries
students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 95]},
    {"name": "Charlie", "grades": [78, 85, 80]}
]

print("Students with grades:")
for student in students:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades) / len(grades)
    print(f"  {name}: {grades} (avg: {average:.1f})")

# Dictionary with lists
company = {
    "name": "TechCorp",
    "departments": ["Engineering", "Marketing", "Sales"],
    "employees": {
        "Engineering": ["Alice", "Bob"],
        "Marketing": ["Charlie", "Diana"],
        "Sales": ["Eve", "Frank"]
    }
}

print(f"\nCompany structure:")
print(f"Name: {company['name']}")
print(f"Departments: {company['departments']}")
print(f"Engineering team: {company['employees']['Engineering']}")

# =============================================================================
# 7. PRACTICAL EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL EXAMPLES")
print("-" * 22)

# Example 1: Shopping Cart System
def shopping_cart_system():
    """Demonstrate shopping cart with data structures."""
    cart = []
    inventory = {
        "apple": {"price": 1.50, "stock": 10},
        "banana": {"price": 0.75, "stock": 15},
        "orange": {"price": 2.00, "stock": 8}
    }
    
    # Add items to cart
    cart.append({"item": "apple", "quantity": 3})
    cart.append({"item": "banana", "quantity": 5})
    
    print("Shopping Cart:")
    total = 0
    for item in cart:
        name = item["item"]
        quantity = item["quantity"]
        price = inventory[name]["price"]
        item_total = price * quantity
        total += item_total
        print(f"  {name}: {quantity} x ${price} = ${item_total:.2f}")
    
    print(f"  Total: ${total:.2f}")

shopping_cart_system()

# Example 2: Student Grade Manager
def student_grade_manager():
    """Manage student grades using data structures."""
    students = {
        "Alice": {"math": 95, "science": 87, "english": 92},
        "Bob": {"math": 78, "science": 85, "english": 88},
        "Charlie": {"math": 92, "science": 90, "english": 85}
    }
    
    print("\nStudent Grade Manager:")
    for name, grades in students.items():
        average = sum(grades.values()) / len(grades)
        print(f"  {name}: {grades} (avg: {average:.1f})")
    
    # Find top student
    top_student = max(students.items(), key=lambda x: sum(x[1].values()) / len(x[1]))
    print(f"  Top student: {top_student[0]} with average {sum(top_student[1].values()) / len(top_student[1]):.1f}")

student_grade_manager()

# Example 3: Word Frequency Counter
def word_frequency_counter():
    """Count word frequencies in text."""
    text = "hello world hello python world python hello"
    words = text.split()
    
    # Count frequencies
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    print(f"\nWord Frequency Counter:")
    print(f"Text: {text}")
    print(f"Word frequencies: {word_count}")
    
    # Find most common word
    most_common = max(word_count.items(), key=lambda x: x[1])
    print(f"Most common word: '{most_common[0]}' appears {most_common[1]} times")

word_frequency_counter()

# =============================================================================
# 8. DATA STRUCTURE COMPARISON
# =============================================================================

print("\n📊 DATA STRUCTURE COMPARISON")
print("-" * 35)

print("""
Data Structure Comparison:

Lists:
- Ordered: Yes
- Mutable: Yes
- Duplicates: Allowed
- Use cases: Shopping lists, to-do items, sequences

Tuples:
- Ordered: Yes
- Mutable: No
- Duplicates: Allowed
- Use cases: Coordinates, database records, function returns

Sets:
- Ordered: No
- Mutable: Yes
- Duplicates: No
- Use cases: Unique items, membership testing, set operations

Dictionaries:
- Ordered: Yes (Python 3.7+)
- Mutable: Yes
- Duplicates: No (keys only)
- Use cases: User profiles, configurations, mappings
""")

# =============================================================================
# 9. COMMON OPERATIONS
# =============================================================================

print("\n🔧 COMMON OPERATIONS")
print("-" * 20)

# List comprehensions
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]

print(f"List comprehensions:")
print(f"Numbers: {numbers}")
print(f"Squared: {squared}")
print(f"Evens: {evens}")

# Dictionary comprehensions
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
print(f"Word lengths: {word_lengths}")

# Set comprehensions
unique_lengths = {len(word) for word in ["hello", "world", "python", "code"]}
print(f"Unique lengths: {unique_lengths}")

# =============================================================================
# 10. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice what you've learned:

Exercise 1: Create a contact book
- Use a dictionary to store contacts
- Add, remove, and search contacts
- Display all contacts

Exercise 2: Build a simple inventory system
- Use a dictionary to track items and quantities
- Add, remove, and update inventory
- Check stock levels

Exercise 3: Create a word analyzer
- Count word frequencies in text
- Find most common words
- Remove common words (stop words)

Exercise 4: Build a simple database
- Store student records with grades
- Calculate averages and rankings
- Find top performers

Exercise 5: Create a text processor
- Remove duplicates from a list
- Sort items alphabetically
- Group items by category
""")

# =============================================================================
# 11. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
Best practices for data structures:

1. Choose the right data structure for your needs
   ✅ Lists for ordered, mutable data
   ✅ Tuples for immutable data
   ✅ Sets for unique items
   ✅ Dictionaries for key-value pairs

2. Use list comprehensions for simple transformations
   ✅ squared = [x**2 for x in numbers]
   ❌ squared = []
       for x in numbers:
           squared.append(x**2)

3. Use dictionary.get() for safe access
   ✅ value = my_dict.get('key', 'default')
   ❌ value = my_dict['key']  # Can raise KeyError

4. Use sets for membership testing
   ✅ if item in my_set:
   ❌ if item in my_list:  # Slower for large lists

5. Use tuples for function returns
   ✅ return (x, y, z)
   ❌ return [x, y, z]  # Unless you need mutability

6. Document your data structures
   ✅ # Dictionary mapping student names to grades
   ❌ # Some data structure

7. Use meaningful variable names
   ✅ student_grades = {}
   ❌ data = {}
""")

# =============================================================================
# 12. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common mistakes and how to avoid them:

1. Modifying list while iterating
   ❌ for item in my_list:
         my_list.remove(item)
   ✅ for item in my_list.copy():

2. Using mutable default arguments
   ❌ def func(my_list=[]):
   ✅ def func(my_list=None):
         if my_list is None:
             my_list = []

3. Confusing list and tuple syntax
   ❌ my_tuple = (1)  # This is an integer
   ✅ my_tuple = (1,)  # This is a tuple

4. Using lists for membership testing
   ❌ if item in my_list:  # O(n) operation
   ✅ if item in my_set:  # O(1) operation

5. Not handling KeyError in dictionaries
   ❌ value = my_dict['key']  # Can crash
   ✅ value = my_dict.get('key', 'default')

6. Modifying tuples
   ❌ my_tuple[0] = 5  # Tuples are immutable
   ✅ my_list[0] = 5  # Use lists for mutable data
""")

# =============================================================================
# 13. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ Lists are ordered, mutable collections
✅ Tuples are ordered, immutable collections
✅ Sets are unordered, unique collections
✅ Dictionaries store key-value pairs
✅ Each data structure has specific use cases
✅ Nested structures allow complex data organization
✅ List/dictionary comprehensions are powerful tools
✅ Choose the right structure for your needs

Next Steps:
- Practice with the exercises
- Build projects using these data structures
- Explore advanced Python features
""")

# =============================================================================
# 14. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 5 of your Python journey!

You now understand:
- How to work with lists, tuples, sets, and dictionaries
- When to use each data structure
- How to organize complex data
- Best practices for data structure usage
- How to avoid common mistakes

Data structures are the foundation of programming!
Practice with the exercises to master these essential concepts.

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 5: Data Structures Tutorial")
    print("Run this file to see all examples in action!")
