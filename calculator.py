def add(a, b):
    """Return sum of two numbers."""
    return a + b


def divide(a, b):
    """Return a / b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
