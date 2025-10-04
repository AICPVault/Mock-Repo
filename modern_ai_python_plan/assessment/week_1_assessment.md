
# Week 1 Knowledge Assessment: Python Foundations

This assessment covers topics from Day 1 to Day 7. Try to answer the questions
without looking at the tutorial files.

---

### Part 1: Multiple Choice Questions

1.  What is the key difference between a list and a tuple in Python?
    a) Lists are ordered, tuples are unordered.
    b) Lists can store mixed data types, tuples cannot.
    c) Lists are mutable, tuples are immutable.
    d) Lists use `[]`, tuples use `{}`.

2.  What does the `my_string[1:4]` slice expression return for `my_string = "HelloPython"`?
    a) `"ell"`
    b) `"ello"`
    c) `"el"`
    d) `"Hel"`

3.  Which of the following is considered "falsy" in Python?
    a) `True`
    b) `1`
    c) `[]` (an empty list)
    d) `"0"`

4.  What is the primary purpose of the `zip()` function?
    a) To compress files.
    b) To iterate over a single list with indices.
    c) To combine multiple iterables into a single iterator of tuples.
    d) To sort a list in reverse order.

5.  In a `match/case` statement, what is the purpose of the `_` case?
    a) To match the underscore character specifically.
    b) It's a wildcard that acts as a default case if no other matches are found.
    c) It's an error and is not valid syntax.
    d) It matches only empty or `None` values.

---

### Part 2: What's the Output?

Predict the output of the following code snippets.

1.  ```python
    my_list = [1, 2, 3]
    my_list.append([4, 5])
    print(len(my_list))
    ```

2.  ```python
    my_set_a = {1, 2, 3, 4}
    my_set_b = {3, 4, 5, 6}
    print(my_set_a & my_set_b)
    ```

3.  ```python
    for i in range(5):
        if i == 2:
            continue
        if i == 4:
            break
        print(i, end=" ")
    ```

---

### Part 3: Find the Bug

Identify and fix the bug in each code snippet.

1.  ```python
    # Goal: Create a tuple with a single item.
    my_tuple = (5)
    print(type(my_tuple)) # This doesn't print <class 'tuple'>
    ```

2.  ```python
    # Goal: Update the user's name in the dictionary.
    user_profile = {
        "name": "Alice",
        "age": 30
    }
    user_profile.add("name", "Alicia")
    print(user_profile)
    ```

---

### Part 4: Short Coding Challenges

1.  **List Filtering:**
    Given the list `numbers = [10, 21, 4, 45, 66, 93]`, write a single line of code (preferably a list comprehension) to create a new list that contains only the odd numbers from the original list.

2.  **Dictionary Creation:**
    You have two lists: `keys = ['name', 'city', 'role']` and `values = ['Bob', 'Paris', 'Developer']`. Create a dictionary from these two lists.

3.  **FizzBuzz Variation:**
    Write a `for` loop that iterates from 1 to 20. For each number, print "Fizz" if the number is divisible by 3, "Buzz" if it's divisible by 5, and the number itself otherwise. If it's divisible by both 3 and 5, it should also print "Fizz".

---
---

## Answers

<details>
<summary>Click to expand</summary>

### Part 1: Multiple Choice Questions

1.  **c) Lists are mutable, tuples are immutable.** (Lists can be changed after creation, tuples cannot).
2.  **a) `"ell"`** (Slicing goes from the start index up to, but not including, the stop index).
3.  **c) `[]` (an empty list)** (Empty collections, `None`, `False`, and numeric zero are falsy).
4.  **c) To combine multiple iterables into a single iterator of tuples.**
5.  **b) It's a wildcard that acts as a default case if no other matches are found.**

### Part 2: What's the Output?

1.  `4`
    *Explanation: `append` adds the entire list `[4, 5]` as a single, nested element. The list becomes `[1, 2, 3, [4, 5]]`.*

2.  `{3, 4}`
    *Explanation: The `&` operator finds the intersection of the two sets (the elements they have in common).*

3.  `0 1 3`
    *Explanation: The loop prints 0 and 1. When `i` is 2, `continue` skips the `print`. When `i` is 3, it prints. When `i` is 4, `break` terminates the loop entirely.*

### Part 3: Find the Bug

1.  **Bug:** A single-item tuple needs a trailing comma to distinguish it from a grouping parenthesis.
    **Fix:**
    ```python
    my_tuple = (5,) # Add a trailing comma
    print(type(my_tuple))
    ```

2.  **Bug:** Dictionaries do not have an `.add()` method. You update an existing key by direct assignment.
    **Fix:**
    ```python
    user_profile = {
        "name": "Alice",
        "age": 30
    }
    user_profile["name"] = "Alicia" # Use assignment to update the value
    print(user_profile)
    ```

### Part 4: Short Coding Challenges

1.  **List Filtering:**
    ```python
    numbers = [10, 21, 4, 45, 66, 93]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    print(odd_numbers) # Output: [21, 45, 93]
    ```

2.  **Dictionary Creation:**
    ```python
    keys = ['name', 'city', 'role']
    values = ['Bob', 'Paris', 'Developer']
    user_dict = dict(zip(keys, values))
    # A comprehension also works: {k: v for k, v in zip(keys, values)}
    print(user_dict)
    ```

3.  **FizzBuzz Variation:**
    ```python
    for i in range(1, 21):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    ```
</details>
