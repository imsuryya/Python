# Decorators and Descriptors in OOP
# Advanced Python OOP concepts

# ============ CLASS DECORATORS ============

class staticmethod_example:
    """Demo: staticmethod doesn't need instance or class"""
    
    @staticmethod
    def greet(name):
        return f"Hello, {name}!"
    
    @staticmethod
    def add(a, b):
        return a + b


class classmethod_example:
    """Demo: classmethod receives class as first argument"""
    
    count = 0
    
    def __init__(self, name):
        self.name = name
        classmethod_example.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @classmethod
    def create_anonymous(cls):
        """Factory method using classmethod"""
        return cls("Anonymous")


class property_example:
    """Demo: property decorator for getters/setters"""
    
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Read-only computed property"""
        return self._celsius * 9/5 + 32
    
    @property
    def kelvin(self):
        """Read-only computed property"""
        return self._celsius + 273.15


# ============ CUSTOM DECORATORS ============

def singleton(cls):
    """Singleton decorator - ensures only one instance exists"""
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


@singleton
class DatabaseConnection:
    """Only one instance will ever exist"""
    
    def __init__(self):
        self.connection_id = id(self)
        print(f"Creating connection: {self.connection_id}")


def validate_types(**type_hints):
    """Decorator to validate argument types"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Validate positional args
            func_params = func.__code__.co_varnames[:func.__code__.co_argcount]
            for i, (param, arg) in enumerate(zip(func_params, args)):
                if param in type_hints and not isinstance(arg, type_hints[param]):
                    raise TypeError(f"Argument '{param}' must be {type_hints[param].__name__}")
            # Validate keyword args
            for key, value in kwargs.items():
                if key in type_hints and not isinstance(value, type_hints[key]):
                    raise TypeError(f"Argument '{key}' must be {type_hints[key].__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


class Calculator:
    @validate_types(a=(int, float), b=(int, float))
    def add(self, a, b):
        return a + b


# ============ DESCRIPTORS ============

class Validator:
    """Base descriptor for validation"""
    
    def __set_name__(self, owner, name):
        self.name = name
        self.private_name = f"_{name}"
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)
    
    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)
    
    def validate(self, value):
        pass  # Override in subclasses


class String(Validator):
    """Descriptor for string validation"""
    
    def __init__(self, min_length=0, max_length=None):
        self.min_length = min_length
        self.max_length = max_length
    
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string")
        if len(value) < self.min_length:
            raise ValueError(f"{self.name} must be at least {self.min_length} characters")
        if self.max_length and len(value) > self.max_length:
            raise ValueError(f"{self.name} must be at most {self.max_length} characters")


class Number(Validator):
    """Descriptor for number validation"""
    
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
    
    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} must be a number")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be at least {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be at most {self.max_value}")


class Person:
    """Class using descriptors for validation"""
    
    name = String(min_length=1, max_length=50)
    age = Number(min_value=0, max_value=150)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"


# ============ DATA CLASS (Python 3.7+) ============

from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:
    """Automatic __init__, __repr__, __eq__, etc."""
    name: str
    price: float
    quantity: int = 0
    tags: List[str] = field(default_factory=list)
    
    @property
    def total_value(self):
        return self.price * self.quantity


@dataclass(frozen=True)
class ImmutablePoint:
    """Immutable dataclass (frozen=True)"""
    x: float
    y: float


@dataclass(order=True)
class Student:
    """Orderable dataclass"""
    sort_index: float = field(init=False, repr=False)
    name: str
    grade: float
    
    def __post_init__(self):
        self.sort_index = self.grade


if __name__ == "__main__":
    # Static and Class methods
    print("=== Static and Class Methods ===")
    print(staticmethod_example.greet("World"))
    print(staticmethod_example.add(5, 3))
    
    obj1 = classmethod_example("First")
    obj2 = classmethod_example("Second")
    print(f"Count: {classmethod_example.get_count()}")
    
    anon = classmethod_example.create_anonymous()
    print(f"Anonymous: {anon.name}")
    
    # Property decorator
    print("\n=== Property Decorator ===")
    temp = property_example(25)
    print(f"Celsius: {temp.celsius}")
    print(f"Fahrenheit: {temp.fahrenheit}")
    print(f"Kelvin: {temp.kelvin}")
    
    temp.celsius = 30
    print(f"Updated Fahrenheit: {temp.fahrenheit}")
    
    # Singleton
    print("\n=== Singleton Pattern ===")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"db1 is db2: {db1 is db2}")
    
    # Type validation decorator
    print("\n=== Type Validation Decorator ===")
    calc = Calculator()
    print(f"add(5, 3): {calc.add(5, 3)}")
    
    # Descriptors
    print("\n=== Descriptors ===")
    person = Person("Alice", 30)
    print(person)
    
    try:
        person.age = -5
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Data classes
    print("\n=== Data Classes ===")
    product = Product("Laptop", 999.99, 5, ["electronics", "computers"])
    print(product)
    print(f"Total value: ${product.total_value}")
    
    # Immutable point
    point = ImmutablePoint(3.0, 4.0)
    print(f"Point: {point}")
    
    # Orderable students
    students = [
        Student("Alice", 85.5),
        Student("Bob", 92.0),
        Student("Charlie", 78.3)
    ]
    print("\nSorted students by grade:")
    for s in sorted(students, reverse=True):
        print(f"  {s.name}: {s.grade}")
