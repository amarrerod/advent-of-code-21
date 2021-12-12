import numpy as np

filename = 'data/input_11.txt'


def read_input(input_filename=filename):
    board = []
    with open(input_filename, 'r') as file:
        matrix = file.read().splitlines()
        for row in matrix:
            row = [int(x) for x in list(row)]
            board.append(row)

        return board, (len(board), len(board[0]))


def print_map(board):
    print(f"\n{'='*20}")
    for r in board:
        print(*r)
    print(f"{'='*20}")


def gen_adjacent_octopuses(board, size, x, y):
    max_x, max_y = size
    for diag_y in (-1, 0, 1):
        n_y = y + diag_y
        if n_y >= max_y or n_y < 0:
            continue
        for diag_x in (-1, 0, 1):
            n_x = x + diag_x
            if n_x >= max_x or n_x < 0:
                continue
            if n_x == x and n_y == y:
                continue
            yield n_x, n_y, board[n_x][n_y]


def iterate_through_board(board, size):
    max_x, max_y = size
    for y in range(max_y):
        for x in range(max_x):
            yield x, y, board[x][y]


def modelise(board, board_size):
    new_board = board.copy()
    for x, y, level in iterate_through_board(board, board_size):
        new_board[x][y] = level + 1

    has_flashed = set([])
    to_flash = {
        (x, y)
        for x, y, level in iterate_through_board(new_board, board_size)
        if level > 9
    }

    while to_flash:
        (x, y) = to_flash.pop()
        if (x, y) in has_flashed:
            continue
        for n_x, n_y, level in gen_adjacent_octopuses(new_board, board_size, x, y):
            new_level = level + 1
            new_board[n_x][n_y] = new_level
            if new_level > 9:  # To Flash
                to_flash.add((n_x, n_y))

        has_flashed.add((x, y))

    for (x, y) in has_flashed:
        new_board[x][y] = 0

    return new_board, len(has_flashed)


def run(board, board_size, steps=None):
    counter = 0
    if not steps:  # Part two
        counter = 1
        keep_running = True
        while keep_running:
            board, flashes = modelise(board, board_size)
            print_map(board)
            if flashes == board_size[0] * board_size[1]:
                break
            else:
                counter += 1
    else:
        for _ in range(steps):
            board, flashes = modelise(board, board_size)
            print_map(board)
            counter += flashes

    return counter


if __name__ == '__main__':
    board, size = read_input()
    print_map(board)
    flashes = run(board, size)
    print(flashes)
