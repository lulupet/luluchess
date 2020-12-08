from .utils import (
    get_next_column,
    get_next_row,
    get_previous_column,
    get_previous_row
)


def get_attacked_diagonals(key, board):
    attacked_diagonals = []
    i = key[0]
    j = key[1]
    found_attacked = False
    while i != 'h' and j != '8' and not found_attacked:
        i = get_next_column(i)
        j = get_next_row(j)
        if i + j in board.keys():
            if board[i + j]['color'] != board[key]['color']:
                attacked_diagonals.append(i + j)
                found_attacked = True
        else:
            attacked_diagonals.append(i + j)
    i = key[0]
    j = key[1]
    found_attacked = False
    while i != 'h' and j != '1' and not found_attacked:
        i = get_next_column(i)
        j = get_previous_row(j)
        if i + j in board.keys():
            if board[i + j]['color'] != board[key]['color']:
                attacked_diagonals.append(i + j)
                found_attacked = True
        else:
            attacked_diagonals.append(i + j)
    i = key[0]
    j = key[1]
    found_attacked = False
    while i != 'a' and j != '8' and not found_attacked:
        i = get_previous_column(i)
        j = get_next_row(j)
        if i + j in board.keys():
            if board[i + j]['color'] != board[key]['color']:
                attacked_diagonals.append(i + j)
                found_attacked = True
        else:
            attacked_diagonals.append(i + j)
    i = key[0]
    j = key[1]
    found_attacked = False
    while i != 'a' and j != '1' and not found_attacked:
        i = get_previous_column(i)
        j = get_previous_row(j)
        if i + j in board.keys():
            if board[i + j]['color'] != board[key]['color']:
                attacked_diagonals.append(i + j)
                found_attacked = True
        else:
            attacked_diagonals.append(i + j)
    return attacked_diagonals


def get_attacked_lines(key, board):
    attacked_lines = []
    i = key[0]
    j = key[1]
    found_attacked = False
    while i != 'a' and not found_attacked:
        i = get_previous_column(i)
        if i + j in board.keys():
            if board[i + j]['color'] != board[key]['color']:
                attacked_lines.append(i + j)
                found_attacked = True
        else:
            attacked_lines.append(i + j)
    i = key[0]
    j = key[1]
    found_attacked = False
    while i != 'h' and not found_attacked:
        i = get_next_column(i)
        if i + j in board.keys():
            if board[i + j]['color'] != board[key]['color']:
                attacked_lines.append(i + j)
                found_attacked = True
        else:
            attacked_lines.append(i + j)
    i = key[0]
    j = key[1]
    found_attacked = False
    while j != '1' and not found_attacked:
        j = get_previous_row(j)
        if i + j in board.keys():
            if board[i + j]['color'] != board[key]['color']:
                attacked_lines.append(i + j)
                found_attacked = True
        else:
            attacked_lines.append(i + j)
    i = key[0]
    j = key[1]
    found_attacked = False
    while j != '8' and not found_attacked:
        j = get_next_row(j)
        if i + j in board.keys():
            if board[i + j]['color'] != board[key]['color']:
                attacked_lines.append(i + j)
                found_attacked = True
        else:
            attacked_lines.append(i + j)
    return attacked_lines


def get_attacked_knight(key, board):
    attacked = []
    if key[1] != '1':
        if key[0] not in ['g', 'h']:
            i = get_next_column(get_next_column(key[0]))
            j = get_previous_row(key[1])
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
        if key[0] not in ['a', 'b']:
            i = get_previous_column(get_previous_column(key[0]))
            j = get_previous_row(key[1])
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
    if key[1] not in ['1', '2']:
        if key[0] != 'h':
            i = get_next_column(key[0])
            j = get_previous_row(get_previous_row(key[1]))
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
        if key[0] != 'a':
            i = get_previous_column(key[0])
            j = get_previous_row(get_previous_row(key[1]))
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
    if key[1] != '8':
        if key[0] != 'h':
            i = get_next_column(key[0])
            j = get_next_row(get_next_row(key[1]))
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
        if key[0] != 'a':
            i = get_previous_column(key[0])
            j = get_next_row(get_next_row(key[1]))
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
    if key[1] not in ['7', '8']:
        if key[0] not in ['g', 'h']:
            i = get_next_column(key[0])
            j = get_next_row(key[1])
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
        if key[0] not in ['a', 'b']:
            i = get_previous_column(key[0])
            j = get_next_row(key[1])
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
    return attacked


def get_attacked_king(key, board):
    attacked = []
    if key[1] != '1':
        i = key[0]
        j = get_previous_row(key[1])
        if i + j in board.keys():
            if board[i + j]['color'] != board[key]['color']:
                attacked.append(i + j)
        else:
            attacked.append(i + j)
        if key[0] != 'a':
            i = get_previous_column(key[0])
            j = get_previous_row(key[1])
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
        if key[0] != 'h':
            i = get_next_column(key[0])
            j = get_previous_row(key[1])
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
    if key[1] != '8':
        i = key[0]
        j = get_next_row(key[1])
        if i + j in board.keys():
            if board[i + j]['color'] != board[key]['color']:
                attacked.append(i + j)
        else:
            attacked.append(i + j)
        if key[0] != 'a':
            i = get_previous_column(key[0])
            j = get_next_row(key[1])
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
        if key[0] != 'h':
            i = get_next_column(key[0])
            j = get_next_row(key[1])
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
    if key[0] != 'a':
        i = get_next_column(key[0])
        j = key[1]
        if i + j in board.keys():
            if board[i + j]['color'] != board[key]['color']:
                attacked.append(i + j)
        else:
            attacked.append(i + j)
    if key[0] != 'h':
        i = get_previous_column(key[0])
        j = key[1]
        if i + j in board.keys():
            if board[i + j]['color'] != board[key]['color']:
                attacked.append(i + j)
        else:
            attacked.append(i + j)
    return attacked


def get_attacked_pawn(key, board):
    attacked = []
    if board[key]['color'] == 'white':
        if key[0] != 'a':
            i = get_previous_column(key[0])
            j = get_next_row(key[1])
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
        if key[0] != 'h':
            i = get_next_column(key[0])
            j = get_next_row(key[1])
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
    else:
        if key[0] != 'a':
            i = get_previous_column(key[0])
            j = get_previous_row(key[1])
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
        if key[0] != 'h':
            i = get_next_column(key[0])
            j = get_previous_row(key[1])
            if i + j in board.keys():
                if board[i + j]['color'] != board[key]['color']:
                    attacked.append(i + j)
            else:
                attacked.append(i + j)
    return attacked


def get_attacked_squares(board, key):
    if board[key]['type'] == 'B':
        attacked = get_attacked_diagonals(key, board)
    elif board[key]['type'] == 'R':
        attacked = get_attacked_lines(key, board)
    elif board[key]['type'] == 'Q':
        attacked = get_attacked_lines(key, board)
        attacked += get_attacked_diagonals(key, board)
    elif board[key]['type'] == 'C':
        attacked = get_attacked_knight(key, board)
    elif board[key]['type'] == 'K':
        attacked = get_attacked_king(key, board)
    else:
        attacked = get_attacked_pawn(key, board)
    return attacked
