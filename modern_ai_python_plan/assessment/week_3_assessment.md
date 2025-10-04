
# Week 3 Knowledge Assessment: Error Handling, Code Quality, and Tools

This assessment covers topics from Day 15 to Day 21.

---

### Part 1: Multiple Choice Questions

1.  What is the primary purpose of the `finally` block in a `try...except` statement?
    a) To execute code only if an exception occurs.
    b) To execute code only if no exception occurs.
    c) To execute cleanup code regardless of whether an exception occurred or not.
    d) To log the error message to the console.

2.  Why is it generally better to create a custom exception class instead of using `raise Exception("My message")`?
    a) Custom exceptions can hold more data.
    b) It allows for more specific `except` blocks, so you can handle different application-specific errors differently.
    c) Custom exceptions are faster to raise.
    d) It's the only way to add a custom error message.

3.  What is the main benefit of using `@functools.cache`?
    a) It makes the function's code shorter.
    b) It stores the results of function calls and returns the cached result for the same inputs, improving performance for expensive operations.
    c) It automatically logs every time the function is called.
    d) It allows the function to accept more arguments.

4.  What problem does `functools.wraps` solve when writing decorators?
    a) It makes the decorated function run faster.
    b) It prevents the decorator from being applied more than once.
    c) It hides the original function's docstring for security.
    d) It preserves the original function's metadata (like `__name__` and `__doc__`) on the wrapped function.

5.  What is the role of a linter like Ruff?
    a) To execute Python code.
    b) To analyze code for potential errors, bugs, and stylistic issues without running it.
    c) To convert Python code into a binary executable.
    d) To automatically write documentation for the code.

---

### Part 2: What's the Output?

Predict the output of the following code snippets.

1.  ```python
    import logging
    logging.basicConfig(level=logging.WARNING)
    logging.info("Starting up...")
    logging.warning("Something looks off.")
    ```

2.  ```python
    def my_func():
        try:
            print("Start")
            return "Returned from try"
        finally:
            print("Finally block")

    print(my_func())
    ```

3.  ```python
    import functools

    def multiply(a, b):
        return a * b

    double = functools.partial(multiply, 2)
    print(double(10))
    ```

---

### Part 3: Find the Bug

Identify and fix the bug in each code snippet.

1.  ```python
    # Goal: Catch only the error from a bad dictionary key access.
    my_dict = {"a": 1}
    try:
        print(my_dict["b"])
    except Exception as e: # This is too broad and can hide other bugs.
        print(f"Caught an error: {e}")
    ```

2.  ```python
    # Goal: Create a custom error for validation.
    class ValidationError(Exception):
        pass

    def validate_age(age):
        if age < 18:
            # This runs, but the error isn't triggered.
            ValidationError("User must be 18 or older.")
        else:
            print("User is valid.")

    validate_age(15)
    ```

---

### Part 4: Short Coding Challenges

1.  **Custom Exception and Validation:**
    Create a custom exception called `InvalidEmailError`. Write a function `register_user(email: str)` that checks if the email string contains an `@` symbol. If it does not, `raise` your `InvalidEmailError`. Write the code to call this function and gracefully handle the potential error.

2.  **Context Manager with `with`:**
    You have a file `data.txt`. Write a script that uses a `with` statement to open the file for reading. Inside the `with` block, it should read the first line and print it. If a `FileNotFoundError` occurs during the `open` call, the program should print a user-friendly message like "The data file is missing."

3.  **Ruff Configuration:**
    Write a valid `[tool.ruff.lint]` section for a `pyproject.toml` file that enables the standard `flake8` rules (`E`, `F`) and the `isort` rules (`I`), but specifically disables the rule `E501` (line too long).

---
---

## Answers

<details>
<summary>Click to expand</summary>

### Part 1: Multiple Choice Questions

1.  **c) To execute cleanup code regardless of whether an exception occurred or not.**
2.  **b) It allows for more specific `except` blocks, so you can handle different application-specific errors differently.**
3.  **b) It stores the results of function calls and returns the cached result for the same inputs, improving performance for expensive operations.**
4.  **d) It preserves the original function's metadata (like `__name__` and `__doc__`) on the wrapped function.**
5.  **b) To analyze code for potential errors, bugs, and stylistic issues without running it.**

### Part 2: What's the Output?

1.  `Something looks off.`
    *Explanation: `basicConfig` was set to `level=logging.WARNING`. This means it will only process messages that are `WARNING` level or higher (`ERROR`, `CRITICAL`). The `INFO` message is ignored.*

2.  ```
    Start
    Finally block
    Returned from try
    ```
    *Explanation: The `finally` block is executed *after* the `try` block decides to `return`, but *before* the function actually returns the value. This guarantees cleanup happens.*

3.  `20`
    *Explanation: `functools.partial` creates a new function `double` which is equivalent to `multiply(2, x)`. Calling `double(10)` is the same as calling `multiply(2, 10)`.*

### Part 3: Find the Bug

1.  **Bug:** Catching the base `Exception` is too generic. It can hide unexpected errors and make debugging harder. You should catch the most specific exception possible.
    **Fix:**
    ```python
    my_dict = {"a": 1}
    try:
        print(my_dict["b"])
    except KeyError as e: # Catch the specific KeyError
        print(f"Caught a specific error: {e}")
    ```

2.  **Bug:** The `ValidationError` is created but not `raise`d. To trigger an exception, you must use the `raise` keyword.
    **Fix:**
    ```python
    class ValidationError(Exception):
        pass

    def validate_age(age):
        if age < 18:
            raise ValidationError("User must be 18 or older.")
        else:
            print("User is valid.")
    try:
        validate_age(15)
    except ValidationError as e:
        print(e)
    ```

### Part 4: Short Coding Challenges

1.  **Custom Exception and Validation:**
    ```python
    class InvalidEmailError(ValueError): # Inheriting from ValueError is also common
        pass

    def register_user(email: str):
        if "@" not in email:
            raise InvalidEmailError(f"'{email}' is not a valid email address.")
        print(f"User with email '{email}' registered successfully.")

    try:
        register_user("test.example.com")
    except InvalidEmailError as e:
        print(f"Registration failed: {e}")
    ```

2.  **Context Manager with `with`:**
    ```python
    try:
        with open("data.txt", "r") as f:
            first_line = f.readline()
            print(f"First line: {first_line.strip()}")
    except FileNotFoundError:
        print("Error: The data file is missing.")
    ```

3.  **Ruff Configuration:**
    ```toml
    # In pyproject.toml
    [tool.ruff.lint]
    select = ["E", "F", "I"]
    ignore = ["E501"]
    ```
</details>
