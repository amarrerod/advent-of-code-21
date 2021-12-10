
import re
from typing import Counter, DefaultDict
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

filename = 'data/input_5.txt'


def read_input(input_filename=filename):
    board = []
    max_x = 0
    max_y = 0
    with open(input_filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            x_1, y_1, _, x_2, y_2, _ = re.split(',|\s', line)
            x_1 = int(x_1)
            x_2 = int(x_2)
            y_1 = int(y_1)
            y_2 = int(y_2)
            max_x = max(x_1, x_2, max_x)
            max_y = max(y_1, y_2, max_y)
            board.append((x_1, y_1, x_2, y_2))
    return board, 0, 0, max_x, max_y


def count_overlap(points, max_x, max_y):
    overlap_map = Counter()
    for x_1, y_1, x_2, y_2 in points:
        # Vertical lines
        if x_1 == x_2:
            x = x_1
            y = min(y_1, y_2)
            high_y = max(y_1, y_2)
            while y <= high_y:
                overlap_map[(x, y)] += 1
                y += 1
        elif y_1 == y_2:  # Horizontal lines
            y = y_1
            x = min(x_1, x_2)
            high_x = max(x_1, x_2)
            while x <= high_x:
                overlap_map[(x, y)] += 1
                x += 1
        else:
            delta_x = 1 if x_1 < x_2 else -1
            delta_y = 1 if y_1 < y_2 else -1
            start_point = [x_1, y_1]
            end_point = [x_2, y_2]
            overlap_map[(x_2, y_2)] += 1
            while start_point != end_point:
                overlap_map[(start_point[0], start_point[1])] += 1
                start_point[0] += delta_x
                start_point[1] += delta_y
    sol = sum([
        1 if overlap_map[k] > 1 else 0
        for k in overlap_map])
    print(sol)


if __name__ == '__main__':
    points, min_x, min_y, max_x, max_y = read_input()
    count_overlap(points, max_x, max_y)
