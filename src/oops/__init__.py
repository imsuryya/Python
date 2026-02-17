# OOP Concepts Package
# This package contains examples of all Object-Oriented Programming concepts in Python

"""
OOP Concepts covered in this package:

1. classes_and_objects.py - Basic class structure, objects, constructors, methods
2. inheritance.py - Single, Multiple, Multilevel inheritance, MRO
3. polymorphism.py - Method overriding, operator overloading, duck typing
4. encapsulation.py - Access modifiers, properties, data hiding
5. abstraction.py - Abstract classes, interfaces, protocols
6. magic_methods.py - Dunder methods (__init__, __str__, __add__, etc.)
7. decorators_and_descriptors.py - @property, @classmethod, @staticmethod, descriptors
8. composition_aggregation.py - Composition vs aggregation, dependency injection, mixins
"""

from .classes_and_objects import Car
from .inheritance import Animal, Dog, Cat
from .polymorphism import Shape, Rectangle, Circle
from .encapsulation import BankAccount
from .abstraction import Database

__all__ = [
    'Car',
    'Animal', 'Dog', 'Cat',
    'Shape', 'Rectangle', 'Circle',
    'BankAccount',
    'Database'
]
