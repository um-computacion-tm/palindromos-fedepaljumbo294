import unittest

from palindromo import palindromo

class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple1(self):
        result = palindromo('neuquen')
        self.assertEqual(result, True)
    def test_palindrome_simple2(self):
        result = palindromo('agita falsos usos la fatiga')
        self.assertEqual(result, True)
    def test_palindrome_simple3(self):
        result = palindromo('hola como omoc aloh')
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()