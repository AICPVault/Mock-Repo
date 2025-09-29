"""
Day 20: NumPy Fundamentals for AI/ML
====================================

Today we'll learn about NumPy - the fundamental library for numerical computing
in Python. NumPy is essential for AI/ML, data science, and scientific computing.

Learning Objectives:
- Understand NumPy arrays and their advantages
- Master array creation and manipulation
- Learn broadcasting and vectorized operations
- Practice mathematical operations with arrays
- Explore NumPy for AI/ML applications
- Build efficient numerical computations

Let's master NumPy for AI/ML!
"""

print("🐍 Welcome to Day 20: NumPy Fundamentals for AI/ML!")
print("=" * 60)

import numpy as np
import matplotlib.pyplot as plt
import time
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# 1. WHAT IS NUMPY?
# =============================================================================

print("\n🔢 WHAT IS NUMPY?")
print("-" * 20)

"""
NumPy (Numerical Python) is:
- The fundamental package for scientific computing in Python
- Provides N-dimensional array objects
- Offers tools for integrating C/C++ and Fortran code
- Essential for AI/ML, data science, and scientific computing

Key Features:
- Fast array operations (vectorized)
- Broadcasting capabilities
- Linear algebra operations
- Random number generation
- Memory efficient
- Foundation for pandas, scikit-learn, TensorFlow, PyTorch

Why NumPy for AI/ML:
- Efficient numerical computations
- Vectorized operations (no loops needed)
- Memory efficient storage
- Optimized for mathematical operations
- Foundation for all ML libraries
"""

# =============================================================================
# 2. ARRAY CREATION AND BASICS
# =============================================================================

print("\n🏗️ ARRAY CREATION AND BASICS")
print("-" * 35)

def demonstrate_array_creation():
    """Demonstrate various ways to create NumPy arrays."""
    print("Array Creation Methods:")
    
    # 1. From Python lists
    print("\n1. From Python Lists:")
    python_list = [1, 2, 3, 4, 5]
    arr_from_list = np.array(python_list)
    print(f"Python list: {python_list}")
    print(f"NumPy array: {arr_from_list}")
    print(f"Array shape: {arr_from_list.shape}")
    print(f"Array dtype: {arr_from_list.dtype}")
    
    # 2. Multi-dimensional arrays
    print("\n2. Multi-dimensional Arrays:")
    matrix_2d = np.array([[1, 2, 3], [4, 5, 6]])
    matrix_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    
    print(f"2D array:\n{matrix_2d}")
    print(f"2D shape: {matrix_2d.shape}")
    print(f"3D array:\n{matrix_3d}")
    print(f"3D shape: {matrix_3d.shape}")
    
    # 3. Array creation functions
    print("\n3. Array Creation Functions:")
    
    # Zeros
    zeros_arr = np.zeros((3, 4))
    print(f"Zeros array:\n{zeros_arr}")
    
    # Ones
    ones_arr = np.ones((2, 3))
    print(f"Ones array:\n{ones_arr}")
    
    # Identity matrix
    identity = np.eye(3)
    print(f"Identity matrix:\n{identity}")
    
    # Full array
    full_arr = np.full((2, 3), 7)
    print(f"Full array (7s):\n{full_arr}")
    
    # 4. Range and sequences
    print("\n4. Range and Sequences:")
    
    # Arange
    range_arr = np.arange(0, 10, 2)
    print(f"Arange (0 to 10, step 2): {range_arr}")
    
    # Linspace
    linspace_arr = np.linspace(0, 1, 5)
    print(f"Linspace (0 to 1, 5 points): {linspace_arr}")
    
    # 5. Random arrays
    print("\n5. Random Arrays:")
    np.random.seed(42)  # For reproducible results
    
    random_arr = np.random.random((3, 3))
    print(f"Random array:\n{random_arr}")
    
    normal_arr = np.random.normal(0, 1, (3, 3))
    print(f"Normal distribution:\n{normal_arr}")
    
    return arr_from_list, matrix_2d, matrix_3d

arrays = demonstrate_array_creation()

# =============================================================================
# 3. ARRAY INDEXING AND SLICING
# =============================================================================

print("\n🎯 ARRAY INDEXING AND SLICING")
print("-" * 35)

def demonstrate_indexing():
    """Demonstrate array indexing and slicing."""
    print("Array Indexing and Slicing:")
    
    # Create sample array
    arr = np.arange(12).reshape(3, 4)
    print(f"Original array:\n{arr}")
    
    # 1. Basic indexing
    print("\n1. Basic Indexing:")
    print(f"Element at [1, 2]: {arr[1, 2]}")
    print(f"First row: {arr[0, :]}")
    print(f"Second column: {arr[:, 1]}")
    
    # 2. Slicing
    print("\n2. Slicing:")
    print(f"First two rows:\n{arr[:2, :]}")
    print(f"Last two columns:\n{arr[:, -2:]}")
    print(f"Middle section:\n{arr[1:3, 1:3]}")
    
    # 3. Boolean indexing
    print("\n3. Boolean Indexing:")
    mask = arr > 5
    print(f"Mask (values > 5):\n{mask}")
    print(f"Values > 5: {arr[mask]}")
    
    # 4. Fancy indexing
    print("\n4. Fancy Indexing:")
    indices = [0, 2]
    print(f"Rows at indices {indices}:\n{arr[indices, :]}")
    
    # 5. Modifying arrays
    print("\n5. Modifying Arrays:")
    arr_copy = arr.copy()
    arr_copy[0, 0] = 99
    print(f"Modified array:\n{arr_copy}")
    
    return arr

indexed_arr = demonstrate_indexing()

# =============================================================================
# 4. ARRAY OPERATIONS AND MATHEMATICS
# =============================================================================

print("\n🧮 ARRAY OPERATIONS AND MATHEMATICS")
print("-" * 40)

def demonstrate_operations():
    """Demonstrate array operations and mathematics."""
    print("Array Operations and Mathematics:")
    
    # Create sample arrays
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    
    # 1. Element-wise operations
    print("\n1. Element-wise Operations:")
    print(f"Addition: {arr1 + arr2}")
    print(f"Subtraction: {arr1 - arr2}")
    print(f"Multiplication: {arr1 * arr2}")
    print(f"Division: {arr1 / arr2}")
    print(f"Power: {arr1 ** 2}")
    
    # 2. Mathematical functions
    print("\n2. Mathematical Functions:")
    print(f"Square root: {np.sqrt(arr1)}")
    print(f"Exponential: {np.exp(arr1)}")
    print(f"Logarithm: {np.log(arr1)}")
    print(f"Sine: {np.sin(arr1)}")
    print(f"Cosine: {np.cos(arr1)}")
    
    # 3. Statistical operations
    print("\n3. Statistical Operations:")
    data = np.random.normal(0, 1, 100)
    print(f"Mean: {np.mean(data):.4f}")
    print(f"Standard deviation: {np.std(data):.4f}")
    print(f"Variance: {np.var(data):.4f}")
    print(f"Min: {np.min(data):.4f}")
    print(f"Max: {np.max(data):.4f}")
    print(f"Sum: {np.sum(data):.4f}")
    
    # 4. Matrix operations
    print("\n4. Matrix Operations:")
    print(f"Matrix 1:\n{matrix1}")
    print(f"Matrix 2:\n{matrix2}")
    print(f"Matrix multiplication:\n{np.dot(matrix1, matrix2)}")
    print(f"Element-wise multiplication:\n{matrix1 * matrix2}")
    print(f"Matrix transpose:\n{matrix1.T}")
    print(f"Matrix determinant: {np.linalg.det(matrix1):.4f}")
    
    # 5. Aggregation operations
    print("\n5. Aggregation Operations:")
    arr_2d = np.random.randint(0, 10, (3, 4))
    print(f"2D array:\n{arr_2d}")
    print(f"Sum along axis 0 (columns): {np.sum(arr_2d, axis=0)}")
    print(f"Sum along axis 1 (rows): {np.sum(arr_2d, axis=1)}")
    print(f"Mean along axis 0: {np.mean(arr_2d, axis=0)}")
    print(f"Max along axis 1: {np.max(arr_2d, axis=1)}")
    
    return arr1, arr2, matrix1, matrix2

operations_result = demonstrate_operations()

# =============================================================================
# 5. BROADCASTING
# =============================================================================

print("\n📡 BROADCASTING")
print("-" * 15)

def demonstrate_broadcasting():
    """Demonstrate NumPy broadcasting."""
    print("NumPy Broadcasting:")
    
    # 1. Basic broadcasting
    print("\n1. Basic Broadcasting:")
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    scalar = 10
    
    print(f"Array:\n{arr}")
    print(f"Scalar: {scalar}")
    print(f"Array + scalar:\n{arr + scalar}")
    print(f"Array * scalar:\n{arr * scalar}")
    
    # 2. Array broadcasting
    print("\n2. Array Broadcasting:")
    arr1 = np.array([[1, 2, 3]])
    arr2 = np.array([[1], [2], [3]])
    
    print(f"Array 1 (1x3):\n{arr1}")
    print(f"Array 2 (3x1):\n{arr2}")
    print(f"Broadcasted addition:\n{arr1 + arr2}")
    
    # 3. Broadcasting with different shapes
    print("\n3. Broadcasting with Different Shapes:")
    arr_3d = np.random.randint(0, 5, (2, 3, 4))
    arr_1d = np.array([1, 2, 3, 4])
    
    print(f"3D array shape: {arr_3d.shape}")
    print(f"1D array shape: {arr_1d.shape}")
    print(f"Broadcasted result shape: {(arr_3d + arr_1d).shape}")
    
    # 4. Broadcasting rules
    print("\n4. Broadcasting Rules:")
    print("Rule 1: Arrays with different dimensions are padded with 1s")
    print("Rule 2: Arrays with size 1 in any dimension can broadcast")
    print("Rule 3: Arrays are compatible if they match in all dimensions")
    
    # 5. Practical broadcasting example
    print("\n5. Practical Broadcasting Example:")
    # Normalize each row
    data = np.random.randn(5, 3)
    row_means = np.mean(data, axis=1, keepdims=True)
    row_stds = np.std(data, axis=1, keepdims=True)
    normalized = (data - row_means) / row_stds
    
    print(f"Original data:\n{data}")
    print(f"Row means:\n{row_means}")
    print(f"Row stds:\n{row_stds}")
    print(f"Normalized data:\n{normalized}")
    
    return arr, arr1, arr2

broadcasting_result = demonstrate_broadcasting()

# =============================================================================
# 6. VECTORIZED OPERATIONS
# =============================================================================

print("\n⚡ VECTORIZED OPERATIONS")
print("-" * 30)

def demonstrate_vectorization():
    """Demonstrate vectorized operations vs loops."""
    print("Vectorized Operations vs Loops:")
    
    # Create large arrays
    size = 1000000
    arr1 = np.random.randn(size)
    arr2 = np.random.randn(size)
    
    # 1. Vectorized operations (NumPy)
    print("\n1. Vectorized Operations (NumPy):")
    start_time = time.time()
    result_vectorized = arr1 + arr2
    numpy_time = time.time() - start_time
    print(f"NumPy addition time: {numpy_time:.6f} seconds")
    
    # 2. Loop-based operations (Python)
    print("\n2. Loop-based Operations (Python):")
    start_time = time.time()
    result_loop = []
    for i in range(size):
        result_loop.append(arr1[i] + arr2[i])
    loop_time = time.time() - start_time
    print(f"Python loop time: {loop_time:.6f} seconds")
    
    # 3. Performance comparison
    print(f"\n3. Performance Comparison:")
    print(f"NumPy is {loop_time/numpy_time:.1f}x faster than Python loops!")
    
    # 4. Memory efficiency
    print("\n4. Memory Efficiency:")
    print(f"NumPy array memory usage: {arr1.nbytes / 1024 / 1024:.2f} MB")
    print(f"Python list memory usage: {sys.getsizeof(result_loop) / 1024 / 1024:.2f} MB")
    
    # 5. Vectorized mathematical operations
    print("\n5. Vectorized Mathematical Operations:")
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x) * np.cos(x) + np.exp(-x/10)
    
    print(f"Vectorized computation of sin(x)*cos(x) + exp(-x/10)")
    print(f"Result shape: {y.shape}")
    print(f"First 5 values: {y[:5]}")
    
    return result_vectorized, result_loop

vectorization_result = demonstrate_vectorization()

# =============================================================================
# 7. NUMPY FOR AI/ML APPLICATIONS
# =============================================================================

print("\n🤖 NUMPY FOR AI/ML APPLICATIONS")
print("-" * 35)

def demonstrate_ai_ml_applications():
    """Demonstrate NumPy applications in AI/ML."""
    print("NumPy for AI/ML Applications:")
    
    # 1. Data preprocessing
    print("\n1. Data Preprocessing:")
    
    # Generate sample dataset
    np.random.seed(42)
    features = np.random.randn(1000, 5)  # 1000 samples, 5 features
    labels = np.random.randint(0, 2, 1000)  # Binary classification
    
    print(f"Features shape: {features.shape}")
    print(f"Labels shape: {labels.shape}")
    
    # Normalize features
    features_normalized = (features - np.mean(features, axis=0)) / np.std(features, axis=0)
    print(f"Normalized features mean: {np.mean(features_normalized, axis=0)}")
    print(f"Normalized features std: {np.std(features_normalized, axis=0)}")
    
    # 2. Train-test split
    print("\n2. Train-Test Split:")
    n_samples = len(features)
    train_size = int(0.8 * n_samples)
    
    # Shuffle indices
    indices = np.random.permutation(n_samples)
    train_indices = indices[:train_size]
    test_indices = indices[train_size:]
    
    X_train, X_test = features_normalized[train_indices], features_normalized[test_indices]
    y_train, y_test = labels[train_indices], labels[test_indices]
    
    print(f"Training set: {X_train.shape}, {y_train.shape}")
    print(f"Test set: {X_test.shape}, {y_test.shape}")
    
    # 3. Simple linear regression
    print("\n3. Simple Linear Regression:")
    
    # Generate linear data
    X_linear = np.random.randn(100, 1)
    y_linear = 2 * X_linear.flatten() + 1 + 0.1 * np.random.randn(100)
    
    # Add bias term
    X_with_bias = np.column_stack([np.ones(X_linear.shape[0]), X_linear])
    
    # Normal equation: theta = (X^T X)^(-1) X^T y
    theta = np.linalg.inv(X_with_bias.T @ X_with_bias) @ X_with_bias.T @ y_linear
    
    print(f"Linear regression coefficients: {theta}")
    
    # 4. Distance calculations
    print("\n4. Distance Calculations (for KNN):")
    
    # Calculate Euclidean distances
    def euclidean_distance(x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))
    
    # Example: distance between first two samples
    dist = euclidean_distance(X_train[0], X_train[1])
    print(f"Distance between first two samples: {dist:.4f}")
    
    # Vectorized distance calculation
    def pairwise_distances(X):
        return np.sqrt(np.sum((X[:, np.newaxis] - X[np.newaxis, :]) ** 2, axis=2))
    
    # Calculate distances for first 5 samples
    distances = pairwise_distances(X_train[:5])
    print(f"Pairwise distances (first 5 samples):\n{distances}")
    
    # 5. Activation functions
    print("\n5. Activation Functions:")
    
    def sigmoid(x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))  # Clip to prevent overflow
    
    def relu(x):
        return np.maximum(0, x)
    
    def tanh(x):
        return np.tanh(x)
    
    x = np.linspace(-5, 5, 100)
    sigmoid_vals = sigmoid(x)
    relu_vals = relu(x)
    tanh_vals = tanh(x)
    
    print(f"Sigmoid range: [{np.min(sigmoid_vals):.4f}, {np.max(sigmoid_vals):.4f}]")
    print(f"ReLU range: [{np.min(relu_vals):.4f}, {np.max(relu_vals):.4f}]")
    print(f"Tanh range: [{np.min(tanh_vals):.4f}, {np.max(tanh_vals):.4f}]")
    
    # 6. Gradient descent
    print("\n6. Gradient Descent:")
    
    def gradient_descent(X, y, learning_rate=0.01, epochs=100):
        m = len(y)
        theta = np.zeros(X.shape[1])
        
        for epoch in range(epochs):
            predictions = X @ theta
            errors = predictions - y
            gradient = (1/m) * X.T @ errors
            theta -= learning_rate * gradient
            
            if epoch % 20 == 0:
                cost = np.mean(errors ** 2)
                print(f"Epoch {epoch}: Cost = {cost:.4f}")
        
        return theta
    
    # Run gradient descent
    theta_gd = gradient_descent(X_with_bias, y_linear, learning_rate=0.1, epochs=100)
    print(f"Gradient descent coefficients: {theta_gd}")
    
    return features, labels, X_train, X_test, y_train, y_test

ai_ml_result = demonstrate_ai_ml_applications()

# =============================================================================
# 8. ADVANCED NUMPY OPERATIONS
# =============================================================================

print("\n🚀 ADVANCED NUMPY OPERATIONS")
print("-" * 35)

def demonstrate_advanced_operations():
    """Demonstrate advanced NumPy operations."""
    print("Advanced NumPy Operations:")
    
    # 1. Array reshaping and manipulation
    print("\n1. Array Reshaping and Manipulation:")
    
    arr = np.arange(24)
    print(f"Original array: {arr}")
    
    # Reshape
    reshaped = arr.reshape(4, 6)
    print(f"Reshaped (4x6):\n{reshaped}")
    
    # Transpose
    transposed = reshaped.T
    print(f"Transposed (6x4):\n{transposed}")
    
    # Flatten
    flattened = reshaped.flatten()
    print(f"Flattened: {flattened}")
    
    # 2. Array concatenation and splitting
    print("\n2. Array Concatenation and Splitting:")
    
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    
    # Concatenate along axis 0
    concat_axis0 = np.concatenate([arr1, arr2], axis=0)
    print(f"Concatenate axis 0:\n{concat_axis0}")
    
    # Concatenate along axis 1
    concat_axis1 = np.concatenate([arr1, arr2], axis=1)
    print(f"Concatenate axis 1:\n{concat_axis1}")
    
    # Split array
    split_arrays = np.split(concat_axis0, 2, axis=0)
    print(f"Split arrays: {[arr.tolist() for arr in split_arrays]}")
    
    # 3. Advanced indexing
    print("\n3. Advanced Indexing:")
    
    arr = np.random.randint(0, 10, (5, 5))
    print(f"Random array:\n{arr}")
    
    # Find indices where condition is true
    indices = np.where(arr > 5)
    print(f"Indices where arr > 5: {list(zip(indices[0], indices[1]))}")
    
    # Get values at specific indices
    values = arr[indices]
    print(f"Values > 5: {values}")
    
    # 4. Sorting and searching
    print("\n4. Sorting and Searching:")
    
    data = np.random.randint(0, 100, 10)
    print(f"Original data: {data}")
    
    # Sort
    sorted_data = np.sort(data)
    print(f"Sorted data: {sorted_data}")
    
    # Argsort (indices that would sort the array)
    sort_indices = np.argsort(data)
    print(f"Sort indices: {sort_indices}")
    
    # Search
    search_val = 50
    closest_idx = np.argmin(np.abs(data - search_val))
    print(f"Closest to {search_val}: {data[closest_idx]} at index {closest_idx}")
    
    # 5. Set operations
    print("\n5. Set Operations:")
    
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([3, 4, 5, 6, 7])
    
    # Intersection
    intersection = np.intersect1d(arr1, arr2)
    print(f"Intersection: {intersection}")
    
    # Union
    union = np.union1d(arr1, arr2)
    print(f"Union: {union}")
    
    # Set difference
    diff = np.setdiff1d(arr1, arr2)
    print(f"Set difference (arr1 - arr2): {diff}")
    
    # 6. Linear algebra operations
    print("\n6. Linear Algebra Operations:")
    
    # Create matrices
    A = np.random.randn(3, 3)
    b = np.random.randn(3)
    
    print(f"Matrix A:\n{A}")
    print(f"Vector b: {b}")
    
    # Solve linear system Ax = b
    x = np.linalg.solve(A, b)
    print(f"Solution x: {x}")
    
    # Verify solution
    verification = A @ x
    print(f"Verification (A @ x): {verification}")
    print(f"Error: {np.linalg.norm(verification - b):.10f}")
    
    # Eigenvalues and eigenvectors
    eigenvals, eigenvecs = np.linalg.eig(A)
    print(f"Eigenvalues: {eigenvals}")
    print(f"Eigenvectors:\n{eigenvecs}")
    
    return arr, reshaped, transposed

advanced_result = demonstrate_advanced_operations()

# =============================================================================
# 9. PERFORMANCE OPTIMIZATION
# =============================================================================

print("\n⚡ PERFORMANCE OPTIMIZATION")
print("-" * 30)

def demonstrate_performance():
    """Demonstrate NumPy performance optimization techniques."""
    print("NumPy Performance Optimization:")
    
    # 1. Memory layout optimization
    print("\n1. Memory Layout Optimization:")
    
    # C-contiguous vs F-contiguous
    arr_c = np.array([[1, 2, 3], [4, 5, 6]], order='C')
    arr_f = np.array([[1, 2, 3], [4, 5, 6]], order='F')
    
    print(f"C-contiguous: {arr_c.flags.c_contiguous}")
    print(f"F-contiguous: {arr_f.flags.f_contiguous}")
    
    # 2. In-place operations
    print("\n2. In-place Operations:")
    
    arr = np.random.randn(1000, 1000)
    
    # Regular operation (creates new array)
    start_time = time.time()
    result1 = arr + 1
    time1 = time.time() - start_time
    
    # In-place operation (modifies existing array)
    start_time = time.time()
    arr += 1
    time2 = time.time() - start_time
    
    print(f"Regular operation time: {time1:.6f} seconds")
    print(f"In-place operation time: {time2:.6f} seconds")
    print(f"In-place is {time1/time2:.1f}x faster!")
    
    # 3. Vectorized operations vs loops
    print("\n3. Vectorized Operations vs Loops:")
    
    def loop_sum(arr):
        total = 0
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                total += arr[i, j]
        return total
    
    def vectorized_sum(arr):
        return np.sum(arr)
    
    # Test with large array
    large_arr = np.random.randn(1000, 1000)
    
    # Loop version
    start_time = time.time()
    loop_result = loop_sum(large_arr)
    loop_time = time.time() - start_time
    
    # Vectorized version
    start_time = time.time()
    vectorized_result = vectorized_sum(large_arr)
    vectorized_time = time.time() - start_time
    
    print(f"Loop sum time: {loop_time:.6f} seconds")
    print(f"Vectorized sum time: {vectorized_time:.6f} seconds")
    print(f"Vectorized is {loop_time/vectorized_time:.1f}x faster!")
    print(f"Results match: {np.isclose(loop_result, vectorized_result)}")
    
    # 4. Memory usage optimization
    print("\n4. Memory Usage Optimization:")
    
    # Different data types
    arr_int8 = np.array([1, 2, 3, 4], dtype=np.int8)
    arr_int64 = np.array([1, 2, 3, 4], dtype=np.int64)
    arr_float32 = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32)
    arr_float64 = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float64)
    
    print(f"int8 memory: {arr_int8.nbytes} bytes")
    print(f"int64 memory: {arr_int64.nbytes} bytes")
    print(f"float32 memory: {arr_float32.nbytes} bytes")
    print(f"float64 memory: {arr_float64.nbytes} bytes")
    
    return arr_c, arr_f, large_arr

performance_result = demonstrate_performance()

# =============================================================================
# 10. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice NumPy fundamentals:

Exercise 1: Image Processing with NumPy
- Load an image as a NumPy array
- Apply filters (blur, edge detection)
- Resize and crop images
- Convert between color spaces

Exercise 2: Financial Data Analysis
- Calculate moving averages
- Compute technical indicators
- Analyze price trends
- Build trading signals

Exercise 3: Scientific Computing
- Solve differential equations
- Perform Fourier transforms
- Analyze signal processing
- Implement numerical methods

Exercise 4: Machine Learning from Scratch
- Implement linear regression
- Build a neural network
- Create clustering algorithms
- Develop classification models

Exercise 5: Data Visualization
- Create heatmaps and contour plots
- Generate 3D visualizations
- Build interactive plots
- Analyze statistical distributions
""")

# =============================================================================
# 11. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
NumPy best practices:

1. Use vectorized operations
   ✅ np.sum(arr) instead of sum(arr)
   ❌ for loops for mathematical operations

2. Choose appropriate data types
   ✅ np.float32 for memory efficiency
   ❌ np.float64 when float32 is sufficient

3. Use broadcasting effectively
   ✅ arr + scalar
   ❌ arr + np.full_like(arr, scalar)

4. Avoid unnecessary copies
   ✅ arr += 1 (in-place)
   ❌ arr = arr + 1 (creates copy)

5. Use memory-efficient operations
   ✅ np.zeros_like(arr)
   ❌ np.zeros(arr.shape)

6. Leverage NumPy's optimized functions
   ✅ np.dot() for matrix multiplication
   ❌ Manual loops for matrix operations

7. Handle edge cases
   ✅ np.clip() to prevent overflow
   ❌ Ignoring numerical stability

8. Profile your code
   ✅ Use time.time() to measure performance
   ❌ Assume operations are efficient
""")

# =============================================================================
# 12. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common NumPy mistakes:

1. Using Python lists instead of arrays
   ❌ [1, 2, 3] + [4, 5, 6]
   ✅ np.array([1, 2, 3]) + np.array([4, 5, 6])

2. Not understanding broadcasting
   ❌ arr + np.array([1, 2, 3])  # Shape mismatch
   ✅ arr + np.array([1, 2, 3]).reshape(-1, 1)

3. Modifying arrays unintentionally
   ❌ arr2 = arr1; arr2[0] = 999  # Modifies arr1
   ✅ arr2 = arr1.copy(); arr2[0] = 999

4. Using loops instead of vectorization
   ❌ for i in range(len(arr)): arr[i] += 1
   ✅ arr += 1

5. Ignoring data types
   ❌ arr = np.array([1, 2, 3], dtype=object)
   ✅ arr = np.array([1, 2, 3], dtype=np.int32)

6. Not handling NaN values
   ❌ np.sum(arr_with_nan)
   ✅ np.nansum(arr_with_nan)

7. Memory inefficient operations
   ❌ arr = arr + 1; arr = arr * 2
   ✅ arr += 1; arr *= 2
""")

# =============================================================================
# 13. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ NumPy array creation and manipulation
✅ Array indexing and slicing techniques
✅ Mathematical operations and functions
✅ Broadcasting and vectorized operations
✅ AI/ML applications with NumPy
✅ Advanced NumPy operations
✅ Performance optimization techniques
✅ Best practices and common mistakes

Next Steps:
- Practice with real-world datasets
- Explore NumPy with other libraries
- Learn advanced numerical computing
- Build AI/ML applications
""")

# =============================================================================
# 14. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 20 of your Python journey!

You now understand:
- NumPy fundamentals and array operations
- Broadcasting and vectorized operations
- AI/ML applications with NumPy
- Performance optimization techniques
- Best practices for numerical computing

NumPy is the foundation for all AI/ML libraries!
Practice with the exercises to master this essential library.

Happy coding! 🐍✨
""")

# =============================================================================
# 15. COMPLETE LEARNING JOURNEY SUMMARY
# =============================================================================

print("\n🎓 COMPLETE LEARNING JOURNEY SUMMARY")
print("-" * 40)

print("""
Congratulations! You've completed a comprehensive 20-day Python learning journey:

Days 1-5: Foundation
- Day 1: Python Basics
- Day 2: Operators & Conditionals
- Day 3: Loops & Iteration
- Day 4: Functions & Scope
- Day 5: Data Structures

Days 6-10: Intermediate
- Day 6: File Handling
- Day 7: Exception Handling
- Day 8: Object-Oriented Programming
- Day 9: Modules & Packages
- Day 10: Advanced Data Structures

Days 11-16: Advanced
- Day 11: Regular Expressions
- Day 12: Web Scraping & APIs
- Day 13: Data Analysis with Pandas
- Day 14: Web Development with Flask
- Day 15: Testing & Debugging
- Day 16: Deployment & Production

Days 17-20: AI/ML & Scientific Computing
- Day 17: AI and Machine Learning
- Day 18: AI Integration with Python
- Day 19: SQL Database Operations
- Day 20: NumPy Fundamentals

You now have a complete foundation in Python programming, AI/ML, and scientific computing!
Continue practicing and building projects to master these skills.

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 20: NumPy Fundamentals for AI/ML Tutorial")
    print("Run this file to see all examples in action!")
