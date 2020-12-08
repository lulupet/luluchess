from .utils import (
    get_previous_column,
    get_previous_row,
    get_next_column,
    get_next_row
)


def get_king_moves(key):
    moves = []
    if key[1] != '1':
        moves.append(key[0] + get_previous_row(key[1]))
        if key[0] != 'a':
            moves.append(
                get_previous_column(key[0]) + get_previous_row(key[1]))
        if key[0] != 'h':
            moves.append(get_next_column(key[0]) + get_previous_row(key[1]))
    if key[1] != '8':
        moves.append(key[0] + get_next_row(key[1]))
        if key[0] != 'a':
            moves.append(get_previous_column(key[0]) + get_next_row(key[1]))
        if key[0] != 'h':
            moves.append(get_next_column(key[0]) + get_next_row(key[1]))
    if key[0] != 'a':
        moves.append(get_next_column(key[0]) + key[1])
    if key[0] != 'h':
        moves.append(get_previous_column(key[0]) + key[1])
    return moves
