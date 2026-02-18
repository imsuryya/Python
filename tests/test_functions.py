import pytest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(5, 0) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_default_parameters():
    assert greet("John") == "Hello, John!"
    assert greet("Jane", "Hi") == "Hi, Jane!"

def test_lambda_function():
    square = lambda x: x ** 2
    assert square(4) == 16
    assert square(5) == 25

def test_map_function():
    numbers = [1, 2, 3, 4]
    squared = list(map(lambda x: x**2, numbers))
    assert squared == [1, 4, 9, 16]

def test_filter_function():
    numbers = [1, 2, 3, 4, 5, 6]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    assert evens == [2, 4, 6]
