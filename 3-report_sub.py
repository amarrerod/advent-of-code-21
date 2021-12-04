
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


def oxygen_c02_report(data):
    cols = 12
    zeros = 0
    ones = 0
    remaining_oxygen = data.copy()
    remaining_co2 = data.copy()
    keep_searching = True
    i = 0
    while len(remaining_oxygen) != 1:
        zeros = 0
        ones = 0
        # First the oxygen
        if len(remaining_oxygen) != 1:
            for line in remaining_oxygen:
                if line[i] == '1':
                    ones += 1
                else:
                    zeros += 1
            if ones >= zeros:
                remaining_oxygen = list(
                    filter(lambda x: x[i] == '1', remaining_oxygen))
            else:
                remaining_oxygen = list(
                    filter(lambda x: x[i] == '0', remaining_oxygen))

        zeros = 0
        ones = 0
        # Second the Co2
        if len(remaining_co2) != 1:
            for line in remaining_co2:
                if line[i] == '1':
                    ones += 1
                else:
                    zeros += 1
            if ones >= zeros:
                remaining_co2 = list(
                    filter(lambda x: x[i] == '0', remaining_co2))
            else:
                remaining_co2 = list(
                    filter(lambda x: x[i] == '1', remaining_co2))

        i += 1
    print(remaining_oxygen)
    print(remaining_co2)
    print(int(remaining_co2[0], 2) * int(remaining_oxygen[0], 2))


if __name__ == '__main__':
    process_report(filename)
    lines = read_input()
    oxygen_c02_report(lines)
