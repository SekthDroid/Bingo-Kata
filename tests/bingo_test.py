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

    def test_bingo_card_should_not_check_a_non_existing_number(self):
        columns = self.generate_columns()
        card = BingoCard(columns)

        card.check_number(120)
        self.assertTrue(120 not in card.checked)


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

    def test_bingo_check_bingo_card_that_has_checked_all_his_numbers(self):
        # We are going to allow the player to join after the start (I think this is not allowed in the real life)
        numbers = self.call_twenty_five_numbers()
        columns = self.create_column_with(numbers)
        card = BingoCard(columns)

        self.assertTrue(self.bingo.check_card(card))

    def test_bingo_check_bingo_card_that_has_not_checked_all_his_numbers(self):
        numbers = [i for i in range(1, 76)]
        card = BingoCard(self.create_column_with(numbers[1:25]))

        self.assertFalse(self.bingo.check_card(card))

    def call_twenty_five_numbers(self):
        return [self.bingo.call_number() for _ in range(25)]

    def create_column_with(self, numbers):
        return [numbers[x:x + 5] for x in range(5)]



