
filename = 'data/input_2.txt'


def read_input(input_filename=filename):
    """
        Reads the input
    """
    with open(input_filename, 'r') as file:
        return [line.split() for line in file.readlines()]


def pilot(input):
    horizontal = 0
    depth = 0
    for m, v in input:
        v = int(v)
        if m == 'forward':
            horizontal += v
        elif m == 'up':
            depth -= v
        else:
            depth += v
    print(
        f'Horizontal: {horizontal} Depth: {depth}, Multiplication: {horizontal * depth}')


def aim_to_shoot(data):
    horizontal = 0
    depth = 0
    aim = 0
    for m, v in data:
        v = int(v)
        if m == 'forward':
            horizontal += v
            depth += aim * v
        elif m == 'up':
            aim -= v
        else:
            aim += v
    print(
        f'Horizontal: {horizontal} Depth: {depth}, Multiplication: {horizontal * depth}')


if __name__ == '__main__':
    data = read_input()
    pilot(data)
    aim_to_shoot(data)
