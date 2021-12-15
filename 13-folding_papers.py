
import re
import numpy as np

filename = 'data/input_13.txt'


def read_input(input=filename):
    coords = set()
    folds = []
    with open(input, 'r') as file:
        for line in file.readlines():
            m = re.match(r'(\d+),(\d+)', line)
            if m:
                coords.add((int(m.group(1)), int(m.group(2))))
            m = re.match(r'fold along (x|y)=(\d+)', line)
            if m:
                folds.append((m.group(1), int(m.group(2))))

    return coords, folds


def map_str(matrix, matrix_shape):
    max_x, max_y = matrix_shape
    map_state = ''
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            map_state += '█' if (x, y) in matrix else ' '
        map_state += '\n'
    return map_state


def fold(matrix, folds):
    for axis, pos in folds:
        for x, y in tuple(matrix):
            if axis == 'x':
                if x > pos:
                    matrix.remove((x, y))
                    matrix.add((2 * pos - x, y))
            elif y > pos:
                matrix.remove((x, y))
                matrix.add((x, 2 * pos - y))

    return matrix


if __name__ == '__main__':
    matrix, folds = read_input()
    matrix = fold(matrix, folds)
    x_max = max(x for x, _ in matrix)
    y_max = max(y for _, y in matrix)
    matrix_shape = (x_max, y_max)
    with open('results_13.txt', 'w') as file:
        file.write(map_str(matrix, matrix_shape))
