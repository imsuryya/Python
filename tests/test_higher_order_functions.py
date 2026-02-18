import pytest
from functools import reduce

def test_map_basic():
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    assert squared == [1, 4, 9, 16, 25]

def test_map_with_strings():
    names = ["surya", "priya", "arjun"]
    capitalized = list(map(str.capitalize, names))
    assert capitalized == ["Surya", "Priya", "Arjun"]

def test_map_multiple_lists():
    a = [1, 2, 3]
    b = [4, 5, 6]
    result = list(map(lambda x, y: x + y, a, b))
    assert result == [5, 7, 9]

def test_filter_basic():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    assert evens == [2, 4, 6, 8, 10]

def test_filter_with_condition():
    marks = [85, 92, 78, 95, 88, 65]
    high_marks = list(filter(lambda m: m >= 90, marks))
    assert high_marks == [92, 95]

def test_reduce_sum():
    numbers = [1, 2, 3, 4, 5]
    total = reduce(lambda x, y: x + y, numbers)
    assert total == 15

def test_reduce_product():
    numbers = [2, 3, 4]
    product = reduce(lambda x, y: x * y, numbers)
    assert product == 24

def test_reduce_max():
    numbers = [45, 23, 78, 12, 56]
    maximum = reduce(lambda x, y: x if x > y else y, numbers)
    assert maximum == 78

def test_reduce_with_initial():
    numbers = [1, 2, 3, 4]
    total = reduce(lambda x, y: x + y, numbers, 10)
    assert total == 20

def test_combining_map_filter():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
    assert result == [4, 16, 36, 64, 100]

def test_combining_all_three():
    numbers = [1, 2, 3, 4, 5]
    doubled = map(lambda x: x * 2, numbers)
    evens = filter(lambda x: x > 5, doubled)
    total = reduce(lambda x, y: x + y, evens)
    assert total == 18

def test_custom_higher_order_function():
    def apply_discount(discount_percent):
        return lambda price: price * (1 - discount_percent / 100)
    
    discount_10 = apply_discount(10)
    assert discount_10(1000) == 900
    
    discount_20 = apply_discount(20)
    assert discount_20(1000) == 800

def test_map_with_function_reference():
    numbers = [1, 4, 9, 16, 25]
    
    def square_root(n):
        return n ** 0.5
    
    result = list(map(square_root, numbers))
    assert result == [1.0, 2.0, 3.0, 4.0, 5.0]
