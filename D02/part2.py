def run(list_of_object):
    """
    function to linearize a list of data with a system where it sum 3 number to compare only the sums
    199  A
    200  A B
    208  A B C
    210    B C D 607
    200  E   C D 618
    207  E F   D618
    :param list_of_object: (list(int)) List of numbers
    :return: return the list of the sums
    """
    depth, forward, aim = 0, 0, 0

    for line in list_of_object:
        direction, value = line[0], 0
        if line[1].isdigit():
            value = int(line[1])
        if direction == 'forward':
            forward += value
            depth += aim * value
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
    return depth * forward
