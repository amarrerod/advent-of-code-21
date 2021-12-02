
from itertools import islice

filename = 'input.txt'


def read_input(input_filename=filename):
    """
        Reads the input
    """
    with open(input_filename, 'r') as file:
        return [int(line.rstrip()) for line in file.readlines()]


def initial_version(input):
    increased = 0
    previous = input[0]
    for measure in input[1:]:
        if measure > previous:
            increased += 1
        previous = measure

    print(f'Increased {increased} times')
    return increased


def sliding_window(input):
    """For part two counting how many times n+1 + n+2 + n+3 > n + n+1 + n+2."""
    increased = 0
    previous = input[0] + input[1] + input[2]
    for index in range(1, len(input)-2):
        current = input[index] + input[index+1] + input[index+2]
        if current > previous:
            increased += 1
        previous = current
    return increased


if __name__ == "__main__":
    data = read_input()
    increased = initial_version(data)
    print(increased)
    increased = sliding_window(data)
    print(increased)
