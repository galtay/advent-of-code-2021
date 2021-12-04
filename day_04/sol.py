import numpy as np


BOARD_SIZE = 5


def read_input_lines(file_path):
    with open(file_path, 'r') as fp:
        lines = [line.strip() for line in fp.readlines()]
    return lines

def parse_input_lines(lines):
    draws = [int(el) for el in lines[0].split(',')]
    num_boards = len(lines[1:]) // (BOARD_SIZE + 1)
    boards = np.zeros((num_boards, BOARD_SIZE, BOARD_SIZE), dtype=int)

    ii_row = 0
    ii_board = 0
    for line in lines[2:]:
        if ii_row != BOARD_SIZE:
            line = [int(el) for el in line.split(' ') if el != '']
            for ii_col in range(BOARD_SIZE):
                boards[ii_board, ii_row, ii_col] = line[ii_col]
        if ii_row == BOARD_SIZE:
            ii_board += 1
        ii_row += 1
        if ii_row == 6:
            ii_row = 0

    return draws, boards



lines = read_input_lines("input.txt")
draws, boards = parse_input_lines(lines)
num_boards = boards.shape[0]
marks = np.zeros_like(boards)


def check_mark_for_win(mark):
    for axis in [0, 1]:
        if any(mark.sum(axis=axis) == BOARD_SIZE):
            return True
    return False


for draw in draws:

    mark_add = (boards==draw).astype(int)
    marks += mark_add
    marks[marks > 1] = 1

    for iboard in range(marks.shape[0]):
        has_win = check_mark_for_win(marks[iboard])
        if has_win:
            break

    if has_win:
        break

board = boards[iboard]
mark = marks[iboard]
sum_unmarked = board[mark==0].sum()
final = draw * sum_unmarked
print('final: ', final)



board_wins = []
board_metas = []
marks = np.zeros_like(boards)

for ii_draw, draw in enumerate(draws):

    for iboard in range(marks.shape[0]):

        if iboard in board_wins:
            continue

        mark_add = (boards[iboard]==draw).astype(int)
        marks[iboard] += mark_add
        marks[marks>1] = 1

        has_win = check_mark_for_win(marks[iboard])
        if has_win:
            board_wins.append(iboard)
            board_metas.append((iboard, draw, ii_draw))

iboard = board_wins[-1]
board = boards[iboard]
mark = marks[iboard]

sum_unmarked = board[mark==0].sum()
final_draw = board_metas[-1][1]
final = final_draw * sum_unmarked
print('final: ', final)
