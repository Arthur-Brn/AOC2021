from Day import Day
from utils.Utils import getListOfObject


class D02(Day):

    def __init__(self):
        super().__init__('D02', 2)
        self.default_value = getListOfObject(self.input_path)

    def part1(self):
        return self.part1f(self.default_value)

    def part2(self):
        return self.part2f(self.default_value)
