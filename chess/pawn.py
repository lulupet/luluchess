from .utils import (
    get_next_column,
    get_next_row,
    get_previous_column,
    get_previous_row
)


def get_pawn_moves(key, color):
    moves = []
    if color == 'white':
        moves.append(key[0] + get_next_row(key[1]))
        if key[0] != 'a':
            moves.append(get_previous_column(key[0]) + get_next_row(key[1]))
        if key[0] != 'h':
            moves.append(get_next_column(key[0]) + get_next_row(key[1]))
        if key[1] == '2':
            moves.append(key[0] + get_next_row(get_next_row(key[1])))
    else:
        moves.append(key[0] + get_previous_row(key[1]))
        if key[0] != 'a':
            moves.append(
                get_previous_column(key[0]) + get_previous_row(key[1]))
        if key[0] != 'h':
            moves.append(get_next_column(key[0]) + get_previous_row(key[1]))
        if key[1] == '7':
            moves.append(key[0] + get_previous_row(get_previous_row(key[1])))
    return moves
