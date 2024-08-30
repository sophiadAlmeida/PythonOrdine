import unittest

def maior(a, b):
   if n1 > n2:
        return n1
    else:
        return n2
        
class TestAddFunction(unittest.TestCase):
    def test_add_negative_numbers(self):
        self.assertEqual(maior(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(maior(-2, 3), 1)


if __name__ == '__main__':
     unittest.main()