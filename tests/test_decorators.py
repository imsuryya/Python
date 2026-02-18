import pytest
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result
    return wrapper

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def test_basic_decorator():
    @timer_decorator
    def add(a, b):
        return a + b
    
    result = add(5, 3)
    assert result == 8

def test_uppercase_decorator():
    @uppercase_decorator
    def greet(name):
        return f"hello, {name}"
    
    result = greet("surya")
    assert result == "HELLO, SURYA"

def test_multiple_decorators():
    def exclaim(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + "!"
        return wrapper
    
    @exclaim
    @uppercase_decorator
    def greet(name):
        return f"hi {name}"
    
    result = greet("priya")
    assert result == "HI PRIYA!"

def test_decorator_with_arguments():
    def repeat(times):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = []
                for _ in range(times):
                    result.append(func(*args, **kwargs))
                return result
            return wrapper
        return decorator
    
    @repeat(3)
    def get_name():
        return "Surya"
    
    result = get_name()
    assert len(result) == 3
    assert all(name == "Surya" for name in result)

def test_decorator_preserves_function():
    @timer_decorator
    def multiply(x, y):
        return x * y
    
    assert multiply(4, 5) == 20
    assert multiply(10, 2) == 20
