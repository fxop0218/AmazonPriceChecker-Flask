import unittest
from helpful_funcions import encript


class TestEnc(unittest.TestCase):
    def test_enc(self):
        result = encript("Hello")
        expected = encript("Hello")
        self.assertEqual(result, expected)  # add assertion here
        self.assertEqual(result, "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969")
        expected = encript("Hello2")
        self.assertNotEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
