

import numpy as np
from typing import Counter


filename = 'data/input_7.txt'


def read_input(input=filename):
    with open(input, 'r') as file:
        return [int(x) for x in file.readline().split(',')]


def align_crabs(crabs, part_two=False):
    counter = Counter(crabs)
    most_common = sorted(counter, reverse=True)
    mean = np.mean(crabs, dtype=int)
    median = int(np.median(crabs))
    most_common.append(mean)
    most_common.append(median)
    total_fuels = []
    for ap in most_common:
        ap_fuel = 0
        for crab in crabs:
            if part_two:
                diff = abs(ap - crab)
                ap_fuel += sum(list(range(1, diff + 1)))
            else:
                ap_fuel += abs(ap - crab)

        total_fuels.append(ap_fuel)
    return total_fuels


if __name__ == '__main__':
    crabs = read_input()
    print(crabs)
    total_fuel = align_crabs(crabs)
    print(min(total_fuel))
