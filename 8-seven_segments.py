
from typing import Counter
filename = 'data/input_8.txt'


def read_input(input=filename):
    codes = Counter()
    with open(input, 'r') as file:
        for line in file.readlines():
            line = line.strip().split('|')[1]
            for token in line.split():
                if len(token) in (2, 3, 4, 7):
                    codes[token] += 1

    print(sum(codes.values()))
    return codes


if __name__ == '__main__':
    print(read_input())
