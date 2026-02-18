import pytest

def test_basic_for_loop():
    result = []
    for i in range(5):
        result.append(i)
    assert result == [0, 1, 2, 3, 4]

def test_for_loop_with_list():
    fruits = ["apple", "banana", "cherry"]
    count = 0
    for fruit in fruits:
        count += 1
    assert count == 3

def test_for_range_with_step():
    result = []
    for i in range(0, 10, 2):
        result.append(i)
    assert result == [0, 2, 4, 6, 8]

def test_enumerate():
    fruits = ["apple", "banana"]
    indices = []
    for idx, fruit in enumerate(fruits):
        indices.append(idx)
    assert indices == [0, 1]

def test_nested_for_loop():
    result = []
    for i in range(2):
        for j in range(2):
            result.append((i, j))
    assert len(result) == 4

def test_basic_while_loop():
    count = 0
    result = []
    while count < 5:
        result.append(count)
        count += 1
    assert result == [0, 1, 2, 3, 4]

def test_while_with_break():
    count = 0
    while True:
        count += 1
        if count == 5:
            break
    assert count == 5

def test_while_with_continue():
    count = 0
    result = []
    while count < 10:
        count += 1
        if count % 2 == 0:
            continue
        result.append(count)
    assert result == [1, 3, 5, 7, 9]
