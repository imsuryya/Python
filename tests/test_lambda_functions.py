import pytest

def test_basic_lambda():
    add = lambda x, y: x + y
    assert add(5, 3) == 8
    assert add(10, 20) == 30

def test_lambda_square():
    square = lambda x: x ** 2
    assert square(5) == 25
    assert square(10) == 100

def test_lambda_with_conditional():
    grade = lambda marks: "Pass" if marks >= 40 else "Fail"
    assert grade(75) == "Pass"
    assert grade(35) == "Fail"
    assert grade(40) == "Pass"

def test_lambda_with_strings():
    uppercase = lambda text: text.upper()
    assert uppercase("python") == "PYTHON"
    
    reverse = lambda text: text[::-1]
    assert reverse("surya") == "ayrus"

def test_lambda_with_sorted():
    students = [
        {"name": "Surya", "marks": 95},
        {"name": "Priya", "marks": 88},
        {"name": "Arjun", "marks": 92}
    ]
    
    sorted_students = sorted(students, key=lambda s: s["marks"])
    assert sorted_students[0]["name"] == "Priya"
    assert sorted_students[-1]["name"] == "Surya"

def test_lambda_in_function():
    def apply_operation(x, y, operation):
        return operation(x, y)
    
    result = apply_operation(10, 5, lambda a, b: a + b)
    assert result == 15
    
    result = apply_operation(10, 5, lambda a, b: a * b)
    assert result == 50

def test_lambda_max_of_two():
    max_of_two = lambda a, b: a if a > b else b
    assert max_of_two(10, 20) == 20
    assert max_of_two(50, 30) == 50

def test_lambda_multiple_arguments():
    calculate_percentage = lambda marks, total: (marks / total) * 100
    assert calculate_percentage(85, 100) == 85.0
    assert calculate_percentage(45, 50) == 90.0

def test_lambda_with_map():
    numbers = [1, 2, 3, 4, 5]
    doubled = list(map(lambda x: x * 2, numbers))
    assert doubled == [2, 4, 6, 8, 10]

def test_lambda_with_filter():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    assert evens == [2, 4, 6, 8, 10]
