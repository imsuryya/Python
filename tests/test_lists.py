import pytest

@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def fruits():
    return ["apple", "banana", "cherry"]

def test_append(numbers):
    numbers.append(6)
    assert numbers[-1] == 6
    assert len(numbers) == 6

def test_insert(numbers):
    numbers.insert(0, 0)
    assert numbers[0] == 0
    assert len(numbers) == 6

def test_remove(numbers):
    numbers.remove(3)
    assert 3 not in numbers
    assert len(numbers) == 4

def test_pop(numbers):
    popped = numbers.pop()
    assert popped == 5
    assert len(numbers) == 4

def test_indexing(numbers):
    assert numbers[0] == 1
    assert numbers[-1] == 5

def test_slicing(numbers):
    sliced = numbers[1:3]
    assert sliced == [2, 3]

def test_extend(numbers):
    numbers.extend([6, 7])
    assert len(numbers) == 7
    assert 6 in numbers

def test_sort():
    unsorted = [5, 2, 8, 1, 9]
    unsorted.sort()
    assert unsorted == [1, 2, 5, 8, 9]

def test_reverse(numbers):
    numbers.reverse()
    assert numbers == [5, 4, 3, 2, 1]

def test_count():
    numbers = [1, 2, 2, 3, 2, 4]
    assert numbers.count(2) == 3

def test_list_comprehension():
    squared = [x**2 for x in range(1, 6)]
    assert squared == [1, 4, 9, 16, 25]

def test_list_comprehension_with_condition():
    evens = [x for x in range(1, 11) if x % 2 == 0]
    assert evens == [2, 4, 6, 8, 10]
