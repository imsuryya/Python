# Inheritance in Python
# Inheritance allows a class to inherit attributes and methods from another class

# Base/Parent class
class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        """Generic speak method"""
        return "Some sound"
    
    def eat(self):
        """Eating behavior"""
        return f"{self.name} is eating"
    
    def sleep(self):
        """Sleeping behavior"""
        return f"{self.name} is sleeping"


# Single Inheritance
class Dog(Animal):
    """Dog class inherits from Animal"""
    
    def __init__(self, name, age, breed):
        # Call parent constructor
        super().__init__(name, age)
        self.breed = breed
    
    # Override parent method
    def speak(self):
        return f"{self.name} says: Woof!"
    
    # New method specific to Dog
    def fetch(self):
        return f"{self.name} is fetching the ball"


class Cat(Animal):
    """Cat class inherits from Animal"""
    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        return f"{self.name} says: Meow!"
    
    def climb(self):
        return f"{self.name} is climbing"


# Multilevel Inheritance
class Puppy(Dog):
    """Puppy inherits from Dog (which inherits from Animal)"""
    
    def __init__(self, name, age, breed, is_trained):
        super().__init__(name, age, breed)
        self.is_trained = is_trained
    
    def play(self):
        return f"{self.name} the puppy is playing!"


# Multiple Inheritance
class Flyable:
    """Mixin class for flying ability"""
    
    def fly(self):
        return f"{self.name} is flying"


class Swimmable:
    """Mixin class for swimming ability"""
    
    def swim(self):
        return f"{self.name} is swimming"


class Duck(Animal, Flyable, Swimmable):
    """Duck inherits from Animal, Flyable, and Swimmable"""
    
    def speak(self):
        return f"{self.name} says: Quack!"


if __name__ == "__main__":
    # Single inheritance
    dog = Dog("Buddy", 3, "Golden Retriever")
    print(dog.speak())
    print(dog.eat())
    print(dog.fetch())
    
    cat = Cat("Whiskers", 2, "Orange")
    print(cat.speak())
    print(cat.climb())
    
    # Multilevel inheritance
    puppy = Puppy("Max", 1, "Labrador", False)
    print(puppy.speak())
    print(puppy.play())
    
    # Multiple inheritance
    duck = Duck("Donald", 2)
    print(duck.speak())
    print(duck.fly())
    print(duck.swim())
    
    # Check inheritance
    print(f"\nIs dog an Animal? {isinstance(dog, Animal)}")
    print(f"Is Duck subclass of Animal? {issubclass(Duck, Animal)}")
    
    # Method Resolution Order (MRO)
    print(f"\nDuck MRO: {Duck.__mro__}")
