import random

def generate_random_numbers(count, start, end):
    """
    Genera una lista de números aleatorios.
    :param count: Cantidad de números a generar.
    :param start: Valor mínimo.
    :param end: Valor máximo.
    :return: Lista de números aleatorios.
    """
    return [random.randint(start, end) for _ in range(count)]

def find_max_number(numbers):
    """Encuentra el número máximo en una lista."""
    return max(numbers)

def find_min_number(numbers):
    """Encuentra el número mínimo en una lista."""
    return min(numbers)

if __name__ == "__main__":
    numbers = generate_random_numbers(10, 1, 100)
    print("Lista de números:", numbers)
    print("Número máximo:", find_max_number(numbers))
    print("Número mínimo:", find_min_number(numbers))
