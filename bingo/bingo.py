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