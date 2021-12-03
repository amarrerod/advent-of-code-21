
import numpy as np

filename = 'data/input_3.txt'


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


if __name__ == '__main__':
    process_report(filename)
