"""
Day 6: File Handling and I/O Operations
=======================================

Today we'll learn about file handling in Python - how to read from and write to files,
work with different file formats, and manage file operations safely.

Learning Objectives:
- Understand file operations (read, write, append)
- Learn about different file modes
- Work with text and binary files
- Handle file paths and directories
- Practice safe file operations
- Learn about context managers

Let's explore file handling!
"""

print("🐍 Welcome to Day 6: File Handling and I/O Operations!")
print("=" * 60)

# =============================================================================
# 1. WHAT IS FILE HANDLING?
# =============================================================================

print("\n📁 WHAT IS FILE HANDLING?")
print("-" * 25)

"""
File handling allows us to:
- Read data from files
- Write data to files
- Append data to existing files
- Work with different file formats
- Manage file operations safely
- Handle file paths and directories

Essential for data persistence and program interaction!
"""

# =============================================================================
# 2. BASIC FILE OPERATIONS
# =============================================================================

print("\n📝 BASIC FILE OPERATIONS")
print("-" * 25)

# Writing to a file
def write_to_file():
    """Demonstrate writing to a file."""
    filename = "sample.txt"
    
    # Write mode (creates new file or overwrites existing)
    with open(filename, 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a sample file.\n")
        file.write("Python file handling is awesome!\n")
    
    print(f"✅ Written to {filename}")

write_to_file()

# Reading from a file
def read_from_file():
    """Demonstrate reading from a file."""
    filename = "sample.txt"
    
    # Read mode
    with open(filename, 'r') as file:
        content = file.read()
        print(f"📖 Content of {filename}:")
        print(content)

read_from_file()

# Appending to a file
def append_to_file():
    """Demonstrate appending to a file."""
    filename = "sample.txt"
    
    # Append mode
    with open(filename, 'a') as file:
        file.write("This line was appended!\n")
        file.write("File handling is fun!\n")
    
    print(f"✅ Appended to {filename}")

append_to_file()

# =============================================================================
# 3. FILE MODES
# =============================================================================

print("\n🔧 FILE MODES")
print("-" * 15)

print("""
Common file modes:
- 'r': Read mode (default)
- 'w': Write mode (overwrites existing file)
- 'a': Append mode (adds to end of file)
- 'x': Exclusive creation (fails if file exists)
- 'b': Binary mode (for images, videos, etc.)
- 't': Text mode (default)
- '+': Read and write mode

Combinations:
- 'r+': Read and write
- 'w+': Write and read (overwrites)
- 'a+': Append and read
- 'rb': Read binary
- 'wb': Write binary
""")

# =============================================================================
# 4. READING FILE METHODS
# =============================================================================

print("\n📖 READING FILE METHODS")
print("-" * 28)

def demonstrate_reading_methods():
    """Demonstrate different ways to read files."""
    filename = "sample.txt"
    
    with open(filename, 'r') as file:
        print("Method 1: read() - reads entire file")
        content = file.read()
        print(f"Content: {content[:50]}...")
        
        # Reset file pointer
        file.seek(0)
        
        print("\nMethod 2: readline() - reads one line at a time")
        line1 = file.readline()
        print(f"First line: {line1.strip()}")
        
        print("\nMethod 3: readlines() - reads all lines into a list")
        file.seek(0)
        lines = file.readlines()
        print(f"All lines: {lines}")
        
        print("\nMethod 4: Iterating over file object")
        file.seek(0)
        for i, line in enumerate(file, 1):
            print(f"Line {i}: {line.strip()}")

demonstrate_reading_methods()

# =============================================================================
# 5. WORKING WITH CSV FILES
# =============================================================================

print("\n📊 WORKING WITH CSV FILES")
print("-" * 28)

import csv

def csv_operations():
    """Demonstrate CSV file operations."""
    # Writing CSV data
    csv_filename = "students.csv"
    
    students = [
        ["Name", "Age", "Grade"],
        ["Alice", "20", "A"],
        ["Bob", "19", "B"],
        ["Charlie", "21", "A"]
    ]
    
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)
    
    print(f"✅ Written CSV data to {csv_filename}")
    
    # Reading CSV data
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        print(f"📖 Reading {csv_filename}:")
        for row in reader:
            print(f"  {row}")

csv_operations()

# =============================================================================
# 6. WORKING WITH JSON FILES
# =============================================================================

print("\n📋 WORKING WITH JSON FILES")
print("-" * 30)

import json

def json_operations():
    """Demonstrate JSON file operations."""
    # Writing JSON data
    json_filename = "data.json"
    
    data = {
        "name": "Alice",
        "age": 25,
        "city": "New York",
        "hobbies": ["reading", "coding", "traveling"],
        "is_student": True
    }
    
    with open(json_filename, 'w') as file:
        json.dump(data, file, indent=2)
    
    print(f"✅ Written JSON data to {json_filename}")
    
    # Reading JSON data
    with open(json_filename, 'r') as file:
        loaded_data = json.load(file)
        print(f"📖 Reading {json_filename}:")
        print(f"  Name: {loaded_data['name']}")
        print(f"  Age: {loaded_data['age']}")
        print(f"  Hobbies: {loaded_data['hobbies']}")

json_operations()

# =============================================================================
# 7. FILE PATH OPERATIONS
# =============================================================================

print("\n🗂️ FILE PATH OPERATIONS")
print("-" * 25)

import os

def path_operations():
    """Demonstrate file path operations."""
    # Current working directory
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")
    
    # List files in directory
    files = os.listdir('.')
    print(f"Files in current directory: {files}")
    
    # Check if file exists
    filename = "sample.txt"
    if os.path.exists(filename):
        print(f"✅ {filename} exists")
        
        # Get file size
        size = os.path.getsize(filename)
        print(f"File size: {size} bytes")
        
        # Get file modification time
        mtime = os.path.getmtime(filename)
        print(f"Last modified: {mtime}")
    else:
        print(f"❌ {filename} does not exist")
    
    # Create directory
    if not os.path.exists("test_dir"):
        os.makedirs("test_dir")
        print("✅ Created test_dir")
    
    # Join paths
    file_path = os.path.join("test_dir", "test_file.txt")
    print(f"File path: {file_path}")

path_operations()

# =============================================================================
# 8. ERROR HANDLING IN FILE OPERATIONS
# =============================================================================

print("\n⚠️ ERROR HANDLING IN FILE OPERATIONS")
print("-" * 40)

def safe_file_operations():
    """Demonstrate safe file operations with error handling."""
    filename = "nonexistent.txt"
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"❌ File {filename} not found")
    except PermissionError:
        print(f"❌ Permission denied to read {filename}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    else:
        print("✅ File read successfully")
    finally:
        print("File operation completed")

safe_file_operations()

# =============================================================================
# 9. CONTEXT MANAGERS
# =============================================================================

print("\n🔒 CONTEXT MANAGERS")
print("-" * 20)

class FileManager:
    """Custom context manager for file operations."""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening {self.filename} in {self.mode} mode")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        return False

# Using custom context manager
def custom_context_manager():
    """Demonstrate custom context manager."""
    with FileManager("test.txt", "w") as file:
        file.write("This is a test file created with custom context manager!")
    
    with FileManager("test.txt", "r") as file:
        content = file.read()
        print(f"Content: {content}")

custom_context_manager()

# =============================================================================
# 10. PRACTICAL EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL EXAMPLES")
print("-" * 22)

# Example 1: Log File Manager
def log_manager():
    """Demonstrate log file management."""
    log_filename = "app.log"
    
    # Write log entries
    with open(log_filename, 'a') as log_file:
        log_file.write("2024-01-01 10:00:00 - Application started\n")
        log_file.write("2024-01-01 10:01:00 - User logged in\n")
        log_file.write("2024-01-01 10:02:00 - Data processed\n")
    
    # Read and display logs
    with open(log_filename, 'r') as log_file:
        print("Application Logs:")
        for line in log_file:
            print(f"  {line.strip()}")

log_manager()

# Example 2: Configuration File Manager
def config_manager():
    """Demonstrate configuration file management."""
    config_filename = "config.json"
    
    # Default configuration
    default_config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "myapp"
        },
        "app": {
            "debug": True,
            "version": "1.0.0"
        }
    }
    
    # Write configuration
    with open(config_filename, 'w') as config_file:
        json.dump(default_config, config_file, indent=2)
    
    # Read configuration
    with open(config_filename, 'r') as config_file:
        config = json.load(config_file)
        print("Application Configuration:")
        print(f"  Database: {config['database']['host']}:{config['database']['port']}")
        print(f"  App Version: {config['app']['version']}")
        print(f"  Debug Mode: {config['app']['debug']}")

config_manager()

# =============================================================================
# 11. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice file handling:

Exercise 1: Create a simple text editor
- Write a function to create a new file
- Write a function to read and display file content
- Write a function to append text to existing file

Exercise 2: Build a data logger
- Create a function to log events with timestamps
- Read and display log entries
- Filter logs by date or event type

Exercise 3: Create a configuration manager
- Store application settings in JSON format
- Read and update configuration values
- Validate configuration data

Exercise 4: Build a file backup system
- Copy files to backup directory
- Create timestamped backups
- Restore files from backups

Exercise 5: Create a CSV data processor
- Read CSV data and perform calculations
- Write processed data to new CSV file
- Handle missing or invalid data
""")

# =============================================================================
# 12. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
File handling best practices:

1. Always use context managers (with statement)
   ✅ with open('file.txt', 'r') as file:
   ❌ file = open('file.txt', 'r')

2. Handle exceptions properly
   ✅ try-except blocks for file operations
   ❌ Ignoring potential errors

3. Use appropriate file modes
   ✅ 'r' for reading, 'w' for writing, 'a' for appending
   ❌ Using wrong modes for operations

4. Close files properly
   ✅ Context managers handle this automatically
   ❌ Forgetting to close files

5. Use absolute paths when necessary
   ✅ os.path.abspath() for absolute paths
   ❌ Relying on relative paths only

6. Validate file existence
   ✅ os.path.exists() before operations
   ❌ Assuming files exist

7. Use appropriate encoding
   ✅ open('file.txt', 'r', encoding='utf-8')
   ❌ Ignoring encoding issues
""")

# =============================================================================
# 13. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ How to read from and write to files
✅ Different file modes and their uses
✅ Working with CSV and JSON files
✅ File path operations and directory management
✅ Error handling in file operations
✅ Context managers for safe file handling
✅ Best practices for file operations

Next Steps:
- Day 7: Exception Handling and Error Management
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
You've completed Day 6 of your Python journey!

You now understand:
- How to work with files safely and efficiently
- Different file formats and their uses
- File path operations and directory management
- Error handling in file operations
- Best practices for file handling

File handling is essential for data persistence!
Practice with the exercises to master this important skill.

Happy coding! 🐍✨
""")

# Clean up created files
import os
files_to_clean = ["sample.txt", "students.csv", "data.json", "test.txt", "app.log", "config.json"]
for file in files_to_clean:
    if os.path.exists(file):
        os.remove(file)
        print(f"🧹 Cleaned up {file}")

# Run the tutorial
if __name__ == "__main__":
    print("Day 6: File Handling and I/O Operations Tutorial")
    print("Run this file to see all examples in action!")
