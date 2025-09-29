"""
Day 7: Exception Handling and Error Management
==============================================

Today we'll learn about exception handling in Python - how to handle errors gracefully,
prevent program crashes, and create robust applications that can handle unexpected situations.

Learning Objectives:
- Understand what exceptions are and why they occur
- Learn about try-except blocks and error handling
- Master different types of exceptions
- Practice raising and creating custom exceptions
- Learn about finally blocks and context managers
- Build robust error-handling strategies

Let's master exception handling!
"""

print("🐍 Welcome to Day 7: Exception Handling and Error Management!")
print("=" * 65)

# =============================================================================
# 1. WHAT ARE EXCEPTIONS?
# =============================================================================

print("\n⚠️ WHAT ARE EXCEPTIONS?")
print("-" * 25)

"""
Exceptions are:
- Errors that occur during program execution
- Unexpected events that disrupt normal program flow
- Python's way of handling runtime errors
- Essential for creating robust applications

Common types of exceptions:
- SyntaxError: Code syntax errors
- NameError: Undefined variable names
- TypeError: Wrong data type operations
- ValueError: Wrong value for operation
- IndexError: List index out of range
- KeyError: Dictionary key not found
- FileNotFoundError: File doesn't exist
"""

# =============================================================================
# 2. BASIC EXCEPTION HANDLING
# =============================================================================

print("\n🛡️ BASIC EXCEPTION HANDLING")
print("-" * 30)

# Example 1: Division by zero
def safe_division(a, b):
    """Demonstrate basic exception handling."""
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print(f"❌ Error: Cannot divide {a} by zero!")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

print("Basic Exception Handling:")
safe_division(10, 2)
safe_division(10, 0)
safe_division(10, "2")  # This will cause TypeError

# =============================================================================
# 3. MULTIPLE EXCEPTION HANDLING
# =============================================================================

print("\n🔧 MULTIPLE EXCEPTION HANDLING")
print("-" * 35)

def robust_calculator(operation, a, b):
    """Handle multiple types of exceptions."""
    try:
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            result = a / b
        else:
            raise ValueError(f"Unknown operation: {operation}")
        
        print(f"{a} {operation} {b} = {result}")
        return result
        
    except ZeroDivisionError:
        print(f"❌ Error: Cannot divide by zero!")
        return None
    except TypeError:
        print(f"❌ Error: Invalid data types for operation!")
        return None
    except ValueError as e:
        print(f"❌ Error: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

print("Multiple Exception Handling:")
robust_calculator("add", 5, 3)
robust_calculator("divide", 10, 0)
robust_calculator("multiply", "5", 3)
robust_calculator("power", 2, 3)

# =============================================================================
# 4. TRY-EXCEPT-ELSE-FINALLY
# =============================================================================

print("\n🔄 TRY-EXCEPT-ELSE-FINALLY")
print("-" * 30)

def file_operation_demo():
    """Demonstrate try-except-else-finally blocks."""
    filename = "test_file.txt"
    
    try:
        # Attempt to open and read file
        with open(filename, 'r') as file:
            content = file.read()
            print(f"📖 Successfully read {filename}")
            
    except FileNotFoundError:
        print(f"❌ File {filename} not found")
        # Create the file as fallback
        with open(filename, 'w') as file:
            file.write("This is a test file created as fallback!")
            print(f"✅ Created {filename} as fallback")
            
    except PermissionError:
        print(f"❌ Permission denied to read {filename}")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        
    else:
        print("✅ File operation completed successfully")
        
    finally:
        print("🧹 Cleanup: File operation finished")

file_operation_demo()

# =============================================================================
# 5. RAISING EXCEPTIONS
# =============================================================================

print("\n🚨 RAISING EXCEPTIONS")
print("-" * 22)

def validate_age(age):
    """Demonstrate raising exceptions."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    if age > 150:
        raise ValueError("Age seems unrealistic")
    
    return f"Valid age: {age}"

print("Raising Exceptions:")
try:
    print(validate_age(25))
    print(validate_age(-5))
except (TypeError, ValueError) as e:
    print(f"❌ Validation error: {e}")

try:
    print(validate_age("25"))
except TypeError as e:
    print(f"❌ Type error: {e}")

# =============================================================================
# 6. CUSTOM EXCEPTIONS
# =============================================================================

print("\n🎯 CUSTOM EXCEPTIONS")
print("-" * 22)

class CustomError(Exception):
    """Custom exception class."""
    pass

class ValidationError(Exception):
    """Custom validation exception."""
    def __init__(self, message, field=None):
        self.message = message
        self.field = field
        super().__init__(self.message)

class BusinessLogicError(Exception):
    """Custom business logic exception."""
    def __init__(self, message, error_code=None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

def validate_user_data(name, email, age):
    """Demonstrate custom exceptions."""
    errors = []
    
    try:
        if not name or len(name.strip()) < 2:
            raise ValidationError("Name must be at least 2 characters", "name")
        
        if "@" not in email:
            raise ValidationError("Invalid email format", "email")
        
        if age < 18:
            raise BusinessLogicError("User must be 18 or older", "AGE_RESTRICTION")
        
        return f"✅ User {name} validated successfully"
        
    except ValidationError as e:
        return f"❌ Validation error in {e.field}: {e.message}"
    except BusinessLogicError as e:
        return f"❌ Business logic error ({e.error_code}): {e.message}"

print("Custom Exceptions:")
print(validate_user_data("Alice", "alice@example.com", 25))
print(validate_user_data("A", "alice@example.com", 25))
print(validate_user_data("Alice", "invalid-email", 25))
print(validate_user_data("Alice", "alice@example.com", 16))

# =============================================================================
# 7. EXCEPTION CHAINING
# =============================================================================

print("\n🔗 EXCEPTION CHAINING")
print("-" * 22)

def process_data(data):
    """Demonstrate exception chaining."""
    try:
        # Simulate data processing
        if not data:
            raise ValueError("Data cannot be empty")
        
        result = data * 2
        return result
        
    except ValueError as e:
        # Chain the exception with additional context
        raise RuntimeError(f"Failed to process data: {e}") from e

def handle_data_processing():
    """Handle data processing with exception chaining."""
    try:
        result = process_data(None)
        print(f"✅ Processed data: {result}")
    except RuntimeError as e:
        print(f"❌ Processing failed: {e}")
        print(f"   Original error: {e.__cause__}")

print("Exception Chaining:")
handle_data_processing()

# =============================================================================
# 8. CONTEXT MANAGERS AND EXCEPTIONS
# =============================================================================

print("\n🔒 CONTEXT MANAGERS AND EXCEPTIONS")
print("-" * 40)

class SafeFileManager:
    """Context manager that handles file operations safely."""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            print(f"✅ Opened {self.filename} in {self.mode} mode")
            return self.file
        except FileNotFoundError:
            print(f"❌ File {self.filename} not found")
            raise
        except PermissionError:
            print(f"❌ Permission denied for {self.filename}")
            raise
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"🔒 Closed {self.filename}")
        
        if exc_type:
            print(f"⚠️ Exception occurred: {exc_type.__name__}: {exc_val}")
        
        return False  # Don't suppress exceptions

def demonstrate_safe_file_operations():
    """Demonstrate safe file operations."""
    try:
        with SafeFileManager("nonexistent.txt", "r") as file:
            content = file.read()
            print(f"Content: {content}")
    except FileNotFoundError:
        print("Handled file not found error gracefully")

demonstrate_safe_file_operations()

# =============================================================================
# 9. PRACTICAL EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL EXAMPLES")
print("-" * 22)

# Example 1: Database Connection Handler
class DatabaseConnection:
    """Simulate database connection with error handling."""
    
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database
        self.connected = False
    
    def connect(self):
        """Simulate database connection."""
        try:
            if not self.host:
                raise ValueError("Host cannot be empty")
            
            if self.port < 1 or self.port > 65535:
                raise ValueError("Port must be between 1 and 65535")
            
            # Simulate connection
            self.connected = True
            print(f"✅ Connected to {self.database} at {self.host}:{self.port}")
            
        except ValueError as e:
            print(f"❌ Connection failed: {e}")
            raise
        except Exception as e:
            print(f"❌ Unexpected connection error: {e}")
            raise
    
    def disconnect(self):
        """Disconnect from database."""
        if self.connected:
            self.connected = False
            print(f"🔌 Disconnected from {self.database}")

def database_operations():
    """Demonstrate database operations with error handling."""
    try:
        # Valid connection
        db = DatabaseConnection("localhost", 5432, "myapp")
        db.connect()
        db.disconnect()
        
        # Invalid connection
        db_invalid = DatabaseConnection("", 5432, "myapp")
        db_invalid.connect()
        
    except ValueError as e:
        print(f"Database error handled: {e}")

database_operations()

# Example 2: API Request Handler
import requests

def safe_api_request(url):
    """Make safe API requests with error handling."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises exception for HTTP errors
        return response.json()
        
    except requests.exceptions.Timeout:
        print(f"❌ Request to {url} timed out")
        return None
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection error to {url}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request error: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

# Example 3: Data Validation System
def validate_user_input(data):
    """Comprehensive data validation with error handling."""
    errors = []
    
    try:
        # Validate name
        if not data.get('name'):
            errors.append("Name is required")
        elif len(data['name'].strip()) < 2:
            errors.append("Name must be at least 2 characters")
        
        # Validate email
        email = data.get('email', '')
        if not email:
            errors.append("Email is required")
        elif '@' not in email or '.' not in email:
            errors.append("Invalid email format")
        
        # Validate age
        age = data.get('age')
        if age is None:
            errors.append("Age is required")
        elif not isinstance(age, int):
            errors.append("Age must be a number")
        elif age < 18:
            errors.append("Age must be 18 or older")
        
        if errors:
            raise ValidationError(f"Validation failed: {', '.join(errors)}")
        
        return f"✅ User {data['name']} validated successfully"
        
    except ValidationError as e:
        return f"❌ {e.message}"
    except Exception as e:
        return f"❌ Unexpected validation error: {e}"

print("Data Validation System:")
test_data = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "A", "email": "alice@example.com", "age": 25},
    {"name": "Bob", "email": "invalid-email", "age": 25},
    {"name": "Charlie", "email": "charlie@example.com", "age": 16}
]

for data in test_data:
    result = validate_user_input(data)
    print(f"  {result}")

# =============================================================================
# 10. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice exception handling:

Exercise 1: Create a robust calculator
- Handle division by zero
- Handle invalid operations
- Handle non-numeric inputs
- Provide meaningful error messages

Exercise 2: Build a file processor
- Handle file not found errors
- Handle permission errors
- Handle corrupted file errors
- Implement retry logic

Exercise 3: Create a data validator
- Validate different data types
- Handle missing required fields
- Provide detailed error messages
- Implement custom validation rules

Exercise 4: Build a network client
- Handle connection timeouts
- Handle network errors
- Implement retry mechanisms
- Handle different HTTP status codes

Exercise 5: Create a configuration loader
- Handle missing configuration files
- Validate configuration values
- Handle malformed configuration data
- Provide default values
""")

# =============================================================================
# 11. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
Exception handling best practices:

1. Be specific with exception types
   ✅ except ValueError as e:
   ❌ except Exception as e:

2. Handle exceptions at the right level
   ✅ Handle where you can recover
   ❌ Handle everywhere just in case

3. Provide meaningful error messages
   ✅ "Invalid email format: missing @ symbol"
   ❌ "Error occurred"

4. Use finally blocks for cleanup
   ✅ Close files, connections, etc.
   ❌ Forget to clean up resources

5. Don't suppress exceptions silently
   ✅ Log or handle appropriately
   ❌ except: pass

6. Use custom exceptions for business logic
   ✅ class ValidationError(Exception):
   ❌ raise Exception("Validation failed")

7. Chain exceptions when appropriate
   ✅ raise RuntimeError("Failed") from original_error
   ❌ Lose original error context

8. Test your exception handling
   ✅ Test error scenarios
   ❌ Assume exceptions won't occur
""")

# =============================================================================
# 12. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common exception handling mistakes:

1. Catching too broad exceptions
   ❌ except Exception:  # Too broad
   ✅ except ValueError:  # Specific

2. Suppressing exceptions silently
   ❌ except: pass  # Silent failure
   ✅ except: log_error()  # Handle appropriately

3. Not handling exceptions at all
   ❌ result = risky_operation()  # Can crash
   ✅ try: result = risky_operation() except: handle_error()

4. Using exceptions for control flow
   ❌ try: return data[key] except KeyError: return default
   ✅ return data.get(key, default)

5. Not cleaning up resources
   ❌ file = open('file.txt')  # Can leak
   ✅ with open('file.txt') as file:  # Auto cleanup

6. Raising generic exceptions
   ❌ raise Exception("Error")
   ✅ raise ValueError("Invalid input")

7. Not providing error context
   ❌ raise ValueError("Error")
   ✅ raise ValueError(f"Invalid value: {value}")
""")

# =============================================================================
# 13. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ How to handle exceptions gracefully
✅ Different types of exceptions and when to use them
✅ Try-except-else-finally blocks
✅ Raising and creating custom exceptions
✅ Exception chaining and context managers
✅ Best practices for robust error handling
✅ Common mistakes to avoid

Next Steps:
- Day 8: Object-Oriented Programming
- Day 9: Modules and Packages
- Day 10: Advanced Data Structures
""")

# =============================================================================
# 14. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 7 of your Python journey!

You now understand:
- How to handle errors gracefully in your programs
- Different types of exceptions and their uses
- How to create custom exceptions
- Best practices for robust error handling
- How to avoid common mistakes

Exception handling is crucial for robust applications!
Practice with the exercises to master this essential skill.

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 7: Exception Handling and Error Management Tutorial")
    print("Run this file to see all examples in action!")
