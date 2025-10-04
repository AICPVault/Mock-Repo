"""
Day 11: Regular Expressions (Regex)
===================================

Today we'll learn about Regular Expressions - a powerful tool for pattern matching
and text processing. Regex is essential for data validation, text parsing, and
string manipulation.

Learning Objectives:
- Understand what regular expressions are and why they're useful
- Learn basic regex patterns and syntax
- Master common regex operations in Python
- Practice real-world text processing scenarios
- Build robust pattern matching solutions
- Handle complex text manipulation tasks

Let's master regular expressions!
"""

print("🐍 Welcome to Day 11: Regular Expressions (Regex)!")
print("=" * 60)

import re

# =============================================================================
# 1. WHAT ARE REGULAR EXPRESSIONS?
# =============================================================================

print("\n🔍 WHAT ARE REGULAR EXPRESSIONS?")
print("-" * 35)

"""
Regular Expressions (Regex) are:
- Patterns used to match character combinations in strings
- Powerful tools for text processing and validation
- Used for searching, replacing, and extracting text
- Essential for data cleaning and parsing
- Supported by most programming languages

Common use cases:
- Email validation
- Phone number formatting
- Text extraction from documents
- Data cleaning and preprocessing
- URL parsing and validation
"""

# =============================================================================
# 2. BASIC REGEX PATTERNS
# =============================================================================

print("\n📝 BASIC REGEX PATTERNS")
print("-" * 25)

# Basic character classes
text = "Hello World! 123 Python 456"

print("Basic Character Classes:")
print(f"Text: {text}")

# \d - digits
digits = re.findall(r'\d', text)
print(f"Digits: {digits}")

# \w - word characters (letters, digits, underscore)
word_chars = re.findall(r'\w', text)
print(f"Word characters: {word_chars}")

# \s - whitespace characters
whitespace = re.findall(r'\s', text)
print(f"Whitespace: {whitespace}")

# \D - non-digits
non_digits = re.findall(r'\D', text)
print(f"Non-digits: {non_digits}")

# \W - non-word characters
non_word = re.findall(r'\W', text)
print(f"Non-word characters: {non_word}")

# =============================================================================
# 3. QUANTIFIERS
# =============================================================================

print("\n🔢 QUANTIFIERS")
print("-" * 15)

# Quantifiers specify how many times a pattern should match
sample_text = "aa aaa aaaa aaaaa"

print("Quantifiers:")
print(f"Text: {sample_text}")

# * - zero or more
zero_or_more = re.findall(r'a*', sample_text)
print(f"Zero or more 'a': {zero_or_more}")

# + - one or more
one_or_more = re.findall(r'a+', sample_text)
print(f"One or more 'a': {one_or_more}")

# ? - zero or one
zero_or_one = re.findall(r'a?', sample_text)
print(f"Zero or one 'a': {zero_or_one}")

# {n} - exactly n times
exactly_two = re.findall(r'a{2}', sample_text)
print(f"Exactly 2 'a': {exactly_two}")

# {n,m} - between n and m times
between_two_four = re.findall(r'a{2,4}', sample_text)
print(f"Between 2-4 'a': {between_two_four}")

# =============================================================================
# 4. ANCHORS AND BOUNDARIES
# =============================================================================

print("\n⚓ ANCHORS AND BOUNDARIES")
print("-" * 28)

# Anchors specify position in the string
test_strings = [
    "Hello World",
    "World Hello",
    "Hello",
    "World"
]

print("Anchors and Boundaries:")

for text in test_strings:
    print(f"\nText: '{text}'")
    
    # ^ - start of string
    starts_with_hello = re.search(r'^Hello', text)
    print(f"  Starts with 'Hello': {bool(starts_with_hello)}")
    
    # $ - end of string
    ends_with_world = re.search(r'World$', text)
    print(f"  Ends with 'World': {bool(ends_with_world)}")
    
    # \b - word boundary
    word_hello = re.search(r'\bHello\b', text)
    print(f"  Contains word 'Hello': {bool(word_hello)}")

# =============================================================================
# 5. CHARACTER SETS AND RANGES
# =============================================================================

print("\n📋 CHARACTER SETS AND RANGES")
print("-" * 35)

# Character sets allow matching any character in a set
text = "abc123XYZ!@#"

print("Character Sets:")
print(f"Text: {text}")

# [abc] - any of a, b, or c
abc_chars = re.findall(r'[abc]', text)
print(f"Letters a, b, c: {abc_chars}")

# [a-z] - any lowercase letter
lowercase = re.findall(r'[a-z]', text)
print(f"Lowercase letters: {lowercase}")

# [A-Z] - any uppercase letter
uppercase = re.findall(r'[A-Z]', text)
print(f"Uppercase letters: {uppercase}")

# [0-9] - any digit
digits = re.findall(r'[0-9]', text)
print(f"Digits: {digits}")

# [a-zA-Z0-9] - alphanumeric
alphanumeric = re.findall(r'[a-zA-Z0-9]', text)
print(f"Alphanumeric: {alphanumeric}")

# [^abc] - any character except a, b, or c
not_abc = re.findall(r'[^abc]', text)
print(f"Not a, b, c: {not_abc}")

# =============================================================================
# 6. GROUPS AND CAPTURING
# =============================================================================

print("\n👥 GROUPS AND CAPTURING")
print("-" * 25)

# Groups allow capturing parts of a match
text = "John Doe, Jane Smith, Bob Johnson"

print("Groups and Capturing:")
print(f"Text: {text}")

# Capturing groups with parentheses
names = re.findall(r'(\w+)\s+(\w+)', text)
print(f"Captured names: {names}")

# Named groups
named_groups = re.findall(r'(?P<first>\w+)\s+(?P<last>\w+)', text)
print(f"Named groups: {named_groups}")

# Non-capturing groups
non_capturing = re.findall(r'(?:\w+)\s+(\w+)', text)
print(f"Non-capturing (only last names): {non_capturing}")

# =============================================================================
# 7. COMMON REGEX OPERATIONS
# =============================================================================

print("\n🔧 COMMON REGEX OPERATIONS")
print("-" * 30)

# re.search() - find first match
text = "Contact us at support@example.com or sales@company.com"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

first_email = re.search(email_pattern, text)
print(f"First email found: {first_email.group() if first_email else 'None'}")

# re.findall() - find all matches
all_emails = re.findall(email_pattern, text)
print(f"All emails: {all_emails}")

# re.sub() - replace matches
masked_text = re.sub(email_pattern, '[EMAIL]', text)
print(f"Masked text: {masked_text}")

# re.split() - split by pattern
split_by_spaces = re.split(r'\s+', "Hello    World   Python")
print(f"Split by spaces: {split_by_spaces}")

# =============================================================================
# 8. PRACTICAL EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL EXAMPLES")
print("-" * 22)

# Example 1: Email Validation
def validate_email(email):
    """Validate email format using regex."""
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
    return bool(re.match(pattern, email))

print("Email Validation:")
test_emails = [
    "user@example.com",
    "invalid.email",
    "test@domain.co.uk",
    "not-an-email"
]

for email in test_emails:
    is_valid = validate_email(email)
    print(f"  {email}: {'✅ Valid' if is_valid else '❌ Invalid'}")

# Example 2: Phone Number Formatting
def format_phone_number(phone):
    """Format phone number to standard format."""
    # Remove all non-digits
    digits_only = re.sub(r'\D', '', phone)
    
    # Format as (XXX) XXX-XXXX
    if len(digits_only) == 10:
        return f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    elif len(digits_only) == 11 and digits_only[0] == '1':
        return f"({digits_only[1:4]}) {digits_only[4:7]}-{digits_only[7:]}"
    else:
        return "Invalid phone number"

print(f"\nPhone Number Formatting:")
test_phones = [
    "1234567890",
    "123-456-7890",
    "(123) 456-7890",
    "11234567890",
    "123-45-6789"
]

for phone in test_phones:
    formatted = format_phone_number(phone)
    print(f"  {phone} -> {formatted}")

# Example 3: Text Extraction
def extract_information(text):
    """Extract various information from text."""
    # Extract dates (MM/DD/YYYY or MM-DD-YYYY)
    dates = re.findall(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{4}\b', text)
    
    # Extract phone numbers
    phones = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text)
    
    # Extract URLs
    urls = re.findall(r'https?://[^\s]+', text)
    
    # Extract hashtags
    hashtags = re.findall(r'#\w+', text)
    
    return {
        'dates': dates,
        'phones': phones,
        'urls': urls,
        'hashtags': hashtags
    }

sample_text = """
Contact us at support@example.com or call (555) 123-4567.
Visit our website: https://www.example.com
Meeting scheduled for 12/25/2023 at 2:00 PM.
Follow us on social media #python #programming #tech
"""

extracted = extract_information(sample_text)
print(f"\nText Extraction:")
print(f"  Dates: {extracted['dates']}")
print(f"  Phones: {extracted['phones']}")
print(f"  URLs: {extracted['urls']}")
print(f"  Hashtags: {extracted['hashtags']}")

# =============================================================================
# 9. ADVANCED REGEX PATTERNS
# =============================================================================

print("\n🚀 ADVANCED REGEX PATTERNS")
print("-" * 30)

# Lookahead and lookbehind assertions
text = "password123 secret456 key789"

print("Lookahead and Lookbehind:")
print(f"Text: {text}")

# Positive lookahead - match word followed by digits
words_with_digits = re.findall(r'\w+(?=\d)', text)
print(f"Words followed by digits: {words_with_digits}")

# Negative lookahead - match word not followed by digits
words_without_digits = re.findall(r'\w+(?!\d)', text)
print(f"Words not followed by digits: {words_without_digits}")

# Positive lookbehind - match digits preceded by word
digits_after_words = re.findall(r'(?<=\w)\d+', text)
print(f"Digits after words: {digits_after_words}")

# =============================================================================
# 10. REGEX FLAGS
# =============================================================================

print("\n🚩 REGEX FLAGS")
print("-" * 15)

# Different flags for regex operations
text = "Hello World\nPython Programming\nRegular Expressions"

print("Regex Flags:")
print(f"Text: {repr(text)}")

# re.IGNORECASE (re.I) - case insensitive
case_insensitive = re.findall(r'python', text, re.IGNORECASE)
print(f"Case insensitive 'python': {case_insensitive}")

# re.MULTILINE (re.M) - ^ and $ match start/end of each line
multiline = re.findall(r'^[A-Z]\w+', text, re.MULTILINE)
print(f"Words starting with capital (multiline): {multiline}")

# re.DOTALL (re.S) - . matches newline
dotall = re.findall(r'Hello.*Programming', text, re.DOTALL)
print(f"Dotall match: {dotall}")

# re.VERBOSE (re.X) - ignore whitespace and comments
verbose_pattern = re.compile(r'''
    \b          # Word boundary
    [A-Za-z]+   # One or more letters
    \s+         # One or more spaces
    [A-Za-z]+   # One or more letters
    \b          # Word boundary
''', re.VERBOSE)

verbose_matches = verbose_pattern.findall(text)
print(f"Verbose pattern matches: {verbose_matches}")

# =============================================================================
# 11. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice regular expressions:

Exercise 1: Create a Password Validator
- At least 8 characters
- Contains uppercase and lowercase letters
- Contains at least one digit
- Contains at least one special character

Exercise 2: Build a Text Cleaner
- Remove extra whitespace
- Remove special characters except letters and numbers
- Convert to lowercase
- Remove duplicate words

Exercise 3: Create a Log Parser
- Extract IP addresses from log entries
- Extract timestamps
- Extract error messages
- Count different log levels

Exercise 4: Build a Data Extractor
- Extract phone numbers in various formats
- Extract email addresses
- Extract URLs
- Extract credit card numbers (masked)

Exercise 5: Create a Text Formatter
- Format phone numbers consistently
- Format dates consistently
- Remove HTML tags
- Extract text from HTML
""")

# =============================================================================
# 12. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
Regex best practices:

1. Use raw strings (r'pattern')
   ✅ r'\d+' 
   ❌ '\\d+'

2. Compile patterns for reuse
   ✅ pattern = re.compile(r'\d+')
   ❌ re.findall(r'\d+', text) every time

3. Use specific patterns
   ✅ r'^\d{3}-\d{3}-\d{4}$' for phone
   ❌ r'.*' for everything

4. Test your patterns thoroughly
   ✅ Test with various inputs
   ❌ Assume patterns work

5. Use named groups for clarity
   ✅ r'(?P<year>\d{4})-(?P<month>\d{2})'
   ❌ r'(\d{4})-(\d{2})'

6. Handle edge cases
   ✅ Empty strings, None values
   ❌ Ignore potential errors

7. Document complex patterns
   ✅ Add comments for complex regex
   ❌ Leave patterns unexplained

8. Consider performance
   ✅ Use appropriate quantifiers
   ❌ Use overly complex patterns
""")

# =============================================================================
# 13. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common regex mistakes and how to avoid them:

1. Greedy vs non-greedy matching
   ❌ r'<.*>' (greedy - matches too much)
   ✅ r'<.*?>' (non-greedy - matches minimum)

2. Not escaping special characters
   ❌ r'1.2.3.4' (matches any character)
   ✅ r'1\.2\.3\.4' (matches literal dots)

3. Using . instead of \.
   ❌ r'file.txt' (matches fileXtxt)
   ✅ r'file\.txt' (matches file.txt)

4. Not anchoring patterns
   ❌ r'\d+' (matches anywhere)
   ✅ r'^\d+$' (matches entire string)

5. Overusing .*
   ❌ r'.*pattern.*' (inefficient)
   ✅ r'pattern' (more efficient)

6. Not handling case sensitivity
   ❌ r'Python' (case sensitive)
   ✅ r'Python' with re.IGNORECASE flag

7. Not testing edge cases
   ❌ Only testing happy path
   ✅ Test empty strings, special characters
""")

# =============================================================================
# 14. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ Basic regex patterns and syntax
✅ Quantifiers and anchors
✅ Character sets and groups
✅ Common regex operations in Python
✅ Practical text processing examples
✅ Advanced patterns and flags
✅ Best practices for regex usage
✅ Common mistakes to avoid

Next Steps:
- Day 12: Web Scraping and APIs
- Day 13: Data Analysis with Pandas
- Day 14: Web Development with Flask
- Day 15: Testing and Debugging
""")

# =============================================================================
# 15. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 11 of your Python journey!

You now understand:
- How to use regular expressions for pattern matching
- Common regex patterns and their uses
- How to process and validate text data
- Advanced regex techniques and flags
- Best practices for efficient regex usage

Regular expressions are powerful tools for text processing!
Practice with the exercises to master this essential skill.

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 11: Regular Expressions Tutorial")
    print("Run this file to see all examples in action!")
