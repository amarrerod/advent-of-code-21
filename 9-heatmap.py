

import numpy as np
from typing import Counter


filename = 'data/input_9.txt'


def read_input(input=filename):
    heatmap = []
    with open(input, 'r') as file:
        for line in file.readlines():
            row = list(line)
            row = [int(x) for x in row if x != '\n']
            heatmap.append(row)

    return heatmap


def count_adjacent(heatmap):
    low_points = []
    low_points_coords = []
    for i in range(len(heatmap)):
        for j in range(len(heatmap[i])):
            adjacent = [
                heatmap[i][j - 1] if j > 0 else np.inf,
                heatmap[i][j + 1] if j < (len(heatmap[i]) - 1) else np.inf,
                heatmap[i - 1][j] if i > 0 else np.inf,
                heatmap[i + 1][j] if i < (len(heatmap) - 1) else np.inf
            ]
            if all(x > heatmap[i][j] for x in adjacent):
                low_points.append(heatmap[i][j] + 1)
                low_points_coords.append((i, j))

    print(sum(low_points))
    return low_points, low_points_coords


def get_adyacent_not_9(heatmap, i, j):
    neighbors = []
    if j > 0 and heatmap[i][j-1] != 9:
        neighbors.append((i, j-1))
        heatmap[i][j-1] = 9
    if j < (len(heatmap[i]) - 1) and heatmap[i][j + 1] != 9:
        neighbors.append((i, j + 1))
        heatmap[i][j+1] = 9
    if i > 0 and heatmap[i - 1][j] != 9:
        neighbors.append((i - 1, j))
        heatmap[i - 1][j] = 9
    if i < (len(heatmap) - 1) and heatmap[i + 1][j] != 9:
        neighbors.append((i + 1, j))
        heatmap[i+1][j] = 9

    return neighbors, heatmap


def print_heatmap(heatmap):
    print("\n================================")
    for r in heatmap:
        print(*r)
    print("\n================================")


def measure_basins(heatmap, low_points_coords):
    basins = []
    for i, j in low_points_coords:
        # Para cada punto debemos buscar sus adyacentes que no sean 9
        neighbors = []
        heatmap[i][j] = 9
        neighbors, heatmap = get_adyacent_not_9(heatmap, i, j)
        basin_size = 1
        # Para cada adyacente --> repetir
        while neighbors:
            cell_i, cell_j = neighbors.pop()
            basin_size += 1
            new_neighbors, heatmap = get_adyacent_not_9(
                heatmap, cell_i, cell_j)
            neighbors = neighbors + new_neighbors

        basins.append(basin_size)

    return np.prod(sorted(basins, reverse=True)[:3])


if __name__ == '__main__':
    heatmap = read_input()
    _, low_points_coords = count_adjacent(heatmap)
    answer = measure_basins(heatmap, low_points_coords)
    print(answer)
