def getFile(path):
    with open(path, "r") as file:
        return [line.rstrip() for line in file.readlines()]


def getListOfNumber(path):
    return [int(line) for line in getFile(path)]
