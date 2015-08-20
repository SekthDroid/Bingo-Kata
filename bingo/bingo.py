from random import randrange

__author__ = 'SekthDroid'


class Bingo(object):
    available_numbers = []

    def __init__(self):
        super().__init__()
        self.available_numbers = [i for i in range(1, 75)]

    def call_number(self):
        if len(self.available_numbers) is 0:
            return

        random = self.available_numbers[self.__generate_random_number(0, len(self.available_numbers))]
        self.available_numbers.remove(random)
        return random

    def generate_random_numbers_with_bounds(self, lower_bound, upper_bound):
        numbers = set()
        while len(numbers) != 25:
            numbers.add(self.__generate_random_number(lower_bound, upper_bound))
        return numbers

    @staticmethod
    def fill_card_with(numbers):
        card = [0] * 5
        for i in range(0, len(card)):
            card[i] = [numbers.pop(), numbers.pop(), numbers.pop(), numbers.pop(), numbers.pop()]
        return card

    def generate_card(self, lower_bound, upper_bound):
        numbers = self.generate_random_numbers_with_bounds(lower_bound, upper_bound)

        return self.fill_card_with(numbers)

    @staticmethod
    def __generate_random_number(lower_bound, upper_bound):
        return randrange(lower_bound, upper_bound)