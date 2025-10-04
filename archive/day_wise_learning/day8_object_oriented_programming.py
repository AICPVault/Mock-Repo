"""
Day 8: Object-Oriented Programming (OOP)
========================================

Today we'll learn about Object-Oriented Programming in Python - one of the most
important programming paradigms. We'll explore classes, objects, inheritance,
polymorphism, and encapsulation.

Learning Objectives:
- Understand the principles of OOP
- Learn about classes and objects
- Master inheritance and polymorphism
- Explore encapsulation and abstraction
- Practice creating robust class hierarchies
- Build real-world applications using OOP

Let's dive into Object-Oriented Programming!
"""

print("🐍 Welcome to Day 8: Object-Oriented Programming (OOP)!")
print("=" * 60)

# =============================================================================
# 1. WHAT IS OBJECT-ORIENTED PROGRAMMING?
# =============================================================================

print("\n🏗️ WHAT IS OBJECT-ORIENTED PROGRAMMING?")
print("-" * 40)

"""
Object-Oriented Programming (OOP) is a programming paradigm based on:

1. CLASSES: Blueprints for creating objects
2. OBJECTS: Instances of classes with data and behavior
3. ENCAPSULATION: Bundling data and methods together
4. INHERITANCE: Creating new classes based on existing ones
5. POLYMORPHISM: Same interface, different implementations
6. ABSTRACTION: Hiding complex implementation details

Benefits of OOP:
- Code reusability and modularity
- Better organization and structure
- Easier maintenance and debugging
- Real-world modeling capabilities
"""

# =============================================================================
# 2. CLASSES AND OBJECTS
# =============================================================================

print("\n🏗️ CLASSES AND OBJECTS")
print("-" * 25)

class Person:
    """A simple Person class to demonstrate basic OOP concepts."""
    
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    
    def __init__(self, name, age, city):
        """Constructor method - called when creating a new instance."""
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        self.city = city
        self.is_adult = age >= 18
    
    def introduce(self):
        """Instance method - behavior of the object."""
        return f"Hi! I'm {self.name}, {self.age} years old, from {self.city}."
    
    def have_birthday(self):
        """Method that modifies the object's state."""
        self.age += 1
        self.is_adult = self.age >= 18
        return f"{self.name} is now {self.age} years old!"
    
    def get_info(self):
        """Method that returns object information."""
        return {
            "name": self.name,
            "age": self.age,
            "city": self.city,
            "is_adult": self.is_adult,
            "species": self.species
        }

# Creating objects (instances) of the Person class
print("Creating Person objects:")
person1 = Person("Alice", 25, "New York")
person2 = Person("Bob", 17, "Los Angeles")

print(person1.introduce())
print(person2.introduce())

print(f"\nPerson1 info: {person1.get_info()}")
print(f"Person2 info: {person2.get_info()}")

# Modifying object state
print(f"\n{person2.have_birthday()}")
print(f"Updated Person2 info: {person2.get_info()}")

# =============================================================================
# 3. ENCAPSULATION
# =============================================================================

print("\n🔒 ENCAPSULATION")
print("-" * 18)

class BankAccount:
    """Demonstrate encapsulation with private attributes."""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self._balance = initial_balance  # Protected attribute (convention)
        self.__pin = "1234"  # Private attribute (name mangling)
        self._transaction_history = []
    
    def deposit(self, amount):
        """Public method to deposit money."""
        if amount > 0:
            self._balance += amount
            self._transaction_history.append(f"Deposited: ${amount}")
            return f"✅ Deposited ${amount}. New balance: ${self._balance}"
        else:
            return "❌ Invalid deposit amount"
    
    def withdraw(self, amount, pin):
        """Public method to withdraw money with PIN verification."""
        if pin != self.__pin:
            return "❌ Invalid PIN"
        
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self._transaction_history.append(f"Withdrew: ${amount}")
            return f"✅ Withdrew ${amount}. New balance: ${self._balance}"
        else:
            return "❌ Invalid withdrawal amount or insufficient funds"
    
    def get_balance(self):
        """Public method to get balance."""
        return f"Account {self.account_number} balance: ${self._balance}"
    
    def get_transaction_history(self):
        """Public method to get transaction history."""
        return self._transaction_history.copy()
    
    def change_pin(self, old_pin, new_pin):
        """Public method to change PIN."""
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "✅ PIN changed successfully"
        else:
            return "❌ Invalid old PIN"

# Demonstrate encapsulation
print("Bank Account with Encapsulation:")
account = BankAccount("12345", 1000)

print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200, "1234"))
print(account.withdraw(200, "0000"))  # Wrong PIN
print(account.get_balance())

print(f"\nTransaction History: {account.get_transaction_history()}")

# =============================================================================
# 4. INHERITANCE
# =============================================================================

print("\n👨‍👩‍👧‍👦 INHERITANCE")
print("-" * 20)

class Animal:
    """Base class for all animals."""
    
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_alive = True
    
    def speak(self):
        """Base speak method - to be overridden by subclasses."""
        return f"{self.name} makes a sound"
    
    def eat(self, food):
        """Common method for all animals."""
        return f"{self.name} is eating {food}"
    
    def sleep(self):
        """Common method for all animals."""
        return f"{self.name} is sleeping"
    
    def get_info(self):
        """Get animal information."""
        return f"{self.name} is a {self.age}-year-old {self.species}"

class Dog(Animal):
    """Dog class inheriting from Animal."""
    
    def __init__(self, name, age, breed):
        super().__init__(name, "Dog", age)  # Call parent constructor
        self.breed = breed
        self.tricks = []
    
    def speak(self):
        """Override parent's speak method."""
        return f"{self.name} barks: Woof! Woof!"
    
    def learn_trick(self, trick):
        """Dog-specific method."""
        self.tricks.append(trick)
        return f"{self.name} learned to {trick}!"
    
    def perform_tricks(self):
        """Dog-specific method."""
        if self.tricks:
            return f"{self.name} can: {', '.join(self.tricks)}"
        else:
            return f"{self.name} hasn't learned any tricks yet"

class Cat(Animal):
    """Cat class inheriting from Animal."""
    
    def __init__(self, name, age, color):
        super().__init__(name, "Cat", age)
        self.color = color
        self.lives = 9
    
    def speak(self):
        """Override parent's speak method."""
        return f"{self.name} meows: Meow! Meow!"
    
    def climb(self, height):
        """Cat-specific method."""
        return f"{self.name} climbed {height} feet high!"
    
    def lose_life(self):
        """Cat-specific method."""
        if self.lives > 0:
            self.lives -= 1
            return f"{self.name} has {self.lives} lives left"
        else:
            return f"{self.name} has no lives left"

# Demonstrate inheritance
print("Inheritance Example:")
dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Orange")

print(dog.get_info())
print(cat.get_info())

print(f"\n{dog.speak()}")
print(f"{cat.speak()}")

print(f"\n{dog.eat('dog food')}")
print(f"{cat.eat('cat food')}")

print(f"\n{dog.learn_trick('sit')}")
print(f"{dog.learn_trick('roll over')}")
print(dog.perform_tricks())

print(f"\n{cat.climb(10)}")
print(f"{cat.lose_life()}")

# =============================================================================
# 5. POLYMORPHISM
# =============================================================================

print("\n🔄 POLYMORPHISM")
print("-" * 18)

class Shape:
    """Base class for all shapes."""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """Abstract method - to be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement area()")
    
    def perimeter(self):
        """Abstract method - to be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement perimeter()")
    
    def describe(self):
        """Common method for all shapes."""
        return f"This is a {self.name}"

class Rectangle(Shape):
    """Rectangle class implementing Shape interface."""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate rectangle area."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle class implementing Shape interface."""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Calculate circle area."""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate circle perimeter (circumference)."""
        import math
        return 2 * math.pi * self.radius

class Triangle(Shape):
    """Triangle class implementing Shape interface."""
    
    def __init__(self, base, height, side1, side2):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def area(self):
        """Calculate triangle area."""
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        """Calculate triangle perimeter."""
        return self.base + self.side1 + self.side2

# Demonstrate polymorphism
def calculate_shape_info(shape):
    """Function that works with any Shape object (polymorphism)."""
    print(f"{shape.describe()}")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")

print("Polymorphism Example:")
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(6, 4, 5, 5)
]

for shape in shapes:
    calculate_shape_info(shape)
    print()

# =============================================================================
# 6. ADVANCED OOP CONCEPTS
# =============================================================================

print("\n🚀 ADVANCED OOP CONCEPTS")
print("-" * 30)

# Multiple Inheritance
class Flyable:
    """Mixin class for flying capability."""
    
    def fly(self):
        return f"{self.name} is flying!"

class Swimmable:
    """Mixin class for swimming capability."""
    
    def swim(self):
        return f"{self.name} is swimming!"

class Duck(Animal, Flyable, Swimmable):
    """Duck class with multiple inheritance."""
    
    def __init__(self, name, age):
        super().__init__(name, "Duck", age)
    
    def speak(self):
        return f"{self.name} quacks: Quack! Quack!"

# Demonstrate multiple inheritance
duck = Duck("Donald", 5)
print(f"Multiple Inheritance Example:")
print(duck.get_info())
print(duck.speak())
print(duck.fly())
print(duck.swim())

# Class methods and static methods
class MathUtils:
    """Class demonstrating class methods and static methods."""
    
    class_variable = "Math utilities"
    
    def __init__(self, value):
        self.value = value
    
    @classmethod
    def from_string(cls, string_value):
        """Class method - alternative constructor."""
        return cls(float(string_value))
    
    @staticmethod
    def add(a, b):
        """Static method - doesn't need class or instance."""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Static method - doesn't need class or instance."""
        return a * b
    
    def instance_method(self):
        """Instance method - needs instance."""
        return f"Value: {self.value}"

print(f"\nClass and Static Methods:")
# Using class method
math_obj = MathUtils.from_string("10.5")
print(math_obj.instance_method())

# Using static methods
print(f"Static add: {MathUtils.add(5, 3)}")
print(f"Static multiply: {MathUtils.multiply(4, 6)}")

# =============================================================================
# 7. PROPERTY DECORATORS
# =============================================================================

print("\n🏷️ PROPERTY DECORATORS")
print("-" * 25)

class Temperature:
    """Class demonstrating property decorators."""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius temperature."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius temperature with validation."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Property to get temperature in Fahrenheit."""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Property to set temperature from Fahrenheit."""
        self._celsius = (value - 32) * 5/9
    
    def __str__(self):
        return f"{self._celsius}°C ({self.fahrenheit}°F)"

# Demonstrate property decorators
print("Property Decorators Example:")
temp = Temperature(25)
print(f"Initial: {temp}")

temp.celsius = 30
print(f"After setting celsius to 30: {temp}")

temp.fahrenheit = 86
print(f"After setting fahrenheit to 86: {temp}")

try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")

# =============================================================================
# 8. PRACTICAL EXAMPLES
# =============================================================================

print("\n💼 PRACTICAL EXAMPLES")
print("-" * 22)

# Example 1: Library Management System
class Book:
    """Book class for library management."""
    
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.is_borrowed = False
        self.borrower = None
    
    def borrow(self, borrower_name):
        """Borrow the book."""
        if self.is_borrowed:
            return f"❌ Book is already borrowed by {self.borrower}"
        else:
            self.is_borrowed = True
            self.borrower = borrower_name
            return f"✅ Book '{self.title}' borrowed by {borrower_name}"
    
    def return_book(self):
        """Return the book."""
        if not self.is_borrowed:
            return f"❌ Book is not borrowed"
        else:
            borrower = self.borrower
            self.is_borrowed = False
            self.borrower = None
            return f"✅ Book '{self.title}' returned by {borrower}"
    
    def get_info(self):
        """Get book information."""
        status = f"Borrowed by {self.borrower}" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} ({self.year}) - {status}"

class Library:
    """Library class to manage books."""
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.borrowers = set()
    
    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        return f"✅ Added '{book.title}' to library"
    
    def find_book(self, title):
        """Find a book by title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def borrow_book(self, title, borrower_name):
        """Borrow a book from the library."""
        book = self.find_book(title)
        if book:
            self.borrowers.add(borrower_name)
            return book.borrow(borrower_name)
        else:
            return f"❌ Book '{title}' not found in library"
    
    def return_book(self, title):
        """Return a book to the library."""
        book = self.find_book(title)
        if book:
            return book.return_book()
        else:
            return f"❌ Book '{title}' not found in library"
    
    def list_books(self):
        """List all books in the library."""
        if not self.books:
            return "No books in library"
        
        book_list = []
        for book in self.books:
            book_list.append(book.get_info())
        return "\n".join(book_list)

# Demonstrate library management system
print("Library Management System:")
library = Library("Central Library")

# Add books
book1 = Book("Python Programming", "John Doe", "123456789", 2023)
book2 = Book("Data Structures", "Jane Smith", "987654321", 2022)

library.add_book(book1)
library.add_book(book2)

print(f"\nBooks in library:")
print(library.list_books())

# Borrow and return books
print(f"\n{library.borrow_book('Python Programming', 'Alice')}")
print(f"{library.borrow_book('Data Structures', 'Bob')}")
print(f"{library.borrow_book('Python Programming', 'Charlie')}")  # Already borrowed

print(f"\nBooks after borrowing:")
print(library.list_books())

print(f"\n{library.return_book('Python Programming')}")
print(f"\nBooks after return:")
print(library.list_books())

# =============================================================================
# 9. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice OOP concepts:

Exercise 1: Create a Student Management System
- Student class with name, ID, grades
- Methods to add grades, calculate average
- Class to manage multiple students

Exercise 2: Build a Vehicle Hierarchy
- Base Vehicle class
- Car, Truck, Motorcycle subclasses
- Different methods for each vehicle type
- Polymorphic behavior

Exercise 3: Design a Bank Account System
- Account class with balance, account number
- Savings and Checking account subclasses
- Different interest rates and fees
- Transaction history

Exercise 4: Create a Shape Calculator
- Base Shape class with abstract methods
- Rectangle, Circle, Triangle subclasses
- Calculate area and perimeter for each
- Use polymorphism to handle different shapes

Exercise 5: Build a Restaurant Management System
- MenuItem class for food items
- Order class to manage customer orders
- Restaurant class to manage everything
- Calculate totals and manage inventory
""")

# =============================================================================
# 10. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
OOP best practices:

1. Use meaningful class and method names
   ✅ class BankAccount:
   ❌ class BA:

2. Keep classes focused and cohesive
   ✅ One responsibility per class
   ❌ God classes that do everything

3. Use inheritance appropriately
   ✅ "is-a" relationship
   ❌ "has-a" relationship (use composition)

4. Prefer composition over inheritance
   ✅ class Car: def __init__(self): self.engine = Engine()
   ❌ class Car(Engine):  # If Car is not a type of Engine

5. Use private attributes when appropriate
   ✅ self._balance  # Protected
   ✅ self.__pin     # Private
   ❌ self.balance   # Public (if should be protected)

6. Document your classes and methods
   ✅ """Docstring for class"""
   ❌ # No documentation

7. Use properties for computed attributes
   ✅ @property def area(self): return self.width * self.height
   ❌ def get_area(self): return self.width * self.height

8. Follow the Single Responsibility Principle
   ✅ One class, one responsibility
   ❌ One class doing multiple unrelated things
""")

# =============================================================================
# 11. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common OOP mistakes and how to avoid them:

1. Overusing inheritance
   ❌ class Dog(Animal, Vehicle, Furniture):  # Dog is not a vehicle
   ✅ class Dog(Animal):  # Dog is an animal

2. Not using composition when appropriate
   ❌ class Car(Engine, Wheels, Seats):  # Car has these, not is these
   ✅ class Car: def __init__(self): self.engine = Engine()

3. Making everything public
   ❌ self.balance = 1000  # Should be protected
   ✅ self._balance = 1000  # Protected attribute

4. Not using super() in inheritance
   ❌ Animal.__init__(self, name)  # Hard to maintain
   ✅ super().__init__(name)  # Flexible and maintainable

5. Creating too many small classes
   ❌ class Name: class Age: class City:  # Over-engineering
   ✅ class Person: def __init__(self, name, age, city):

6. Not using abstract base classes
   ❌ class Shape: def area(self): pass  # No enforcement
   ✅ from abc import ABC, abstractmethod
       class Shape(ABC): @abstractmethod def area(self): pass

7. Ignoring the Liskov Substitution Principle
   ❌ Subclass that changes parent behavior
   ✅ Subclass that extends parent behavior
""")

# =============================================================================
# 12. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ Classes and objects - the foundation of OOP
✅ Encapsulation - data hiding and protection
✅ Inheritance - code reuse and hierarchy
✅ Polymorphism - same interface, different behavior
✅ Advanced concepts - multiple inheritance, properties
✅ Best practices for clean OOP code
✅ Common mistakes to avoid

Next Steps:
- Day 9: Modules and Packages
- Day 10: Advanced Data Structures
- Day 11: Regular Expressions
- Day 12: Working with APIs
""")

# =============================================================================
# 13. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 8 of your Python journey!

You now understand:
- How to design and implement classes
- The principles of object-oriented programming
- How to create robust class hierarchies
- Advanced OOP concepts and patterns
- Best practices for clean, maintainable code

Object-Oriented Programming is essential for building complex applications!
Practice with the exercises to master this powerful paradigm.

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 8: Object-Oriented Programming Tutorial")
    print("Run this file to see all examples in action!")
