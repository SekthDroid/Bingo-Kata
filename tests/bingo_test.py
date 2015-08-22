from unittest import TestCase
from bingo.bingo import Bingo

__author__ = 'SekthDroid'


class BingoTest(TestCase):
    LOWER_BOUND = 1
    UPPER_BOUND = 75
    US_BINGO_CELLS = 25

    def setUp(self):
        super().setUp()
        self.bingo = Bingo()

    def test_bingo_call_number_should_return_number_between_one_and_seventyfive_inclusive(self):
        number = self.bingo.call_number()
        self.assertGreaterEqual(number, self.LOWER_BOUND)
        self.assertLessEqual(number, self.UPPER_BOUND)

    def test_bingo_call_number_should_return_unique_random_numbers_between_one_and_seventyfive_inclusive(self):
        numbers = set()

        for i in range(0, self.UPPER_BOUND):
            numbers.add(self.bingo.call_number())

        self.assertEqual(self.UPPER_BOUND, len(numbers))

    def test_bingo_can_generate_bingo_cards_with_25_numbers_between_the_bingo_bounds(self):
        card = self.bingo.generate_card(1, self.UPPER_BOUND)
        items = 0
        for row in card:
            items += len(row)

        self.assertEqual(self.US_BINGO_CELLS, items)

        for row in card:
            for cell in row:
                self.assertGreaterEqual(cell, self.LOWER_BOUND)
                self.assertLessEqual(cell, self.UPPER_BOUND)

    def test_bingo_generate_bingo_cards_with_25_unique_numbers(self):
        numbers = set()

        card = self.bingo.generate_card(self.LOWER_BOUND, self.UPPER_BOUND)
        for row in card:
            for cell in row:
                numbers.add(cell)

        self.assertEqual(self.US_BINGO_CELLS, len(numbers))

    def test_first_bingo_card_column_should_have_numbers_between_1_and_15_inclusive(self):
        card = self.bingo.generate_card(self.LOWER_BOUND, self.UPPER_BOUND)

        for i in range(0, 5):
            self.assertGreaterEqual(card[i][0], 1)
            self.assertLessEqual(card[i][0], 15)

    def test_second_bingo_card_column_should_have_numbers_between_16_and_30_inclusive(self):
        card = self.bingo.generate_card(self.LOWER_BOUND, self.UPPER_BOUND)

        for i in range(0, 5):
            self.assertGreaterEqual(card[i][1], 16)
            self.assertLessEqual(card[i][1], 30)

    def test_third_bingo_card_column_should_have_numbers_between_31_and_45_inclusive(self):
        card = self.bingo.generate_card(self.LOWER_BOUND, self.UPPER_BOUND)

        for i in range(0, 5):
            self.assertGreaterEqual(card[i][2], 31)
            self.assertLessEqual(card[i][2], 45)

    def test_fourth_bingo_card_column_should_have_numbers_between_46_and_60_inclusive(self):
        card = self.bingo.generate_card(self.LOWER_BOUND, self.UPPER_BOUND)

        for i in range(0, 5):
            self.assertGreaterEqual(card[i][3], 46)
            self.assertLessEqual(card[i][3], 60)

    def test_fifth_bingo_card_column_should_have_numbers_between_61_and_75_inclusive(self):
        card = self.bingo.generate_card(self.LOWER_BOUND, self.UPPER_BOUND)

        for i in range(0, 5):
            self.assertGreaterEqual(card[i][4], 61)
            self.assertLessEqual(card[i][4], 75)