import pytest

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

def test_object_creation():
    dog = Dog("Buddy", 3)
    assert dog.name == "Buddy"
    assert dog.age == 3

def test_method_call():
    dog = Dog("Max", 5)
    assert dog.bark() == "Max says Woof!"

def test_multiple_objects():
    dog1 = Dog("Rex", 2)
    dog2 = Dog("Spot", 4)
    assert dog1.name != dog2.name

def test_encapsulation():
    account = BankAccount(100)
    assert account.get_balance() == 100

def test_deposit():
    account = BankAccount(50)
    account.deposit(100)
    assert account.get_balance() == 150

def test_invalid_deposit():
    account = BankAccount(100)
    result = account.deposit(-50)
    assert result == False
    assert account.get_balance() == 100

def test_inheritance():
    cat = Cat("Whiskers")
    assert cat.name == "Whiskers"

def test_method_override():
    cat = Cat("Fluffy")
    assert cat.speak() == "Meow"

def test_parent_method():
    animal = Animal("Unknown")
    assert animal.speak() == "Some sound"

def test_polymorphism():
    animals = [Cat("Tom"), Animal("Jerry")]
    sounds = [animal.speak() for animal in animals]
    assert sounds[0] == "Meow"
    assert sounds[1] == "Some sound"
