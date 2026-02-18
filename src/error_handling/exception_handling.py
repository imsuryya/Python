print("=== Basic Exception Handling ===")

try:
    result = 100 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

try:
    students = ["Surya", "Priya", "Arjun"]
    print(students[5])
except IndexError:
    print("Error: Student index out of range!")

try:
    student_info = {"name": "Surya", "age": 25}
    print(student_info["grade"])
except KeyError as e:
    print(f"Error: Key {e} not found in student info!")

print("\n=== Multiple Exception Handling ===")

def calculate_percentage(marks, total):
    try:
        percentage = (marks / total) * 100
        return percentage
    except ZeroDivisionError:
        print("Error: Total marks cannot be zero!")
        return None
    except TypeError:
        print("Error: Marks must be numbers!")
        return None

print(f"Percentage: {calculate_percentage(85, 100)}")
print(f"Percentage: {calculate_percentage(85, 0)}")

print("\n=== Try-Except-Else-Finally ===")

def read_student_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    else:
        print("File read successfully!")
        return content
    finally:
        print("Cleaning up resources...")
        if 'file' in locals():
            file.close()

data = read_student_file("students.txt")

print("\n=== Custom Exceptions ===")

class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(
                f"{self.account_holder}'s account has insufficient balance: ₹{self.balance}"
            )
        self.balance -= amount
        print(f"Withdrawal successful! Remaining balance: ₹{self.balance}")

surya_account = BankAccount("Surya", 5000)

try:
    surya_account.withdraw(3000)
    surya_account.withdraw(3000)
except InsufficientBalanceError as e:
    print(f"Transaction failed: {e}")

print("\n=== Raising Exceptions ===")

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age > 150:
        raise ValueError("Age seems unrealistic!")
    else:
        print(f"Valid age: {age}")

try:
    validate_age(25)
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

print("\n=== Exception Information ===")

try:
    marks = int("ninety")
except ValueError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")

print("\nException handling examples completed!")
