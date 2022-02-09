from Day import Day
from utils.Utils import getFile


class D03(Day):

    def __init__(self):
        super().__init__('D03', 3)
        self.default_value = getFile(self.input_path)

    def part1(self):
        return self.part1f(self.default_value)

    def part2(self):
        return self.part2f(self.default_value)
