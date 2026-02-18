file_path = "sample.txt"

with open(file_path, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Learning Python file handling.\n")

print("File written successfully")

with open(file_path, "r") as file:
    content = file.read()
    print("Full content:")
    print(content)

with open(file_path, "r") as file:
    first_line = file.readline()
    print("First line:", first_line.strip())

with open(file_path, "r") as file:
    lines = file.readlines()
    print("\nAll lines:")
    for line in lines:
        print(line.strip())

with open(file_path, "a") as file:
    file.write("Appended line 1\n")
    file.write("Appended line 2\n")

print("\nAfter appending:")
with open(file_path, "r") as file:
    print(file.read())

lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("multiple_lines.txt", "w") as file:
    file.writelines(lines_to_write)

with open("multiple_lines.txt", "r") as file:
    for i, line in enumerate(file, 1):
        print(f"Line {i}: {line.strip()}")

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("\nFile not found!")

import os

if os.path.exists(file_path):
    print(f"\n{file_path} exists")
    print(f"File size: {os.path.getsize(file_path)} bytes")

with open("binary_file.bin", "wb") as file:
    data = bytes([65, 66, 67, 68, 69])
    file.write(data)

with open("binary_file.bin", "rb") as file:
    binary_data = file.read()
    print(f"\nBinary data: {binary_data}")

data = {"name": "John", "age": 30, "city": "New York"}
with open("data.txt", "w") as file:
    for key, value in data.items():
        file.write(f"{key}: {value}\n")

with open("data.txt", "r") as file:
    print("\nData from file:")
    print(file.read())

with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{i}\n")

with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]
    print(f"\nNumbers: {numbers}")
    print(f"Sum: {sum(numbers)}")

file = open("manual_close.txt", "w")
file.write("This file is manually closed\n")
file.close()

with open("position_demo.txt", "w") as file:
    file.write("0123456789")

with open("position_demo.txt", "r") as file:
    print(f"\nCurrent position: {file.tell()}")
    file.read(5)
    print(f"After reading 5 chars: {file.tell()}")
    file.seek(0)
    print(f"After seek(0): {file.tell()}")

import os
files_to_cleanup = ["sample.txt", "multiple_lines.txt", "binary_file.bin", 
                    "data.txt", "numbers.txt", "manual_close.txt", "position_demo.txt"]
for f in files_to_cleanup:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up: {f}")
