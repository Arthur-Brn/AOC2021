import importlib
from abc import ABC, abstractmethod

gbl = globals()


class Day(ABC):

    def __init__(self, name, number):
        """
        This method initialize a Day

        :param name: (str) the name of the day
        :param number: (int) the number of the day
        """
        self.name = name
        self.number = number
        self.input_path = f'{name}/input.txt'
        gbl['part1'] = importlib.import_module(f'{name}.part1')
        self.part1f = getattr(globals()['part1'], 'run')
        gbl['part2'] = importlib.import_module(f'{name}.part2')
        self.part2f = getattr(globals()['part2'], 'run')
        pass

    @abstractmethod
    def part1(self):
        """
        Function to run the part 1 of the day
        :return: the solution of the part 1
        """
        pass

    @abstractmethod
    def part2(self):
        """
        Function to run the part 2 of the day
        :return: the solution of the part 1
        """
        pass


