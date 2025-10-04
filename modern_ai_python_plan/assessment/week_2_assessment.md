
# Week 2 Knowledge Assessment: Functions, Files, and Data Formats

This assessment covers topics from Day 8 to Day 14.

---

### Part 1: Multiple Choice Questions

1.  What does `*args` in a function signature allow you to do?
    a) Accept only keyword arguments.
    b) Accept any number of positional arguments, which are collected into a tuple.
    c) Make all arguments after it keyword-only.
    d) Reference global arguments.

2.  Which of the following is the correct syntax for a keyword-only argument `api_key`?
    a) `def connect(api_key=*, ...):`
    b) `def connect(api_key, /, ...):`
    c) `def connect(*, api_key, ...):`
    d) `def connect(keyword api_key, ...):`

3.  What is the primary advantage of using `pathlib` over string paths?
    a) It's always faster.
    b) It treats paths as objects with methods, making manipulation cleaner and OS-agnostic.
    c) It can handle web URLs.
    d) It automatically validates that a file exists.

4.  When reading a TOML file using Python's built-in `tomllib`, how must the file be opened?
    a) In text mode (`'r'`).
    b) In append mode (`'a'`).
    c) In binary mode (`'rb'`).
    d) It doesn't need to be opened; `tomllib` handles it.

5.  What is the key difference between `map()` and `filter()`?
    a) `map()` returns a list, `filter()` returns an iterator.
    b) `map()` applies a function to every element, while `filter()` selects elements based on a function that returns a boolean.
    c) `map()` can only be used with lambda functions.
    d) `filter()` is used for sorting, while `map()` is for transformation.

---

### Part 2: What's the Output?

Predict the output of the following code snippets.

1.  ```python
    def process_data(a, b, /):
        print(a + b)

    try:
        process_data(a=5, b=10)
    except TypeError as e:
        print(e)
    ```

2.  ```python
    import json

    data = {"users": ["Alice", "Bob"], "count": 2}
    json_string = json.dumps(data, indent=None)
    print(json_string)
    ```

3.  ```python
    words = ["a", "short", "list"]
    result = sorted(words, key=len)
    print(result)
    ```

---

### Part 3: Find the Bug

Identify and fix the bug in each code snippet.

1.  ```python
    # Goal: Get a list of the first letters of each word.
    words = ["apple", "banana", "cherry"]
    first_letters = map(lambda w: w[0], words)
    print(first_letters[0]) # This will raise a TypeError
    ```

2.  ```python
    # Goal: Create a dictionary of users and their scores.
    users = ["Alice", "Bob"]
    scores = [95, 88]
    user_scores = {user: score for user in users for score in scores}
    print(user_scores) # The output is not what's expected.
    ```

---

### Part 4: Short Coding Challenges

1.  **Lambda for Sorting:**
    You have a list of dictionaries: `data = [{'name': 'Eve', 'age': 22}, {'name': 'Frank', 'age': 19}]`. Write a single line of code to sort this list by `age` in descending order.

2.  **File Writer Function:**
    Write a function `save_greetings(name: str)` that takes a name and appends a line `Hello, {name}!` to a file named `greetings.log`. The function should use `pathlib` and a `with` statement.

3.  **JSON to List of Tuples:**
    You are given the following JSON string:
    `'{"101": "Product A", "102": "Product B", "103": "Product C"}'`
    Write code to parse this JSON and convert it into a list of tuples, where each tuple is `(id, name)`. The ID should be an integer. The final list should be `[(101, 'Product A'), (102, 'Product B'), (103, 'Product C')]`.

---
---

## Answers

<details>
<summary>Click to expand</summary>

### Part 1: Multiple Choice Questions

1.  **b) Accept any number of positional arguments, which are collected into a tuple.**
2.  **c) `def connect(*, api_key, ...):`** (Arguments after a bare `*` must be specified by keyword).
3.  **b) It treats paths as objects with methods, making manipulation cleaner and OS-agnostic.**
4.  **c) In binary mode (`'rb'`).**
5.  **b) `map()` applies a function to every element, while `filter()` selects elements based on a function that returns a boolean.**

### Part 2: What's the Output?

1.  `process_data() got some positional-only arguments passed as keyword arguments: 'a, b'` (or similar `TypeError` message).
    *Explanation: The `/` in the function signature makes `a` and `b` positional-only arguments.*

2.  `{"users": ["Alice", "Bob"], "count": 2}`
    *Explanation: `json.dumps` with `indent=None` creates the most compact single-line JSON representation.*

3.  `['a', 'list', 'short']`
    *Explanation: `sorted` with `key=len` sorts the elements based on the return value of the `len` function for each element, from shortest to longest.*

### Part 3: Find the Bug

1.  **Bug:** `map()` (and `filter()`) returns an iterator, not a list. Iterators do not support indexing (`[0]`).
    **Fix:** Convert the iterator to a list first.
    ```python
    words = ["apple", "banana", "cherry"]
    first_letters_iterator = map(lambda w: w[0], words)
    first_letters_list = list(first_letters_iterator) # Convert to list
    print(first_letters_list[0])
    ```

2.  **Bug:** A nested comprehension iterates over *every combination* of the outer and inner loops. This creates a dictionary where every user is mapped to the last score.
    **Fix:** Use `zip` to pair the items correctly.
    ```python
    users = ["Alice", "Bob"]
    scores = [95, 88]
    user_scores = {user: score for user, score in zip(users, scores)}
    print(user_scores) # Output: {'Alice': 95, 'Bob': 88}
    ```

### Part 4: Short Coding Challenges

1.  **Lambda for Sorting:**
    ```python
    data = [{'name': 'Eve', 'age': 22}, {'name': 'Frank', 'age': 19}]
    sorted_data = sorted(data, key=lambda item: item['age'], reverse=True)
    print(sorted_data)
    ```

2.  **File Writer Function:**
    ```python
    from pathlib import Path

    def save_greetings(name: str):
        log_file = Path("greetings.log")
        with log_file.open(mode="a", encoding="utf-8") as f:
            f.write(f"Hello, {name}!\n")

    # Example usage:
    save_greetings("Dave")
    save_greetings("Grace")
    ```

3.  **JSON to List of Tuples:**
    ```python
    import json

    json_string = '{"101": "Product A", "102": "Product B", "103": "Product C"}'
    data = json.loads(json_string)
    product_list = [(int(id_str), name) for id_str, name in data.items()]
    print(product_list)
    ```
</details>
