
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


class Dijsktra:
    def __init__(self, graph: Graph, start_point: tuple, end_point: tuple):
        self.graph = graph
        self.start_point = start_point
        self.end_point = end_point
        self.visited = []

    def run(self, verbose=False):
        if verbose:
            print(
                f'Running Dijkstra Algorithm from {self.start_point} to {self.end_point}')

        distances = {node: np.inf for node in self.graph.nodes.keys()}
        distances[self.start_point] = 0
        pq = PriorityQueue()
        pq.put((0, self.start_point))
        while not pq.empty():
            (dist, node) = pq.get()
            self.visited.append(node)
            for neighbor in self.graph.get_neighbours(node):
                if neighbor not in self.visited:
                    old_cost = distances[neighbor]
                    new_cost = distances[node] + self.graph.get_cost(neighbor)
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        distances[neighbor] = new_cost

        return distances


class ExtMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = (len(self.matrix), len(self.matrix[0]))
        self.real_size = (self.size[0] * 5, self.size[1] * 5)

    def get_value(self, x, y):
        real_x = x % self.real_size[0]
        real_y = y % self.real_size[1]
        cost = self.matrix[real_x][real_y]
        cost += y / self.real_size[1] + x / self.real_size[0]
        return cost % 9 if cost > 9 else cost


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
    ext_matrix = ExtMatrix(matrix)
    print(ext_matrix.real_size)
    #algorithm = Dijsktra(graph, (0, 0), shape)
    #path = algorithm.run(True)
    # print(path)
