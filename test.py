import unittest
from helpful_funcions import encript


class TestCase(unittest.TestCase):
    def enocode_test(self):
        result = encript("Hello")
        expected = encript("Hello")
        self.assertEqual(result, expected)  # add assertion here


if __name__ == '__main__':
    unittest.main()
