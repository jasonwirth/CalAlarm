import unittest

class TestTest(unittest.TestCase):
    def test_first_test(self):
        self.assertFail("Initial Tests")

if __name__ == "__main__":
    unittest.main()