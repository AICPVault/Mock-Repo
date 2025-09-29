"""
Day 15: Testing and Debugging
=============================

Today we'll learn about testing and debugging in Python - essential skills for
building reliable and maintainable applications. We'll explore different testing
approaches, debugging techniques, and best practices.

Learning Objectives:
- Understand the importance of testing
- Learn unit testing with unittest and pytest
- Master debugging techniques and tools
- Explore test-driven development (TDD)
- Practice error handling and logging
- Build robust, testable applications

Let's master testing and debugging!
"""

print("🐍 Welcome to Day 15: Testing and Debugging!")
print("=" * 50)

import unittest
import pytest
import logging
import sys
import traceback
from unittest.mock import Mock, patch
import pdb
import time

# =============================================================================
# 1. WHAT IS TESTING?
# =============================================================================

print("\n🧪 WHAT IS TESTING?")
print("-" * 20)

"""
Testing is:
- The process of verifying that code works as expected
- Essential for building reliable software
- Helps catch bugs before they reach production
- Improves code quality and maintainability
- Builds confidence in code changes

Types of testing:
- Unit testing: Test individual components
- Integration testing: Test component interactions
- System testing: Test entire system
- Acceptance testing: Test user requirements

Benefits:
- Catch bugs early
- Document expected behavior
- Enable refactoring with confidence
- Improve code design
"""

# =============================================================================
# 2. UNIT TESTING WITH UNITTEST
# =============================================================================

print("\n🔬 UNIT TESTING WITH UNITTEST")
print("-" * 35)

# Sample functions to test
def add_numbers(a, b):
    """Add two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    return a + b

def divide_numbers(a, b):
    """Divide two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(number):
    """Check if a number is even."""
    if not isinstance(number, int):
        raise TypeError("Argument must be an integer")
    return number % 2 == 0

# Test class using unittest
class TestMathFunctions(unittest.TestCase):
    """Test cases for math functions."""
    
    def test_add_numbers_positive(self):
        """Test adding positive numbers."""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(10, 20), 30)
        self.assertEqual(add_numbers(0, 5), 5)
    
    def test_add_numbers_negative(self):
        """Test adding negative numbers."""
        self.assertEqual(add_numbers(-2, -3), -5)
        self.assertEqual(add_numbers(-10, 5), -5)
    
    def test_add_numbers_float(self):
        """Test adding float numbers."""
        self.assertAlmostEqual(add_numbers(1.5, 2.5), 4.0)
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3, places=10)
    
    def test_add_numbers_type_error(self):
        """Test type error for invalid inputs."""
        with self.assertRaises(TypeError):
            add_numbers("2", 3)
        with self.assertRaises(TypeError):
            add_numbers(2, "3")
    
    def test_divide_numbers_normal(self):
        """Test normal division."""
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertEqual(divide_numbers(15, 3), 5)
        self.assertAlmostEqual(divide_numbers(1, 3), 0.3333333333333333)
    
    def test_divide_numbers_zero_division(self):
        """Test division by zero."""
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)
    
    def test_divide_numbers_type_error(self):
        """Test type error for invalid inputs."""
        with self.assertRaises(TypeError):
            divide_numbers("10", 2)
    
    def test_is_even_true(self):
        """Test even numbers."""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-2))
    
    def test_is_even_false(self):
        """Test odd numbers."""
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))
    
    def test_is_even_type_error(self):
        """Test type error for invalid inputs."""
        with self.assertRaises(TypeError):
            is_even("2")
        with self.assertRaises(TypeError):
            is_even(2.5)

# Run the tests
print("Running unittest tests:")
test_suite = unittest.TestLoader().loadTestsFromTestCase(TestMathFunctions)
test_runner = unittest.TextTestRunner(verbosity=2)
test_result = test_runner.run(test_suite)

# =============================================================================
# 3. TESTING WITH PYTEST
# =============================================================================

print("\n🔬 TESTING WITH PYTEST")
print("-" * 25)

# Pytest-style test functions
def test_add_numbers_pytest():
    """Test add_numbers function with pytest."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(10, 20) == 30
    assert add_numbers(0, 5) == 5

def test_divide_numbers_pytest():
    """Test divide_numbers function with pytest."""
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(15, 3) == 5
    assert abs(divide_numbers(1, 3) - 0.3333333333333333) < 1e-10

def test_divide_numbers_zero_pytest():
    """Test division by zero with pytest."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_numbers(10, 0)

def test_add_numbers_type_error_pytest():
    """Test type error with pytest."""
    with pytest.raises(TypeError, match="Arguments must be numbers"):
        add_numbers("2", 3)

# Parametrized tests
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (10, 20, 30),
    (0, 5, 5),
    (-2, -3, -5),
    (-10, 5, -5)
])
def test_add_numbers_parametrized(a, b, expected):
    """Parametrized test for add_numbers."""
    assert add_numbers(a, b) == expected

@pytest.mark.parametrize("number,expected", [
    (2, True),
    (4, True),
    (0, True),
    (-2, True),
    (1, False),
    (3, False),
    (-1, False)
])
def test_is_even_parametrized(number, expected):
    """Parametrized test for is_even."""
    assert is_even(number) == expected

print("Pytest test functions defined:")
print("  - test_add_numbers_pytest")
print("  - test_divide_numbers_pytest")
print("  - test_divide_numbers_zero_pytest")
print("  - test_add_numbers_type_error_pytest")
print("  - Parametrized tests for add_numbers and is_even")

# =============================================================================
# 4. MOCKING AND PATCHING
# =============================================================================

print("\n🎭 MOCKING AND PATCHING")
print("-" * 25)

# Example class that makes external API calls
class WeatherService:
    """Weather service that makes API calls."""
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_weather(self, city):
        """Get weather for a city (simulated API call)."""
        # Simulate API call
        time.sleep(0.1)  # Simulate network delay
        return f"Weather in {city}: 22°C, Sunny"

class WeatherApp:
    """Weather application that uses WeatherService."""
    
    def __init__(self, weather_service):
        self.weather_service = weather_service
    
    def get_weather_info(self, city):
        """Get weather information for a city."""
        try:
            weather = self.weather_service.get_weather(city)
            return f"Current weather: {weather}"
        except Exception as e:
            return f"Error getting weather: {str(e)}"

# Test with mocking
class TestWeatherApp(unittest.TestCase):
    """Test cases for WeatherApp with mocking."""
    
    def test_get_weather_info_success(self):
        """Test successful weather retrieval."""
        # Create mock weather service
        mock_service = Mock()
        mock_service.get_weather.return_value = "Weather in London: 15°C, Cloudy"
        
        # Create weather app with mock service
        weather_app = WeatherApp(mock_service)
        
        # Test the method
        result = weather_app.get_weather_info("London")
        
        # Assertions
        self.assertEqual(result, "Current weather: Weather in London: 15°C, Cloudy")
        mock_service.get_weather.assert_called_once_with("London")
    
    def test_get_weather_info_error(self):
        """Test weather retrieval with error."""
        # Create mock service that raises exception
        mock_service = Mock()
        mock_service.get_weather.side_effect = Exception("API Error")
        
        # Create weather app with mock service
        weather_app = WeatherApp(mock_service)
        
        # Test the method
        result = weather_app.get_weather_info("London")
        
        # Assertions
        self.assertEqual(result, "Error getting weather: API Error")
        mock_service.get_weather.assert_called_once_with("London")

# Test with patching
@patch('time.sleep')  # Patch time.sleep to avoid actual delay
def test_weather_service_with_patch(mock_sleep):
    """Test WeatherService with patching."""
    service = WeatherService("test_key")
    result = service.get_weather("Paris")
    
    assert "Weather in Paris" in result
    mock_sleep.assert_called_once_with(0.1)

print("Mocking and patching examples:")
print("  - Mock objects for external dependencies")
print("  - Patching functions and methods")
print("  - Testing error scenarios")

# =============================================================================
# 5. DEBUGGING TECHNIQUES
# =============================================================================

print("\n🐛 DEBUGGING TECHNIQUES")
print("-" * 25)

def demonstrate_debugging():
    """Demonstrate various debugging techniques."""
    print("Debugging Techniques:")
    
    # 1. Print debugging
    def debug_with_print():
        """Debug using print statements."""
        x = 10
        y = 20
        print(f"Debug: x = {x}, y = {y}")
        result = x + y
        print(f"Debug: result = {result}")
        return result
    
    print("1. Print debugging:")
    debug_with_print()
    
    # 2. Logging
    def debug_with_logging():
        """Debug using logging."""
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        
        x = 10
        y = 20
        logger.debug(f"x = {x}, y = {y}")
        result = x + y
        logger.debug(f"result = {result}")
        return result
    
    print("\n2. Logging debugging:")
    debug_with_logging()
    
    # 3. Exception handling
    def debug_with_exceptions():
        """Debug using exception handling."""
        try:
            x = 10
            y = 0
            result = x / y
            return result
        except ZeroDivisionError as e:
            print(f"Exception caught: {e}")
            print(f"Exception type: {type(e)}")
            return None
    
    print("\n3. Exception handling:")
    debug_with_exceptions()
    
    # 4. Traceback
    def debug_with_traceback():
        """Debug using traceback."""
        try:
            x = 10
            y = 0
            result = x / y
            return result
        except Exception as e:
            print(f"Exception: {e}")
            print("Traceback:")
            traceback.print_exc()
            return None
    
    print("\n4. Traceback debugging:")
    debug_with_traceback()

demonstrate_debugging()

# =============================================================================
# 6. LOGGING
# =============================================================================

print("\n📝 LOGGING")
print("-" * 10)

def demonstrate_logging():
    """Demonstrate logging configuration and usage."""
    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Create logger
    logger = logging.getLogger('demo_app')
    
    # Different log levels
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    
    # Logging with context
    def process_data(data):
        """Process data with logging."""
        logger.info(f"Processing data: {data}")
        
        try:
            result = data * 2
            logger.info(f"Data processed successfully: {result}")
            return result
        except Exception as e:
            logger.error(f"Error processing data: {e}")
            raise
    
    # Test logging
    process_data(5)
    try:
        process_data("invalid")
    except Exception:
        pass

demonstrate_logging()

# =============================================================================
# 7. TEST-DRIVEN DEVELOPMENT (TDD)
# =============================================================================

print("\n🔄 TEST-DRIVEN DEVELOPMENT (TDD)")
print("-" * 35)

def demonstrate_tdd():
    """Demonstrate Test-Driven Development approach."""
    print("TDD Cycle: Red -> Green -> Refactor")
    
    # Step 1: Write a failing test (Red)
    def test_calculator_add():
        """Test calculator add method (failing test)."""
        # This test will fail because Calculator class doesn't exist yet
        try:
            calc = Calculator()
            result = calc.add(2, 3)
            assert result == 5
            print("✅ Test passed")
        except NameError:
            print("❌ Test failed - Calculator class doesn't exist")
    
    # Step 2: Write minimal code to pass the test (Green)
    class Calculator:
        """Simple calculator class."""
        
        def add(self, a, b):
            """Add two numbers."""
            return a + b
        
        def subtract(self, a, b):
            """Subtract two numbers."""
            return a - b
        
        def multiply(self, a, b):
            """Multiply two numbers."""
            return a * b
        
        def divide(self, a, b):
            """Divide two numbers."""
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
    
    # Step 3: Run the test again (should pass now)
    print("\nRunning tests after implementing Calculator:")
    test_calculator_add()
    
    # Step 4: Add more tests and refactor
    def test_calculator_subtract():
        """Test calculator subtract method."""
        calc = Calculator()
        assert calc.subtract(5, 3) == 2
        print("✅ Subtract test passed")
    
    def test_calculator_multiply():
        """Test calculator multiply method."""
        calc = Calculator()
        assert calc.multiply(3, 4) == 12
        print("✅ Multiply test passed")
    
    def test_calculator_divide():
        """Test calculator divide method."""
        calc = Calculator()
        assert calc.divide(10, 2) == 5
        print("✅ Divide test passed")
    
    def test_calculator_divide_zero():
        """Test calculator divide by zero."""
        calc = Calculator()
        try:
            calc.divide(10, 0)
            print("❌ Divide by zero test failed")
        except ValueError:
            print("✅ Divide by zero test passed")
    
    # Run all tests
    test_calculator_subtract()
    test_calculator_multiply()
    test_calculator_divide()
    test_calculator_divide_zero()

demonstrate_tdd()

# =============================================================================
# 8. PRACTICAL TESTING EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL TESTING EXAMPLES")
print("-" * 35)

# Example 1: Testing a User Management System
class User:
    """User class for testing."""
    
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
        self.is_active = True
    
    def activate(self):
        """Activate user account."""
        self.is_active = True
    
    def deactivate(self):
        """Deactivate user account."""
        self.is_active = False
    
    def can_vote(self):
        """Check if user can vote."""
        return self.age >= 18 and self.is_active

class UserManager:
    """User management system."""
    
    def __init__(self):
        self.users = []
    
    def add_user(self, user):
        """Add a user to the system."""
        if not isinstance(user, User):
            raise TypeError("User must be a User instance")
        self.users.append(user)
    
    def get_user(self, username):
        """Get user by username."""
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def get_active_users(self):
        """Get all active users."""
        return [user for user in self.users if user.is_active]
    
    def get_voters(self):
        """Get all users who can vote."""
        return [user for user in self.users if user.can_vote()]

# Test cases for User Management System
class TestUserManagement(unittest.TestCase):
    """Test cases for User Management System."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.user_manager = UserManager()
        self.user1 = User("alice", "alice@example.com", 25)
        self.user2 = User("bob", "bob@example.com", 17)
        self.user3 = User("charlie", "charlie@example.com", 30)
    
    def test_add_user(self):
        """Test adding a user."""
        self.user_manager.add_user(self.user1)
        self.assertEqual(len(self.user_manager.users), 1)
        self.assertIn(self.user1, self.user_manager.users)
    
    def test_add_invalid_user(self):
        """Test adding invalid user."""
        with self.assertRaises(TypeError):
            self.user_manager.add_user("not a user")
    
    def test_get_user(self):
        """Test getting a user."""
        self.user_manager.add_user(self.user1)
        found_user = self.user_manager.get_user("alice")
        self.assertEqual(found_user, self.user1)
    
    def test_get_nonexistent_user(self):
        """Test getting nonexistent user."""
        found_user = self.user_manager.get_user("nonexistent")
        self.assertIsNone(found_user)
    
    def test_get_active_users(self):
        """Test getting active users."""
        self.user_manager.add_user(self.user1)
        self.user_manager.add_user(self.user2)
        self.user2.deactivate()
        
        active_users = self.user_manager.get_active_users()
        self.assertEqual(len(active_users), 1)
        self.assertIn(self.user1, active_users)
        self.assertNotIn(self.user2, active_users)
    
    def test_get_voters(self):
        """Test getting voters."""
        self.user_manager.add_user(self.user1)  # 25, active
        self.user_manager.add_user(self.user2)  # 17, active
        self.user_manager.add_user(self.user3)  # 30, active
        
        voters = self.user_manager.get_voters()
        self.assertEqual(len(voters), 2)
        self.assertIn(self.user1, voters)
        self.assertIn(self.user3, voters)
        self.assertNotIn(self.user2, voters)

# Run the tests
print("Running User Management System tests:")
test_suite = unittest.TestLoader().loadTestsFromTestCase(TestUserManagement)
test_runner = unittest.TextTestRunner(verbosity=2)
test_result = test_runner.run(test_suite)

# =============================================================================
# 9. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice testing and debugging:

Exercise 1: Test a Calculator Class
- Create a calculator class with basic operations
- Write comprehensive unit tests
- Test edge cases and error conditions
- Use parametrized tests for multiple inputs

Exercise 2: Test a File Processing System
- Create a file processor that reads CSV files
- Write tests for different file formats
- Test error handling for missing files
- Mock file operations for testing

Exercise 3: Test a Web Scraper
- Create a web scraper class
- Mock HTTP requests for testing
- Test data extraction and parsing
- Test error handling for network issues

Exercise 4: Test a Database Application
- Create a simple ORM-like class
- Mock database operations
- Test CRUD operations
- Test transaction handling

Exercise 5: Test a Machine Learning Pipeline
- Create a simple ML pipeline
- Test data preprocessing
- Test model training and prediction
- Test error handling for invalid data
""")

# =============================================================================
# 10. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
Testing and debugging best practices:

1. Write tests first (TDD)
   ✅ Write failing test, then code
   ❌ Write code first, then tests

2. Test edge cases
   ✅ Test boundary conditions
   ❌ Only test happy path

3. Use descriptive test names
   ✅ test_user_cannot_vote_if_under_18
   ❌ test_user

4. Keep tests independent
   ✅ Each test should be standalone
   ❌ Tests that depend on each other

5. Use appropriate assertions
   ✅ assertEqual, assertTrue, assertRaises
   ❌ Generic assert statements

6. Mock external dependencies
   ✅ Mock API calls, database operations
   ❌ Make real external calls in tests

7. Test error conditions
   ✅ Test exception handling
   ❌ Only test success scenarios

8. Use logging for debugging
   ✅ Structured logging with levels
   ❌ Print statements everywhere
""")

# =============================================================================
# 11. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common testing and debugging mistakes:

1. Not testing edge cases
   ❌ Only testing normal inputs
   ✅ Test boundary conditions and edge cases

2. Writing tests that are too complex
   ❌ One test that does everything
   ✅ Simple, focused tests

3. Not cleaning up test data
   ❌ Tests that leave data behind
   ✅ Clean up after each test

4. Not using proper assertions
   ❌ assert True  # Always passes
   ✅ assert result == expected

5. Not testing error conditions
   ❌ Only testing success paths
   ✅ Test exception handling

6. Not mocking external dependencies
   ❌ Making real API calls in tests
   ✅ Mock external services

7. Not documenting test failures
   ❌ Silent test failures
   ✅ Clear error messages and documentation
""")

# =============================================================================
# 12. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ Unit testing with unittest and pytest
✅ Mocking and patching for testing
✅ Debugging techniques and tools
✅ Logging and error handling
✅ Test-driven development (TDD)
✅ Best practices for testing
✅ Common mistakes to avoid

Next Steps:
- Day 16: Deployment and Production
""")

# =============================================================================
# 13. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 15 of your Python journey!

You now understand:
- How to write effective tests
- How to debug applications
- How to use logging and error handling
- How to follow test-driven development
- Best practices for testing and debugging

Testing and debugging are essential for building reliable software!
Practice with the exercises to master these crucial skills.

Happy coding! 🐍✨
""")

# Clean up created files
import os
if os.path.exists('app.log'):
    os.remove('app.log')
    print("🧹 Cleaned up app.log")

# Run the tutorial
if __name__ == "__main__":
    print("Day 15: Testing and Debugging Tutorial")
    print("Run this file to see all examples in action!")
