"""
Day 17: Ruff - Modern Linting & Formatting
===========================================

Writing code that works is only the first step. Writing code that is clean,
consistent, and free of common errors is crucial for long-term maintenance
and collaboration. Ruff is the modern, all-in-one tool for this.

Learning Objectives:
1.  Understand what linting and formatting are.
2.  Appreciate why a tool like Ruff is a game-changer (speed and integration).
3.  Configure Ruff in your `pyproject.toml` file.
4.  Use Ruff from the command line to check and fix your code.
5.  Integrate Ruff with VS Code for a seamless "format on save" workflow.
"""

# =============================================================================
# 1. WHAT ARE LINTING AND FORMATTING?
# =============================================================================

"""
Linting:
- The process of analyzing code to detect programming errors, bugs, stylistic
  errors, and suspicious constructs.
- A linter acts like a strict grammar checker for your code.
- It helps you catch errors *before* you even run the program.
- Examples: flagging unused variables, incorrect function arguments, or unreachable code.
- Old tools: Flake8, Pylint

Formatting:
- The process of automatically rewriting your code to conform to a consistent style guide.
- It handles things like line length, indentation, quotes, and spacing.
- This eliminates all arguments about code style on a team.
- Old tools: Black, isort (for sorting imports)

Ruff combines both of these (and more) into a single, blazing-fast tool.
"""

# =============================================================================
# 2. GETTING STARTED WITH RUFF
# =============================================================================

# You should have `uv` installed from Day 1.
# Ruff is a command-line tool. You can install it into your project's
# virtual environment.

# Action: In your terminal (with your venv activated):
# > uv pip install ruff

# To check that it's installed:
# > ruff --version


# =============================================================================
# 3. CONFIGURING RUFF IN `pyproject.toml`
# =============================================================================

"""
Ruff is configured in the `pyproject.toml` file at the root of your project.
This is the modern standard for configuring Python tools.

Create a `pyproject.toml` file in your project's root directory and add a
`[tool.ruff]` section.
"""

# --- Example `pyproject.toml` configuration ---
"""
# pyproject.toml

[tool.ruff]
# Set the maximum line length.
line-length = 88

# Set the target Python version to enforce rules for.
target-version = "py312" # e.g., Python 3.12

[tool.ruff.lint]
# Select the rule codes to enforce.
# "E", "F" -> standard flake8 rules (errors, pyflakes)
# "I" -> isort (import sorting)
# "N" -> pep8-naming
# "C90" -> McCabe complexity
# See the Ruff docs for hundreds of available rules!
select = ["E", "F", "I", "N", "C90"]

# You can also ignore specific rules.
ignore = ["N803"] # e.g., allow lowercase argument names in functions

[tool.ruff.format
# You can configure the formatter, but the defaults are great.
# Use double quotes for strings.
quote-style = "double"
"""

# Action: Create a `pyproject.toml` file in the root of your `ai_learning_plan`
# parent folder and add the configuration above.


# =============================================================================
# 4. USING RUFF FROM THE COMMAND LINE
# =============================================================================

# Let's write some messy code to see Ruff in action.
import sys, os # Bad: multiple imports on one line

def my_function(UserName,user_age): # Bad: inconsistent naming (PascalCase and snake_case)
    Unused_variable = "hello" # Bad: unused variable, PascalCase
    if user_age>18:
        print(f"{UserName} is an adult.") # Bad: inconsistent quotes if config is "double"
    return None

# --- Checking for errors ---
# `ruff check .` will scan the current directory and report issues.
# > ruff check .

# --- Automatically fixing errors ---
# `ruff check --fix .` will automatically fix everything it can.
# `ruff format .` will format the code according to style rules.
# The command `ruff format . && ruff check --fix .` is a powerful combo.

# After running the fixers, the code above would look like this:
"""
import os
import sys

def my_function(user_name, user_age):
    if user_age > 18:
        print(f"{user_name} is an adult.")
    return None
"""
# Notice: imports are sorted, names are corrected, unused variable is gone, quotes are fixed.


# =============================================================================
# 5. VS CODE INTEGRATION
# =============================================================================

# This is where the magic happens. You already installed the Ruff extension on Day 1.
# Now, let's configure VS Code to use it automatically.

# Action: Open VS Code settings (settings.json)
# 1. Press `Ctrl+Shift+P` and type "Open User Settings (JSON)".
# 2. Add these lines to your `settings.json` file:
"""
{
    // ... your other settings ...
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff", // Set Ruff as the default formatter
        "editor.formatOnSave": true, // Format the file every time you save
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit" // Automatically fix lint errors on save
        }
    },
}
"""
# Now, every time you save a Python file, Ruff will instantly format it and fix any linting errors.
# This creates a tight feedback loop that teaches you to write cleaner code naturally.


# =============================================================================
# EXERCISES
# =============================================================================

# 1. Create a Messy File:
#    - Create a new Python file called `messy_code.py`.
#    - Add some poorly formatted code to it. Include:
#      - An unused import (`import math`).
#      - A function with multiple arguments on one line `def f(a,b,c): ...`.
#      - A long line of code (> 90 characters).
#      - Inconsistent use of single and double quotes.

# 2. Fix it with the CLI:
#    - Open your terminal.
#    - Run `ruff format messy_code.py`. Observe the changes.
#    - Run `ruff check --fix messy_code.py`. Observe the rest of the changes.

# 3. Test the VS Code Integration:
#    - Undo the changes to `messy_code.py` (with `git restore` or Ctrl+Z).
#    - Open the file in VS Code.
#    - Press `Ctrl+S` to save the file.
#    - Watch as Ruff automatically cleans everything up for you. This is the workflow
#      you will use from now on.

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- Code quality is as important as correctness.
- Ruff provides a single, ultra-fast tool for both linting and formatting.
- Configuring Ruff in `pyproject.toml` is the modern standard.
- The real power of Ruff is unlocked through IDE integration, which provides
  instant feedback and automates the process of writing clean code.

Next up: Day 18 - Logging, for when `print()` isn't enough.
"""
