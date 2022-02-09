def getFile(path):
    """
    Function to return a file like a list
    :param path: (str) the path of the file
    :return: (list(str)) Return a list of every line of the file
    """
    with open(path, "r") as file:
        return [line.rstrip() for line in file.readlines()]


def getListOfNumber(path):
    """
    Function to get the content of a file like a list of number
    :param path: (str) path of the file
    :return: (list(int)) a list of number
    """
    return [int(line) for line in getFile(path)]


def getListOfObject(path):
    return [line.split() for line in getFile(path)]
