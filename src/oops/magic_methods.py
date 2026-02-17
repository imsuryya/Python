# Magic Methods (Dunder Methods) in Python
# Special methods that start and end with double underscores

class Book:
    """A Book class demonstrating various magic methods"""
    
    def __init__(self, title, author, pages):
        """Constructor - called when creating a new instance"""
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """Human-readable string representation"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Return length (number of pages)"""
        return self.pages
    
    def __eq__(self, other):
        """Equality comparison"""
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        """Less than comparison (by pages)"""
        return self.pages < other.pages
    
    def __le__(self, other):
        """Less than or equal comparison"""
        return self.pages <= other.pages
    
    def __gt__(self, other):
        """Greater than comparison"""
        return self.pages > other.pages
    
    def __ge__(self, other):
        """Greater than or equal comparison"""
        return self.pages >= other.pages
    
    def __hash__(self):
        """Make object hashable (can be used in sets/dicts)"""
        return hash((self.title, self.author))
    
    def __bool__(self):
        """Boolean conversion"""
        return self.pages > 0


class Library:
    """Library class demonstrating container magic methods"""
    
    def __init__(self):
        self._books = []
    
    def __len__(self):
        """Number of books in library"""
        return len(self._books)
    
    def __getitem__(self, index):
        """Get book by index or slice"""
        return self._books[index]
    
    def __setitem__(self, index, book):
        """Set book at index"""
        self._books[index] = book
    
    def __delitem__(self, index):
        """Delete book at index"""
        del self._books[index]
    
    def __iter__(self):
        """Iterator for library"""
        return iter(self._books)
    
    def __contains__(self, book):
        """Check if book is in library"""
        return book in self._books
    
    def __add__(self, other):
        """Combine two libraries"""
        new_library = Library()
        new_library._books = self._books + other._books
        return new_library
    
    def add_book(self, book):
        """Add a book to the library"""
        self._books.append(book)
    
    def __str__(self):
        return f"Library with {len(self)} books"


class Counter:
    """Counter class demonstrating numeric magic methods"""
    
    def __init__(self, value=0):
        self.value = value
    
    def __add__(self, other):
        """Addition"""
        if isinstance(other, Counter):
            return Counter(self.value + other.value)
        return Counter(self.value + other)
    
    def __radd__(self, other):
        """Right addition (when Counter is on the right)"""
        return Counter(self.value + other)
    
    def __iadd__(self, other):
        """In-place addition (+=)"""
        if isinstance(other, Counter):
            self.value += other.value
        else:
            self.value += other
        return self
    
    def __sub__(self, other):
        """Subtraction"""
        if isinstance(other, Counter):
            return Counter(self.value - other.value)
        return Counter(self.value - other)
    
    def __mul__(self, other):
        """Multiplication"""
        return Counter(self.value * other)
    
    def __truediv__(self, other):
        """True division"""
        return Counter(self.value / other)
    
    def __floordiv__(self, other):
        """Floor division"""
        return Counter(self.value // other)
    
    def __neg__(self):
        """Negation (unary -)"""
        return Counter(-self.value)
    
    def __abs__(self):
        """Absolute value"""
        return Counter(abs(self.value))
    
    def __int__(self):
        """Integer conversion"""
        return int(self.value)
    
    def __float__(self):
        """Float conversion"""
        return float(self.value)
    
    def __str__(self):
        return f"Counter({self.value})"
    
    def __repr__(self):
        return f"Counter({self.value})"


class ContextManager:
    """Demonstrates context manager magic methods"""
    
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Entering context: {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        print(f"Exiting context: {self.name}")
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions


class CallableClass:
    """Demonstrates __call__ magic method"""
    
    def __init__(self, multiplier):
        self.multiplier = multiplier
    
    def __call__(self, value):
        """Makes the instance callable like a function"""
        return value * self.multiplier


if __name__ == "__main__":
    # Book examples
    print("=== Book Magic Methods ===")
    book1 = Book("Python Basics", "John Doe", 300)
    book2 = Book("Advanced Python", "Jane Smith", 500)
    book3 = Book("Python Basics", "John Doe", 300)
    
    print(f"str: {str(book1)}")
    print(f"repr: {repr(book1)}")
    print(f"len: {len(book1)} pages")
    print(f"book1 == book3: {book1 == book3}")
    print(f"book1 < book2: {book1 < book2}")
    print(f"bool(book1): {bool(book1)}")
    
    # Library examples
    print("\n=== Library Magic Methods ===")
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    
    print(f"Library length: {len(library)}")
    print(f"First book: {library[0]}")
    print(f"book1 in library: {book1 in library}")
    
    print("Iterating library:")
    for book in library:
        print(f"  - {book}")
    
    # Counter examples
    print("\n=== Counter Magic Methods ===")
    c1 = Counter(10)
    c2 = Counter(5)
    
    print(f"c1 + c2 = {c1 + c2}")
    print(f"c1 - c2 = {c1 - c2}")
    print(f"c1 * 3 = {c1 * 3}")
    print(f"-c1 = {-c1}")
    print(f"5 + c1 = {5 + c1}")  # Uses __radd__
    
    c1 += 5
    print(f"c1 += 5: {c1}")
    
    # Context Manager
    print("\n=== Context Manager ===")
    with ContextManager("MyContext") as ctx:
        print(f"Inside context: {ctx.name}")
    
    # Callable class
    print("\n=== Callable Class ===")
    double = CallableClass(2)
    triple = CallableClass(3)
    
    print(f"double(5) = {double(5)}")
    print(f"triple(5) = {triple(5)}")
