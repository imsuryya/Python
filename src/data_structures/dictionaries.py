person = {"name": "John", "age": 30, "city": "New York"}
print("Dictionary:", person)

print("Name:", person["name"])
print("Age:", person.get("age"))

person["job"] = "Developer"
print("After adding job:", person)

person["age"] = 31
print("After updating age:", person)

del person["city"]
print("After deleting city:", person)

removed = person.pop("job")
print("Removed value:", removed)
print("After pop:", person)

person.update({"age": 32, "country": "USA", "salary": 80000})
print("After update:", person)

print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())

print("Key 'name' exists:", "name" in person)
print("Key 'city' exists:", "city" in person)

for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key} = {value}")

student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
print("\nStudent scores:", student_scores)

high_scorers = {name: score for name, score in student_scores.items() if score >= 90}
print("High scorers:", high_scorers)

nested_dict = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
}
print("\nNested dictionary:", nested_dict)
print("User1 name:", nested_dict["user1"]["name"])

default_dict = person.copy()
print("Copied dictionary:", default_dict)

person.clear()
print("After clear:", person)

config = {"host": "localhost", "port": 8080}
host = config.setdefault("host", "127.0.0.1")
timeout = config.setdefault("timeout", 30)
print("Config after setdefault:", config)
