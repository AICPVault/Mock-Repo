"""
Day 14: Handling JSON, TOML, and YAML
======================================

Today we'll learn to work with three of the most common data serialization
and configuration file formats used in modern software development.

Learning Objectives:
1.  Read and write data in JSON format using the `json` module.
2.  Understand and parse TOML, the modern standard for Python project configuration.
3.  Get an introduction to YAML, a popular format for configuration and data.
4.  Know which format to choose for different use cases.
"""

import json
import tomllib  # For reading TOML, available in Python 3.11+
# For writing TOML and handling YAML, we need to install third-party libraries:
# uv pip install tomlkit pyyaml
import tomlkit # A popular library for writing/editing TOML
import yaml
from pathlib import Path

# Setup a directory for our data files
data_dir = Path("config_data")
data_dir.mkdir(exist_ok=True)

# =============================================================================
# 1. JSON (JavaScript Object Notation)
# =============================================================================
"""
- Ubiquitous for web APIs and data exchange.
- Human-readable but can be a bit verbose (curly braces, quotes everywhere).
- Natively supported in Python with the `json` module.
- Maps directly to Python dictionaries, lists, strings, numbers, booleans, and None.
"""

# A Python dictionary we want to store
python_data = {
    "name": "Project Apollo",
    "version": "1.2.0",
    "is_active": True,
    "team_members": ["Alice", "Bob", "Charlie"],
    "settings": None
}

# --- Writing JSON ---
json_file = data_dir / "config.json"
with json_file.open(mode="w", encoding="utf-8") as f:
    # `json.dump` writes the object to a file-like object.
    # `indent=2` makes it human-readable.
    json.dump(python_data, f, indent=2)

print(f"--- Wrote JSON to {json_file} ---")
print(json_file.read_text())

# --- Reading JSON ---
with json_file.open(mode="r", encoding="utf-8") as f:
    # `json.load` reads from a file-like object and parses it into a Python object.
    loaded_json_data = json.load(f)

print(f"--- Read JSON data back into Python ---")
print(f"Project Name: {loaded_json_data['name']}")
assert python_data == loaded_json_data


# =============================================================================
# 2. TOML (Tom's Obvious, Minimal Language)
# =============================================================================
"""
- The official standard for Python package configuration (`pyproject.toml`).
- Designed to be explicitly structured and easy for humans to read.
- Great for configuration files that are maintained by developers.
- Natively supported for reading in Python 3.11+ (`tomllib`).
"""

# --- Reading TOML ---
# Let's first create a TOML file to read.
toml_content = """
# This is a TOML configuration file.
title = "My Awesome App"
version = "0.1.0"

[database]
host = "localhost"
port = 5432
enabled = true

[users]
roles = ["admin", "editor", "viewer"]
"""
toml_file = data_dir / "config.toml"
toml_file.write_text(toml_content)

print(f"\n--- Wrote TOML to {toml_file} ---")
print(toml_content)

# Python 3.11+ has a built-in reader
with toml_file.open(mode="rb") as f: # Must be opened in binary mode
    loaded_toml_data = tomllib.load(f)

print("--- Read TOML data back into Python ---")
print(f"Database host: {loaded_toml_data['database']['host']}")
print(f"User roles: {loaded_toml_data['users']['roles']}")


# =============================================================================
# 3. YAML (YAML Ain't Markup Language)
# =============================================================================
"""
- Very popular for configuration (e.g., Docker Compose, GitHub Actions).
- Minimalist syntax relies on indentation, making it very clean to read.
- Can be more powerful than JSON (supports comments, anchors, multi-line strings).
- Requires a third-party library like `PyYAML`.
"""

# --- Writing YAML ---
yaml_file = data_dir / "config.yaml"
with yaml_file.open(mode="w", encoding="utf-8") as f:
    # `yaml.dump` works similarly to `json.dump`.
    # `sort_keys=False` preserves the original order of our dictionary.
    yaml.dump(python_data, f, sort_keys=False, default_flow_style=False)

print(f"\n--- Wrote YAML to {yaml_file} ---")
print(yaml_file.read_text())

# --- Reading YAML ---
with yaml_file.open(mode="r", encoding="utf-8") as f:
    # Use `yaml.safe_load` to prevent arbitrary code execution from untrusted files.
    loaded_yaml_data = yaml.safe_load(f)

print("--- Read YAML data back into Python ---")
print(f"Team members from YAML: {loaded_yaml_data['team_members']}")
assert python_data == loaded_yaml_data


# =============================================================================
# EXERCISES
# =============================================================================

# 1. JSON User Preferences:
#    - Create a Python dictionary representing user preferences (e.g., `theme`, `notifications`, `language`).
#    - Write this dictionary to a file named `user_prefs.json` in a human-readable format.
#    - Read the file back into a new Python variable and print one of the preferences.

# 2. Parse a `pyproject.toml`:
#    - Find a `pyproject.toml` file in a Python project you have on your machine, or use this example:
#      ```toml
#      [tool.poetry]
#      name = "my-project"
#      version = "1.0.0"
#      description = "A cool project."
#
#      [tool.poetry.dependencies]
#      python = "^3.11"
#      fastapi = "^0.104.1"
#      ```
#    - Write a script to read this file and print out the project's `name` and its `python` version requirement.

# 3. Create a Docker Compose-like YAML:
#    - Create a Python dictionary that models a simple web service configuration. It should have a top-level
#      key `services`, which contains another dictionary for a `web` service. The `web` service should
#      have keys like `image`, `ports`, and `environment`.
#    - Write this dictionary to a `docker-style.yaml` file.

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
- **JSON**: Best for data interchange (APIs). Universal support.
- **TOML**: Best for developer-maintained configuration files. The Python standard.
- **YAML**: Best for complex, human-written configuration (DevOps, CI/CD). Clean syntax.
- Always use standard libraries (`json`, `tomllib`) when available.
- For third-party formats, choose well-maintained libraries (`tomlkit`, `PyYAML`).

This concludes Week 2! You've gone from basic functions to building a CLI app
and handling common file formats.

Next up: Week 3 - Error Handling and Code Quality.
"""
