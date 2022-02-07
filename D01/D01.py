from Day import Day
from utils.Utils import getListOfNumber


class D01(Day):

    def __init__(self):
        super().__init__('D01', 1)
        self.default_value = getListOfNumber(self.input_path)

    def part1(self):
        return self.part1f(self.default_value)

    def part2(self):
        return self.part1f(self.part2f(self.default_value))
