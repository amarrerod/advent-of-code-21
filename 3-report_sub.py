
import numpy as np

filename = 'data/input_3.txt'


def read_input(input_filename=filename):
    with open(input_filename, 'r') as f:
        lines = f.read().splitlines()
    return lines


def process_report(input_filename=filename):
    cols = 12
    zeros = np.zeros(cols)
    ones = np.zeros(cols)
    gamma = ''
    epsilon = ''
    with open(input_filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            for i in range(cols):
                if line[i] == '1':
                    ones[i] += 1
                else:
                    zeros[i] += 1
        for z, o in zip(zeros, ones):
            if z > o:
                gamma += '0'
                epsilon += '1'
            else:
                gamma += '1'
                epsilon += '0'
        gamma = int(gamma, 2)
        epsilon = int(epsilon, 2)
        return gamma * epsilon


def filter_data(data, i, oxygen=True):
    ones = 0
    zeros = 0
    def filter_zeros(data): return filter(lambda x: x[i] == '0', data)
    def filter_ones(data): return filter(lambda x: x[i] == '1', data)
    for line in data:
        if line[i] == '1':
            ones += 1
        else:
            zeros += 1
    if oxygen:
        if ones >= zeros:
            return list(filter_ones(data))
        else:
            return list(filter_zeros(data))
    else:
        if ones >= zeros:
            return list(filter_zeros(data))
        else:
            return list(filter_ones(data))


def oxygen_c02_report(data):
    remaining_oxygen = data.copy()
    remaining_co2 = data.copy()
    i = 0
    done_yet = False
    while not done_yet:
        # First the oxygen
        if len(remaining_oxygen) != 1:
            remaining_oxygen = filter_data(remaining_oxygen, i)
        # Second the Co2
        if len(remaining_co2) != 1:
            remaining_co2 = filter_data(remaining_co2, i, oxygen=False)
        i += 1
        if len(remaining_oxygen) == 1 and len(remaining_co2) == 1:
            done_yet = True

    print(remaining_oxygen)
    print(remaining_co2)
    print(int(remaining_co2[0], 2) * int(remaining_oxygen[0], 2))


if __name__ == '__main__':
    process_report(filename)
    lines = read_input()
    oxygen_c02_report(lines)
