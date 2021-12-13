import numpy as np
from collections import defaultdict

filename = 'data/input_12.txt'


def read_input(input_filename=filename):
    caves = defaultdict(list)
    with open(input_filename, 'r') as file:
        for line in file.readlines():
            head, tail = line.strip().split('-')
            caves[head].append(tail)
            caves[tail].append(head)
    return caves


def is_big_cave(cave):
    return cave != cave.lower()


def is_small_cave(cave):
    return cave == cave.lower()


def part_two_restrictions(path):
    if path.count('start') > 1 or path.count('end') > 1:
        return False

    small_caves = set([c for c in path if is_small_cave(c)])
    n_small_caves = len(small_caves)
    counters = [path.count(c) for c in small_caves]
    return sum(counters) in (n_small_caves, n_small_caves + 1)


def find_all_paths(paths):
    stack = [('start',)]
    n_paths = 0
    while stack:
        n_paths += 1
        path = stack.pop()
        *tail, head = path
        for next_cave in paths[head]:
            new_path = (*path, next_cave)
            if next_cave == 'end':
                yield new_path
            elif is_big_cave(next_cave) or part_two_restrictions(new_path):
                stack.append(new_path)


if __name__ == '__main__':
    paths = read_input()
    print(paths)
    print(len(list(find_all_paths(paths))))
