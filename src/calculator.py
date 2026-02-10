def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

def subtract(a, b):
    """Subtracts b from a and returns the result."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

def divide(a, b):
    """Divides a by b. Returns a float or an error message if b is 0."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulo(a, b):
    """Returns the remainder of dividing a by b."""
    if b == 0:
        return "Error: Division by zero"
    return a % b
