"""
Day 5: Collections II - Dictionaries and Sets
===============================================

Today we move on to two more essential collection types: dictionaries for
key-value storage and sets for unique, unordered items.

Learning Objectives:
1.  Create and manipulate dictionaries (key-value pairs).
2.  Access, add, update, and remove dictionary items.
3.  Iterate over dictionary keys, values, and items.
4.  Understand and use sets for uniqueness and mathematical set operations.
5.  Know when to use a dictionary vs. a set vs. a list.
"""

# =============================================================================
# 1. DICTIONARIES (dict) - KEY-VALUE PAIRS
# =============================================================================

# A dictionary is an unordered (in Python < 3.7) collection of key-value pairs.
# It's mutable and does not allow duplicate keys.
# Created with curly braces `{}` with `key: value` items.

# An empty dictionary
empty_dict: dict = {}

# A dictionary representing a user profile
user_profile: dict[str, str | int | list[str]] = {
    "username": "ada_lovelace",
    "email": "ada@example.com",
    "birth_year": 1815,
    "skills": ["mathematics", "analytics", "programming"],
}
print(f"User profile dictionary: {user_profile}")

# --- Accessing Values ---
# Use the key in square brackets. This will raise a KeyError if the key doesn't exist.
print(f"Username: {user_profile['username']}")

# A safer way is using the .get() method, which returns None (or a default value) if the key is not found.
print(f"Email: {user_profile.get('email')}")
print(f"Location (not present): {user_profile.get('location')}")
print(f"Location with default: {user_profile.get('location', 'London')}")

# --- Adding and Updating Items ---
# Add a new key-value pair
user_profile["location"] = "London"
print(f"After adding location: {user_profile}")

# Update an existing value
user_profile["email"] = "ada.lovelace@newdomain.com"
print(f"After updating email: {user_profile}")

# --- Removing Items ---
# Remove an item by key and return its value
email = user_profile.pop("email")
print(f"Popped email: {email}, Dict is now: {user_profile}")

# --- Iterating over Dictionaries ---
print("\nIterating over the dictionary:")
# Iterate over keys (the default)
for key in user_profile:
    print(f"  Key: {key}, Value: {user_profile[key]}")

# Iterate over values
for value in user_profile.values():
    print(f"  Value: {value}")

# Iterate over key-value pairs (items) - the most common way
for key, value in user_profile.items():
    print(f"  Item: {key} -> {value}")


# =============================================================================
# 2. SETS - UNIQUE, UNORDERED COLLECTIONS
# =============================================================================

# A set is an unordered, mutable collection with no duplicate elements.
# Created with curly braces `{}` or the `set()` function.
# Note: To create an empty set, you MUST use `set()`, because `{}` creates an empty dictionary.

# Creating a set from a list to get unique items
numbers: list[int] = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers: set[int] = set(numbers)
print(f"\nUnique numbers from list: {unique_numbers}")

# --- Set Operations ---
# Add an item
unique_numbers.add(6)
print(f"After adding 6: {unique_numbers}")
unique_numbers.add(1) # Adding an existing item does nothing
print(f"After adding 1 again: {unique_numbers}")

# Remove an item
unique_numbers.remove(3) # Raises KeyError if not found
print(f"After removing 3: {unique_numbers}")
unique_numbers.discard(10) # Does NOT raise an error if not found

# --- Mathematical Set Operations ---
# These are incredibly fast and useful.
set_a: set[int] = {1, 2, 3, 4}
set_b: set[int] = {3, 4, 5, 6}

# Union: items present in either set
print(f"Union (A | B): {set_a | set_b}")

# Intersection: items present in both sets
print(f"Intersection (A & B): {set_a & set_b}")

# Difference: items in A but not in B
print(f"Difference (A - B): {set_a - set_b}")

# Symmetric Difference: items in A or B, but not both
print(f"Symmetric Difference (A ^ B): {set_a ^ set_b}")

# Use case: Quickly find the difference between two lists
required_skills = {"python", "git", "sql"}
user_skills = {"python", "docker"}
missing_skills = required_skills - user_skills
print(f"Missing skills: {missing_skills}")


# =============================================================================
# EXERCISES
# =============================================================================

# 1. Configuration Manager:
#    - Create a dictionary to hold application settings.
#    - Include keys like `theme` (e.g., "dark"), `font_size` (e.g., 14), and `show_toolbar` (e.g., True).
#    - Use the `.get()` method to safely access a `language` setting, providing "en" as a default.
#    - Update the `font_size` to 16.
#    - Print all the key-value pairs in the final configuration.

# 2. Tag Uniqueness:
#    - You are given a list of tags for a blog post, with duplicates:
#      `tags = ["python", "ai", "machine learning", "python", "fastapi"]`
#    - Create a set from this list to get the unique tags.
#    - Add a new tag, "webdev".
#    - Check if the tag "docker" is in the set of tags.
#    - Print the final set of unique tags.

# 3. User Permissions:
#    - Define two sets of permissions: `admin_permissions` and `editor_permissions`.
#      - `admin`: {"create_user", "delete_user", "edit_content"}
#      - `editor`: {"edit_content", "view_analytics"}
#    - Find the permissions that both roles have in common (intersection).
#    - Find all possible permissions across both roles (union).
#    - Find the permissions that are unique to admins (difference).

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- **Dictionaries** (`{key: value}`) are for storing data by a unique key. Extremely fast for lookups.
- **Sets** (`{item1, item2}`) are for storing unique items and performing mathematical set logic.
- Dictionaries are the backbone of many Python applications (e.g., JSON data).
- Sets are highly optimized for membership testing (`in`) and uniqueness checks.

Next up: Day 6 - Control Flow with if/elif/else and the modern match/case.
"""
