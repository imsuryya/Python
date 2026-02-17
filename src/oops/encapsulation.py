# Encapsulation in Python
# Encapsulation is the bundling of data and methods that operate on that data within a single unit (class)
# It also provides data hiding using access modifiers

class BankAccount:
    """Demonstrates encapsulation with a bank account"""
    
    def __init__(self, account_holder, initial_balance=0):
        # Public attribute
        self.account_holder = account_holder
        
        # Protected attribute (convention: single underscore)
        self._account_number = self._generate_account_number()
        
        # Private attribute (name mangling: double underscore)
        self.__balance = initial_balance
        self.__transaction_history = []
    
    def _generate_account_number(self):
        """Protected method to generate account number"""
        import random
        return f"ACC{random.randint(100000, 999999)}"
    
    # Getter for balance (property decorator)
    @property
    def balance(self):
        """Get the current balance"""
        return self.__balance
    
    # Setter for balance with validation
    @balance.setter
    def balance(self, amount):
        """Set balance with validation"""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount
    
    # Getter for account number (read-only property)
    @property
    def account_number(self):
        """Get the account number"""
        return self._account_number
    
    # Public methods
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        self.__record_transaction("DEPOSIT", amount)
        return f"Deposited ${amount}. New balance: ${self.__balance}"
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.__record_transaction("WITHDRAWAL", amount)
        return f"Withdrew ${amount}. New balance: ${self.__balance}"
    
    def __record_transaction(self, transaction_type, amount):
        """Private method to record transactions"""
        from datetime import datetime
        self.__transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "timestamp": datetime.now().isoformat()
        })
    
    def get_transaction_history(self):
        """Get a copy of transaction history"""
        return self.__transaction_history.copy()
    
    def __str__(self):
        return f"BankAccount({self.account_holder}, Balance: ${self.__balance})"


# Using property() function instead of decorators
class Employee:
    """Employee class using property() function"""
    
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    def _get_name(self):
        return self._name
    
    def _set_name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()
    
    def _get_salary(self):
        return self._salary
    
    def _set_salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value
    
    # Using property() function
    name = property(_get_name, _set_name)
    salary = property(_get_salary, _set_salary)
    
    def get_annual_salary(self):
        return self._salary * 12


# Encapsulation with slots (memory optimization)
class Point:
    """A point class using __slots__ for memory efficiency"""
    __slots__ = ['_x', '_y']
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __str__(self):
        return f"Point({self._x}, {self._y})"


if __name__ == "__main__":
    # Bank Account example
    account = BankAccount("John Doe", 1000)
    print(f"Account: {account}")
    print(f"Account Number: {account.account_number}")
    
    # Using public methods
    print(account.deposit(500))
    print(account.withdraw(200))
    
    # Accessing balance through property
    print(f"Current Balance: ${account.balance}")
    
    # Trying to access private attribute directly (Name Mangling)
    # print(account.__balance)  # This would raise AttributeError
    
    # Can still access using name mangling (but shouldn't!)
    # print(account._BankAccount__balance)  # Works but bad practice
    
    # Transaction history
    print(f"\nTransaction History: {account.get_transaction_history()}")
    
    # Employee example
    emp = Employee("Alice Smith", 5000)
    print(f"\nEmployee: {emp.name}")
    print(f"Monthly Salary: ${emp.salary}")
    print(f"Annual Salary: ${emp.get_annual_salary()}")
    
    # Update salary using setter
    emp.salary = 6000
    print(f"Updated Annual Salary: ${emp.get_annual_salary()}")
    
    # Point with slots
    p = Point(3, 4)
    print(f"\n{p}")
