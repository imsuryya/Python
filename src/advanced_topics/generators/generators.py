print("=== Basic Generator ===")

def number_generator(n):
    for i in range(n):
        yield i

gen = number_generator(5)
for num in gen:
    print(f"Generated: {num}")

print("\n=== Student Marks Generator ===")

def student_marks_generator(students):
    for student in students:
        yield f"{student['name']}: {student['marks']}"

students = [
    {"name": "Surya", "marks": 95},
    {"name": "Priya", "marks": 88},
    {"name": "Arjun", "marks": 92}
]

for result in student_marks_generator(students):
    print(result)

print("\n=== Fibonacci Generator ===")

def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

print("First 10 Fibonacci numbers:")
for fib in fibonacci_generator(10):
    print(fib, end=" ")
print()

print("\n=== File Reader Generator ===")

def read_large_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        yield "File not found"

with open("temp_students.txt", "w") as f:
    f.write("Surya\nPriya\nArjun\nRavi\nMeera\n")

print("\nReading students from file:")
for student in read_large_file("temp_students.txt"):
    print(f"Student: {student}")

import os
if os.path.exists("temp_students.txt"):
    os.remove("temp_students.txt")

print("\n=== Even Numbers Generator ===")

def even_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

print("\nEven numbers from 1 to 20:")
print(list(even_numbers(1, 20)))

print("\n=== Generator Expression ===")

squares = (x**2 for x in range(1, 6))
print("Squares:", list(squares))

marks = [85, 92, 78, 95, 88]
high_marks = (mark for mark in marks if mark >= 90)
print("High marks:", list(high_marks))

print("\n=== Infinite Generator ===")

def counter_generator(start=0):
    count = start
    while True:
        yield count
        count += 1

counter = counter_generator(1)
print("\nFirst 5 counts:")
for _ in range(5):
    print(next(counter), end=" ")
print()

print("\n=== Generator with Send ===")

def average_generator():
    total = 0
    count = 0
    average = 0
    while True:
        value = yield average
        if value is None:
            break
        total += value
        count += 1
        average = total / count

avg_gen = average_generator()
next(avg_gen)
print(f"\nAverage after 85: {avg_gen.send(85)}")
print(f"Average after 92: {avg_gen.send(92)}")
print(f"Average after 78: {avg_gen.send(78)}")

print("\nGenerator examples completed!")
