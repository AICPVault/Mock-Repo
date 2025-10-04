"""
Day 13: Data Analysis with Pandas
=================================

Today we'll learn about data analysis using Pandas - one of the most powerful
libraries for data manipulation and analysis in Python. We'll explore data
structures, operations, and real-world data analysis techniques.

Learning Objectives:
- Understand Pandas DataFrames and Series
- Learn data loading and saving techniques
- Master data cleaning and preprocessing
- Explore data analysis and visualization
- Practice real-world data analysis scenarios
- Build comprehensive data analysis workflows

Let's dive into data analysis with Pandas!
"""

print("🐍 Welcome to Day 13: Data Analysis with Pandas!")
print("=" * 55)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# 1. WHAT IS PANDAS?
# =============================================================================

print("\n📊 WHAT IS PANDAS?")
print("-" * 20)

"""
Pandas is:
- A powerful data manipulation and analysis library
- Built on top of NumPy for numerical computing
- Provides data structures for efficient data analysis
- Essential for data science and machine learning
- Supports various data formats (CSV, Excel, JSON, SQL)

Key features:
- DataFrame: 2D labeled data structure
- Series: 1D labeled array
- Data cleaning and preprocessing
- Data aggregation and grouping
- Time series analysis
- Data visualization integration
"""

# =============================================================================
# 2. PANDAS DATA STRUCTURES
# =============================================================================

print("\n🏗️ PANDAS DATA STRUCTURES")
print("-" * 30)

# Creating Series
print("Creating Series:")
series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(f"Series:\n{series}")
print(f"Series type: {type(series)}")

# Creating DataFrame
print("\nCreating DataFrame:")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [50000, 60000, 70000, 55000, 65000]
}
df = pd.DataFrame(data)
print(f"DataFrame:\n{df}")
print(f"DataFrame shape: {df.shape}")
print(f"DataFrame columns: {df.columns.tolist()}")

# =============================================================================
# 3. DATA LOADING AND SAVING
# =============================================================================

print("\n📁 DATA LOADING AND SAVING")
print("-" * 30)

# Create sample data for demonstration
sample_data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Price': [999.99, 29.99, 79.99, 299.99, 149.99],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories'],
    'Stock': [10, 50, 25, 15, 30],
    'Date': pd.date_range('2024-01-01', periods=5, freq='D')
}

df_demo = pd.DataFrame(sample_data)
print("Sample DataFrame:")
print(df_demo)

# Save to different formats
print("\nSaving data to different formats:")
df_demo.to_csv('sample_data.csv', index=False)
df_demo.to_excel('sample_data.xlsx', index=False)
df_demo.to_json('sample_data.json', orient='records')

print("✅ Data saved to CSV, Excel, and JSON formats")

# Load data from different formats
print("\nLoading data from different formats:")
df_csv = pd.read_csv('sample_data.csv')
df_excel = pd.read_excel('sample_data.xlsx')
df_json = pd.read_json('sample_data.json')

print(f"CSV shape: {df_csv.shape}")
print(f"Excel shape: {df_excel.shape}")
print(f"JSON shape: {df_json.shape}")

# =============================================================================
# 4. DATA EXPLORATION
# =============================================================================

print("\n🔍 DATA EXPLORATION")
print("-" * 20)

# Basic information about the dataset
print("Dataset Information:")
print(f"Shape: {df_demo.shape}")
print(f"Columns: {df_demo.columns.tolist()}")
print(f"Data types:\n{df_demo.dtypes}")

# Statistical summary
print("\nStatistical Summary:")
print(df_demo.describe())

# Data info
print("\nData Info:")
print(df_demo.info())

# First and last rows
print("\nFirst 3 rows:")
print(df_demo.head(3))
print("\nLast 3 rows:")
print(df_demo.tail(3))

# =============================================================================
# 5. DATA CLEANING AND PREPROCESSING
# =============================================================================

print("\n🧹 DATA CLEANING AND PREPROCESSING")
print("-" * 40)

# Create sample data with missing values and inconsistencies
dirty_data = {
    'Name': ['Alice', 'Bob', None, 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'Email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'diana@email.com', 'eve@email.com'],
    'Salary': [50000, 60000, 70000, 55000, 65000],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT'],
    'Join_Date': ['2020-01-15', '2019-03-20', '2021-06-10', '2020-09-05', '2021-12-01']
}

df_dirty = pd.DataFrame(dirty_data)
print("Original dirty data:")
print(df_dirty)

# Handle missing values
print("\nHandling missing values:")
print(f"Missing values:\n{df_dirty.isnull().sum()}")

# Fill missing values
df_cleaned = df_dirty.copy()
df_cleaned['Name'] = df_cleaned['Name'].fillna('Unknown')
print(f"After filling missing names:\n{df_cleaned}")

# Remove duplicates
print(f"\nDuplicate rows: {df_cleaned.duplicated().sum()}")

# Data type conversion
df_cleaned['Join_Date'] = pd.to_datetime(df_cleaned['Join_Date'])
print(f"\nAfter date conversion:\n{df_cleaned.dtypes}")

# =============================================================================
# 6. DATA SELECTION AND FILTERING
# =============================================================================

print("\n🎯 DATA SELECTION AND FILTERING")
print("-" * 35)

# Select specific columns
print("Selecting specific columns:")
selected_cols = df_cleaned[['Name', 'Age', 'Salary']]
print(selected_cols)

# Filter data
print("\nFiltering data:")
# Filter by age
young_employees = df_cleaned[df_cleaned['Age'] < 30]
print(f"Young employees (< 30):\n{young_employees}")

# Filter by department
it_employees = df_cleaned[df_cleaned['Department'] == 'IT']
print(f"IT employees:\n{it_employees}")

# Multiple conditions
high_salary_young = df_cleaned[(df_cleaned['Salary'] > 60000) & (df_cleaned['Age'] < 35)]
print(f"High salary young employees:\n{high_salary_young}")

# =============================================================================
# 7. DATA AGGREGATION AND GROUPING
# =============================================================================

print("\n📈 DATA AGGREGATION AND GROUPING")
print("-" * 35)

# Group by department
print("Grouping by department:")
dept_stats = df_cleaned.groupby('Department').agg({
    'Salary': ['mean', 'sum', 'count'],
    'Age': ['mean', 'min', 'max']
})
print(dept_stats)

# Simple groupby operations
print("\nDepartment statistics:")
dept_summary = df_cleaned.groupby('Department')['Salary'].agg(['mean', 'sum', 'count'])
print(dept_summary)

# Pivot table
print("\nPivot table:")
pivot_table = df_cleaned.pivot_table(
    values='Salary',
    index='Department',
    columns='Age',
    aggfunc='mean',
    fill_value=0
)
print(pivot_table)

# =============================================================================
# 8. DATA VISUALIZATION
# =============================================================================

print("\n📊 DATA VISUALIZATION")
print("-" * 25)

# Create sample data for visualization
np.random.seed(42)
viz_data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'] * 20,
    'Value': np.random.normal(100, 15, 100),
    'Score': np.random.uniform(0, 100, 100),
    'Date': pd.date_range('2024-01-01', periods=100, freq='D')
})

print("Sample data for visualization:")
print(viz_data.head())

# Basic plots
print("\nCreating visualizations:")
try:
    # Set up the plotting style
    plt.style.use('default')
    
    # Create subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Histogram
    axes[0, 0].hist(viz_data['Value'], bins=20, alpha=0.7, color='skyblue')
    axes[0, 0].set_title('Value Distribution')
    axes[0, 0].set_xlabel('Value')
    axes[0, 0].set_ylabel('Frequency')
    
    # Box plot
    viz_data.boxplot(column='Value', by='Category', ax=axes[0, 1])
    axes[0, 1].set_title('Value by Category')
    axes[0, 1].set_xlabel('Category')
    axes[0, 1].set_ylabel('Value')
    
    # Scatter plot
    axes[1, 0].scatter(viz_data['Value'], viz_data['Score'], alpha=0.6, color='green')
    axes[1, 0].set_title('Value vs Score')
    axes[1, 0].set_xlabel('Value')
    axes[1, 0].set_ylabel('Score')
    
    # Line plot
    daily_avg = viz_data.groupby('Date')['Value'].mean()
    axes[1, 1].plot(daily_avg.index, daily_avg.values, color='red', linewidth=2)
    axes[1, 1].set_title('Daily Average Value')
    axes[1, 1].set_xlabel('Date')
    axes[1, 1].set_ylabel('Average Value')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('pandas_visualization.png', dpi=150, bbox_inches='tight')
    print("✅ Visualization saved as 'pandas_visualization.png'")
    plt.close()
    
except Exception as e:
    print(f"Visualization error: {e}")

# =============================================================================
# 9. TIME SERIES ANALYSIS
# =============================================================================

print("\n⏰ TIME SERIES ANALYSIS")
print("-" * 25)

# Create time series data
dates = pd.date_range('2024-01-01', periods=365, freq='D')
ts_data = pd.DataFrame({
    'Date': dates,
    'Sales': np.random.normal(1000, 200, 365) + np.sin(np.arange(365) * 2 * np.pi / 365) * 100,
    'Temperature': 20 + 10 * np.sin(np.arange(365) * 2 * np.pi / 365) + np.random.normal(0, 2, 365)
})

print("Time series data:")
print(ts_data.head())

# Set date as index
ts_data.set_index('Date', inplace=True)

# Time series operations
print("\nTime series operations:")
print(f"Data shape: {ts_data.shape}")
print(f"Date range: {ts_data.index.min()} to {ts_data.index.max()}")

# Resampling
monthly_sales = ts_data['Sales'].resample('M').mean()
print(f"\nMonthly average sales:\n{monthly_sales.head()}")

# Rolling window
rolling_avg = ts_data['Sales'].rolling(window=7).mean()
print(f"\n7-day rolling average (first 10 days):\n{rolling_avg.head(10)}")

# =============================================================================
# 10. PRACTICAL DATA ANALYSIS EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL DATA ANALYSIS EXAMPLES")
print("-" * 40)

# Example 1: Sales Analysis
def sales_analysis():
    """Demonstrate sales data analysis."""
    # Create sample sales data
    np.random.seed(42)
    sales_data = pd.DataFrame({
        'Date': pd.date_range('2024-01-01', periods=100, freq='D'),
        'Product': np.random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor'], 100),
        'Sales': np.random.normal(1000, 300, 100),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
        'Salesperson': np.random.choice(['Alice', 'Bob', 'Charlie', 'Diana'], 100)
    })
    
    print("Sales Analysis:")
    print(f"Total sales: ${sales_data['Sales'].sum():,.2f}")
    print(f"Average daily sales: ${sales_data['Sales'].mean():,.2f}")
    
    # Product performance
    product_performance = sales_data.groupby('Product')['Sales'].agg(['sum', 'mean', 'count'])
    print(f"\nProduct Performance:\n{product_performance}")
    
    # Regional analysis
    regional_sales = sales_data.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    print(f"\nRegional Sales:\n{regional_sales}")
    
    # Top salesperson
    top_salesperson = sales_data.groupby('Salesperson')['Sales'].sum().idxmax()
    print(f"\nTop salesperson: {top_salesperson}")

sales_analysis()

# Example 2: Customer Analysis
def customer_analysis():
    """Demonstrate customer data analysis."""
    # Create sample customer data
    np.random.seed(42)
    customer_data = pd.DataFrame({
        'Customer_ID': range(1, 101),
        'Age': np.random.normal(35, 10, 100).astype(int),
        'Income': np.random.normal(50000, 15000, 100),
        'Spending': np.random.normal(2000, 500, 100),
        'Region': np.random.choice(['Urban', 'Suburban', 'Rural'], 100),
        'Segment': np.random.choice(['Premium', 'Standard', 'Basic'], 100)
    })
    
    print("\nCustomer Analysis:")
    print(f"Total customers: {len(customer_data)}")
    print(f"Average age: {customer_data['Age'].mean():.1f}")
    print(f"Average income: ${customer_data['Income'].mean():,.2f}")
    print(f"Average spending: ${customer_data['Spending'].mean():,.2f}")
    
    # Customer segmentation
    segment_analysis = customer_data.groupby('Segment').agg({
        'Age': 'mean',
        'Income': 'mean',
        'Spending': 'mean'
    })
    print(f"\nSegment Analysis:\n{segment_analysis}")
    
    # High-value customers
    high_value = customer_data[customer_data['Spending'] > customer_data['Spending'].quantile(0.8)]
    print(f"\nHigh-value customers: {len(high_value)} ({len(high_value)/len(customer_data)*100:.1f}%)")

customer_analysis()

# =============================================================================
# 11. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice data analysis with Pandas:

Exercise 1: Stock Market Analysis
- Load stock price data
- Calculate daily returns
- Identify trends and patterns
- Create moving averages
- Analyze volatility

Exercise 2: E-commerce Data Analysis
- Analyze sales trends
- Identify top-selling products
- Customer segmentation
- Seasonal analysis
- Revenue forecasting

Exercise 3: Social Media Analytics
- Analyze engagement metrics
- Identify viral content
- User behavior analysis
- Content performance tracking
- Sentiment analysis

Exercise 4: Healthcare Data Analysis
- Patient demographics
- Treatment outcomes
- Cost analysis
- Risk factor identification
- Predictive modeling

Exercise 5: Financial Data Analysis
- Transaction analysis
- Fraud detection
- Risk assessment
- Portfolio optimization
- Performance metrics
""")

# =============================================================================
# 12. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
Pandas best practices:

1. Use appropriate data types
   ✅ df['column'] = df['column'].astype('category')
   ❌ Keep all columns as object type

2. Handle missing data properly
   ✅ df.dropna() or df.fillna()
   ❌ Ignore missing values

3. Use vectorized operations
   ✅ df['new_col'] = df['col1'] + df['col2']
   ❌ Use loops for calculations

4. Optimize memory usage
   ✅ Use categorical data types
   ❌ Keep unnecessary precision

5. Use method chaining
   ✅ df.groupby().agg().reset_index()
   ❌ Multiple separate operations

6. Document your analysis
   ✅ Add comments and markdown
   ❌ Write code without explanation

7. Test your data transformations
   ✅ Verify results after operations
   ❌ Assume transformations are correct

8. Use appropriate indexing
   ✅ Set meaningful indexes
   ❌ Use default integer indexes
""")

# =============================================================================
# 13. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common Pandas mistakes:

1. Using loops instead of vectorized operations
   ❌ for i in range(len(df)): df.iloc[i] = ...
   ✅ df['new_col'] = df['col1'] + df['col2']

2. Not handling missing data
   ❌ Ignoring NaN values
   ✅ df.dropna() or df.fillna()

3. Using inplace operations unnecessarily
   ❌ df.dropna(inplace=True) always
   ✅ df = df.dropna() when appropriate

4. Not setting proper indexes
   ❌ Using default integer index
   ✅ df.set_index('date') for time series

5. Not using appropriate data types
   ❌ Keeping everything as object
   ✅ df['category'] = df['category'].astype('category')

6. Not handling duplicates
   ❌ Ignoring duplicate rows
   ✅ df.drop_duplicates()

7. Not validating data
   ❌ Assuming data is clean
   ✅ df.info(), df.describe(), df.isnull().sum()
""")

# =============================================================================
# 14. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ Pandas DataFrames and Series
✅ Data loading and saving
✅ Data cleaning and preprocessing
✅ Data selection and filtering
✅ Data aggregation and grouping
✅ Data visualization with Pandas
✅ Time series analysis
✅ Real-world data analysis examples

Next Steps:
- Day 14: Web Development with Flask
- Day 15: Testing and Debugging
- Day 16: Deployment and Production
""")

# =============================================================================
# 15. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 13 of your Python journey!

You now understand:
- How to work with Pandas for data analysis
- Data cleaning and preprocessing techniques
- Data visualization and exploration
- Time series analysis
- Real-world data analysis workflows

Pandas is essential for data science and analysis!
Practice with the exercises to master this powerful library.

Happy coding! 🐍✨
""")

# Clean up created files
import os
files_to_clean = ['sample_data.csv', 'sample_data.xlsx', 'sample_data.json', 'pandas_visualization.png']
for file in files_to_clean:
    if os.path.exists(file):
        os.remove(file)
        print(f"🧹 Cleaned up {file}")

# Run the tutorial
if __name__ == "__main__":
    print("Day 13: Data Analysis with Pandas Tutorial")
    print("Run this file to see all examples in action!")
