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

        random = self.available_numbers[randrange(0, len(self.available_numbers))]
        self.available_numbers.remove(random)
        return random

    def generate_card(self, lower_bound, upper_bound):
        numbers = list()
        for i in range(0, 25):
            random = randrange(lower_bound, upper_bound)
            while random in numbers:
                random = randrange(lower_bound, upper_bound)

            numbers.append(random)

        card = [0] * 5
        for i in range(0, len(card)):
            card[i] = [numbers.pop(), numbers.pop(), numbers.pop(), numbers.pop(), numbers.pop()]

        return card