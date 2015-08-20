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

    def test_bingo_can_generate_bingo_cards_with_25_numbers_between_the_bingo_bounds(self):
        card = self.bingo.generate_card(1, 75)
        items = 0
        for row in card:
            items += len(row)

        self.assertEqual(25, items)

        for row in card:
            for cell in row:
                self.assertGreaterEqual(cell, 1)
                self.assertLessEqual(cell, 75)

    def test_bingo_generate_bingo_cards_with_25_unique_numbers(self):
        numbers = set()

        card = self.bingo.generate_card(1, 75)
        for row in card:
            for cell in row:
                numbers.add(cell)

        self.assertEqual(25, len(numbers))