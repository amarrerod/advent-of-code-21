import numpy as np

filename = 'data/input_4.txt'


def read_input(input_filename=filename):
    random_numbers = []
    with open(input_filename, 'r') as file:
        random_numbers = [int(x) for x in file.readline().split(',')]
        file.readline()
        matrix = [line for line in file.readlines() if line != '\n']
        idx = 0
        counter = 0
        grouped_matrix = {}
        while idx < len(matrix):
            grouped_matrix[counter] = np.array([
                [int(x) for x in matrix[idx].split()],
                [int(x) for x in matrix[idx + 1].split()],
                [int(x) for x in matrix[idx + 2].split()],
                [int(x) for x in matrix[idx + 3].split()],
                [int(x) for x in matrix[idx + 4].split()]
            ])
            idx += 5
            counter += 1
    return random_numbers, grouped_matrix


def check_winner(matrix):
    """
        Comprueba si una matrix ha resultado ganadora.
        Busca 5 valores -1 en las filas o en las columnas.
    """
    for r in matrix:
        if sum(r) == -5:
            return True
    for i in range(5):
        column_sum = 0
        for j in range(5):
            column_sum += matrix[j][i]
        if column_sum == -5:
            return True
    return False


def sum_not_marked(matrix):
    """
        Función que permite calcular
        la suma final de los valores no marcados por el bingo
    """
    total_sum = 0
    for i in range(len(matrix)):
        for j in range(5):
            if matrix[i][j] != -1:
                total_sum += matrix[i][j]
    return total_sum


def resolve(random_numbers, grouped_matrix):
    """
        Resuelve los ejercicios del día 4. Parte 1 y Parte 2.
    """
    scores_in_order = []
    winners = []
    for number in random_numbers:
        for key, matrix in grouped_matrix.items():
            print(
                f'Looking for number: {number} in matrix number: {key}\n{matrix}')
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == number:
                        matrix[i][j] = -1
            if check_winner(matrix) and key not in winners:
                print(f"Winner found in key: {key}")
                scores_in_order.append(number * sum_not_marked(matrix))
                winners.append(key)
    return scores_in_order[0], scores_in_order[-1]


if __name__ == '__main__':
    random_numbers, grouped_matrix = read_input()
    score_part_one, score_part_two = resolve(random_numbers, grouped_matrix)
    print(score_part_one, score_part_two)
