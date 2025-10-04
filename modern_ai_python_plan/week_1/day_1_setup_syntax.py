"""
Day 1: Setup & Basic Syntax
===========================

Welcome to your 61-day journey to becoming AI-ready with Python!
Today is all about setting up a powerful, modern, and fast development environment.

Learning Objectives:
1.  Install Python 3.12+.
2.  Set up `uv` for lightning-fast package management.
3.  Configure Visual Studio Code with the essential Ruff extension.
4.  Understand basic Python syntax, comments, and the `print()` function.
"""

# =============================================================================
# 1. SETUP: PYTHON 3.12+
# =============================================================================

"""
Why Python 3.12+?
- It's the latest stable version with significant performance improvements.
- It includes new features like improved f-strings and more expressive error messages.
- Modern type hint syntax is cleaner and more intuitive.

Action:
- Go to https://www.python.org/downloads/
- Download and install Python 3.12 or newer.
- During installation on Windows, **make sure to check "Add Python to PATH"**.

To verify your installation, open a terminal (PowerShell, Command Prompt, or Terminal) and run:
> python --version
# or on some systems
> python3 --version

You should see an output like "Python 3.12.x".
"""

# =============================================================================
# 2. SETUP: UV - THE SUPER-FAST PACKAGE MANAGER
# =============================================================================

"""
What is `uv`?
- An extremely fast Python package installer and resolver, written in Rust.
- It's a single binary that can replace `pip`, `pip-tools`, `virtualenv`, and `pipx`.
- It's 10-100x faster than `pip` and `Poetry`, which saves you a lot of time.
- Developed by the same team behind `Ruff`.

Action:
- Follow the official installation instructions: https://github.com/astral-sh/uv
- Typically, you can install it with:
  - macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`

Creating a virtual environment with `uv` (the modern best practice):
1. Create a project folder: `mkdir my-python-project && cd my-python-project`
2. Create a virtual environment: `uv venv`
   - This creates a `.venv` folder. It's a sandboxed Python environment.
3. Activate it:
   - macOS/Linux: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`

Your terminal prompt should now be prefixed with `(.venv)`.
Anything you install now will be specific to this project.
"""

# =============================================================================
# 3. SETUP: VS CODE + RUFF EXTENSION
# =============================================================================

"""
Why VS Code + Ruff?
- VS Code is the most popular code editor for Python.
- `Ruff` is an extremely fast Python linter and code formatter, written in Rust.
- It replaces multiple older tools like Black, Flake8, and isort.
- The Ruff VS Code extension will automatically format and lint your code on save.

Action:
1. Download and install VS Code: https://code.visualstudio.com/
2. In VS Code, go to the Extensions view (Ctrl+Shift+X).
3. Search for and install the official "Ruff" extension from `astral-sh`.
4. Also install the official "Python" extension from Microsoft.

Configure "format on save" for a seamless experience:
1. Open VS Code settings (Ctrl+,).
2. Search for "Format On Save" and make sure it's checked.
3. Search for "Default Formatter" and select "Ruff".
"""

# =============================================================================
# 4. PYTHON BASIC SYNTAX
# =============================================================================

# This is a single-line comment. It's ignored by the Python interpreter.

"""
This is a multi-line comment, often used for docstrings.
It's technically a string, but it's the standard way to write block comments.
"""

# The print() function is used to display output to the console.
print("Hello, Modern Python Developer!")

# Python uses indentation (whitespace at the beginning of a line) to define scope.
# Unlike other languages that use curly braces `{}`, Python's use of whitespace is strict.
# You'll see this in action with control flow (Day 6) and functions (Day 8).

if True:
    print("This line is indented, so it's inside the 'if' block.")
    # This consistency is key to Python's readability.

print("This line is not indented, so it's outside the 'if' block.")


# =============================================================================
# EXERCISES
# =============================================================================

# 1. Verify your setup:
#    - Open a new terminal.
#    - Run `python --version` and `uv --version`.

# 2. Practice with the `print()` function:
#    - Write a line of code that prints your name.
#    - Write another line that prints your favorite hobby.

# 3. Experiment with comments:
#    - Write a single-line comment above your print statements.
#    - Write a multi-line comment explaining what your simple script does.

# 4. Test your Ruff formatter:
#    - Write a messy line of code like:
#      print(   "This    is messy."   )
#    - Save the file. If Ruff is configured correctly, it should automatically format to:
#      print("This is messy.")
#
#    - This instant feedback is why Ruff is so powerful for maintaining clean code.

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- A modern Python setup (`uv`, `Ruff`) is fast and helps you write clean code from day one.
- Virtual environments (`uv venv`) are essential for isolating project dependencies.
- Python's syntax is clean and relies on indentation.
- `print()` is your primary tool for seeing the output of your code.

Next up: Day 2 - Variables and Modern Type Hints.
"""
