from unittest import TestCase
from bingo.bingo import Bingo

__author__ = 'SekthDroid'


class BingoTest(TestCase):

    def test_bingo_call_number_should_return_number_between_one_and_seventyfive_inclusive(self):
        bingo = Bingo()
        number = bingo.call_number()
        self.assertGreaterEqual(1, number)
        self.assertLessEqual(number, 75)