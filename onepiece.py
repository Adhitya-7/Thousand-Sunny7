def greet(name):
    """A simple greeting function."""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 3 = {add_numbers(2, 3)}")