import pytest

@pytest.fixture
def fruits():
    return {"apple", "banana", "cherry"}

@pytest.fixture
def numbers():
    return {1, 2, 3, 4, 5}

def test_add(fruits):
    fruits.add("orange")
    assert "orange" in fruits

def test_duplicate_prevention(numbers):
    initial_len = len(numbers)
    numbers.add(3)
    assert len(numbers) == initial_len

def test_remove(fruits):
    fruits.remove("banana")
    assert "banana" not in fruits

def test_discard(fruits):
    fruits.discard("cherry")
    assert "cherry" not in fruits
    fruits.discard("nonexistent")

def test_length(numbers):
    assert len(numbers) == 5

def test_in_operator(numbers):
    assert 3 in numbers
    assert 10 not in numbers

def test_union():
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    union = set_a | set_b
    assert union == {1, 2, 3, 4, 5}

def test_intersection():
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    intersection = set_a & set_b
    assert intersection == {3, 4}

def test_difference():
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    diff = set_a - set_b
    assert diff == {1, 2}

def test_symmetric_difference():
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    sym_diff = set_a ^ set_b
    assert sym_diff == {1, 2, 4, 5}

def test_subset():
    set_a = {1, 2, 3}
    set_b = {1, 2, 3, 4, 5}
    assert set_a.issubset(set_b)

def test_superset():
    set_a = {1, 2, 3, 4, 5}
    set_b = {1, 2, 3}
    assert set_a.issuperset(set_b)

def test_set_comprehension():
    squared = {x**2 for x in range(1, 6)}
    assert squared == {1, 4, 9, 16, 25}
