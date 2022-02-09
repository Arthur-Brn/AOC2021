def run(list_of_bytes):
    return int(recursive(list_of_bytes, mostPresent), 2) * int(
        recursive(list_of_bytes, (lambda l, i: f"{abs(int(mostPresent(l, i)) - 1)}")), 2)


def recursive(list_of_bytes, function, index=0):
    if len(list_of_bytes) == 1:
        return list_of_bytes[0]
    char = function(list_of_bytes, index)
    return recursive(list(filter(lambda byte: byte[index] == char, list_of_bytes)), function, index + 1)


def mostPresent(list_of_bytes, i):
    return '1' if sum([int(byte[i]) for byte in list_of_bytes]) >= len(list_of_bytes) / 2 else '0'
