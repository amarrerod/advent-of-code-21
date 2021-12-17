
from dataclasses import dataclass, field
from typing import DefaultDict, Dict, List, Tuple
import numpy as np
from queue import PriorityQueue
import sys
np.set_printoptions(threshold=sys.maxsize)

filename = 'data/input_15.txt'


class Graph:
    def __init__(self, nodes: Dict, matrix: list):
        self.nodes = nodes
        self.matrix = matrix
        self.visited = []

    def get_neighbours(self, node):
        return self.nodes[node]['neighbors']

    def get_cost(self, node):
        return self.matrix[node[0]][node[1]]

    def get_path_cost(self, path):
        return sum(self.matrix[x][y] for x, y in path) - self.matrix[0][0]

    def print_path(self, path):
        str_path = ""
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                str_path += str(self.matrix[x][y]) if (x, y) in path else "*"
            str_path += "\n"
        print(str_path)


class ExtGraph(Graph):
    def __init__(self, nodes: Dict, matrix):
        self.nodes = nodes
        self.matrix = matrix
        self.real_size = (len(self.matrix), len(self.matrix[0]))
        self.size = (self.real_size[0] * 5, self.real_size[1] * 5)
        self.__extend_nodes()

    def __extend_nodes(self):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.nodes[(x, y)] = {
                    'neighbors': self.get_neighbours((x, y))
                }

    def get_neighbours(self, node):
        x, y = node
        neighbors = []
        if x > 0:
            neighbors.append((x - 1, y))
        if x < self.size[0] - 1:
            neighbors.append((x + 1, y))
        if y > 0:
            neighbors.append((x, y - 1))
        if y < self.size[1] - 1:
            neighbors.append((x, y + 1))
        return neighbors

    def get_size(self):
        return self.size

    def get_cost(self, node):
        x, y = node
        cost = self.matrix[x % self.real_size[0]][y % self.real_size[1]]
        cost += y / self.real_size[1] + x / self.real_size[0]
        cost = cost % 9 if cost > 9 else cost
        return int(cost)


class Dijsktra:
    def __init__(self, graph: Graph, start_point: tuple, end_point: tuple):
        self.graph = graph
        self.start_point = start_point
        self.end_point = end_point
        self.visited = []
        self.ext_matrix = ext_matrix

    def run(self, verbose=False, part_two=False):
        if verbose:
            print(
                f'Running Dijkstra Algorithm from {self.start_point} to {self.end_point}')

        distances = {node: np.inf for node in self.graph.nodes.keys()}
        distances[self.start_point] = 0
        pq = PriorityQueue()
        pq.put((0, self.start_point))
        while not pq.empty():
            (dist, node) = pq.get()
            print(f'Visiting node: {node}')
            self.visited.append(node)
            for neighbor in self.graph.get_neighbours(node):
                if neighbor not in self.visited:
                    old_cost = distances[neighbor]
                    if part_two:
                        new_cost = distances[node] + \
                            self.graph.get_cost(neighbor)
                    else:
                        new_cost = distances[node] + \
                            self.graph.get_cost(neighbor)
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        distances[neighbor] = new_cost

        return distances


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
    return nodes, shape, matrix


def print_matrix(matrix):
    str_path = ''
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            str_path += str(matrix[x][y])
        str_path += "\n"
    print(str_path)


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


if __name__ == '__main__':
    nodes, shape, matrix = read_input()
    graph = Graph(nodes, matrix)
    print_matrix(matrix)
    ext_matrix = ExtGraph(nodes, matrix)
    print(ext_matrix.real_size)
    algorithm = Dijsktra(ext_matrix, (0, 0), ext_matrix.get_size())
    path = algorithm.run(True, part_two=True)
    print(path)
