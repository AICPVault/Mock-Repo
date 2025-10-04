"""
Day 16: Deployment and Production
=================================

Today we'll learn about deploying Python applications to production environments.
We'll explore different deployment strategies, containerization, cloud platforms,
and production best practices.

Learning Objectives:
- Understand deployment concepts and strategies
- Learn about virtual environments and dependencies
- Master containerization with Docker
- Explore cloud deployment platforms
- Practice production configuration
- Build scalable and reliable applications

Let's deploy to production!
"""

print("🐍 Welcome to Day 16: Deployment and Production!")
print("=" * 55)

import os
import sys
import subprocess
import json
import yaml
from pathlib import Path
import logging

# =============================================================================
# 1. WHAT IS DEPLOYMENT?
# =============================================================================

print("\n🚀 WHAT IS DEPLOYMENT?")
print("-" * 25)

"""
Deployment is:
- The process of making software available to users
- Moving code from development to production
- Ensuring applications run reliably in production
- Managing infrastructure and scaling

Deployment strategies:
- Traditional server deployment
- Containerization (Docker)
- Cloud platforms (AWS, GCP, Azure)
- Serverless deployment
- Microservices architecture

Key considerations:
- Scalability and performance
- Security and monitoring
- Backup and disaster recovery
- Cost optimization
- Maintenance and updates
"""

# =============================================================================
# 2. VIRTUAL ENVIRONMENTS AND DEPENDENCIES
# =============================================================================

print("\n🔧 VIRTUAL ENVIRONMENTS AND DEPENDENCIES")
print("-" * 45)

def demonstrate_virtual_environments():
    """Demonstrate virtual environment setup."""
    print("Virtual Environment Setup:")
    
    # Check if virtual environment exists
    venv_path = Path("venv")
    if venv_path.exists():
        print("✅ Virtual environment already exists")
    else:
        print("❌ Virtual environment not found")
        print("To create one, run: python -m venv venv")
    
    # Show requirements.txt example
    requirements_content = """# Production dependencies
Flask==2.3.3
gunicorn==21.2.0
psycopg2-binary==2.9.7
redis==4.6.0
celery==5.3.1

# Development dependencies
pytest==7.4.2
pytest-cov==4.1.0
black==23.7.0
flake8==6.0.0
mypy==1.5.1

# Testing dependencies
pytest-mock==3.11.1
factory-boy==3.3.0
"""
    
    print("\nExample requirements.txt:")
    print(requirements_content)
    
    # Show pip freeze output
    print("To generate requirements.txt from current environment:")
    print("pip freeze > requirements.txt")
    
    # Show installation commands
    print("\nInstallation commands:")
    print("pip install -r requirements.txt")
    print("pip install --upgrade pip")

demonstrate_virtual_environments()

# =============================================================================
# 3. DOCKER CONTAINERIZATION
# =============================================================================

print("\n🐳 DOCKER CONTAINERIZATION")
print("-" * 30)

def demonstrate_docker():
    """Demonstrate Docker containerization."""
    print("Docker Configuration:")
    
    # Dockerfile example
    dockerfile_content = """# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    postgresql-client \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd --create-home --shell /bin/bash app \\
    && chown -R app:app /app
USER app

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:8000/health || exit 1

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:app"]
"""
    
    print("Dockerfile:")
    print(dockerfile_content)
    
    # Docker Compose example
    docker_compose_content = """version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/myapp
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - web
    restart: unless-stopped

volumes:
  postgres_data:
"""
    
    print("\nDocker Compose configuration:")
    print(docker_compose_content)
    
    # Docker commands
    print("\nDocker Commands:")
    print("docker build -t myapp .")
    print("docker run -p 8000:8000 myapp")
    print("docker-compose up -d")
    print("docker-compose down")
    print("docker logs <container_name>")

demonstrate_docker()

# =============================================================================
# 4. CLOUD DEPLOYMENT PLATFORMS
# =============================================================================

print("\n☁️ CLOUD DEPLOYMENT PLATFORMS")
print("-" * 35)

def demonstrate_cloud_deployment():
    """Demonstrate cloud deployment options."""
    print("Cloud Deployment Platforms:")
    
    # AWS deployment
    print("\n1. AWS (Amazon Web Services):")
    print("   - EC2: Virtual servers")
    print("   - ECS: Container orchestration")
    print("   - Lambda: Serverless functions")
    print("   - RDS: Managed databases")
    print("   - S3: Object storage")
    print("   - CloudFront: CDN")
    
    # Google Cloud deployment
    print("\n2. Google Cloud Platform (GCP):")
    print("   - Compute Engine: Virtual machines")
    print("   - Cloud Run: Serverless containers")
    print("   - App Engine: Platform as a service")
    print("   - Cloud SQL: Managed databases")
    print("   - Cloud Storage: Object storage")
    
    # Azure deployment
    print("\n3. Microsoft Azure:")
    print("   - Virtual Machines: Compute instances")
    print("   - Container Instances: Serverless containers")
    print("   - App Service: Web app hosting")
    print("   - SQL Database: Managed databases")
    print("   - Blob Storage: Object storage")
    
    # Heroku deployment
    print("\n4. Heroku:")
    print("   - Simple deployment process")
    print("   - Git-based deployments")
    print("   - Add-ons for databases and services")
    print("   - Automatic scaling")
    print("   - Easy to use for beginners")
    
    # DigitalOcean deployment
    print("\n5. DigitalOcean:")
    print("   - Droplets: Virtual machines")
    print("   - App Platform: Managed applications")
    print("   - Managed databases")
    print("   - Load balancers")
    print("   - Cost-effective option")

demonstrate_cloud_deployment()

# =============================================================================
# 5. PRODUCTION CONFIGURATION
# =============================================================================

print("\n⚙️ PRODUCTION CONFIGURATION")
print("-" * 30)

def demonstrate_production_config():
    """Demonstrate production configuration."""
    print("Production Configuration:")
    
    # Environment variables
    env_vars = """# Production environment variables
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/production_db
REDIS_URL=redis://localhost:6379/0
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
"""
    
    print("Environment Variables:")
    print(env_vars)
    
    # Production settings
    production_config = """# Production configuration
import os
from datetime import timedelta

class ProductionConfig:
    # Basic settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = False
    TESTING = False
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Redis settings
    REDIS_URL = os.environ.get('REDIS_URL')
    
    # Mail settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # Security settings
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    # Logging settings
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'app.log'
    
    # Performance settings
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 20,
        'pool_recycle': 3600,
        'pool_pre_ping': True
    }
"""
    
    print("\nProduction Configuration Class:")
    print(production_config)
    
    # Nginx configuration
    nginx_config = """# Nginx configuration for production
server {
    listen 80;
    server_name your-domain.com;
    
    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com;
    
    # SSL configuration
    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    ssl_prefer_server_ciphers off;
    
    # Security headers
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
    
    # Gzip compression
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css text/xml text/javascript application/javascript application/xml+rss application/json;
    
    # Proxy to Flask application
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Static files
    location /static {
        alias /app/static;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
"""
    
    print("\nNginx Configuration:")
    print(nginx_config)

demonstrate_production_config()

# =============================================================================
# 6. MONITORING AND LOGGING
# =============================================================================

print("\n📊 MONITORING AND LOGGING")
print("-" * 30)

def demonstrate_monitoring():
    """Demonstrate monitoring and logging setup."""
    print("Monitoring and Logging:")
    
    # Logging configuration
    logging_config = """# Logging configuration for production
import logging
import logging.handlers
from datetime import datetime

def setup_logging():
    # Create logger
    logger = logging.getLogger('app')
    logger.setLevel(logging.INFO)
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    )
    simple_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    
    # File handler with rotation
    file_handler = logging.handlers.RotatingFileHandler(
        'app.log', maxBytes=10*1024*1024, backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(detailed_formatter)
    
    # Error file handler
    error_handler = logging.handlers.RotatingFileHandler(
        'error.log', maxBytes=10*1024*1024, backupCount=5
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(detailed_formatter)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(error_handler)
    
    return logger
"""
    
    print("Logging Configuration:")
    print(logging_config)
    
    # Health check endpoint
    health_check = """# Health check endpoint
@app.route('/health')
def health_check():
    '''Health check endpoint for monitoring.'''
    try:
        # Check database connection
        db.session.execute('SELECT 1')
        db_status = 'healthy'
    except Exception as e:
        db_status = f'unhealthy: {str(e)}'
    
    try:
        # Check Redis connection
        redis_client.ping()
        redis_status = 'healthy'
    except Exception as e:
        redis_status = f'unhealthy: {str(e)}'
    
    health_data = {
        'status': 'healthy' if db_status == 'healthy' and redis_status == 'healthy' else 'unhealthy',
        'timestamp': datetime.utcnow().isoformat(),
        'database': db_status,
        'redis': redis_status,
        'version': '1.0.0'
    }
    
    status_code = 200 if health_data['status'] == 'healthy' else 503
    return jsonify(health_data), status_code
"""
    
    print("\nHealth Check Endpoint:")
    print(health_check)
    
    # Monitoring tools
    print("\nMonitoring Tools:")
    print("1. Application Performance Monitoring (APM):")
    print("   - New Relic")
    print("   - Datadog")
    print("   - AppDynamics")
    print("   - Sentry")
    
    print("\n2. Infrastructure Monitoring:")
    print("   - Prometheus + Grafana")
    print("   - CloudWatch (AWS)")
    print("   - Stackdriver (GCP)")
    print("   - Azure Monitor")
    
    print("\n3. Log Management:")
    print("   - ELK Stack (Elasticsearch, Logstash, Kibana)")
    print("   - Splunk")
    print("   - CloudWatch Logs")
    print("   - Papertrail")

demonstrate_monitoring()

# =============================================================================
# 7. SECURITY CONSIDERATIONS
# =============================================================================

print("\n🔒 SECURITY CONSIDERATIONS")
print("-" * 30)

def demonstrate_security():
    """Demonstrate security considerations for production."""
    print("Security Best Practices:")
    
    # Security checklist
    security_checklist = """# Production Security Checklist

## 1. Environment Security
- Use environment variables for secrets
- Never commit secrets to version control
- Use different secrets for different environments
- Rotate secrets regularly

## 2. Application Security
- Enable HTTPS/TLS encryption
- Use secure session cookies
- Implement CSRF protection
- Validate and sanitize all inputs
- Use parameterized queries (SQL injection prevention)

## 3. Authentication & Authorization
- Use strong password policies
- Implement multi-factor authentication
- Use OAuth for third-party authentication
- Implement proper session management
- Use JWT tokens securely

## 4. Database Security
- Use encrypted connections
- Implement database access controls
- Regular security updates
- Backup encryption
- Audit database access

## 5. Infrastructure Security
- Use firewalls and security groups
- Regular security updates
- Monitor for suspicious activity
- Implement intrusion detection
- Use secure communication protocols

## 6. Data Protection
- Encrypt sensitive data at rest
- Use secure data transmission
- Implement data retention policies
- Regular security audits
- Compliance with regulations (GDPR, HIPAA)
"""
    
    print(security_checklist)
    
    # Security headers
    security_headers = """# Security headers middleware
from flask import Flask, request, jsonify
import hmac
import hashlib
import time

def security_headers_middleware(app):
    '''Add security headers to all responses.'''
    
    @app.after_request
    def add_security_headers(response):
        # Prevent clickjacking
        response.headers['X-Frame-Options'] = 'DENY'
        
        # Prevent MIME type sniffing
        response.headers['X-Content-Type-Options'] = 'nosniff'
        
        # XSS protection
        response.headers['X-XSS-Protection'] = '1; mode=block'
        
        # Strict Transport Security
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        
        # Content Security Policy
        response.headers['Content-Security-Policy'] = "default-src 'self'"
        
        # Referrer Policy
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        
        return response

def rate_limit_middleware(app):
    '''Implement rate limiting.'''
    from collections import defaultdict
    import time
    
    request_counts = defaultdict(list)
    
    @app.before_request
    def rate_limit():
        client_ip = request.remote_addr
        current_time = time.time()
        
        # Clean old requests
        request_counts[client_ip] = [
            req_time for req_time in request_counts[client_ip]
            if current_time - req_time < 60  # 1 minute window
        ]
        
        # Check rate limit (100 requests per minute)
        if len(request_counts[client_ip]) >= 100:
            return jsonify({'error': 'Rate limit exceeded'}), 429
        
        # Add current request
        request_counts[client_ip].append(current_time)
"""
    
    print("\nSecurity Middleware:")
    print(security_headers)

demonstrate_security()

# =============================================================================
# 8. SCALING AND PERFORMANCE
# =============================================================================

print("\n⚡ SCALING AND PERFORMANCE")
print("-" * 30)

def demonstrate_scaling():
    """Demonstrate scaling and performance optimization."""
    print("Scaling and Performance:")
    
    # Performance optimization
    performance_tips = """# Performance Optimization Tips

## 1. Database Optimization
- Use database indexes
- Optimize queries
- Use connection pooling
- Implement caching
- Use read replicas

## 2. Application Optimization
- Use async/await for I/O operations
- Implement caching (Redis, Memcached)
- Use CDN for static files
- Optimize images and assets
- Use compression (gzip, brotli)

## 3. Code Optimization
- Profile your application
- Use efficient algorithms
- Avoid N+1 queries
- Use lazy loading
- Implement pagination

## 4. Infrastructure Scaling
- Horizontal scaling (more servers)
- Vertical scaling (better hardware)
- Load balancing
- Auto-scaling groups
- Container orchestration (Kubernetes)

## 5. Monitoring Performance
- Application metrics
- Database performance
- Server resources
- Response times
- Error rates
"""
    
    print(performance_tips)
    
    # Caching implementation
    caching_example = """# Redis caching implementation
import redis
import json
from functools import wraps

# Redis connection
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_result(expiration=300):
    '''Cache function result for specified seconds.'''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create cache key
            cache_key = f"{func.__name__}:{hash(str(args) + str(kwargs))}"
            
            # Try to get from cache
            cached_result = redis_client.get(cache_key)
            if cached_result:
                return json.loads(cached_result)
            
            # Execute function
            result = func(*args, **kwargs)
            
            # Store in cache
            redis_client.setex(
                cache_key, 
                expiration, 
                json.dumps(result, default=str)
            )
            
            return result
        return wrapper
    return decorator

# Usage example
@cache_result(expiration=600)  # Cache for 10 minutes
def get_user_posts(user_id):
    '''Get user posts with caching.'''
    return Post.query.filter_by(user_id=user_id).all()
"""
    
    print("\nCaching Implementation:")
    print(caching_example)
    
    # Load balancing
    print("\nLoad Balancing Strategies:")
    print("1. Round Robin: Distribute requests evenly")
    print("2. Least Connections: Send to server with fewest connections")
    print("3. IP Hash: Route based on client IP")
    print("4. Weighted: Assign different weights to servers")
    print("5. Health Checks: Only route to healthy servers")

demonstrate_scaling()

# =============================================================================
# 9. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice deployment and production:

Exercise 1: Deploy a Flask Application
- Create a simple Flask app
- Set up Docker containerization
- Deploy to a cloud platform
- Configure environment variables
- Set up monitoring

Exercise 2: Build a CI/CD Pipeline
- Set up automated testing
- Configure deployment pipeline
- Implement blue-green deployment
- Set up rollback procedures
- Monitor deployment success

Exercise 3: Create a Production Environment
- Set up production database
- Configure load balancer
- Implement caching layer
- Set up logging and monitoring
- Configure security measures

Exercise 4: Build a Microservices Architecture
- Split application into services
- Implement service communication
- Set up service discovery
- Configure API gateway
- Implement distributed logging

Exercise 5: Implement Disaster Recovery
- Set up database backups
- Configure failover systems
- Implement data replication
- Test recovery procedures
- Document recovery processes
""")

# =============================================================================
# 10. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
Deployment and production best practices:

1. Use Infrastructure as Code
   ✅ Terraform, CloudFormation
   ❌ Manual infrastructure setup

2. Implement CI/CD
   ✅ Automated testing and deployment
   ❌ Manual deployment processes

3. Use Environment Variables
   ✅ Store secrets in environment variables
   ❌ Hardcode configuration values

4. Implement Monitoring
   ✅ Comprehensive monitoring and alerting
   ❌ Deploy without monitoring

5. Use Version Control
   ✅ Tag releases and track changes
   ❌ Deploy without version control

6. Implement Security
   ✅ Security-first approach
   ❌ Security as an afterthought

7. Plan for Scaling
   ✅ Design for horizontal scaling
   ❌ Assume single-server deployment

8. Document Everything
   ✅ Document deployment procedures
   ❌ Deploy without documentation
""")

# =============================================================================
# 11. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common deployment mistakes:

1. Not using environment variables
   ❌ Hardcoding database credentials
   ✅ Use environment variables for secrets

2. Skipping testing in production
   ❌ Deploying without testing
   ✅ Test in staging environment first

3. Not monitoring applications
   ❌ Deploying without monitoring
   ✅ Set up comprehensive monitoring

4. Not planning for failures
   ❌ Single point of failure
   ✅ Implement redundancy and failover

5. Not securing applications
   ❌ Deploying without security measures
   ✅ Implement security from the start

6. Not backing up data
   ❌ No backup strategy
   ✅ Regular automated backups

7. Not documenting procedures
   ❌ Deploying without documentation
   ✅ Document all deployment procedures
""")

# =============================================================================
# 12. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ Virtual environments and dependency management
✅ Docker containerization
✅ Cloud deployment platforms
✅ Production configuration
✅ Monitoring and logging
✅ Security considerations
✅ Scaling and performance optimization
✅ Best practices for production deployment

Next Steps:
- Continue building and deploying applications
- Explore advanced deployment strategies
- Learn about microservices architecture
- Master cloud platform services
""")

# =============================================================================
# 13. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 16 of your Python journey!

You now understand:
- How to deploy Python applications to production
- Containerization with Docker
- Cloud deployment strategies
- Production configuration and security
- Monitoring and performance optimization
- Best practices for reliable deployments

Deployment and production are essential for real-world applications!
Practice with the exercises to master these crucial skills.

Happy coding! 🐍✨
""")

# =============================================================================
# 14. COMPLETE LEARNING JOURNEY SUMMARY
# =============================================================================

print("\n🎓 COMPLETE LEARNING JOURNEY SUMMARY")
print("-" * 40)

print("""
Congratulations! You've completed a comprehensive 16-day Python learning journey:

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

You now have a solid foundation in Python programming!
Continue practicing and building projects to master these skills.

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 16: Deployment and Production Tutorial")
    print("Run this file to see all examples in action!")
