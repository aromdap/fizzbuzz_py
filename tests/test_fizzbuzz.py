import unittest

class TestFizzbuzz(unittest.TestCase):

    def test_when_given_5_returns_buzz(self):
        self.assertEqual('buzz', fizzbuzz(5))
