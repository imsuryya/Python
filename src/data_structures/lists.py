numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

numbers.append(6)
print("After append:", numbers)

numbers.insert(0, 0)
print("After insert at index 0:", numbers)

numbers.remove(3)
print("After removing 3:", numbers)

popped = numbers.pop()
print("Popped element:", popped)
print("After pop:", numbers)

print("Element at index 2:", numbers[2])
print("Slice [1:4]:", numbers[1:4])

numbers.extend([7, 8, 9])
print("After extend:", numbers)

numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)

print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

print("Count of 5:", numbers.count(5))
print("Index of 7:", numbers.index(7))

squared = [x**2 for x in range(1, 6)]
print("List comprehension - squares:", squared)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", even_numbers)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix)
print("Matrix[1][2]:", matrix[1][2])

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

copied = numbers.copy()
print("Copied list:", copied)

numbers.clear()
print("After clear:", numbers)
