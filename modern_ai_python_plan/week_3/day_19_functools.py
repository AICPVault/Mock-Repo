"""
Day 19: `functools` - Higher-Order Functions and Decorators
===========================================================

The `functools` module provides powerful tools for working with functions.
It contains utilities that make our functions more flexible, efficient, and
reusable. Today, we'll focus on three of its most useful components.

Learning Objectives:
1.  Use `functools.partial` to "freeze" function arguments.
2.  Use `functools.cache` for memoization to speed up expensive function calls.
3.  Understand `functools.wraps` and its importance when writing decorators (preview of Day 27).
"""
import functools
import time

# =============================================================================
# 1. `functools.partial` - Pre-configuring Functions
# =============================================================================

# `partial` allows you to create a new function from an existing one, with some
# of its arguments already filled in.

# A generic function to raise a number to a power.
def power(base, exponent):
    return base ** exponent

# Let's say we frequently need to calculate squares.
# Instead of always writing `power(x, 2)`, we can create a specialized function.

square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)

# The new `square` function is like `power`, but the `exponent` is fixed at 2.
print(f"Using partial for square(5): {square(5)}")
print(f"Using partial for cube(5): {cube(5)}")

# This is useful for making code cleaner and more readable, especially when
# passing functions as arguments (e.g., in `map` or event handlers).
# For example, instead of `map(lambda x: power(x, 2), my_list)`,
# you could just write `map(square, my_list)`.


# =============================================================================
# 2. `@functools.cache` - Memoization for Performance
# =============================================================================

# `@cache` is a decorator (more on decorators on Day 27) that automatically
# stores the results of a function call. If you call the function again with
# the same arguments, it returns the stored result instantly instead of
# re-computing it. This is called "memoization".

# This is extremely useful for computationally expensive functions.
# A classic example is the Fibonacci sequence.

@functools.cache
def fibonacci(n):
    """Calculates the nth Fibonacci number (with caching)."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Without `@cache`, `fibonacci(40)` would take a very long time because it
# re-calculates the same values over and over again.

print("\n--- Testing @cache with Fibonacci ---")
start_time = time.perf_counter()
result = fibonacci(35) # Let's use 35, 40 might be too slow without cache
end_time = time.perf_counter()
print(f"Result for fibonacci(35): {result}")
print(f"Time taken (with cache): {end_time - start_time:.6f} seconds")

# Call it again. The result will be returned instantly from the cache.
start_time_cached = time.perf_counter()
result_cached = fibonacci(35)
end_time_cached = time.perf_counter()
print(f"Time taken on second call (cached): {end_time_cached - start_time_cached:.6f} seconds")

# To see the difference, try commenting out the `@functools.cache` line and running the script again.

# Important: `@cache` only works for functions whose output depends *only* on
# their input arguments, and the arguments must be hashable (e.g., numbers, strings, tuples).


# =============================================================================
# 3. `functools.wraps` - Preserving Function Metadata
# =============================================================================

# This is a key tool for when you write your own decorators.
# A decorator is a function that wraps another function to add functionality.
# We will cover building them in detail on Day 27, but here's the concept.

def my_decorator(func):
    # Without `wraps`, the `wrapper` function "hides" the original `func`.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """This is the wrapper function's docstring."""
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello():
    """This is the original say_hello function's docstring."""
    print("Hello!")

# --- The problem that `wraps` solves ---
# If you DIDN'T use `@functools.wraps(func)` in the decorator, the metadata
# of `say_hello` would be replaced by the wrapper's metadata.
print("\n--- Inspecting function metadata with @wraps ---")
print(f"Function name: {say_hello.__name__}")
print(f"Docstring: {say_hello.__doc__}")

# If you comment out `@functools.wraps(func)`, the name will be "wrapper" and
# the docstring will be "This is the wrapper function's docstring.", which is
# confusing and breaks tools that rely on introspection (like debuggers).

# `@wraps` copies the original function's name, docstring, and other metadata
# over to the wrapper function, making the decorator transparent.


# =============================================================================
# EXERCISES
# =============================================================================

# 1. Partial Logging Functions:
#    - You have a generic logging function: `def log(level, message): print(f"[{level.upper()}] {message}")`.
#    - Use `functools.partial` to create two new functions: `log_info` and `log_error`.
#    - `log_info` should have the `level` argument pre-filled with "info".
#    - `log_error` should have the `level` argument pre-filled with "error".
#    - Call your new functions to test them.

# 2. Cache a Web Request (Simulation):
#    - Write a function `fetch_data(url: str) -> str` that simulates a slow network request.
#    - Inside the function, print "Fetching data from {url}..." and use `time.sleep(2)`
#      to pause for 2 seconds. Then, return f"Data from {url}".
#    - Apply the `@functools.cache` decorator to it.
#    - Call the function twice with the same URL and observe how the second call is instantaneous.

# 3. Basic Decorator with `wraps`:
#    - Write a simple decorator called `@timing_decorator` that prints the time
#      it takes for a function to execute.
#    - Make sure to use `@functools.wraps` inside your decorator.
#    - Apply this decorator to a function that does some work (e.g., `time.sleep(1)`).
#    - Verify that the decorated function still has its original `__name__`.

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- `functools.partial`: Creates specialized versions of functions by pre-filling arguments.
- `functools.cache`: A powerful and easy way to add memoization to your functions,
  drastically improving performance for expensive, repeated computations.
- `functools.wraps`: An essential helper for writing decorators that behave correctly
  and don't hide the metadata of the functions they wrap.

Next up: Day 20 - Project Day! We'll build a command-line task tracker.
"""
