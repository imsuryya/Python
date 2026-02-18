import time
import functools

print("=== Basic Decorator ===")

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def calculate_sum(n):
    total = sum(range(n))
    return total

result = calculate_sum(1000000)
print(f"Sum: {result}\n")

print("=== Authentication Decorator ===")

user_roles = {
    "Surya": "admin",
    "Priya": "user",
    "Arjun": "guest"
}

def require_auth(role):
    def decorator(func):
        def wrapper(username, *args, **kwargs):
            if username not in user_roles:
                print(f"Access Denied: {username} not found")
                return None
            if user_roles[username] != role:
                print(f"Access Denied: {username} is not {role}")
                return None
            return func(username, *args, **kwargs)
        return wrapper
    return decorator

@require_auth("admin")
def delete_user(username, target_user):
    print(f"{username} deleted user: {target_user}")
    return True

@require_auth("user")
def view_profile(username):
    print(f"{username} viewing profile")
    return True

delete_user("Surya", "old_user")
delete_user("Priya", "old_user")
view_profile("Priya")

print("\n=== Logging Decorator ===")

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add_marks(subject, marks):
    return f"{subject}: {marks}"

add_marks("Python", 95)

print("\n=== Multiple Decorators ===")

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet(name):
    return f"Hello, {name}"

print(greet("Surya"))

print("\n=== Cache Decorator ===")

def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
            print(f"Calculating for {n}...")
        else:
            print(f"Using cached value for {n}")
        return cache[n]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fib(5): {fibonacci(5)}")
print(f"Fib(5): {fibonacci(5)}")

print("\nDecorator examples completed!")
