import pytest

def check_positive_negative(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

def check_even_odd(num):
    return "even" if num % 2 == 0 else "odd"

def grade_calculator(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def test_positive_number():
    assert check_positive_negative(5) == "positive"

def test_negative_number():
    assert check_positive_negative(-3) == "negative"

def test_zero():
    assert check_positive_negative(0) == "zero"

def test_even_number():
    assert check_even_odd(4) == "even"
    assert check_even_odd(10) == "even"

def test_odd_number():
    assert check_even_odd(3) == "odd"
    assert check_even_odd(7) == "odd"

def test_grade_a():
    assert grade_calculator(95) == "A"
    assert grade_calculator(90) == "A"

def test_grade_b():
    assert grade_calculator(85) == "B"
    assert grade_calculator(80) == "B"

def test_grade_c():
    assert grade_calculator(75) == "C"

def test_grade_d():
    assert grade_calculator(65) == "D"

def test_grade_f():
    assert grade_calculator(50) == "F"

def test_nested_conditions():
    def categorize_age(age):
        if age < 0:
            return "invalid"
        elif age < 13:
            return "child"
        elif age < 20:
            return "teenager"
        else:
            return "adult"
    
    assert categorize_age(10) == "child"
    assert categorize_age(15) == "teenager"
    assert categorize_age(25) == "adult"
