"""
Day 13: File I/O - Reading and Writing Files
============================================

Interacting with the file system is a fundamental programming task. Today, we'll
explore the modern, object-oriented way to handle file paths and I/O using `pathlib`.

Learning Objectives:
1.  Understand and use the `pathlib.Path` object for path manipulation.
2.  Read data from text files using modern `with` statements.
3.  Write data to text files.
4.  Perform basic CSV file reading and writing using the built-in `csv` module.
"""

from pathlib import Path
import csv

# =============================================================================
# 1. `pathlib` - THE MODERN WAY TO HANDLE FILE PATHS
# =============================================================================

# `pathlib` treats paths as objects with methods, which is much cleaner and
# more intuitive than working with strings.

# Create a Path object. It automatically handles OS-specific separators (e.g., / or \).
# `Path.cwd()` gets the current working directory.
current_dir: Path = Path.cwd()
print(f"Current directory: {current_dir}")

# You can join paths using the `/` operator.
data_dir: Path = current_dir / "data" # Create a path for a "data" subdirectory
print(f"Data directory path: {data_dir}")

# Create the directory if it doesn't exist.
data_dir.mkdir(exist_ok=True) # `exist_ok=True` prevents an error if it's already there

# Create a path to a specific file.
my_file: Path = data_dir / "greetings.txt"
print(f"File path: {my_file}")

# Path objects have useful attributes.
print(f"File name: {my_file.name}")
print(f"File stem (name without extension): {my_file.stem}")
print(f"File suffix (extension): {my_file.suffix}")
print(f"File exists? {my_file.exists()}")


# =============================================================================
# 2. READING FROM TEXT FILES
# =============================================================================

# The `with` statement is the recommended way to open files. It ensures the file
# is automatically closed even if errors occur.

# First, let's write something to the file so we can read it.
# `my_file.write_text()` is a convenient `pathlib` method.
my_file.write_text("Hello from Python!\nWelcome to file I/O.")
print(f"\nWrote to {my_file.name}")

# --- Reading the entire file content at once ---
if my_file.exists():
    content: str = my_file.read_text()
    print("\n--- Reading entire file ---")
    print(content)

# --- Reading a file line by line ---
# This is more memory-efficient for very large files.
print("\n--- Reading file line by line ---")
try:
    with my_file.open(mode='r', encoding='utf-8') as f:
        for line in f:
            print(f"Line: {line.strip()}") # .strip() removes leading/trailing whitespace
except FileNotFoundError:
    print(f"Error: {my_file} not found.")


# =============================================================================
# 3. WRITING TO TEXT FILES
# =============================================================================

# Writing will overwrite the file by default. To add to it, use 'append' mode.
log_file: Path = data_dir / "app.log"

# --- Writing (overwriting) a file ---
# We use .open() with mode 'w' for more control.
with log_file.open(mode='w', encoding='utf-8') as f:
    f.write("Application started.\n")
    f.write("Processing data...\n")
print(f"\nWrote to {log_file.name}")

# --- Appending to a file ---
# Use mode 'a' to add content to the end of the file.
with log_file.open(mode='a', encoding='utf-8') as f:
    f.write("Data processing complete.\n")
    f.write("Application finished.\n")
print(f"Appended to {log_file.name}")

print("\n--- Final log file content ---")
print(log_file.read_text())


# =============================================================================
# 4. BASIC CSV HANDLING
# =============================================================================

# CSV (Comma-Separated Values) is a common format for tabular data.
# Python's built-in `csv` module makes it easy to work with.
users_csv_file: Path = data_dir / "users.csv"

# --- Writing to a CSV file ---
# Data is typically a list of lists (rows).
header: list[str] = ["username", "email", "user_id"]
users_data: list[list] = [
    ["alice_py", "alice@example.com", 101],
    ["bob_rust", "bob@example.com", 102],
]

with users_csv_file.open(mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)   # Write the header row
    writer.writerows(users_data) # Write all the data rows
print(f"\nWrote data to {users_csv_file.name}")

# --- Reading from a CSV file ---
print("\n--- Reading from CSV ---")
try:
    with users_csv_file.open(mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader) # Read the first line as the header
        print(f"Header: {header}")
        for row in reader:
            print(f"  User: {row[0]}, Email: {row[1]}, ID: {row[2]}")
except FileNotFoundError:
    print(f"Error: {users_csv_file} not found.")


# =============================================================================
# EXERCISES
# =============================================================================

# 1. File Lister:
#    - Create a subdirectory in your project named "my_test_files".
#    - Create a few empty text files inside it (e.g., "a.txt", "b.txt", "c.log").
#    - Write a Python script that uses `pathlib` to list all the files in that
#      directory and print their names.

# 2. User Notes Saver:
#    - Write a script that prompts the user to enter a short note.
#    - The script should save this note to a file named `notes.txt`.
#    - Each time the script is run, it should append the new note to the file
#      on a new line, rather than overwriting the old ones.

# 3. Simple CSV Exporter:
#    - You have a list of dictionaries:
#      `products = [
#          {'id': 1, 'name': 'Laptop', 'price': 1200},
#          {'id': 2, 'name': 'Mouse', 'price': 25},
#      ]`
#    - Write a script to export this data to a `products.csv` file with a header row.
#      (Hint: you'll need to extract the header and convert each dictionary to a list).

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- `pathlib.Path` is the modern, object-oriented standard for handling file paths.
- The `with open(...) as f:` syntax is essential for safe file handling as it
  manages closing the file for you.
- `Path.read_text()` and `Path.write_text()` are convenient for simple read/write operations.
- The `csv` module is your go-to for basic reading and writing of CSV files.

Next up: Day 14 - Handling other common data formats: JSON and TOML.
"""
