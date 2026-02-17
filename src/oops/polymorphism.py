# Polymorphism in Python
# Polymorphism allows objects of different classes to be treated as objects of a common base class

from abc import ABC, abstractmethod


# Method Overriding (Runtime Polymorphism)
class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c


# Method Overloading (using default arguments)
class Calculator:
    """Demonstrates method overloading using default arguments"""
    
    def add(self, a, b=0, c=0):
        return a + b + c
    
    # Using *args for variable number of arguments
    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result


# Operator Overloading
class Vector:
    """A 2D vector class with operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Subtraction
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # Multiplication (scalar)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # Equality
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # Length
    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    
    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Representation
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# Duck Typing - "If it walks like a duck and quacks like a duck, it's a duck"
class Duck:
    def speak(self):
        return "Quack!"
    
    def walk(self):
        return "Walking like a duck"


class Person:
    def speak(self):
        return "Hello!"
    
    def walk(self):
        return "Walking like a person"


def make_it_speak(entity):
    """Works with any object that has a speak method"""
    return entity.speak()


if __name__ == "__main__":
    # Polymorphism with shapes
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        Triangle(3, 4, 5)
    ]
    
    print("Shape Areas and Perimeters:")
    for shape in shapes:
        print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")
    
    # Method overloading
    calc = Calculator()
    print(f"\nCalculator:")
    print(f"add(5) = {calc.add(5)}")
    print(f"add(5, 3) = {calc.add(5, 3)}")
    print(f"add(5, 3, 2) = {calc.add(5, 3, 2)}")
    print(f"multiply(2, 3, 4) = {calc.multiply(2, 3, 4)}")
    
    # Operator overloading
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    print(f"\nVector Operations:")
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3 = {v1 * 3}")
    
    # Duck typing
    duck = Duck()
    person = Person()
    print(f"\nDuck Typing:")
    print(f"Duck speaks: {make_it_speak(duck)}")
    print(f"Person speaks: {make_it_speak(person)}")
