"""
Day 10: Advanced Data Structures and Algorithms
===============================================

Today we'll explore advanced data structures and algorithms in Python.
We'll learn about collections, algorithms, and how to solve complex problems
efficiently using Python's powerful built-in tools.

Learning Objectives:
- Master Python's collections module
- Learn about advanced data structures
- Understand algorithm complexity
- Practice common algorithms
- Build efficient data processing solutions
- Explore real-world applications

Let's dive into advanced data structures!
"""

print("🐍 Welcome to Day 10: Advanced Data Structures and Algorithms!")
print("=" * 65)

# =============================================================================
# 1. WHAT ARE ADVANCED DATA STRUCTURES?
# =============================================================================

print("\n🏗️ WHAT ARE ADVANCED DATA STRUCTURES?")
print("-" * 40)

"""
Advanced data structures are specialized ways of organizing data that provide
efficient operations for specific use cases:

COLLECTIONS MODULE:
- deque: Double-ended queue
- Counter: Count hashable objects
- defaultdict: Dictionary with default factory
- OrderedDict: Dictionary that remembers insertion order
- ChainMap: Combine multiple mappings
- namedtuple: Tuple with named fields

ALGORITHMS:
- Sorting algorithms
- Searching algorithms
- Graph algorithms
- Dynamic programming
- Greedy algorithms

Benefits:
- Better performance for specific operations
- More efficient memory usage
- Specialized functionality
- Real-world problem solving
"""

# =============================================================================
# 2. COLLECTIONS MODULE
# =============================================================================

print("\n📦 COLLECTIONS MODULE")
print("-" * 25)

from collections import deque, Counter, defaultdict, OrderedDict, ChainMap, namedtuple

# deque - Double-ended queue
print("DEQUE - Double-ended queue:")
dq = deque([1, 2, 3, 4, 5])
print(f"Initial deque: {dq}")

dq.append(6)  # Add to right
dq.appendleft(0)  # Add to left
print(f"After append operations: {dq}")

dq.pop()  # Remove from right
dq.popleft()  # Remove from left
print(f"After pop operations: {dq}")

# Counter - Count hashable objects
print("\nCOUNTER - Count objects:")
text = "hello world"
counter = Counter(text)
print(f"Counter for '{text}': {counter}")
print(f"Most common 3: {counter.most_common(3)}")

# defaultdict - Dictionary with default factory
print("\nDEFAULTDICT - Dictionary with default factory:")
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
dd['vegetables'].append('carrot')
print(f"DefaultDict: {dict(dd)}")

# OrderedDict - Dictionary that remembers insertion order
print("\nORDEREDDICT - Dictionary with insertion order:")
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
print(f"OrderedDict: {od}")

# ChainMap - Combine multiple mappings
print("\nCHAINMAP - Combine mappings:")
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
chain = ChainMap(dict1, dict2)
print(f"ChainMap: {dict(chain)}")

# namedtuple - Tuple with named fields
print("\nNAMEDTUPLE - Tuple with named fields:")
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(3, 4)
p2 = Point(0, 0)
print(f"Point 1: {p1}, x={p1.x}, y={p1.y}")
print(f"Point 2: {p2}")

# =============================================================================
# 3. ADVANCED LIST OPERATIONS
# =============================================================================

print("\n📋 ADVANCED LIST OPERATIONS")
print("-" * 30)

# List comprehensions with conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print(f"Flattened matrix: {flattened}")

# List comprehensions with multiple conditions
words = ["hello", "world", "python", "programming", "code"]
long_words = [word.upper() for word in words if len(word) > 4 and 'o' in word]
print(f"Long words with 'o': {long_words}")

# =============================================================================
# 4. SORTING ALGORITHMS
# =============================================================================

print("\n🔄 SORTING ALGORITHMS")
print("-" * 25)

def bubble_sort(arr):
    """Bubble sort algorithm."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    """Quick sort algorithm."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """Merge sort algorithm."""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Demonstrate sorting algorithms
test_data = [64, 34, 25, 12, 22, 11, 90]
print(f"Original data: {test_data}")

# Python's built-in sort
sorted_data = sorted(test_data)
print(f"Built-in sort: {sorted_data}")

# Custom sorting
bubble_result = bubble_sort(test_data.copy())
quick_result = quick_sort(test_data.copy())
merge_result = merge_sort(test_data.copy())

print(f"Bubble sort: {bubble_result}")
print(f"Quick sort: {quick_result}")
print(f"Merge sort: {merge_result}")

# =============================================================================
# 5. SEARCHING ALGORITHMS
# =============================================================================

print("\n🔍 SEARCHING ALGORITHMS")
print("-" * 25)

def linear_search(arr, target):
    """Linear search algorithm."""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def binary_search(arr, target):
    """Binary search algorithm (requires sorted array)."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def interpolation_search(arr, target):
    """Interpolation search algorithm."""
    left, right = 0, len(arr) - 1
    
    while left <= right and arr[left] <= target <= arr[right]:
        if left == right:
            return left if arr[left] == target else -1
        
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1

# Demonstrate searching algorithms
sorted_data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11

print(f"Searching for {target} in {sorted_data}")
print(f"Linear search: {linear_search(sorted_data, target)}")
print(f"Binary search: {binary_search(sorted_data, target)}")
print(f"Interpolation search: {interpolation_search(sorted_data, target)}")

# =============================================================================
# 6. GRAPH ALGORITHMS
# =============================================================================

print("\n🕸️ GRAPH ALGORITHMS")
print("-" * 20)

from collections import defaultdict

class Graph:
    """Graph class for demonstrating graph algorithms."""
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        """Add an edge to the graph."""
        self.graph[u].append(v)
    
    def bfs(self, start):
        """Breadth-First Search."""
        visited = set()
        queue = [start]
        result = []
        
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(self.graph[vertex])
        
        return result
    
    def dfs(self, start, visited=None):
        """Depth-First Search."""
        if visited is None:
            visited = set()
        
        visited.add(start)
        result = [start]
        
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        
        return result
    
    def has_path(self, start, end):
        """Check if there's a path between two nodes."""
        visited = set()
        queue = [start]
        
        while queue:
            vertex = queue.pop(0)
            if vertex == end:
                return True
            
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(self.graph[vertex])
        
        return False

# Demonstrate graph algorithms
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Graph structure:")
for node, neighbors in g.graph.items():
    print(f"  {node}: {neighbors}")

print(f"BFS from 2: {g.bfs(2)}")
print(f"DFS from 2: {g.dfs(2)}")
print(f"Path from 0 to 3: {g.has_path(0, 3)}")
print(f"Path from 3 to 0: {g.has_path(3, 0)}")

# =============================================================================
# 7. DYNAMIC PROGRAMMING
# =============================================================================

print("\n💡 DYNAMIC PROGRAMMING")
print("-" * 25)

def fibonacci_dp(n):
    """Fibonacci using dynamic programming."""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def longest_common_subsequence(text1, text2):
    """Find the longest common subsequence."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def knapsack(weights, values, capacity):
    """0/1 Knapsack problem."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], 
                              dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# Demonstrate dynamic programming
print("Fibonacci (DP):")
for i in range(10):
    print(f"F({i}) = {fibonacci_dp(i)}")

print(f"\nLongest Common Subsequence:")
text1 = "ABCDGH"
text2 = "AEDFHR"
lcs_length = longest_common_subsequence(text1, text2)
print(f"LCS of '{text1}' and '{text2}': {lcs_length}")

print(f"\nKnapsack Problem:")
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_value = knapsack(weights, values, capacity)
print(f"Max value for capacity {capacity}: {max_value}")

# =============================================================================
# 8. PRACTICAL EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL EXAMPLES")
print("-" * 22)

# Example 1: Text Analysis
def analyze_text(text):
    """Analyze text using advanced data structures."""
    # Count word frequencies
    words = text.lower().split()
    word_count = Counter(words)
    
    # Find most common words
    most_common = word_count.most_common(5)
    
    # Count characters
    char_count = Counter(text)
    
    # Find unique words
    unique_words = set(words)
    
    return {
        'word_count': word_count,
        'most_common': most_common,
        'char_count': char_count,
        'unique_words': len(unique_words),
        'total_words': len(words)
    }

sample_text = "Python is a great programming language. Python is versatile and Python is powerful."
analysis = analyze_text(sample_text)

print("Text Analysis:")
print(f"Most common words: {analysis['most_common']}")
print(f"Unique words: {analysis['unique_words']}")
print(f"Total words: {analysis['total_words']}")

# Example 2: Data Processing Pipeline
def process_data(data):
    """Process data using advanced algorithms."""
    # Remove duplicates while preserving order
    seen = set()
    unique_data = []
    for item in data:
        if item not in seen:
            seen.add(item)
            unique_data.append(item)
    
    # Sort data
    sorted_data = sorted(unique_data)
    
    # Find median
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    
    # Find mode
    counter = Counter(sorted_data)
    mode = counter.most_common(1)[0][0]
    
    return {
        'unique_data': unique_data,
        'sorted_data': sorted_data,
        'median': median,
        'mode': mode,
        'count': len(unique_data)
    }

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
processed = process_data(data)

print(f"\nData Processing:")
print(f"Original data: {data}")
print(f"Unique data: {processed['unique_data']}")
print(f"Sorted data: {processed['sorted_data']}")
print(f"Median: {processed['median']}")
print(f"Mode: {processed['mode']}")

# Example 3: Cache Implementation
class LRUCache:
    """Least Recently Used Cache implementation."""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        """Get value from cache."""
        if key in self.cache:
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self, key, value):
        """Put value in cache."""
        if key in self.cache:
            # Update existing key
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used
            self.cache.popitem(last=False)
        
        self.cache[key] = value

# Demonstrate LRU Cache
cache = LRUCache(3)
cache.put(1, "one")
cache.put(2, "two")
cache.put(3, "three")
print(f"\nLRU Cache:")
print(f"Get 1: {cache.get(1)}")
cache.put(4, "four")  # This should remove key 2
print(f"Get 2: {cache.get(2)}")  # Should return -1
print(f"Get 4: {cache.get(4)}")

# =============================================================================
# 9. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice advanced data structures:

Exercise 1: Implement a Priority Queue
- Use heapq module
- Add elements with priorities
- Remove highest priority element
- Handle edge cases

Exercise 2: Build a Trie (Prefix Tree)
- Insert words into trie
- Search for words
- Find all words with given prefix
- Delete words from trie

Exercise 3: Create a Graph Traversal System
- Implement BFS and DFS
- Find shortest path between nodes
- Detect cycles in graph
- Find connected components

Exercise 4: Build a Data Compression System
- Implement Huffman coding
- Compress and decompress text
- Calculate compression ratio
- Handle different file types

Exercise 5: Create a Recommendation System
- Use collaborative filtering
- Implement user-based recommendations
- Handle sparse data
- Calculate similarity scores
""")

# =============================================================================
# 10. ALGORITHM COMPLEXITY
# =============================================================================

print("\n⏱️ ALGORITHM COMPLEXITY")
print("-" * 25)

print("""
Algorithm Complexity Analysis:

TIME COMPLEXITY:
- O(1): Constant time - Hash table lookup
- O(log n): Logarithmic time - Binary search
- O(n): Linear time - Linear search
- O(n log n): Linearithmic time - Merge sort
- O(n²): Quadratic time - Bubble sort
- O(2ⁿ): Exponential time - Fibonacci (naive)

SPACE COMPLEXITY:
- O(1): Constant space - In-place sorting
- O(n): Linear space - Array storage
- O(log n): Logarithmic space - Recursive calls

BIG O NOTATION:
- Describes worst-case performance
- Focuses on dominant terms
- Ignores constants and lower-order terms
- Helps choose appropriate algorithms
""")

# =============================================================================
# 11. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
Advanced data structures best practices:

1. Choose the right data structure
   ✅ Use deque for queue operations
   ✅ Use Counter for frequency counting
   ✅ Use defaultdict for missing keys

2. Understand algorithm complexity
   ✅ Choose O(n) over O(n²) when possible
   ✅ Consider space-time tradeoffs
   ✅ Profile your code for bottlenecks

3. Use built-in functions when possible
   ✅ sorted() instead of custom sort
   ✅ Counter instead of manual counting
   ✅ heapq for priority queues

4. Optimize for your use case
   ✅ Consider data size and access patterns
   ✅ Choose between time and space complexity
   ✅ Test with realistic data

5. Document your algorithms
   ✅ Explain the approach
   ✅ Include complexity analysis
   ✅ Provide usage examples

6. Handle edge cases
   ✅ Empty inputs
   ✅ Single elements
   ✅ Duplicate values
   ✅ Invalid inputs
""")

# =============================================================================
# 12. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ Python's collections module and its power
✅ Advanced sorting and searching algorithms
✅ Graph algorithms and traversal
✅ Dynamic programming techniques
✅ Real-world applications of algorithms
✅ Algorithm complexity analysis
✅ Best practices for efficient code

Next Steps:
- Day 11: Regular Expressions
- Day 12: Working with APIs
- Day 13: Web Scraping
- Day 14: Data Analysis with Pandas
""")

# =============================================================================
# 13. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 10 of your Python journey!

You now understand:
- Advanced data structures and their uses
- Efficient algorithms for common problems
- How to analyze algorithm complexity
- Real-world applications of algorithms
- Best practices for performance optimization

Advanced data structures and algorithms are essential for solving complex problems!
Practice with the exercises to master these powerful concepts.

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 10: Advanced Data Structures and Algorithms Tutorial")
    print("Run this file to see all examples in action!")
