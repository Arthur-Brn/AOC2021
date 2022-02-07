import importlib
from abc import ABC, abstractmethod

gbl = globals()


class Day(ABC):

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.input_path = f'{name}/input.txt'
        gbl['part1'] = importlib.import_module(f'{name}.part1')
        self.part1f = getattr(globals()['part1'], 'run')
        gbl['part2'] = importlib.import_module(f'{name}.part2')
        self.part2f = getattr(globals()['part2'], 'run')

        print(self.part1)
        pass

    @abstractmethod
    def part1(self):
        pass

    @abstractmethod
    def part2(self):
        pass
