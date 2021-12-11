
filename = 'data/input_10.txt'


def read_input(input_filename=filename):
    with open(input_filename, 'r') as file:
        return file.read().splitlines()


def find_syntax_errors(lines):
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    corresponding_opening = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    score = 0
    incompleted_lines = []
    for line in lines:
        stack = []
        corrupted = False
        for character in line:
            if character in ('(', '{', '[', '<'):
                stack.append(character)
            else:
                open_char = stack.pop()
                if corresponding_opening[character] != open_char:
                    score += scores[character]
                    corrupted = True
                    break
        if not corrupted:
            incompleted_lines.append(line)

    print(f'Final score is: {score}')
    return score, incompleted_lines


def find_sequence(lines):
    scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    corresponding_close = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    file_scores = []
    for line in lines:
        stack = []
        line_score = 0
        for character in line[::-1]:
            if character in (')', '}', ']', '>'):
                stack.append(character)
            else:
                if stack:
                    stack.pop()
                else:
                    line_score = (line_score * 5) + \
                        scores[corresponding_close[character]]
        file_scores.append(line_score)

    file_scores = sorted(file_scores)
    final_score = file_scores[len(file_scores) // 2]
    print(final_score)
    return final_score


if __name__ == '__main__':
    lines = read_input()
    _, incompleted_lines = find_syntax_errors(lines)
    find_sequence(incompleted_lines)
