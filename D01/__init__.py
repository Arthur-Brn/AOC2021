from utils.Utils import *

from D01.part1 import run as part1
from D01.part2 import run as part2


def init():
    list_of_number = getListOfNumber('D01/input.txt')
    print(part1(list_of_number))
    print(part1(part2(list_of_number)))