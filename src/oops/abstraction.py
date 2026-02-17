# Abstraction in Python
# Abstraction hides complex implementation details and shows only necessary features
# Python uses ABC (Abstract Base Class) module for abstraction

from abc import ABC, abstractmethod


# Abstract Base Class
class Database(ABC):
    """Abstract class for database operations"""
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._connection = None
    
    @abstractmethod
    def connect(self):
        """Establish connection to database"""
        pass
    
    @abstractmethod
    def disconnect(self):
        """Close database connection"""
        pass
    
    @abstractmethod
    def execute_query(self, query):
        """Execute a query"""
        pass
    
    # Concrete method (can be inherited as-is)
    def get_connection_string(self):
        return f"{self.host}:{self.port}"


class MySQLDatabase(Database):
    """MySQL implementation of Database"""
    
    def connect(self):
        print(f"Connecting to MySQL at {self.get_connection_string()}")
        self._connection = "MySQL Connection"
        return True
    
    def disconnect(self):
        print("Disconnecting from MySQL")
        self._connection = None
        return True
    
    def execute_query(self, query):
        if not self._connection:
            raise Exception("Not connected to database")
        print(f"MySQL executing: {query}")
        return f"MySQL Result for: {query}"


class PostgreSQLDatabase(Database):
    """PostgreSQL implementation of Database"""
    
    def connect(self):
        print(f"Connecting to PostgreSQL at {self.get_connection_string()}")
        self._connection = "PostgreSQL Connection"
        return True
    
    def disconnect(self):
        print("Disconnecting from PostgreSQL")
        self._connection = None
        return True
    
    def execute_query(self, query):
        if not self._connection:
            raise Exception("Not connected to database")
        print(f"PostgreSQL executing: {query}")
        return f"PostgreSQL Result for: {query}"


# Abstract Properties
class Vehicle(ABC):
    """Abstract class with abstract properties"""
    
    @property
    @abstractmethod
    def max_speed(self):
        """Maximum speed of the vehicle"""
        pass
    
    @property
    @abstractmethod
    def fuel_type(self):
        """Type of fuel used"""
        pass
    
    @abstractmethod
    def start_engine(self):
        pass


class ElectricCar(Vehicle):
    """Electric car implementation"""
    
    @property
    def max_speed(self):
        return 200  # km/h
    
    @property
    def fuel_type(self):
        return "Electric"
    
    def start_engine(self):
        return "Electric motor started silently"


class DieselTruck(Vehicle):
    """Diesel truck implementation"""
    
    @property
    def max_speed(self):
        return 120  # km/h
    
    @property
    def fuel_type(self):
        return "Diesel"
    
    def start_engine(self):
        return "Diesel engine roaring"


# Protocol-based abstraction (Python 3.8+)
from typing import Protocol, runtime_checkable


@runtime_checkable
class Drawable(Protocol):
    """Protocol for drawable objects"""
    
    def draw(self) -> str:
        """Draw the object"""
        ...


class Square:
    """Square implements Drawable protocol implicitly"""
    
    def __init__(self, side):
        self.side = side
    
    def draw(self) -> str:
        return f"Drawing square with side {self.side}"


class Text:
    """Text implements Drawable protocol implicitly"""
    
    def __init__(self, content):
        self.content = content
    
    def draw(self) -> str:
        return f"Rendering text: {self.content}"


def render(item: Drawable) -> None:
    """Function that works with any Drawable"""
    print(item.draw())


# Interface-like pattern using ABC
class PaymentProcessor(ABC):
    """Interface for payment processing"""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass
    
    @abstractmethod
    def refund(self, transaction_id: str, amount: float) -> bool:
        pass
    
    @abstractmethod
    def get_transaction_status(self, transaction_id: str) -> str:
        pass


class CreditCardProcessor(PaymentProcessor):
    
    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount}")
        return True
    
    def refund(self, transaction_id: str, amount: float) -> bool:
        print(f"Refunding ${amount} for transaction {transaction_id}")
        return True
    
    def get_transaction_status(self, transaction_id: str) -> str:
        return "COMPLETED"


class PayPalProcessor(PaymentProcessor):
    
    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount}")
        return True
    
    def refund(self, transaction_id: str, amount: float) -> bool:
        print(f"PayPal refund of ${amount} for {transaction_id}")
        return True
    
    def get_transaction_status(self, transaction_id: str) -> str:
        return "PENDING"


if __name__ == "__main__":
    # Database abstraction
    print("=== Database Abstraction ===")
    mysql = MySQLDatabase("localhost", 3306)
    mysql.connect()
    result = mysql.execute_query("SELECT * FROM users")
    print(result)
    mysql.disconnect()
    
    print()
    postgres = PostgreSQLDatabase("localhost", 5432)
    postgres.connect()
    result = postgres.execute_query("SELECT * FROM orders")
    print(result)
    postgres.disconnect()
    
    # Cannot instantiate abstract class
    # db = Database("localhost", 1234)  # TypeError
    
    # Vehicle abstraction
    print("\n=== Vehicle Abstraction ===")
    tesla = ElectricCar()
    truck = DieselTruck()
    
    print(f"Tesla: Max Speed = {tesla.max_speed} km/h, Fuel = {tesla.fuel_type}")
    print(tesla.start_engine())
    
    print(f"Truck: Max Speed = {truck.max_speed} km/h, Fuel = {truck.fuel_type}")
    print(truck.start_engine())
    
    # Protocol-based abstraction
    print("\n=== Protocol-based Abstraction ===")
    square = Square(10)
    text = Text("Hello, World!")
    
    render(square)
    render(text)
    
    # Check if object follows protocol
    print(f"Square is Drawable: {isinstance(square, Drawable)}")
    
    # Payment processing abstraction
    print("\n=== Payment Processing ===")
    processors = [CreditCardProcessor(), PayPalProcessor()]
    
    for processor in processors:
        processor.process_payment(100.00)
