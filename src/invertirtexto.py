def reverse_string(s):
    """Invierte una cadena de texto."""
    return s[::-1]

def is_palindrome(s):
    """Verifica si una cadena es un palíndromo."""
    return s == s[::-1]

def count_vowels(s):
    """Cuenta el número de vocales en una cadena de texto."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    sample_text = "ingenieria"
    print("Texto original:", sample_text)
    print("Texto invertido:", reverse_string(sample_text))
    print("Es palíndromo:", is_palindrome(sample_text))
    print("Número de vocales:", count_vowels(sample_text))
