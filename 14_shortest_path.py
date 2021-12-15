
from dataclasses import dataclass, field
from typing import DefaultDict, Dict, List, Tuple
import numpy as np
from queue import PriorityQueue

filename = 'data/input_14_test.txt'


class Graph:
    def __init__(self, nodes: Dict):
        self.nodes = nodes
        self.visited = []


def read_input(input_filename=filename):
    matrix = []
    nodes = {}
    with open(input_filename, 'r') as file:
        lines = file.read().splitlines()
        for row in lines:
            row = [int(x) for x in list(row)]
            matrix.append(row)
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                neighbors = get_neighbours(matrix, x, y)
                if (x, y) not in nodes:
                    nodes[(x, y)] = {
                        'neighbors': neighbors,
                        'h': matrix[x][y]
                    }

    max_x = max(x for x, _ in nodes.keys())
    max_y = max(y for _, y in nodes.keys())
    shape = (max_x, max_y)
    return nodes, shape


def get_neighbours(matrix, x, y):
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < len(matrix) - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < len(matrix[x]) - 1:
        neighbors.append((x, y + 1))

    return neighbors


def lowest_risk_path(nodes, shape):
    solution = 0
    current_position = (0, 0)
    posible_next_positions = nodes[(0, 0)]['neighbors']
    print(posible_next_positions)
    next_position = None


if __name__ == '__main__':
    nodes, shape = read_input()
    solution = lowest_risk_path(nodes, shape)
