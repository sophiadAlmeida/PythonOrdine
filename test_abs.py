import unittest

def abs(a, b):
    return a - b

class TestAddFunction(unittest.TestCase):
    def test_add_negative_numbers(self):
        self.assertEqual(abs(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(abs(-2, 3), 1)


if __name__ == '__main__':
     unittest.main()