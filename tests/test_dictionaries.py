import pytest

@pytest.fixture
def person():
    return {"name": "John", "age": 30, "city": "New York"}

def test_access_by_key(person):
    assert person["name"] == "John"
    assert person["age"] == 30

def test_get_method(person):
    assert person.get("name") == "John"
    assert person.get("country") is None
    assert person.get("country", "USA") == "USA"

def test_add_key_value(person):
    person["job"] = "Developer"
    assert "job" in person
    assert person["job"] == "Developer"

def test_update_value(person):
    person["age"] = 31
    assert person["age"] == 31

def test_delete_key(person):
    del person["city"]
    assert "city" not in person

def test_pop(person):
    age = person.pop("age")
    assert age == 30
    assert "age" not in person

def test_update_method(person):
    person.update({"age": 32, "country": "USA"})
    assert person["age"] == 32
    assert person["country"] == "USA"

def test_keys(person):
    keys = list(person.keys())
    assert "name" in keys
    assert "age" in keys

def test_values(person):
    values = list(person.values())
    assert "John" in values
    assert 30 in values

def test_items(person):
    items = list(person.items())
    assert ("name", "John") in items

def test_in_operator(person):
    assert "name" in person
    assert "email" not in person

def test_dict_comprehension():
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
    high_scorers = {k: v for k, v in scores.items() if v >= 85}
    assert len(high_scorers) == 2
    assert "Alice" in high_scorers
