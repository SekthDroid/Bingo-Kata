from unittest import TestCase
from bingo.bingo import Bingo, BingoCard, bingo_card_generator

__author__ = 'SekthDroid'

LOWER_BOUND = 1
UPPER_BOUND = 75
US_BINGO_CELLS = 25


class BingoCardTest(TestCase):
    def test_bingo_card_return_all_his_numbers(self):
        columns = self.generate_columns()

        card = BingoCard(columns)
        self.assertEqual(25, len(card.get_card_numbers()))

    def generate_columns(self):
        columns = list(
            [[1, 2, 3, 4, 5], [11, 22, 33, 44, 55], [21, 12, 23, 34, 45], [9, 8, 7, 6, 1], [1, 2, 32, 45, 51]])

        return columns

    def test_bingo_card_return_column_that_exists(self):
        columns = self.generate_columns()

        card = BingoCard(columns)
        self.assertEqual(columns[0], card.get_column(0))
        self.assertEqual(columns[1], card.get_column(1))

    def test_bingo_card_return_none_when_column_doesnt_exists(self):
        columns = self.generate_columns()
        card = BingoCard(columns)

        self.assertEqual(None, card.get_column(10))

    def test_bingo_card_check_an_existing_number(self):
        columns = self.generate_columns()
        card = BingoCard(columns)

        card.check_number(1)
        self.assertTrue(1 in card.checked)


class BingoCardGeneratorTest(TestCase):
    def test_bingo_can_generate_columns_with_25_spaces(self):
        columns = bingo_card_generator(5, 5, 1, 75)

        total_items = 5 * 5

        items = 0
        for column in columns:
            items += len(column)

        self.assertEqual(total_items, items)

    def test_first_bingo_card_column_should_have_numbers_between_1_and_15_inclusive(self):
        columns = bingo_card_generator(5, 5, 1, 75)

        for number in columns[0]:
            self.assertGreaterEqual(number, 1)
            self.assertLessEqual(number, 15)

    def test_second_bingo_card_column_should_have_numbers_between_16_and_30_inclusive(self):
        columns = bingo_card_generator(5, 5, 1, 75)

        for number in columns[1]:
            self.assertGreaterEqual(number, 16)
            self.assertLessEqual(number, 30)

    def test_third_bingo_card_column_should_have_numbers_between_31_and_45_inclusive_with_one_free_space(self):
        columns = bingo_card_generator(5, 5, 1, 75)

        column_to_test = columns[2]
        for i in range(0, len(column_to_test)):
            number = column_to_test[i]
            if i is 2:
                self.assertEqual("", number)
            else:
                self.assertGreaterEqual(number, 31)
                self.assertLessEqual(number, 45)

    def test_fourth_bingo_card_column_should_have_numbers_between_46_and_60_inclusive(self):
        columns = bingo_card_generator(5, 5, 1, 75)

        for number in columns[3]:
            self.assertGreaterEqual(number, 46)
            self.assertLessEqual(number, 60)

    def test_fifth_bingo_card_column_should_have_numbers_between_61_and_75_inclusive(self):
        columns = bingo_card_generator(5, 5, 1, 75)

        for number in columns[4]:
            self.assertGreaterEqual(number, 61)
            self.assertLessEqual(number, 75)

    def test_bingo_card_generator_generate_cards_with_25_unique_numbers(self):
        numbers = set()

        columns = bingo_card_generator(5, 5, 1, 75)
        for row in columns:
            for cell in row:
                numbers.add(cell)

        self.assertEqual(US_BINGO_CELLS, len(numbers))


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



