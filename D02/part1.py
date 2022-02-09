def run(list_of_object):
    depth, forward = 0, 0

    for line in list_of_object:
        direction, value = line[0], 0
        if line[1].isdigit():
            value = int(line[1])
        if direction == 'forward':
            forward += value
        elif direction == 'down':
            depth += value
        elif direction == 'up':
            depth -= value
            depth = 0 if depth < 0 else depth
    return depth * forward
