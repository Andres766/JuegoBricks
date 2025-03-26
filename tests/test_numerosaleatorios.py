import unittest
from numerosaleatorios import generate_random_numbers, find_max_number, find_min_number

class TestRandomNumberFunctions(unittest.TestCase):
    def test_generate_random_numbers(self):
        numbers = generate_random_numbers(5, 1, 10)
        self.assertEqual(len(numbers), 5)
        for num in numbers:
            self.assertTrue(1 <= num <= 10)
    
    def test_find_max_number(self):
        numbers = [1, 3, 7, 2, 5]
        self.assertEqual(find_max_number(numbers), 7)
    
    def test_find_min_number(self):
        numbers = [4, 2, 8, 6, 1]
        self.assertEqual(find_min_number(numbers), 1)

if __name__ == "__main__":
    unittest.main()
