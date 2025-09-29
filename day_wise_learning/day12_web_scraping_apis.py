"""
Day 12: Web Scraping and APIs
=============================

Today we'll learn about web scraping and working with APIs in Python.
We'll explore how to extract data from websites, work with REST APIs,
and build applications that interact with web services.

Learning Objectives:
- Understand web scraping concepts and ethics
- Learn to use requests library for HTTP operations
- Master BeautifulSoup for HTML parsing
- Work with REST APIs and JSON data
- Handle authentication and rate limiting
- Build real-world data extraction applications

Let's explore the web with Python!
"""

print("🐍 Welcome to Day 12: Web Scraping and APIs!")
print("=" * 50)

import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urljoin, urlparse

# =============================================================================
# 1. WHAT IS WEB SCRAPING?
# =============================================================================

print("\n🌐 WHAT IS WEB SCRAPING?")
print("-" * 25)

"""
Web Scraping is:
- The process of extracting data from websites
- Automated data collection from web pages
- Converting unstructured web data to structured format
- Essential for data analysis and research

Common use cases:
- Price monitoring and comparison
- News aggregation
- Social media data collection
- Research and academic studies
- Market analysis

Important considerations:
- Respect robots.txt and terms of service
- Implement rate limiting
- Handle dynamic content
- Follow ethical guidelines
"""

# =============================================================================
# 2. HTTP REQUESTS WITH REQUESTS LIBRARY
# =============================================================================

print("\n📡 HTTP REQUESTS WITH REQUESTS LIBRARY")
print("-" * 40)

def demonstrate_http_requests():
    """Demonstrate basic HTTP operations."""
    print("HTTP Requests Examples:")
    
    # GET request
    try:
        response = requests.get('https://httpbin.org/get')
        print(f"GET request status: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        print(f"Response content type: {response.headers.get('content-type')}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    
    # POST request
    try:
        data = {'key': 'value', 'name': 'Python'}
        response = requests.post('https://httpbin.org/post', data=data)
        print(f"POST request status: {response.status_code}")
    except requests.RequestException as e:
        print(f"POST request failed: {e}")
    
    # Request with headers
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        response = requests.get('https://httpbin.org/headers', headers=headers)
        print(f"Request with custom headers status: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request with headers failed: {e}")

demonstrate_http_requests()

# =============================================================================
# 3. HTML PARSING WITH BEAUTIFULSOUP
# =============================================================================

print("\n🍲 HTML PARSING WITH BEAUTIFULSOUP")
print("-" * 35)

def demonstrate_html_parsing():
    """Demonstrate HTML parsing with BeautifulSoup."""
    # Sample HTML content
    html_content = """
    <html>
        <head>
            <title>Sample Web Page</title>
        </head>
        <body>
            <h1>Welcome to Python Web Scraping</h1>
            <div class="content">
                <p>This is a sample paragraph.</p>
                <p>Another paragraph with <a href="https://python.org">Python link</a>.</p>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                    <li>Item 3</li>
                </ul>
            </div>
            <div class="sidebar">
                <h2>Links</h2>
                <a href="https://docs.python.org">Python Docs</a>
                <a href="https://pypi.org">PyPI</a>
            </div>
        </body>
    </html>
    """
    
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    print("HTML Parsing Examples:")
    
    # Get title
    title = soup.title.string
    print(f"Page title: {title}")
    
    # Get all headings
    headings = soup.find_all(['h1', 'h2'])
    print(f"Headings: {[h.get_text() for h in headings]}")
    
    # Get all paragraphs
    paragraphs = soup.find_all('p')
    print(f"Paragraphs: {[p.get_text() for p in paragraphs]}")
    
    # Get all links
    links = soup.find_all('a')
    print(f"Links: {[(link.get_text(), link.get('href')) for link in links]}")
    
    # Get specific elements by class
    content_div = soup.find('div', class_='content')
    if content_div:
        print(f"Content div text: {content_div.get_text()}")
    
    # Get list items
    list_items = soup.find_all('li')
    print(f"List items: {[li.get_text() for li in list_items]}")

demonstrate_html_parsing()

# =============================================================================
# 4. WORKING WITH REST APIs
# =============================================================================

print("\n🔌 WORKING WITH REST APIs")
print("-" * 25)

def demonstrate_api_usage():
    """Demonstrate working with REST APIs."""
    print("REST API Examples:")
    
    # JSONPlaceholder API (free testing API)
    try:
        # GET request to fetch posts
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        if response.status_code == 200:
            post = response.json()
            print(f"Post title: {post['title']}")
            print(f"Post body: {post['body'][:50]}...")
        else:
            print(f"API request failed with status: {response.status_code}")
    except requests.RequestException as e:
        print(f"API request failed: {e}")
    
    # Fetch multiple posts
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        if response.status_code == 200:
            posts = response.json()
            print(f"Fetched {len(posts)} posts")
            print(f"First post title: {posts[0]['title']}")
        else:
            print(f"Failed to fetch posts: {response.status_code}")
    except requests.RequestException as e:
        print(f"Posts request failed: {e}")

demonstrate_api_usage()

# =============================================================================
# 5. PRACTICAL WEB SCRAPING EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL WEB SCRAPING EXAMPLES")
print("-" * 40)

def scrape_news_headlines():
    """Demonstrate scraping news headlines (simulated)."""
    # Simulated HTML content for demonstration
    html_content = """
    <html>
        <body>
            <div class="news-container">
                <article class="news-item">
                    <h2><a href="/news/1">Python 3.12 Released with New Features</a></h2>
                    <p class="summary">The latest Python version includes performance improvements.</p>
                    <span class="date">2024-01-15</span>
                </article>
                <article class="news-item">
                    <h2><a href="/news/2">Web Scraping Best Practices</a></h2>
                    <p class="summary">Learn how to scrape websites ethically and efficiently.</p>
                    <span class="date">2024-01-14</span>
                </article>
                <article class="news-item">
                    <h2><a href="/news/3">Data Science with Python</a></h2>
                    <p class="summary">Explore data analysis and visualization techniques.</p>
                    <span class="date">2024-01-13</span>
                </article>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    print("News Headlines Scraping:")
    
    # Extract news articles
    articles = soup.find_all('article', class_='news-item')
    
    for i, article in enumerate(articles, 1):
        title_link = article.find('h2').find('a')
        title = title_link.get_text()
        link = title_link.get('href')
        summary = article.find('p', class_='summary').get_text()
        date = article.find('span', class_='date').get_text()
        
        print(f"  Article {i}:")
        print(f"    Title: {title}")
        print(f"    Link: {link}")
        print(f"    Summary: {summary}")
        print(f"    Date: {date}")
        print()

def scrape_product_prices():
    """Demonstrate scraping product prices (simulated)."""
    # Simulated HTML content for demonstration
    html_content = """
    <html>
        <body>
            <div class="products">
                <div class="product">
                    <h3>Laptop Pro 15"</h3>
                    <span class="price">$1299.99</span>
                    <span class="rating">4.5 stars</span>
                </div>
                <div class="product">
                    <h3>Wireless Mouse</h3>
                    <span class="price">$29.99</span>
                    <span class="rating">4.2 stars</span>
                </div>
                <div class="product">
                    <h3>Mechanical Keyboard</h3>
                    <span class="price">$89.99</span>
                    <span class="rating">4.7 stars</span>
                </div>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    print("Product Price Scraping:")
    
    products = soup.find_all('div', class_='product')
    
    for product in products:
        name = product.find('h3').get_text()
        price = product.find('span', class_='price').get_text()
        rating = product.find('span', class_='rating').get_text()
        
        print(f"  {name}: {price} ({rating})")

scrape_news_headlines()
scrape_product_prices()

# =============================================================================
# 6. HANDLING DYNAMIC CONTENT
# =============================================================================

print("\n⚡ HANDLING DYNAMIC CONTENT")
print("-" * 30)

def demonstrate_dynamic_content():
    """Demonstrate handling dynamic content (simulated)."""
    print("Dynamic Content Handling:")
    
    # Simulate JavaScript-rendered content
    print("  Note: For real dynamic content, you would use:")
    print("  - Selenium WebDriver")
    print("  - Playwright")
    print("  - Scrapy with Splash")
    print("  - Requests-HTML")
    
    # Example of handling AJAX requests
    print("\n  AJAX Request Example:")
    print("  - Identify API endpoints")
    print("  - Make direct API calls")
    print("  - Parse JSON responses")
    print("  - Handle pagination")

demonstrate_dynamic_content()

# =============================================================================
# 7. ERROR HANDLING AND ROBUSTNESS
# =============================================================================

print("\n🛡️ ERROR HANDLING AND ROBUSTNESS")
print("-" * 35)

def robust_web_scraping():
    """Demonstrate robust web scraping with error handling."""
    print("Robust Web Scraping:")
    
    # Simulate different scenarios
    scenarios = [
        {"url": "https://httpbin.org/status/200", "description": "Success"},
        {"url": "https://httpbin.org/status/404", "description": "Not Found"},
        {"url": "https://httpbin.org/status/500", "description": "Server Error"},
        {"url": "https://invalid-url-that-does-not-exist.com", "description": "Connection Error"}
    ]
    
    for scenario in scenarios:
        try:
            response = requests.get(scenario["url"], timeout=5)
            print(f"  {scenario['description']}: Status {response.status_code}")
        except requests.exceptions.Timeout:
            print(f"  {scenario['description']}: Timeout error")
        except requests.exceptions.ConnectionError:
            print(f"  {scenario['description']}: Connection error")
        except requests.exceptions.RequestException as e:
            print(f"  {scenario['description']}: Request error - {e}")

robust_web_scraping()

# =============================================================================
# 8. RATE LIMITING AND ETHICS
# =============================================================================

print("\n⏱️ RATE LIMITING AND ETHICS")
print("-" * 30)

def demonstrate_rate_limiting():
    """Demonstrate rate limiting and ethical scraping."""
    print("Rate Limiting and Ethics:")
    
    # Simulate rate limiting
    print("  Rate Limiting Strategies:")
    print("  - Add delays between requests")
    print("  - Use time.sleep() to be respectful")
    print("  - Implement exponential backoff")
    print("  - Respect robots.txt")
    print("  - Check website's terms of service")
    
    # Example of respectful scraping
    print("\n  Respectful Scraping Example:")
    for i in range(3):
        print(f"    Request {i+1}: Making request...")
        # In real scenario: time.sleep(1)  # 1 second delay
        print(f"    Request {i+1}: Completed")
    
    print("\n  Ethical Guidelines:")
    print("  - Don't overload servers")
    print("  - Respect robots.txt")
    print("  - Use APIs when available")
    print("  - Don't scrape personal data")
    print("  - Follow terms of service")

demonstrate_rate_limiting()

# =============================================================================
# 9. DATA STORAGE AND PROCESSING
# =============================================================================

print("\n💾 DATA STORAGE AND PROCESSING")
print("-" * 35)

def demonstrate_data_processing():
    """Demonstrate data processing and storage."""
    print("Data Processing and Storage:")
    
    # Simulate scraped data
    scraped_data = [
        {"title": "Python Tutorial", "url": "https://example.com/python", "date": "2024-01-15"},
        {"title": "Web Scraping Guide", "url": "https://example.com/scraping", "date": "2024-01-14"},
        {"title": "Data Analysis", "url": "https://example.com/data", "date": "2024-01-13"}
    ]
    
    print("  Scraped Data:")
    for item in scraped_data:
        print(f"    {item['title']} - {item['date']}")
    
    # Save to JSON
    print("\n  Saving to JSON:")
    with open('scraped_data.json', 'w') as f:
        json.dump(scraped_data, f, indent=2)
    print("    Data saved to scraped_data.json")
    
    # Load from JSON
    print("\n  Loading from JSON:")
    with open('scraped_data.json', 'r') as f:
        loaded_data = json.load(f)
    print(f"    Loaded {len(loaded_data)} items")

demonstrate_data_processing()

# =============================================================================
# 10. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice web scraping and APIs:

Exercise 1: Build a News Aggregator
- Scrape headlines from news websites
- Extract article titles, links, and dates
- Save data to JSON or CSV
- Handle different website structures

Exercise 2: Create a Price Monitor
- Scrape product prices from e-commerce sites
- Track price changes over time
- Send alerts for price drops
- Handle different price formats

Exercise 3: Build a Weather App
- Use weather APIs (OpenWeatherMap, etc.)
- Display current weather and forecasts
- Handle API rate limits
- Implement error handling

Exercise 4: Create a Job Scraper
- Scrape job postings from job boards
- Extract job titles, companies, locations
- Filter by keywords and location
- Save results to database

Exercise 5: Build a Social Media Monitor
- Use social media APIs (Twitter, Reddit)
- Monitor mentions of specific keywords
- Analyze sentiment and engagement
- Generate reports
""")

# =============================================================================
# 11. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
Web scraping and API best practices:

1. Respect robots.txt
   ✅ Check robots.txt before scraping
   ❌ Ignore website policies

2. Implement rate limiting
   ✅ Add delays between requests
   ❌ Make requests as fast as possible

3. Handle errors gracefully
   ✅ Use try-except blocks
   ❌ Let errors crash your program

4. Use appropriate headers
   ✅ Set User-Agent and other headers
   ❌ Use default headers only

5. Cache responses when possible
   ✅ Store data to avoid re-scraping
   ❌ Scrape the same data repeatedly

6. Use APIs when available
   ✅ Prefer official APIs over scraping
   ❌ Scrape when APIs are available

7. Test with small datasets first
   ✅ Start with limited requests
   ❌ Scrape entire websites immediately

8. Monitor your scraping
   ✅ Log requests and responses
   ❌ Scrape without monitoring
""")

# =============================================================================
# 12. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common web scraping mistakes:

1. Not handling dynamic content
   ❌ Only parsing static HTML
   ✅ Use Selenium or similar tools for JS content

2. Ignoring rate limits
   ❌ Making requests too quickly
   ✅ Implement proper delays

3. Not handling errors
   ❌ Assuming all requests succeed
   ✅ Handle timeouts, connection errors

4. Using outdated selectors
   ❌ Hard-coded CSS selectors
   ✅ Use robust, flexible selectors

5. Not respecting robots.txt
   ❌ Ignoring website policies
   ✅ Check and respect robots.txt

6. Not handling authentication
   ❌ Ignoring login requirements
   ✅ Implement proper authentication

7. Not monitoring changes
   ❌ Not updating scrapers
   ✅ Monitor and update selectors
""")

# =============================================================================
# 13. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ How to make HTTP requests with Python
✅ HTML parsing with BeautifulSoup
✅ Working with REST APIs and JSON
✅ Handling dynamic content and errors
✅ Rate limiting and ethical scraping
✅ Data processing and storage
✅ Best practices for web scraping

Next Steps:
- Day 13: Data Analysis with Pandas
- Day 14: Web Development with Flask
- Day 15: Testing and Debugging
- Day 16: Deployment and Production
""")

# =============================================================================
# 14. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 12 of your Python journey!

You now understand:
- How to extract data from websites
- How to work with REST APIs
- How to handle dynamic content
- How to scrape ethically and responsibly
- How to process and store scraped data

Web scraping and APIs are powerful tools for data collection!
Practice with the exercises to master these essential skills.

Happy coding! 🐍✨
""")

# Clean up created files
import os
if os.path.exists('scraped_data.json'):
    os.remove('scraped_data.json')
    print("🧹 Cleaned up scraped_data.json")

# Run the tutorial
if __name__ == "__main__":
    print("Day 12: Web Scraping and APIs Tutorial")
    print("Run this file to see all examples in action!")
