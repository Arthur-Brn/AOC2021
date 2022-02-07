from utils.Utils import *


def run():
    list_of_number = getListOfNumber('D01/input.txt')
    list_of_change = []
    for index in range(len(list_of_number) - 1):
        list_of_change.append(1 if list_of_number[index] < list_of_number[index + 1] else 0)

    return sum(list_of_change)
