import pytest

def test_zero_division_exception():
    with pytest.raises(ZeroDivisionError):
        result = 100 / 0

def test_index_error():
    students = ["Surya", "Priya", "Arjun"]
    with pytest.raises(IndexError):
        student = students[10]

def test_key_error():
    student_info = {"name": "Surya", "age": 25}
    with pytest.raises(KeyError):
        grade = student_info["grade"]

def test_value_error():
    with pytest.raises(ValueError):
        number = int("abc")

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        with open("nonexistent_file_12345.txt", "r") as file:
            file.read()

def test_exception_message():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("Age cannot be negative")
    
    assert "Age cannot be negative" in str(exc_info.value)

def test_custom_exception():
    class InsufficientBalanceError(Exception):
        pass
    
    with pytest.raises(InsufficientBalanceError):
        raise InsufficientBalanceError("Insufficient balance")

def test_try_except_basic():
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return None
    
    assert divide(10, 2) == 5.0
    assert divide(10, 0) is None

def test_multiple_exceptions():
    def process_marks(marks_str):
        try:
            marks = int(marks_str)
            percentage = marks / 100
            return percentage
        except (ValueError, ZeroDivisionError):
            return None
    
    assert process_marks("85") == 0.85
    assert process_marks("abc") is None

def test_exception_with_else():
    def safe_divide(a, b):
        result = None
        success = False
        try:
            result = a / b
        except ZeroDivisionError:
            success = False
        else:
            success = True
        return result, success
    
    value, success = safe_divide(10, 2)
    assert value == 5.0
    assert success == True
    
    value, success = safe_divide(10, 0)
    assert value is None
    assert success == False

def test_exception_with_finally():
    executed_finally = []
    
    def test_function():
        try:
            raise ValueError("Test")
        except ValueError:
            pass
        finally:
            executed_finally.append(True)
    
    test_function()
    assert len(executed_finally) == 1

def test_raise_exception():
    def validate_age(age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        return True
    
    assert validate_age(25) == True
    with pytest.raises(ValueError):
        validate_age(-5)

def test_exception_info():
    try:
        raise ValueError("Test error")
    except ValueError as e:
        assert type(e).__name__ == "ValueError"
        assert str(e) == "Test error"
