"""
Day 14: Web Development with Flask
=================================

Today we'll learn about web development using Flask - a lightweight and flexible
Python web framework. We'll build web applications, handle HTTP requests,
work with templates, and create RESTful APIs.

Learning Objectives:
- Understand web development concepts
- Learn Flask basics and routing
- Master template rendering and forms
- Work with databases and sessions
- Build RESTful APIs
- Deploy web applications

Let's build web applications with Flask!
"""

print("🐍 Welcome to Day 14: Web Development with Flask!")
print("=" * 55)

from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import json

# =============================================================================
# 1. WHAT IS FLASK?
# =============================================================================

print("\n🌐 WHAT IS FLASK?")
print("-" * 20)

"""
Flask is:
- A lightweight Python web framework
- Minimal and flexible
- Easy to learn and use
- Perfect for small to medium applications
- Extensible with extensions

Key features:
- URL routing
- Template rendering
- Request handling
- Session management
- Database integration
- RESTful API support

Flask vs Django:
- Flask: Microframework, more control
- Django: Full-featured, batteries included
"""

# =============================================================================
# 2. BASIC FLASK APPLICATION
# =============================================================================

print("\n🏗️ BASIC FLASK APPLICATION")
print("-" * 30)

# Create Flask app
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for sessions

# Basic routes
@app.route('/')
def home():
    """Home page route."""
    return "Welcome to Flask Web Development!"

@app.route('/about')
def about():
    """About page route."""
    return "This is the about page."

@app.route('/user/<username>')
def user_profile(username):
    """Dynamic route with parameter."""
    return f"Hello, {username}!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    """Route with integer parameter."""
    return f"Post ID: {post_id}"

# HTTP methods
@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    """Route that handles multiple HTTP methods."""
    if request.method == 'GET':
        return jsonify({"message": "GET request received", "data": "sample data"})
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({"message": "POST request received", "received_data": data})

print("Flask routes defined:")
print("  - / (home)")
print("  - /about")
print("  - /user/<username>")
print("  - /post/<int:post_id>")
print("  - /api/data (GET/POST)")

# =============================================================================
# 3. TEMPLATE RENDERING
# =============================================================================

print("\n📄 TEMPLATE RENDERING")
print("-" * 25)

# Template rendering example
@app.route('/template')
def template_example():
    """Route that renders a template."""
    user_data = {
        'name': 'Alice',
        'age': 25,
        'city': 'New York',
        'hobbies': ['Python', 'Web Development', 'Data Science']
    }
    
    return render_template('user_profile.html', user=user_data)

# Template with form
@app.route('/form', methods=['GET', 'POST'])
def form_example():
    """Route that handles forms."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Process form data
        flash(f"Thank you, {name}! Your message has been received.")
        return redirect(url_for('form_example'))
    
    return render_template('contact_form.html')

print("Template routes defined:")
print("  - /template (renders user profile)")
print("  - /form (handles contact form)")

# =============================================================================
# 4. DATABASE INTEGRATION
# =============================================================================

print("\n🗄️ DATABASE INTEGRATION")
print("-" * 25)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define models
class User(db.Model):
    """User model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    """Post model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    author = db.relationship('User', backref=db.backref('posts', lazy=True))
    
    def __repr__(self):
        return f'<Post {self.title}>'

# Database routes
@app.route('/users')
def list_users():
    """List all users."""
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    """Create a new user."""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists!')
            return redirect(url_for('create_user'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists!')
            return redirect(url_for('create_user'))
        
        # Create new user
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        
        flash('User created successfully!')
        return redirect(url_for('list_users'))
    
    return render_template('create_user.html')

print("Database models defined:")
print("  - User (id, username, email, created_at)")
print("  - Post (id, title, content, author_id, created_at)")

# =============================================================================
# 5. RESTful API DEVELOPMENT
# =============================================================================

print("\n🔌 RESTful API DEVELOPMENT")
print("-" * 30)

# API routes
@app.route('/api/users', methods=['GET'])
def api_get_users():
    """Get all users (API)."""
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'created_at': user.created_at.isoformat()
    } for user in users])

@app.route('/api/users/<int:user_id>', methods=['GET'])
def api_get_user(user_id):
    """Get specific user (API)."""
    user = User.query.get_or_404(user_id)
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'created_at': user.created_at.isoformat()
    })

@app.route('/api/users', methods=['POST'])
def api_create_user():
    """Create new user (API)."""
    data = request.get_json()
    
    # Validate required fields
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Username and email are required'}), 400
    
    # Check if user already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 400
    
    # Create new user
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({
        'id': new_user.id,
        'username': new_user.username,
        'email': new_user.email,
        'created_at': new_user.created_at.isoformat()
    }), 201

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def api_update_user(user_id):
    """Update user (API)."""
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    
    db.session.commit()
    
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'created_at': user.created_at.isoformat()
    })

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    """Delete user (API)."""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'User deleted successfully'})

print("API endpoints defined:")
print("  - GET /api/users (list all users)")
print("  - GET /api/users/<id> (get specific user)")
print("  - POST /api/users (create user)")
print("  - PUT /api/users/<id> (update user)")
print("  - DELETE /api/users/<id> (delete user)")

# =============================================================================
# 6. SESSION MANAGEMENT
# =============================================================================

print("\n🔐 SESSION MANAGEMENT")
print("-" * 25)

# Session management routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')  # In real app, hash password
        
        # Simple authentication (in real app, use proper authentication)
        user = User.query.filter_by(username=username).first()
        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """User logout."""
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    """User dashboard."""
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.')
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', user=user)

print("Session management routes defined:")
print("  - /login (user login)")
print("  - /logout (user logout)")
print("  - /dashboard (user dashboard)")

# =============================================================================
# 7. ERROR HANDLING
# =============================================================================

print("\n⚠️ ERROR HANDLING")
print("-" * 18)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    db.session.rollback()
    return render_template('500.html'), 500

@app.errorhandler(403)
def forbidden(error):
    """Handle 403 errors."""
    return render_template('403.html'), 403

print("Error handlers defined:")
print("  - 404 (Not Found)")
print("  - 500 (Internal Server Error)")
print("  - 403 (Forbidden)")

# =============================================================================
# 8. PRACTICAL EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL EXAMPLES")
print("-" * 22)

# Example 1: Blog Application
def create_blog_app():
    """Create a simple blog application."""
    print("Blog Application Features:")
    print("  - User registration and authentication")
    print("  - Create, read, update, delete posts")
    print("  - User profiles and post management")
    print("  - Comment system")
    print("  - Search functionality")

# Example 2: E-commerce API
def create_ecommerce_api():
    """Create an e-commerce API."""
    print("\nE-commerce API Features:")
    print("  - Product catalog management")
    print("  - Shopping cart functionality")
    print("  - Order processing")
    print("  - User management")
    print("  - Payment integration")

# Example 3: Task Management System
def create_task_management():
    """Create a task management system."""
    print("\nTask Management Features:")
    print("  - Task creation and assignment")
    print("  - Priority and status tracking")
    print("  - Team collaboration")
    print("  - Progress monitoring")
    print("  - Notification system")

create_blog_app()
create_ecommerce_api()
create_task_management()

# =============================================================================
# 9. FLASK EXTENSIONS
# =============================================================================

print("\n🔧 FLASK EXTENSIONS")
print("-" * 22)

print("""
Popular Flask Extensions:

1. Flask-SQLAlchemy: Database ORM
   - Easy database operations
   - Model relationships
   - Database migrations

2. Flask-Login: User authentication
   - User session management
   - Login/logout functionality
   - User authentication

3. Flask-WTF: Form handling
   - CSRF protection
   - Form validation
   - File uploads

4. Flask-Mail: Email functionality
   - Send emails
   - Email templates
   - Bulk email support

5. Flask-Migrate: Database migrations
   - Version control for database
   - Schema changes
   - Data migrations

6. Flask-RESTful: REST API development
   - Resource-based APIs
   - Request parsing
   - Response formatting

7. Flask-CORS: Cross-Origin Resource Sharing
   - Handle CORS requests
   - API security
   - Cross-domain support
""")

# =============================================================================
# 10. DEPLOYMENT CONSIDERATIONS
# =============================================================================

print("\n🚀 DEPLOYMENT CONSIDERATIONS")
print("-" * 30)

print("""
Deployment Best Practices:

1. Environment Configuration
   - Use environment variables
   - Separate development/production configs
   - Secure secret keys

2. Database Setup
   - Use production database
   - Set up database migrations
   - Backup strategies

3. Security Measures
   - HTTPS enforcement
   - CSRF protection
   - Input validation
   - SQL injection prevention

4. Performance Optimization
   - Use production WSGI server
   - Implement caching
   - Database query optimization
   - Static file serving

5. Monitoring and Logging
   - Application logging
   - Error tracking
   - Performance monitoring
   - Health checks

6. Scalability
   - Load balancing
   - Database scaling
   - Caching strategies
   - CDN usage
""")

# =============================================================================
# 11. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice Flask web development:

Exercise 1: Personal Blog
- Create a blog with user authentication
- Allow users to create, edit, delete posts
- Implement comment system
- Add search functionality
- Create admin panel

Exercise 2: E-commerce API
- Build product catalog API
- Implement shopping cart
- Add user authentication
- Create order management
- Integrate payment processing

Exercise 3: Task Management System
- Create task CRUD operations
- Implement user roles
- Add task assignment
- Create progress tracking
- Build notification system

Exercise 4: Social Media Platform
- User registration and profiles
- Post creation and sharing
- Follow/unfollow system
- Like and comment functionality
- Real-time updates

Exercise 5: Learning Management System
- Course creation and management
- Student enrollment
- Assignment submission
- Grade tracking
- Progress monitoring
""")

# =============================================================================
# 12. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
Flask development best practices:

1. Project Structure
   ✅ Organize code in modules
   ❌ Put everything in one file

2. Configuration Management
   ✅ Use environment variables
   ❌ Hardcode configuration values

3. Database Design
   ✅ Use proper relationships
   ❌ Create redundant tables

4. Security
   ✅ Validate all inputs
   ❌ Trust user input

5. Error Handling
   ✅ Handle all exceptions
   ❌ Let errors crash the app

6. Testing
   ✅ Write unit tests
   ❌ Skip testing

7. Documentation
   ✅ Document your code
   ❌ Write code without comments

8. Performance
   ✅ Optimize database queries
   ❌ Ignore performance issues
""")

# =============================================================================
# 13. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common Flask mistakes:

1. Not using virtual environments
   ❌ Installing packages globally
   ✅ Use virtual environments

2. Hardcoding configuration
   ❌ app.config['SECRET_KEY'] = 'hardcoded'
   ✅ Use environment variables

3. Not handling errors
   ❌ Let exceptions crash the app
   ✅ Implement proper error handling

4. Not validating input
   ❌ Trust user input
   ✅ Validate all inputs

5. Not using database migrations
   ❌ Manual database changes
   ✅ Use Flask-Migrate

6. Not implementing security
   ❌ No CSRF protection
   ✅ Implement security measures

7. Not testing the application
   ❌ Deploy without testing
   ✅ Write and run tests
""")

# =============================================================================
# 14. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ Flask basics and routing
✅ Template rendering and forms
✅ Database integration with SQLAlchemy
✅ RESTful API development
✅ Session management
✅ Error handling
✅ Flask extensions and deployment

Next Steps:
- Day 15: Testing and Debugging
- Day 16: Deployment and Production
""")

# =============================================================================
# 15. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 14 of your Python journey!

You now understand:
- How to build web applications with Flask
- Database integration and ORM
- RESTful API development
- Session management and authentication
- Error handling and security
- Deployment considerations

Flask is a powerful tool for web development!
Practice with the exercises to master this framework.

Happy coding! 🐍✨
""")

# Note: This is a demonstration file
# In a real application, you would:
# 1. Create the actual HTML templates
# 2. Set up the database
# 3. Implement proper authentication
# 4. Add error handling
# 5. Deploy to a production server

# Run the tutorial
if __name__ == "__main__":
    print("Day 14: Web Development with Flask Tutorial")
    print("Run this file to see all examples in action!")
    print("\nNote: This is a demonstration file.")
    print("In a real application, you would create HTML templates")
    print("and run the Flask application with: app.run()")
