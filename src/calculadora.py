def add(a, b):
    """Suma dos números."""
    return a + b

def subtract(a, b):
    """Resta dos números."""
    return a - b

def multiply(a, b):
    """Multiplica dos números."""
    return a * b

def divide(a, b):
    """Divide dos números, manejando división por cero."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__ == "__main__":
    x, y = 10, 5
    print(f"{x} + {y} =", add(x, y))
    print(f"{x} - {y} =", subtract(x, y))
    print(f"{x} * {y} =", multiply(x, y))
    print(f"{x} / {y} =", divide(x, y))