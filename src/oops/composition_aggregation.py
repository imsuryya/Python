# Composition and Aggregation in Python
# Alternatives to inheritance for code reuse

# ============ COMPOSITION ============
# "Has-a" relationship where the contained object cannot exist independently
# The container controls the lifecycle of the contained objects

class Engine:
    """Engine class for composition example"""
    
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False
    
    def start(self):
        self.is_running = True
        return f"Engine started ({self.horsepower}HP)"
    
    def stop(self):
        self.is_running = False
        return "Engine stopped"


class Wheel:
    """Wheel class for composition"""
    
    def __init__(self, size, material="rubber"):
        self.size = size
        self.material = material
    
    def rotate(self):
        return f"Wheel ({self.size}in) rotating"


class Car:
    """Car class using composition - creates its own parts"""
    
    def __init__(self, brand, horsepower, wheel_size):
        self.brand = brand
        # Composition: Car creates and owns these objects
        self._engine = Engine(horsepower, "gasoline")
        self._wheels = [Wheel(wheel_size) for _ in range(4)]
    
    def start(self):
        engine_msg = self._engine.start()
        return f"{self.brand}: {engine_msg}"
    
    def stop(self):
        engine_msg = self._engine.stop()
        return f"{self.brand}: {engine_msg}"
    
    def drive(self):
        if not self._engine.is_running:
            return "Cannot drive - engine is off"
        wheel_msgs = [wheel.rotate() for wheel in self._wheels]
        return f"{self.brand} is driving... {wheel_msgs[0]}"
    
    @property
    def engine_info(self):
        return f"{self._engine.horsepower}HP {self._engine.fuel_type}"


# ============ AGGREGATION ============
# "Has-a" relationship where contained objects can exist independently
# The container uses but doesn't control the lifecycle

class Author:
    """Author class for aggregation example"""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __str__(self):
        return self.name


class Publisher:
    """Publisher class for aggregation example"""
    
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def __str__(self):
        return f"{self.name} ({self.country})"


class Book:
    """Book class using aggregation - receives existing objects"""
    
    def __init__(self, title, author, publisher):
        self.title = title
        # Aggregation: Book receives but doesn't own these
        self.author = author  # Author can exist without Book
        self.publisher = publisher  # Publisher can exist without Book
    
    def get_info(self):
        return f"'{self.title}' by {self.author}, published by {self.publisher}"


# ============ DEPENDENCY INJECTION ============
# A form of aggregation where dependencies are injected

class Logger:
    """Logger interface"""
    
    def log(self, message):
        raise NotImplementedError


class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[CONSOLE] {message}")


class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename
    
    def log(self, message):
        print(f"[FILE:{self.filename}] {message}")


class OrderService:
    """Service that uses dependency injection for logging"""
    
    def __init__(self, logger: Logger):
        # Dependency is injected
        self._logger = logger
    
    def place_order(self, item, quantity):
        self._logger.log(f"Placing order: {quantity}x {item}")
        # Process order...
        self._logger.log(f"Order placed successfully")
        return True


# ============ MIXIN CLASSES ============
# Another composition pattern using multiple inheritance

class JSONSerializableMixin:
    """Mixin to add JSON serialization capability"""
    
    def to_json(self):
        import json
        return json.dumps(self.__dict__, default=str)
    
    @classmethod
    def from_json(cls, json_str):
        import json
        data = json.loads(json_str)
        return cls(**data)


class ComparableMixin:
    """Mixin to add comparison methods"""
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__
    
    def __ne__(self, other):
        return not self.__eq__(other)


class ValidatableMixin:
    """Mixin to add validation capability"""
    
    def validate(self):
        errors = []
        for field, rules in getattr(self, '_validation_rules', {}).items():
            value = getattr(self, field, None)
            for rule, params in rules.items():
                if rule == 'required' and params and not value:
                    errors.append(f"{field} is required")
                if rule == 'min_length' and value and len(str(value)) < params:
                    errors.append(f"{field} must be at least {params} characters")
                if rule == 'max_length' and value and len(str(value)) > params:
                    errors.append(f"{field} must be at most {params} characters")
        return errors


class User(JSONSerializableMixin, ComparableMixin, ValidatableMixin):
    """User class with multiple mixin capabilities"""
    
    _validation_rules = {
        'username': {'required': True, 'min_length': 3, 'max_length': 20},
        'email': {'required': True}
    }
    
    def __init__(self, username, email, age=None):
        self.username = username
        self.email = email
        self.age = age


# ============ COMPOSITION OVER INHERITANCE ============
# Example showing why composition is often preferred

# Instead of this inheritance hierarchy:
class AnimalInheritance:
    def eat(self): pass
    def sleep(self): pass

class BirdInheritance(AnimalInheritance):
    def fly(self): pass

class FishInheritance(AnimalInheritance):
    def swim(self): pass

# What about a flying fish? Multiple inheritance gets messy!

# Better approach with composition:
class FlyingAbility:
    def fly(self):
        return "Flying through the air!"

class SwimmingAbility:
    def swim(self):
        return "Swimming in water!"

class WalkingAbility:
    def walk(self):
        return "Walking on land!"

class Animal:
    """Base animal with composable abilities"""
    
    def __init__(self, name, abilities=None):
        self.name = name
        self._abilities = abilities or []
    
    def add_ability(self, ability):
        self._abilities.append(ability)
    
    def perform_ability(self, ability_name):
        for ability in self._abilities:
            if hasattr(ability, ability_name):
                return getattr(ability, ability_name)()
        return f"{self.name} cannot {ability_name}"


if __name__ == "__main__":
    # Composition example
    print("=== Composition (Car) ===")
    car = Car("Toyota", 200, 17)
    print(f"Engine: {car.engine_info}")
    print(car.start())
    print(car.drive())
    print(car.stop())
    
    # Aggregation example
    print("\n=== Aggregation (Book) ===")
    author = Author("John Doe", "john@email.com")
    publisher = Publisher("Tech Books", "USA")
    
    book1 = Book("Python Mastery", author, publisher)
    book2 = Book("Advanced Python", author, publisher)  # Same author/publisher
    
    print(book1.get_info())
    print(book2.get_info())
    print(f"Same author: {book1.author is book2.author}")
    
    # Dependency Injection
    print("\n=== Dependency Injection ===")
    console_logger = ConsoleLogger()
    file_logger = FileLogger("orders.log")
    
    service1 = OrderService(console_logger)
    service1.place_order("Laptop", 1)
    
    print()
    service2 = OrderService(file_logger)
    service2.place_order("Mouse", 3)
    
    # Mixins
    print("\n=== Mixin Classes ===")
    user = User("john_doe", "john@email.com", 25)
    
    # JSON serialization from mixin
    json_str = user.to_json()
    print(f"JSON: {json_str}")
    
    # Validation from mixin
    errors = user.validate()
    print(f"Validation errors: {errors}")
    
    # Comparison from mixin
    user2 = User("john_doe", "john@email.com", 25)
    print(f"Users equal: {user == user2}")
    
    # Composition over inheritance
    print("\n=== Composition Over Inheritance ===")
    flying_fish = Animal("Flying Fish")
    flying_fish.add_ability(FlyingAbility())
    flying_fish.add_ability(SwimmingAbility())
    
    print(f"{flying_fish.name} can:")
    print(f"  - {flying_fish.perform_ability('fly')}")
    print(f"  - {flying_fish.perform_ability('swim')}")
    print(f"  - {flying_fish.perform_ability('walk')}")
    
    duck = Animal("Duck")
    duck.add_ability(FlyingAbility())
    duck.add_ability(SwimmingAbility())
    duck.add_ability(WalkingAbility())
    
    print(f"\n{duck.name} can:")
    print(f"  - {duck.perform_ability('fly')}")
    print(f"  - {duck.perform_ability('swim')}")
    print(f"  - {duck.perform_ability('walk')}")
