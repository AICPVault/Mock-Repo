"""
Day 2: Operators, Conditionals, and Input/Output
===============================================

Building on Day 1, today we'll learn about operators, conditional statements,
and how to interact with users through input and output.

Learning Objectives:
- Master Python operators (arithmetic, comparison, logical)
- Understand conditional statements (if, elif, else)
- Learn about input/output operations
- Practice decision-making in code
- Build interactive programs

Let's continue our Python journey!
"""

print("🐍 Welcome to Day 2: Operators, Conditionals, and I/O!")
print("=" * 60)

# =============================================================================
# 1. ARITHMETIC OPERATORS
# =============================================================================

print("\n➕ ARITHMETIC OPERATORS")
print("-" * 25)

# Basic arithmetic operations
a = 10
b = 3

print("Basic Arithmetic Operations:")
print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Assignment operators
print("\nAssignment Operators:")
x = 5
print(f"Initial x: {x}")
x += 3  # x = x + 3
print(f"After x += 3: {x}")
x -= 2  # x = x - 2
print(f"After x -= 2: {x}")
x *= 2  # x = x * 2
print(f"After x *= 2: {x}")
x /= 4  # x = x / 4
print(f"After x /= 4: {x}")

# =============================================================================
# 2. COMPARISON OPERATORS
# =============================================================================

print("\n🔍 COMPARISON OPERATORS")
print("-" * 25)

# Comparison operators return True or False
num1 = 10
num2 = 5

print("Comparison Operations:")
print(f"num1 = {num1}, num2 = {num2}")
print(f"Equal (==): {num1} == {num2} = {num1 == num2}")
print(f"Not Equal (!=): {num1} != {num2} = {num1 != num2}")
print(f"Greater Than (>): {num1} > {num2} = {num1 > num2}")
print(f"Less Than (<): {num1} < {num2} = {num1 < num2}")
print(f"Greater or Equal (>=): {num1} >= {num2} = {num1 >= num2}")
print(f"Less or Equal (<=): {num1} <= {num2} = {num1 <= num2}")

# String comparisons
name1 = "Alice"
name2 = "Bob"
print(f"\nString Comparisons:")
print(f"'{name1}' == '{name2}': {name1 == name2}")
print(f"'{name1}' < '{name2}': {name1 < name2}")  # Alphabetical order

# =============================================================================
# 3. LOGICAL OPERATORS
# =============================================================================

print("\n🧠 LOGICAL OPERATORS")
print("-" * 22)

# Logical operators: and, or, not
age = 25
has_license = True
has_car = False

print("Logical Operations:")
print(f"age = {age}, has_license = {has_license}, has_car = {has_car}")
print(f"age >= 18 and has_license: {age >= 18 and has_license}")
print(f"has_license or has_car: {has_license or has_car}")
print(f"not has_car: {not has_car}")
print(f"age >= 18 and has_license and has_car: {age >= 18 and has_license and has_car}")

# Complex logical expressions
is_weekend = False
is_holiday = True
print(f"\nComplex Logic:")
print(f"is_weekend = {is_weekend}, is_holiday = {is_holiday}")
print(f"is_weekend or is_holiday: {is_weekend or is_holiday}")
print(f"not (is_weekend or is_holiday): {not (is_weekend or is_holiday)}")

# =============================================================================
# 4. CONDITIONAL STATEMENTS (IF, ELIF, ELSE)
# =============================================================================

print("\n🔀 CONDITIONAL STATEMENTS")
print("-" * 30)

# Basic if statement
score = 85
print(f"Score: {score}")

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Multiple conditions
temperature = 75
is_sunny = True

print(f"\nWeather: Temperature = {temperature}°F, Sunny = {is_sunny}")

if temperature > 80 and is_sunny:
    print("Perfect beach weather!")
elif temperature > 70 and is_sunny:
    print("Nice day for a walk!")
elif temperature > 60:
    print("Pleasant weather!")
else:
    print("Stay warm!")

# Nested conditions
age = 20
has_id = True
has_money = True

print(f"\nAge: {age}, Has ID: {has_id}, Has Money: {has_money}")

if age >= 18:
    if has_id:
        if has_money:
            print("Welcome! You can enter and buy drinks.")
        else:
            print("You can enter but need money for drinks.")
    else:
        print("You need an ID to enter.")
else:
    print("Sorry, you must be 18 or older.")

# =============================================================================
# 5. INPUT AND OUTPUT
# =============================================================================

print("\n💬 INPUT AND OUTPUT")
print("-" * 22)

# Basic input (commented out to avoid blocking execution)
print("Input Examples (commented out to avoid blocking):")
print("# name = input('Enter your name: ')")
print("# age = int(input('Enter your age: '))")
print("# print(f'Hello {name}, you are {age} years old!')")

# Simulated input for demonstration
def demonstrate_input():
    """Demonstrate input operations."""
    # Simulating user input
    name = "Alice"  # input('Enter your name: ')
    age = 25  # int(input('Enter your age: '))
    
    print(f"Hello {name}, you are {age} years old!")
    
    if age >= 18:
        print("You are an adult!")
    else:
        print("You are a minor!")

demonstrate_input()

# Formatted output
print("\nFormatted Output Examples:")
name = "John"
age = 30
height = 5.9

# f-string formatting (recommended)
print(f"Name: {name}, Age: {age}, Height: {height}")

# .format() method
print("Name: {}, Age: {}, Height: {}".format(name, age, height))

# % formatting (older style)
print("Name: %s, Age: %d, Height: %.1f" % (name, age, height))

# =============================================================================
# 6. PRACTICAL EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL EXAMPLES")
print("-" * 22)

# Example 1: Grade Calculator
def grade_calculator():
    """Calculate and display grade based on score."""
    score = 87
    
    print(f"Grade Calculator:")
    print(f"Score: {score}")
    
    if score >= 90:
        grade = "A"
        message = "Excellent work!"
    elif score >= 80:
        grade = "B"
        message = "Good job!"
    elif score >= 70:
        grade = "C"
        message = "Satisfactory!"
    elif score >= 60:
        grade = "D"
        message = "Needs improvement!"
    else:
        grade = "F"
        message = "Failed!"
    
    print(f"Grade: {grade}")
    print(f"Message: {message}")

grade_calculator()

# Example 2: Shopping Cart with Discounts
def shopping_cart():
    """Calculate total with discounts."""
    item_price = 100
    quantity = 3
    is_member = True
    is_weekend = False
    
    subtotal = item_price * quantity
    discount = 0
    
    print(f"Shopping Cart:")
    print(f"Item Price: ${item_price}")
    print(f"Quantity: {quantity}")
    print(f"Subtotal: ${subtotal}")
    
    # Apply discounts
    if is_member and is_weekend:
        discount = 0.20  # 20% discount
        print("Member + Weekend discount: 20%")
    elif is_member:
        discount = 0.10  # 10% discount
        print("Member discount: 10%")
    elif is_weekend:
        discount = 0.05  # 5% discount
        print("Weekend discount: 5%")
    
    discount_amount = subtotal * discount
    total = subtotal - discount_amount
    
    print(f"Discount: ${discount_amount:.2f}")
    print(f"Total: ${total:.2f}")

shopping_cart()

# Example 3: Age-based Access Control
def access_control():
    """Demonstrate age-based access control."""
    age = 16
    has_parental_consent = True
    is_weekend = True
    
    print(f"Access Control:")
    print(f"Age: {age}")
    print(f"Parental Consent: {has_parental_consent}")
    print(f"Weekend: {is_weekend}")
    
    if age >= 18:
        print("Access: Full access granted!")
    elif age >= 16 and has_parental_consent:
        print("Access: Limited access with parental consent!")
    elif age >= 13:
        print("Access: Restricted access for minors!")
    else:
        print("Access: No access - too young!")
    
    # Additional weekend restrictions
    if age < 18 and is_weekend:
        print("Note: Weekend access requires adult supervision!")

access_control()

# =============================================================================
# 7. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice what you've learned:

Exercise 1: Create a BMI Calculator
- Ask for height and weight
- Calculate BMI
- Display BMI category (Underweight, Normal, Overweight, Obese)

Exercise 2: Build a Simple Calculator
- Ask for two numbers and an operation (+, -, *, /)
- Perform the calculation
- Display the result

Exercise 3: Create a Password Checker
- Ask for a password
- Check if it meets requirements (length, contains numbers, etc.)
- Display appropriate messages

Exercise 4: Build a Weather App
- Ask for temperature
- Ask if it's sunny, rainy, or cloudy
- Provide appropriate clothing suggestions

Exercise 5: Create a Grade System
- Ask for multiple test scores
- Calculate average
- Determine letter grade
- Display detailed report
""")

# =============================================================================
# 8. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common mistakes and how to avoid them:

1. Using = instead of == in conditions
   ❌ if x = 5:  # This assigns 5 to x
   ✅ if x == 5:  # This compares x with 5

2. Forgetting colons after if/elif/else
   ❌ if x > 5
   ✅ if x > 5:

3. Incorrect indentation
   ❌ if x > 5:
   print("Hello")  # Wrong indentation
   ✅ if x > 5:
       print("Hello")  # Correct indentation

4. Not converting input to appropriate type
   ❌ age = input("Enter age: ")  # This is a string
   ✅ age = int(input("Enter age: "))  # Convert to integer

5. Using and/or incorrectly
   ❌ if x > 5 and < 10:  # Wrong syntax
   ✅ if x > 5 and x < 10:  # Correct syntax
""")

# =============================================================================
# 9. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ Arithmetic operators for calculations
✅ Comparison operators for comparisons
✅ Logical operators for complex conditions
✅ Conditional statements (if, elif, else)
✅ Input/output operations
✅ Decision-making in programs
✅ Practical applications of conditionals

Next Steps:
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
You've completed Day 2 of your Python journey!

You now understand:
- How to use operators effectively
- How to make decisions with conditionals
- How to interact with users through input/output
- How to build interactive programs
- How to avoid common mistakes

Keep practicing with the exercises!
The more you code, the better you'll become!

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 2: Operators, Conditionals, and I/O Tutorial")
    print("Run this file to see all examples in action!")
