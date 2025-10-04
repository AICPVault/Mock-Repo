"""
Day 12: Project - CLI Calculator
================================

Time to put everything we've learned in the first 11 days together!
We will build a simple, robust command-line interface (CLI) calculator
that handles basic arithmetic and provides clear user feedback.

Project Goals:
1.  Create functions for basic arithmetic operations (add, subtract, multiply, divide).
2.  Build a main loop that prompts the user for input.
3.  Parse the user's input to get numbers and an operator.
4.  Implement robust error handling for invalid input and mathematical errors (like division by zero).
5.  Allow the user to quit the application gracefully.

This project will heavily use:
- Functions (Day 8 & 9)
- Control Flow (`if/elif/else`, `match/case`) (Day 6)
- Loops (`while`) (Day 7)
- Error Handling (`try/except`) (We'll get a preview of Day 15)
- Type Annotations (Day 2 & 9)
"""

# =============================================================================
# 1. ARITHMETIC FUNCTIONS
# =============================================================================

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Returns the division of two numbers.
    Raises a ValueError if the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# =============================================================================
# 2. MAIN APPLICATION LOGIC
# =============================================================================

def calculator():
    """Main function to run the CLI calculator."""
    print("Welcome to the Simple CLI Calculator!")
    print("Enter a calculation (e.g., '10 + 5') or 'quit' to exit.")

    while True:
        try:
            # Get user input
            user_input: str = input("> ").strip()

            # Check for quit command
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break

            # Parse the input string
            parts: list[str] = user_input.split()
            if len(parts) != 3:
                print("Invalid format. Please use 'number operator number' (e.g., 10 + 5).")
                continue

            num1_str, operator, num2_str = parts

            # Convert numbers from string to float
            num1: float = float(num1_str)
            num2: float = float(num2_str)

            # Perform the calculation based on the operator
            result: float | None = None
            match operator:
                case '+':
                    result = add(num1, num2)
                case '-':
                    result = subtract(num1, num2)
                case '*':
                    result = multiply(num1, num2)
                case '/':
                    result = divide(num1, num2)
                case _:
                    print(f"Unknown operator: '{operator}'. Please use +, -, *, or /.")
                    continue

            # Print the result
            print(f"Result: {result}")

        # --- Error Handling ---
        except ValueError as e:
            # Catches errors from float() conversion and our custom divide-by-zero error
            print(f"Error: {e}")
        except Exception as e:
            # A general catch-all for any other unexpected errors
            print(f"An unexpected error occurred: {e}")


# =============================================================================
# 3. RUN THE CALCULATOR
# =============================================================================

# This is a standard Python convention. The code inside this `if` block
# will only run when the script is executed directly (not when it's imported).
if __name__ == "__main__":
    calculator()


# =============================================================================
# HOW TO RUN THIS PROJECT
# =============================================================================
"""
1. Save the code as a Python file (e.g., `calculator.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Run the script with the command: `python calculator.py`
5. Follow the on-screen prompts.

Try the following inputs to test it:
- 10 + 5
- 100 * 2.5
- 50 / 2
- 8 - 12
- 10 / 0  (to test error handling)
- ten + five (to test error handling)
- 10 plus 5 (to test error handling)
- quit
"""

# =============================================================================
# POTENTIAL IMPROVEMENTS (FOR YOU TO TRY!)
# =============================================================================
"""
- Add more operations like exponentiation (`**`) or modulus (`%`).
- Allow for continuous calculations (e.g., use the result of the last calculation
  as the first number in the next one).
- Add a "history" feature to store and display past calculations.
- Use a more robust parsing library if you want to handle more complex expressions
  like `10 + 5 * 2`. (This is an advanced topic!).
"""
