# Classes and Objects in Python
# A class is a blueprint for creating objects

class Car:
    """A simple Car class demonstrating basic class structure"""
    
    # Class attribute (shared by all instances)
    wheels = 4
    
    # Constructor (initializer)
    def __init__(self, brand, model, year):
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    # Instance methods
    def start(self):
        """Start the car"""
        self.is_running = True
        return f"{self.brand} {self.model} started!"
    
    def stop(self):
        """Stop the car"""
        self.is_running = False
        return f"{self.brand} {self.model} stopped!"
    
    def get_info(self):
        """Get car information"""
        return f"{self.year} {self.brand} {self.model}"
    
    # String representation
    def __str__(self):
        return f"Car({self.brand}, {self.model}, {self.year})"
    
    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}', {self.year})"


# Creating objects (instances)
if __name__ == "__main__":
    # Create car objects
    car1 = Car("Toyota", "Camry", 2023)
    car2 = Car("Honda", "Civic", 2022)
    
    # Access attributes
    print(f"Car 1: {car1.get_info()}")
    print(f"Car 2: {car2.get_info()}")
    
    # Access class attribute
    print(f"Number of wheels: {Car.wheels}")
    
    # Call methods
    print(car1.start())
    print(car1.stop())
    
    # String representation
    print(str(car1))
    print(repr(car2))
