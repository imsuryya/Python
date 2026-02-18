from functools import reduce

print("=== Map Function ===")

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Numbers: {numbers}")
print(f"Squared: {squared}")

marks = [85, 92, 78, 95, 88]
grades = list(map(lambda m: "A" if m >= 90 else "B" if m >= 80 else "C", marks))
print(f"\nMarks: {marks}")
print(f"Grades: {grades}")

names = ["surya", "priya", "arjun"]
capitalized = list(map(str.capitalize, names))
print(f"\nNames: {names}")
print(f"Capitalized: {capitalized}")

print("\n=== Filter Function ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Numbers: {numbers}")
print(f"Even numbers: {even_numbers}")

students = [
    {"name": "Surya", "marks": 95},
    {"name": "Priya", "marks": 88},
    {"name": "Arjun", "marks": 92},
    {"name": "Ravi", "marks": 75},
    {"name": "Meera", "marks": 98}
]

top_students = list(filter(lambda s: s["marks"] >= 90, students))
print(f"\nTop students (marks >= 90):")
for student in top_students:
    print(f"{student['name']}: {student['marks']}")

print("\n=== Reduce Function ===")

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(f"Numbers: {numbers}")
print(f"Sum: {total}")

numbers = [2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(f"\nNumbers: {numbers}")
print(f"Product: {product}")

numbers = [45, 23, 78, 12, 56]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"\nNumbers: {numbers}")
print(f"Maximum: {maximum}")

print("\n=== Combining Map, Filter, Reduce ===")

sales = [1200, 3500, 800, 4500, 2000, 5500]

high_sales = filter(lambda x: x > 2000, sales)
discounted = map(lambda x: x * 0.9, high_sales)
total_revenue = reduce(lambda x, y: x + y, discounted)

print(f"Sales: {sales}")
print(f"Total revenue (high sales with 10% discount): ₹{total_revenue:.2f}")

print("\n=== Practical Example: Student Data Processing ===")

students = [
    {"name": "Surya", "marks": [85, 90, 88]},
    {"name": "Priya", "marks": [92, 88, 95]},
    {"name": "Arjun", "marks": [78, 82, 80]},
    {"name": "Meera", "marks": [95, 98, 93]}
]

def calculate_average(student):
    avg = sum(student["marks"]) / len(student["marks"])
    return {"name": student["name"], "average": avg}

averages = list(map(calculate_average, students))
print("\nStudent averages:")
for student in averages:
    print(f"{student['name']}: {student['average']:.2f}")

high_performers = list(filter(lambda s: s["average"] >= 90, averages))
print("\nHigh performers (avg >= 90):")
for student in high_performers:
    print(f"{student['name']}: {student['average']:.2f}")

print("\n=== Custom Higher Order Function ===")

def apply_discount(discount_percent):
    return lambda price: price * (1 - discount_percent / 100)

discount_10 = apply_discount(10)
discount_20 = apply_discount(20)

price = 5000
print(f"\nOriginal price: ₹{price}")
print(f"After 10% discount: ₹{discount_10(price)}")
print(f"After 20% discount: ₹{discount_20(price)}")

print("\nHigher order function examples completed!")
