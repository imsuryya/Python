import pytest

def number_generator(n):
    for i in range(n):
        yield i

def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

def even_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

def test_basic_generator():
    gen = number_generator(5)
    result = list(gen)
    assert result == [0, 1, 2, 3, 4]

def test_fibonacci_generator():
    gen = fibonacci_generator(7)
    result = list(gen)
    assert result == [0, 1, 1, 2, 3, 5, 8]

def test_even_numbers_generator():
    gen = even_numbers(1, 10)
    result = list(gen)
    assert result == [2, 4, 6, 8, 10]

def test_generator_with_next():
    gen = number_generator(3)
    assert next(gen) == 0
    assert next(gen) == 1
    assert next(gen) == 2

def test_generator_expression():
    squares = (x**2 for x in range(1, 6))
    result = list(squares)
    assert result == [1, 4, 9, 16, 25]

def test_generator_is_lazy():
    def counting_generator():
        count = 0
        while count < 3:
            yield count
            count += 1
    
    gen = counting_generator()
    assert next(gen) == 0
    assert next(gen) == 1
    assert next(gen) == 2
    
    with pytest.raises(StopIteration):
        next(gen)

def test_generator_with_filter():
    def all_numbers(n):
        for i in range(n):
            yield i
    
    gen = all_numbers(10)
    result = [x for x in gen if x % 2 == 0]
    assert result == [0, 2, 4, 6, 8]
