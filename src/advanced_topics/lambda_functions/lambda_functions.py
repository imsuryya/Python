print("=== Basic Lambda Functions ===")

add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")

multiply = lambda x, y: x * y
print(f"5 * 3 = {multiply(5, 3)}")

square = lambda x: x ** 2
print(f"Square of 7: {square(7)}")

print("\n=== Lambda with Lists ===")

students = [
    {"name": "Surya", "marks": 95},
    {"name": "Priya", "marks": 88},
    {"name": "Arjun", "marks": 92},
    {"name": "Ravi", "marks": 85}
]

students_sorted = sorted(students, key=lambda s: s["marks"], reverse=True)
print("Students sorted by marks:")
for student in students_sorted:
    print(f"{student['name']}: {student['marks']}")

print("\n=== Lambda with Conditional ===")

grade = lambda marks: "Pass" if marks >= 40 else "Fail"
print(f"Marks 75: {grade(75)}")
print(f"Marks 35: {grade(35)}")

max_of_two = lambda a, b: a if a > b else b
print(f"Max of 10 and 20: {max_of_two(10, 20)}")

print("\n=== Lambda with Multiple Arguments ===")

calculate_percentage = lambda marks, total: (marks / total) * 100
print(f"Percentage: {calculate_percentage(85, 100):.2f}%")

full_name = lambda first, last: f"{first} {last}"
print(f"Full name: {full_name('Surya', 'Kumar')}")

print("\n=== Lambda in Function ===")

def apply_operation(x, y, operation):
    return operation(x, y)

result = apply_operation(10, 5, lambda a, b: a + b)
print(f"Addition: {result}")

result = apply_operation(10, 5, lambda a, b: a - b)
print(f"Subtraction: {result}")

print("\n=== Lambda with Strings ===")

uppercase = lambda text: text.upper()
print(f"Uppercase: {uppercase('python programming')}")

reverse = lambda text: text[::-1]
print(f"Reverse: {reverse('Surya')}")

char_count = lambda text: len(text)
print(f"Character count: {char_count('Hello World')}")

print("\n=== Practical Lambda Examples ===")

products = [
    {"name": "Laptop", "price": 45000},
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 1500},
    {"name": "Monitor", "price": 12000}
]

expensive_products = list(filter(lambda p: p["price"] > 5000, products))
print("\nExpensive products (>5000):")
for product in expensive_products:
    print(f"{product['name']}: ₹{product['price']}")

discounted_prices = list(map(lambda p: {"name": p["name"], "price": p["price"] * 0.9}, products))
print("\nAfter 10% discount:")
for product in discounted_prices:
    print(f"{product['name']}: ₹{product['price']:.2f}")

print("\nLambda function examples completed!")
