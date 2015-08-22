from unittest import TestCase, skip
from bingo.bingo import Bingo, BingoCard, bingo_card_generator

__author__ = 'SekthDroid'

LOWER_BOUND = 1
UPPER_BOUND = 75
US_BINGO_CELLS = 25


class BingoCardTest(TestCase):
    def test_bingo_card_return_all_his_numbers(self):
        numbers = list()
        for i in range(5):
            column = list()
            for x in range(5):
                column.append(x)
            numbers.append(column)

        card = BingoCard(numbers)
        self.assertEqual(25, len(card.get_card_numbers()))


class BingoCardGeneratorTest(TestCase):
    def test_bingo_can_generate_columns_with_25_spaces(self):
        columns = bingo_card_generator(5, 5, 1, 75)

        total_items = 5 * 5

        items = 0
        for column in columns:
            items += len(column)

        self.assertEqual(total_items, items)


class BingoTest(TestCase):
    def setUp(self):
        super().setUp()
        self.bingo = Bingo()

    def test_bingo_call_number_should_return_number_between_one_and_seventyfive_inclusive(self):
        number = self.bingo.call_number()
        self.assertGreaterEqual(number, LOWER_BOUND)
        self.assertLessEqual(number, UPPER_BOUND)

    def test_bingo_call_number_should_return_unique_random_numbers_between_one_and_seventyfive_inclusive(self):
        numbers = set()

        for i in range(0, UPPER_BOUND):
            numbers.add(self.bingo.call_number())

        self.assertEqual(UPPER_BOUND, len(numbers))


    def test_bingo_generate_bingo_cards_with_25_unique_numbers(self):
        numbers = set()

        card = self.bingo.generate_card(LOWER_BOUND, UPPER_BOUND)
        for row in card:
            for cell in row:
                numbers.add(cell)

        self.assertEqual(US_BINGO_CELLS, len(numbers))

    def test_first_bingo_card_column_should_have_numbers_between_1_and_15_inclusive(self):
        card = self.bingo.generate_card(LOWER_BOUND, UPPER_BOUND)

        for i in range(0, 5):
            self.assertGreaterEqual(card[i][0], 1)
            self.assertLessEqual(card[i][0], 15)

    def test_second_bingo_card_column_should_have_numbers_between_16_and_30_inclusive(self):
        card = self.bingo.generate_card(LOWER_BOUND, UPPER_BOUND)

        for i in range(0, 5):
            self.assertGreaterEqual(card[i][1], 16)
            self.assertLessEqual(card[i][1], 30)

    def test_third_bingo_card_column_should_have_numbers_between_31_and_45_inclusive(self):
        card = self.bingo.generate_card(LOWER_BOUND, UPPER_BOUND)

        for i in range(0, 5):
            if i is 2:  # We avoid the free space in this test
                continue
            self.assertGreaterEqual(card[i][2], 31)
            self.assertLessEqual(card[i][2], 45)

    def test_fourth_bingo_card_column_should_have_numbers_between_46_and_60_inclusive(self):
        card = self.bingo.generate_card(LOWER_BOUND, UPPER_BOUND)

        for i in range(0, 5):
            self.assertGreaterEqual(card[i][3], 46)
            self.assertLessEqual(card[i][3], 60)

    def test_fifth_bingo_card_column_should_have_numbers_between_61_and_75_inclusive(self):
        card = self.bingo.generate_card(LOWER_BOUND, UPPER_BOUND)

        for i in range(0, 5):
            self.assertGreaterEqual(card[i][4], 61)
            self.assertLessEqual(card[i][4], 75)

    def test_bingo_card_center_should_be_free(self):
        card = self.bingo.generate_card(LOWER_BOUND, UPPER_BOUND)
        self.assertEqual("", card[2][2])
