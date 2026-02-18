fruits = {"apple", "banana", "cherry"}
print("Set:", fruits)

fruits.add("orange")
print("After add:", fruits)

fruits.add("apple")
print("After adding duplicate:", fruits)

fruits.update(["mango", "grape", "kiwi"])
print("After update:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

fruits.discard("cherry")
fruits.discard("pear")
print("After discard:", fruits)

numbers = {1, 2, 3, 4, 5}
print("\nNumbers set:", numbers)

print("Length:", len(numbers))
print("Element 3 exists:", 3 in numbers)
print("Element 10 exists:", 10 in numbers)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

union = set_a | set_b
print("\nUnion:", union)

intersection = set_a & set_b
print("Intersection:", intersection)

difference = set_a - set_b
print("Difference (A - B):", difference)

symmetric_diff = set_a ^ set_b
print("Symmetric difference:", symmetric_diff)

print("\nUsing methods:")
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference:", set_a.difference(set_b))
print("Symmetric difference:", set_a.symmetric_difference(set_b))

set_c = {1, 2, 3}
set_d = {1, 2, 3, 4, 5}

print("\nSubset check:", set_c.issubset(set_d))
print("Superset check:", set_d.issuperset(set_c))
print("Disjoint check:", set_a.isdisjoint(set_b))

numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = set(numbers_with_duplicates)
print("\nUnique numbers:", unique_numbers)

for item in fruits:
    print(f"Fruit: {item}")

squared_set = {x**2 for x in range(1, 6)}
print("\nSquared set:", squared_set)

even_set = {x for x in range(1, 11) if x % 2 == 0}
print("Even set:", even_set)

copied = fruits.copy()
print("Copied set:", copied)

sample = {1, 2, 3, 4, 5, 6, 7, 8, 9}
popped = sample.pop()
print("Popped element:", popped)
print("After pop:", sample)

fruits.clear()
print("After clear:", fruits)
