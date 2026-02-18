coordinates = (10, 20)
print("Tuple:", coordinates)

print("First element:", coordinates[0])
print("Second element:", coordinates[1])

rgb = (255, 128, 0)
print("RGB tuple:", rgb)
print("Slice [1:]:", rgb[1:])

single_element = (42,)
print("Single element tuple:", single_element)
print("Type:", type(single_element))

mixed = (1, "hello", 3.14, True)
print("Mixed tuple:", mixed)

print("Length:", len(coordinates))
print("Max of rgb:", max(rgb))
print("Min of rgb:", min(rgb))

point_3d = (10, 20, 30, 20, 10)
print("Count of 20:", point_3d.count(20))
print("Index of 30:", point_3d.index(30))

x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

r, g, b = rgb
print(f"RGB unpacked: r={r}, g={g}, b={b}")

person = ("Alice", 25, "Engineer")
name, age, job = person
print(f"Person: {name}, {age}, {job}")

nested = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested)
print("First inner tuple:", nested[0])

for item in mixed:
    print(f"Item: {item}")

numbers = (1, 2, 3, 4, 5)
doubled = tuple(x * 2 for x in numbers)
print("Doubled:", doubled)

concatenated = coordinates + rgb
print("Concatenated:", concatenated)

repeated = (1, 2) * 3
print("Repeated:", repeated)

print("Element 3.14 exists:", 3.14 in mixed)
print("Element 'world' exists:", "world" in mixed)

list_data = [1, 2, 3]
tuple_from_list = tuple(list_data)
print("Tuple from list:", tuple_from_list)

dict_items = person
back_to_list = list(dict_items)
print("Back to list:", back_to_list)
