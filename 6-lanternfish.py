

import numpy as np
from typing import Counter


filename = 'data/input_6.txt'


def read_input(input=filename):
    with open(input, 'r') as file:
        return [int(x) for x in file.readline().split(',')]


def modelise(fishes):
    days = 256
    counter = Counter(fishes)
    for _ in range(days):
        new_offspring = counter[0]
        for i in range(9):
            counter[i] = counter[i + 1]
        counter[6] += new_offspring
        counter[8] = new_offspring

    return sum(counter.values())


if __name__ == '__main__':
    fishes = read_input()
    total = modelise(fishes)
    print(total)
