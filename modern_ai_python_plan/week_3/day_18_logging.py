"""
Day 18: Logging
===============

While `print()` is great for quick debugging, it's not suitable for building
real applications. Logging is the standard practice for recording events,
errors, and diagnostic information as your application runs.

Learning Objectives:
1.  Understand why logging is superior to printing.
2.  Configure and use Python's built-in `logging` module.
3.  Learn about the different logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).
4.  Log exceptions effectively.
5.  (Advanced) Get an introduction to structured logging with `structlog`.
"""

import logging

# =============================================================================
# 1. WHY LOGGING IS BETTER THAN `print()`
# =============================================================================

"""
`print()` is simple, but logging gives you:
- Control over Severity: You can filter messages by their importance (e.g., show
  only errors in production, but show debug info during development).
- Timestamps: Logs automatically include when an event happened.
- Configurability: You can easily direct logs to different places (console, files,
  network sockets) without changing your application code.
- Context: Logs can include information like the module name, function name, and
  line number where the event occurred.
- Performance: Logging in production can be disabled at a certain level to avoid
  performance impact.
"""

# =============================================================================
# 2. PYTHON'S BUILT-IN `logging` MODULE
# =============================================================================

# --- Basic Configuration ---
# `logging.basicConfig` is a quick way to set up the root logger.
# You should only call this ONCE at the very start of your application.

logging.basicConfig(
    level=logging.DEBUG,  # Set the lowest level of messages to handle.
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    # filename='app.log', # Uncomment this to log to a file instead of the console.
    # filemode='w' # 'w' for overwrite, 'a' for append
)

# You get a logger instance for a specific module, usually with `__name__`.
# This allows you to know where the log message is coming from.
logger = logging.getLogger(__name__)

# --- Logging Levels ---
# These are used to indicate the severity of an event.
# The logger will only handle messages at its configured level or higher.

logger.debug("This is a debug message. Detailed information, typically of interest only when diagnosing problems.")
logger.info("This is an info message. Confirmation that things are working as expected.")
logger.warning("This is a warning message. An indication that something unexpected happened, but the software is still working as expected.")
logger.error("This is an error message. Due to a more serious problem, the software has not been able to perform some function.")
logger.critical("This is a critical message. A serious error, indicating that the program itself may be unable to continue running.")


# =============================================================================
# 3. LOGGING EXCEPTIONS
# =============================================================================

# The `logging` module has a brilliant feature for handling exceptions.
# `logger.exception()` automatically logs the message AND the full traceback.

try:
    result = 10 / 0
except ZeroDivisionError:
    logger.error("An error occurred during division.")
    # A better way:
    logger.exception("An unhandled exception occurred during division!")

# The output of `logger.exception` includes:
# ERROR - An unhandled exception occurred during division!
# Traceback (most recent call last):
#   File "...", line X, in <module>
#     result = 10 / 0
# ZeroDivisionError: division by zero
# This is invaluable for debugging.


# =============================================================================
# 4. (ADVANCED) INTRODUCTION TO STRUCTURED LOGGING
# =============================================================================
"""
In modern applications, especially those running in the cloud, logs are often
processed by machines (e.g., Datadog, Splunk). Structured logs, typically in
JSON format, are much easier for these systems to parse, filter, and analyze.

`structlog` is a popular library that makes structured logging easy.
"""

# Action: Install structlog
# > uv pip install structlog

import structlog

# You would typically configure structlog at the start of your app.
# This is a basic setup that outputs JSON.
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ]
)

slog = structlog.get_logger()

slog.info(
    "user.logged_in", # The event name is the first argument
    user_id=123,
    user_email="alice@example.com",
    status="success",
)

# The output is a clean, machine-readable JSON string:
# {"user_id": 123, "user_email": "alice@example.com", "status": "success", "event": "user.logged_in", "timestamp": "2023-10-27T10:30:00.123Z"}

# While you'll start with the standard `logging` module, keep `structlog` in
# mind as you build more complex, production-oriented applications.


# =============================================================================
# EXERCISES
# =============================================================================

# 1. Basic Logger Setup:
#    - Create a new Python script.
#    - Configure the `logging` module to log messages of level `INFO` and above
#      to a file named `system.log`.
#    - The log format should include the timestamp, level, and message.
#    - Write a few log messages of different levels (e.g., info, warning, error)
#      and check the contents of `system.log`.

# 2. Logging in a Function:
#    - Create a function `process_data(data: list)`.
#    - The function should take a list of numbers.
#    - It should log an `INFO` message when it starts.
#    - It should loop through the numbers and log a `DEBUG` message for each number
#      it is processing. (Note: You won't see this if your level is INFO).
#    - If it encounters a non-numeric type in the list, it should log an `ERROR`
#      message.
#    - It should log a `WARNING` if the list is empty.
#    - It should log an `INFO` message when it finishes.
#    - Test the function with different lists.

# 3. Exception Logging Practice:
#    - Write a function that reads a file.
#    - Use a `try...except` block to catch `FileNotFoundError`.
#    - Inside the `except` block, use `logger.exception()` to log that the file
#      could not be found, including the traceback.

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- Logging is the professional standard for recording application events.
- Use the different logging levels to control the verbosity of your logs.
- Always get a logger instance via `logging.getLogger(__name__)`.
- Use `logger.exception()` within an `except` block for the best error reporting.
- For modern, machine-readable logs, consider structured logging with libraries
  like `structlog`.

Next up: Day 19 - Diving into the powerful `functools` module.
"""
