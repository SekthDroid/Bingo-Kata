from unittest import TestCase
from bingo.bingo import Bingo

__author__ = 'SekthDroid'


class BingoTest(TestCase):
    def setUp(self):
        super().setUp()
        self.bingo = Bingo()

    def test_bingo_call_number_should_return_number_between_one_and_seventyfive_inclusive(self):
        number = self.bingo.call_number()
        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 75)

    def test_bingo_call_number_should_return_unique_random_numbers_between_one_and_seventyfive_inclusive(self):
        numbers = set()

        for i in range(0, 75):
            numbers.add(self.bingo.call_number())

        self.assertEqual(75, len(numbers))
