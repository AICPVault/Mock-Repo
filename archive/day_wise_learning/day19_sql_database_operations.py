"""
Day 19: SQL Database Operations with Python
===========================================

Today we'll learn about working with SQL databases using Python. We'll explore
different database libraries, execute SQL queries, and build database-driven
applications.

Learning Objectives:
- Understand database concepts and SQL
- Learn to connect to different databases with Python
- Master SQL query execution and data manipulation
- Practice database design and relationships
- Build database-driven applications
- Handle database errors and transactions

Let's master SQL database operations with Python!
"""

print("🐍 Welcome to Day 19: SQL Database Operations with Python!")
print("=" * 60)

import sqlite3
import pandas as pd
import psycopg2
import mysql.connector
from sqlalchemy import create_engine, text
import json
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# 1. WHAT IS SQL AND DATABASES?
# =============================================================================

print("\n🗄️ WHAT IS SQL AND DATABASES?")
print("-" * 35)

"""
SQL (Structured Query Language) is:
- A standard language for managing relational databases
- Used to create, read, update, and delete data
- Essential for data storage and retrieval
- Foundation for most applications

Database Types:
- SQLite: File-based, lightweight, embedded
- PostgreSQL: Advanced, open-source, enterprise-grade
- MySQL: Popular, web applications, open-source
- SQL Server: Microsoft, enterprise, Windows
- Oracle: Enterprise, high-performance, commercial

Python Database Libraries:
- sqlite3: Built-in SQLite support
- psycopg2: PostgreSQL adapter
- mysql-connector: MySQL adapter
- sqlalchemy: ORM and database toolkit
- pandas: Data analysis with database integration
"""

# =============================================================================
# 2. SQLITE DATABASE OPERATIONS
# =============================================================================

print("\n💾 SQLITE DATABASE OPERATIONS")
print("-" * 35)

def demonstrate_sqlite_operations():
    """Demonstrate SQLite database operations."""
    print("SQLite Database Operations:")
    
    # Create and connect to database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Create tables
    print("\n1. Creating Tables:")
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price DECIMAL(10, 2),
            category TEXT,
            stock_quantity INTEGER DEFAULT 0
        )
    ''')
    
    # Orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            total_amount DECIMAL(10, 2),
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')
    
    print("✅ Tables created successfully!")
    
    # Insert data
    print("\n2. Inserting Data:")
    
    # Insert users
    users_data = [
        ('alice', 'alice@example.com', 25),
        ('bob', 'bob@example.com', 30),
        ('charlie', 'charlie@example.com', 35),
        ('diana', 'diana@example.com', 28)
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO users (username, email, age) 
        VALUES (?, ?, ?)
    ''', users_data)
    
    # Insert products
    products_data = [
        ('Laptop', 999.99, 'Electronics', 50),
        ('Mouse', 29.99, 'Accessories', 100),
        ('Keyboard', 79.99, 'Accessories', 75),
        ('Monitor', 299.99, 'Electronics', 25)
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO products (name, price, category, stock_quantity) 
        VALUES (?, ?, ?, ?)
    ''', products_data)
    
    # Insert orders
    orders_data = [
        (1, 1, 2, 1999.98),  # Alice bought 2 laptops
        (2, 2, 1, 29.99),    # Bob bought 1 mouse
        (3, 3, 1, 79.99),    # Charlie bought 1 keyboard
        (1, 4, 1, 299.99)    # Alice bought 1 monitor
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO orders (user_id, product_id, quantity, total_amount) 
        VALUES (?, ?, ?, ?)
    ''', orders_data)
    
    conn.commit()
    print("✅ Data inserted successfully!")
    
    # Query data
    print("\n3. Querying Data:")
    
    # Select all users
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(f"Users: {users}")
    
    # Select users with age > 25
    cursor.execute('SELECT username, email FROM users WHERE age > 25')
    adult_users = cursor.fetchall()
    print(f"Adult users: {adult_users}")
    
    # Join tables
    cursor.execute('''
        SELECT u.username, p.name, o.quantity, o.total_amount
        FROM users u
        JOIN orders o ON u.id = o.user_id
        JOIN products p ON o.product_id = p.id
    ''')
    orders_with_details = cursor.fetchall()
    print(f"Orders with details: {orders_with_details}")
    
    # Aggregate queries
    cursor.execute('''
        SELECT category, COUNT(*) as product_count, AVG(price) as avg_price
        FROM products
        GROUP BY category
    ''')
    category_stats = cursor.fetchall()
    print(f"Category statistics: {category_stats}")
    
    # Update data
    print("\n4. Updating Data:")
    cursor.execute('UPDATE users SET age = 26 WHERE username = ?', ('alice',))
    conn.commit()
    print("✅ User age updated!")
    
    # Delete data
    print("\n5. Deleting Data:")
    cursor.execute('DELETE FROM orders WHERE user_id = ?', (4,))
    conn.commit()
    print("✅ Orders deleted!")
    
    # Close connection
    conn.close()
    print("✅ Database connection closed!")

demonstrate_sqlite_operations()

# =============================================================================
# 3. PANDAS WITH SQL DATABASES
# =============================================================================

print("\n📊 PANDAS WITH SQL DATABASES")
print("-" * 35)

def demonstrate_pandas_sql():
    """Demonstrate using Pandas with SQL databases."""
    print("Pandas with SQL Databases:")
    
    # Create SQLite connection
    conn = sqlite3.connect('example.db')
    
    # Read data into DataFrames
    print("\n1. Reading Data into DataFrames:")
    
    users_df = pd.read_sql_query('SELECT * FROM users', conn)
    products_df = pd.read_sql_query('SELECT * FROM products', conn)
    orders_df = pd.read_sql_query('SELECT * FROM orders', conn)
    
    print(f"Users DataFrame:\n{users_df}")
    print(f"Products DataFrame:\n{products_df}")
    print(f"Orders DataFrame:\n{orders_df}")
    
    # Data analysis with Pandas
    print("\n2. Data Analysis with Pandas:")
    
    # Merge DataFrames
    orders_with_details = pd.merge(
        pd.merge(orders_df, users_df, on='user_id', how='left'),
        products_df, on='product_id', how='left'
    )
    
    print(f"Orders with details:\n{orders_with_details}")
    
    # Calculate statistics
    total_sales = orders_with_details['total_amount'].sum()
    avg_order_value = orders_with_details['total_amount'].mean()
    
    print(f"Total sales: ${total_sales:.2f}")
    print(f"Average order value: ${avg_order_value:.2f}")
    
    # Group by analysis
    sales_by_category = orders_with_details.groupby('category')['total_amount'].sum()
    print(f"Sales by category:\n{sales_by_category}")
    
    # Write DataFrame back to database
    print("\n3. Writing DataFrames to Database:")
    
    # Create new table from DataFrame
    sales_summary = orders_with_details.groupby('username').agg({
        'total_amount': ['sum', 'count', 'mean']
    }).round(2)
    
    sales_summary.columns = ['total_sales', 'order_count', 'avg_order_value']
    sales_summary = sales_summary.reset_index()
    
    print(f"Sales summary:\n{sales_summary}")
    
    # Write to database
    sales_summary.to_sql('sales_summary', conn, if_exists='replace', index=False)
    print("✅ Sales summary written to database!")
    
    conn.close()

demonstrate_pandas_sql()

# =============================================================================
# 4. SQLALCHEMY ORM
# =============================================================================

print("\n🔧 SQLALCHEMY ORM")
print("-" * 20)

def demonstrate_sqlalchemy():
    """Demonstrate SQLAlchemy ORM."""
    print("SQLAlchemy ORM:")
    
    from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker, relationship
    
    # Create engine
    engine = create_engine('sqlite:///sqlalchemy_example.db', echo=False)
    Base = declarative_base()
    
    # Define models
    class User(Base):
        __tablename__ = 'users'
        
        id = Column(Integer, primary_key=True)
        username = Column(String(80), unique=True, nullable=False)
        email = Column(String(120), unique=True, nullable=False)
        age = Column(Integer)
        created_at = Column(DateTime, default=datetime.utcnow)
        
        # Relationship
        orders = relationship("Order", back_populates="user")
    
    class Product(Base):
        __tablename__ = 'products'
        
        id = Column(Integer, primary_key=True)
        name = Column(String(100), nullable=False)
        price = Column(Float)
        category = Column(String(50))
        stock_quantity = Column(Integer, default=0)
        
        # Relationship
        orders = relationship("Order", back_populates="product")
    
    class Order(Base):
        __tablename__ = 'orders'
        
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('users.id'))
        product_id = Column(Integer, ForeignKey('products.id'))
        quantity = Column(Integer)
        total_amount = Column(Float)
        order_date = Column(DateTime, default=datetime.utcnow)
        
        # Relationships
        user = relationship("User", back_populates="orders")
        product = relationship("Product", back_populates="orders")
    
    # Create tables
    Base.metadata.create_all(engine)
    print("✅ Tables created with SQLAlchemy!")
    
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create and add objects
    print("\n1. Creating Objects:")
    
    # Create users
    user1 = User(username='alice_orm', email='alice_orm@example.com', age=25)
    user2 = User(username='bob_orm', email='bob_orm@example.com', age=30)
    
    # Create products
    product1 = Product(name='Laptop ORM', price=999.99, category='Electronics', stock_quantity=50)
    product2 = Product(name='Mouse ORM', price=29.99, category='Accessories', stock_quantity=100)
    
    # Add to session
    session.add_all([user1, user2, product1, product2])
    session.commit()
    
    print("✅ Objects created and saved!")
    
    # Query objects
    print("\n2. Querying Objects:")
    
    # Get all users
    all_users = session.query(User).all()
    print(f"All users: {[(u.username, u.email) for u in all_users]}")
    
    # Get user by username
    alice = session.query(User).filter_by(username='alice_orm').first()
    print(f"Alice: {alice.username}, {alice.email}")
    
    # Get products by category
    electronics = session.query(Product).filter_by(category='Electronics').all()
    print(f"Electronics: {[p.name for p in electronics]}")
    
    # Create order
    print("\n3. Creating Relationships:")
    
    order1 = Order(
        user_id=user1.id,
        product_id=product1.id,
        quantity=1,
        total_amount=999.99
    )
    
    session.add(order1)
    session.commit()
    
    # Query with relationships
    user_with_orders = session.query(User).filter_by(username='alice_orm').first()
    print(f"Alice's orders: {len(user_with_orders.orders)}")
    
    # Close session
    session.close()
    print("✅ Session closed!")

demonstrate_sqlalchemy()

# =============================================================================
# 5. POSTGRESQL DATABASE OPERATIONS
# =============================================================================

print("\n🐘 POSTGRESQL DATABASE OPERATIONS")
print("-" * 40)

def demonstrate_postgresql():
    """Demonstrate PostgreSQL database operations."""
    print("PostgreSQL Database Operations:")
    
    # Note: This is a demonstration - actual connection would require PostgreSQL server
    print("\n1. PostgreSQL Connection (Simulated):")
    
    # Connection parameters
    connection_params = {
        'host': 'localhost',
        'port': 5432,
        'database': 'myapp',
        'user': 'postgres',
        'password': 'password'
    }
    
    print(f"Connection parameters: {connection_params}")
    
    # Simulated connection
    try:
        # In real scenario: conn = psycopg2.connect(**connection_params)
        print("✅ Connected to PostgreSQL!")
        
        # Create table
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            department VARCHAR(50),
            salary DECIMAL(10, 2),
            hire_date DATE
        )
        '''
        print("✅ Table created!")
        
        # Insert data
        insert_sql = '''
        INSERT INTO employees (name, department, salary, hire_date) 
        VALUES (%s, %s, %s, %s)
        '''
        
        employee_data = [
            ('John Doe', 'Engineering', 75000.00, '2023-01-15'),
            ('Jane Smith', 'Marketing', 65000.00, '2023-02-20'),
            ('Bob Johnson', 'Engineering', 80000.00, '2023-03-10')
        ]
        
        print("✅ Data inserted!")
        
        # Query data
        query_sql = '''
        SELECT name, department, salary 
        FROM employees 
        WHERE salary > 70000
        ORDER BY salary DESC
        '''
        
        print("✅ Data queried!")
        
        # Close connection
        print("✅ Connection closed!")
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("Note: This is a simulation. Install PostgreSQL to run actual queries.")

demonstrate_postgresql()

# =============================================================================
# 6. MYSQL DATABASE OPERATIONS
# =============================================================================

print("\n🐬 MYSQL DATABASE OPERATIONS")
print("-" * 35)

def demonstrate_mysql():
    """Demonstrate MySQL database operations."""
    print("MySQL Database Operations:")
    
    # Note: This is a demonstration - actual connection would require MySQL server
    print("\n1. MySQL Connection (Simulated):")
    
    # Connection parameters
    connection_params = {
        'host': 'localhost',
        'port': 3306,
        'database': 'myapp',
        'user': 'root',
        'password': 'password'
    }
    
    print(f"Connection parameters: {connection_params}")
    
    # Simulated connection
    try:
        # In real scenario: conn = mysql.connector.connect(**connection_params)
        print("✅ Connected to MySQL!")
        
        # Create table
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE,
            phone VARCHAR(20),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        '''
        print("✅ Table created!")
        
        # Insert data
        insert_sql = '''
        INSERT INTO customers (name, email, phone) 
        VALUES (%s, %s, %s)
        '''
        
        customer_data = [
            ('Alice Brown', 'alice@example.com', '555-0101'),
            ('Bob Green', 'bob@example.com', '555-0102'),
            ('Charlie White', 'charlie@example.com', '555-0103')
        ]
        
        print("✅ Data inserted!")
        
        # Query data
        query_sql = '''
        SELECT name, email, phone 
        FROM customers 
        WHERE name LIKE 'A%'
        ORDER BY created_at DESC
        '''
        
        print("✅ Data queried!")
        
        # Close connection
        print("✅ Connection closed!")
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("Note: This is a simulation. Install MySQL to run actual queries.")

demonstrate_mysql()

# =============================================================================
# 7. DATABASE TRANSACTIONS AND ERROR HANDLING
# =============================================================================

print("\n🔄 DATABASE TRANSACTIONS AND ERROR HANDLING")
print("-" * 50)

def demonstrate_transactions():
    """Demonstrate database transactions and error handling."""
    print("Database Transactions and Error Handling:")
    
    # Create connection
    conn = sqlite3.connect('transactions_example.db')
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            balance DECIMAL(10, 2) NOT NULL
        )
    ''')
    
    # Insert sample data
    cursor.execute('DELETE FROM accounts')  # Clear existing data
    cursor.execute('INSERT INTO accounts (name, balance) VALUES (?, ?)', ('Alice', 1000.00))
    cursor.execute('INSERT INTO accounts (name, balance) VALUES (?, ?)', ('Bob', 500.00))
    conn.commit()
    
    print("✅ Sample data inserted!")
    
    # Transaction example: Money transfer
    def transfer_money(from_account, to_account, amount):
        """Transfer money between accounts with transaction."""
        try:
            # Start transaction
            conn.execute('BEGIN TRANSACTION')
            
            # Check if sender has enough balance
            cursor.execute('SELECT balance FROM accounts WHERE name = ?', (from_account,))
            sender_balance = cursor.fetchone()[0]
            
            if sender_balance < amount:
                raise ValueError(f"Insufficient balance. Available: {sender_balance}")
            
            # Deduct from sender
            cursor.execute('''
                UPDATE accounts 
                SET balance = balance - ? 
                WHERE name = ?
            ''', (amount, from_account))
            
            # Add to receiver
            cursor.execute('''
                UPDATE accounts 
                SET balance = balance + ? 
                WHERE name = ?
            ''', (amount, to_account))
            
            # Commit transaction
            conn.commit()
            print(f"✅ Transfer successful: ${amount} from {from_account} to {to_account}")
            
        except Exception as e:
            # Rollback transaction
            conn.rollback()
            print(f"❌ Transfer failed: {e}")
            raise
    
    # Test successful transfer
    print("\n1. Successful Transfer:")
    transfer_money('Alice', 'Bob', 200.00)
    
    # Check balances
    cursor.execute('SELECT name, balance FROM accounts ORDER BY name')
    balances = cursor.fetchall()
    print(f"Account balances: {balances}")
    
    # Test failed transfer (insufficient funds)
    print("\n2. Failed Transfer (Insufficient Funds):")
    try:
        transfer_money('Bob', 'Alice', 1000.00)  # Bob only has 700
    except ValueError as e:
        print(f"Expected error: {e}")
    
    # Check balances (should be unchanged)
    cursor.execute('SELECT name, balance FROM accounts ORDER BY name')
    balances = cursor.fetchall()
    print(f"Account balances after failed transfer: {balances}")
    
    # Close connection
    conn.close()
    print("✅ Connection closed!")

demonstrate_transactions()

# =============================================================================
# 8. DATABASE DESIGN AND RELATIONSHIPS
# =============================================================================

print("\n🏗️ DATABASE DESIGN AND RELATIONSHIPS")
print("-" * 40)

def demonstrate_database_design():
    """Demonstrate database design and relationships."""
    print("Database Design and Relationships:")
    
    # Create connection
    conn = sqlite3.connect('design_example.db')
    cursor = conn.cursor()
    
    # Create normalized database schema
    print("\n1. Creating Normalized Database Schema:")
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Categories table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description TEXT
        )
    ''')
    
    # Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price DECIMAL(10, 2),
            category_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )
    ''')
    
    # Orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Order items table (junction table)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            price DECIMAL(10, 2),
            FOREIGN KEY (order_id) REFERENCES orders (id),
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')
    
    print("✅ Normalized schema created!")
    
    # Insert sample data
    print("\n2. Inserting Sample Data:")
    
    # Insert categories
    categories = [
        ('Electronics', 'Electronic devices and accessories'),
        ('Clothing', 'Apparel and fashion items'),
        ('Books', 'Books and educational materials')
    ]
    cursor.executemany('INSERT INTO categories (name, description) VALUES (?, ?)', categories)
    
    # Insert users
    users = [
        ('alice', 'alice@example.com'),
        ('bob', 'bob@example.com'),
        ('charlie', 'charlie@example.com')
    ]
    cursor.executemany('INSERT INTO users (username, email) VALUES (?, ?)', users)
    
    # Insert products
    products = [
        ('Laptop', 999.99, 1),
        ('Smartphone', 699.99, 1),
        ('T-Shirt', 19.99, 2),
        ('Jeans', 49.99, 2),
        ('Python Book', 29.99, 3),
        ('JavaScript Book', 34.99, 3)
    ]
    cursor.executemany('INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)', products)
    
    # Insert orders
    orders = [
        (1, '2024-01-15', 'completed'),
        (2, '2024-01-16', 'pending'),
        (1, '2024-01-17', 'shipped')
    ]
    cursor.executemany('INSERT INTO orders (user_id, order_date, status) VALUES (?, ?, ?)', orders)
    
    # Insert order items
    order_items = [
        (1, 1, 1, 999.99),  # Order 1: 1 Laptop
        (1, 3, 2, 39.98),   # Order 1: 2 T-Shirts
        (2, 2, 1, 699.99),  # Order 2: 1 Smartphone
        (3, 5, 1, 29.99),   # Order 3: 1 Python Book
        (3, 6, 1, 34.99)    # Order 3: 1 JavaScript Book
    ]
    cursor.executemany('INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)', order_items)
    
    conn.commit()
    print("✅ Sample data inserted!")
    
    # Complex queries
    print("\n3. Complex Queries:")
    
    # Query: Get user order history with product details
    cursor.execute('''
        SELECT 
            u.username,
            o.order_date,
            o.status,
            p.name as product_name,
            oi.quantity,
            oi.price,
            c.name as category_name
        FROM users u
        JOIN orders o ON u.id = o.user_id
        JOIN order_items oi ON o.id = oi.order_id
        JOIN products p ON oi.product_id = p.id
        JOIN categories c ON p.category_id = c.id
        ORDER BY u.username, o.order_date
    ''')
    
    order_history = cursor.fetchall()
    print("Order History:")
    for row in order_history:
        print(f"  {row[0]} - {row[1]} - {row[2]} - {row[3]} (x{row[4]}) - ${row[5]} - {row[6]}")
    
    # Query: Get sales summary by category
    cursor.execute('''
        SELECT 
            c.name as category,
            COUNT(oi.id) as total_items,
            SUM(oi.quantity) as total_quantity,
            SUM(oi.price * oi.quantity) as total_revenue
        FROM categories c
        JOIN products p ON c.id = p.category_id
        JOIN order_items oi ON p.id = oi.product_id
        GROUP BY c.name
        ORDER BY total_revenue DESC
    ''')
    
    sales_summary = cursor.fetchall()
    print("\nSales Summary by Category:")
    for row in sales_summary:
        print(f"  {row[0]}: {row[1]} items, {row[2]} quantity, ${row[3]:.2f} revenue")
    
    # Close connection
    conn.close()
    print("\n✅ Connection closed!")

demonstrate_database_design()

# =============================================================================
# 9. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice SQL database operations with Python:

Exercise 1: Build a Library Management System
- Create tables for books, authors, borrowers, and loans
- Implement book checkout and return functionality
- Track overdue books and fines
- Generate reports on book usage

Exercise 2: Create an E-commerce Database
- Design product catalog with categories and inventory
- Implement shopping cart and order management
- Track customer orders and shipping
- Generate sales and inventory reports

Exercise 3: Build a Student Information System
- Create tables for students, courses, and enrollments
- Track grades and academic progress
- Implement course registration system
- Generate academic transcripts

Exercise 4: Develop a Hospital Management System
- Create tables for patients, doctors, and appointments
- Track medical records and treatments
- Implement appointment scheduling
- Generate patient and medical reports

Exercise 5: Create a Social Media Database
- Design user profiles and relationships
- Implement posts, comments, and likes
- Track user activity and engagement
- Generate social media analytics
""")

# =============================================================================
# 10. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
SQL Database Best Practices:

1. Database Design
   ✅ Use proper normalization
   ❌ Create denormalized tables

2. Security
   ✅ Use parameterized queries
   ❌ Concatenate user input into SQL

3. Performance
   ✅ Create appropriate indexes
   ❌ Ignore query performance

4. Error Handling
   ✅ Handle database errors gracefully
   ❌ Let errors crash the application

5. Transactions
   ✅ Use transactions for data integrity
   ❌ Ignore transaction boundaries

6. Connection Management
   ✅ Close connections properly
   ❌ Leave connections open

7. Data Validation
   ✅ Validate data before database operations
   ❌ Trust user input

8. Backup and Recovery
   ✅ Implement regular backups
   ❌ Ignore data protection
""")

# =============================================================================
# 11. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common SQL Database mistakes:

1. SQL Injection
   ❌ cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
   ✅ cursor.execute("SELECT * FROM users WHERE name = ?", (name,))

2. Not using transactions
   ❌ Multiple operations without transaction
   ✅ Use transactions for related operations

3. Ignoring indexes
   ❌ No indexes on frequently queried columns
   ✅ Create indexes on search columns

4. Not handling errors
   ❌ Let database errors crash the app
   ✅ Implement proper error handling

5. Not closing connections
   ❌ Leave database connections open
   ✅ Always close connections

6. Poor database design
   ❌ Denormalized tables
   ✅ Follow normalization rules

7. Not validating data
   ❌ Insert invalid data into database
   ✅ Validate data before insertion
""")

# =============================================================================
# 12. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ SQL database concepts and operations
✅ SQLite database operations with Python
✅ Pandas integration with databases
✅ SQLAlchemy ORM for database operations
✅ PostgreSQL and MySQL connections
✅ Database transactions and error handling
✅ Database design and relationships
✅ Best practices for database operations

Next Steps:
- Practice with real-world database projects
- Learn advanced SQL techniques
- Explore NoSQL databases
- Build database-driven applications
""")

# =============================================================================
# 13. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 19 of your Python journey!

You now understand:
- How to work with SQL databases in Python
- Different database libraries and their uses
- Database design and relationships
- Transaction management and error handling
- Best practices for database operations

SQL database operations are essential for most applications!
Practice with the exercises to master these crucial skills.

Happy coding! 🐍✨
""")

# =============================================================================
# 14. COMPLETE LEARNING JOURNEY SUMMARY
# =============================================================================

print("\n🎓 COMPLETE LEARNING JOURNEY SUMMARY")
print("-" * 40)

print("""
Congratulations! You've completed a comprehensive 19-day Python learning journey:

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

Days 17-19: AI/ML & Databases
- Day 17: AI and Machine Learning
- Day 18: AI Integration with Python
- Day 19: SQL Database Operations

You now have a complete foundation in Python programming, AI/ML, and database operations!
Continue practicing and building projects to master these skills.

Happy coding! 🐍✨
""")

# Clean up created files
import os
files_to_clean = ['example.db', 'sqlalchemy_example.db', 'transactions_example.db', 'design_example.db']
for file in files_to_clean:
    if os.path.exists(file):
        os.remove(file)
        print(f"🧹 Cleaned up {file}")

# Run the tutorial
if __name__ == "__main__":
    print("Day 19: SQL Database Operations with Python Tutorial")
    print("Run this file to see all examples in action!")
