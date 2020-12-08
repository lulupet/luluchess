import copy

from .utils import (
    get_next_column,
    get_previous_column,
    get_previous_row,
    get_next_row
)


def is_en_passant(game, start, end):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    return end[0] != start[0] and end not in board.keys()


def en_passant_eaten_pawn(start, end):
    return end[0] + start[1]


def get_en_passant_moves(key, game):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    if len(game) < 2 or board[key]['type'] != 'P':
        return []
    else:
        if board[key]['color'] == 'white':
            if key[1] != '5':
                return []
            else:
                last_board = copy.copy(game[str(max_key - 1)])
                if key[0] != 'a':
                    if get_previous_column(key[0]) + key[1] in board.keys():
                        if board[get_previous_column(key[0]) + key[1]] == \
                                {'type': 'P', 'color': 'black'}:
                            if get_previous_column(key[0]) + key[1] \
                                    not in last_board.keys():
                                if get_previous_column(key[0]) \
                                        + get_next_row(key[1]) \
                                        not in last_board.keys():
                                    return [
                                        get_previous_column(key[0]) +
                                        get_next_row(key[1])]
                if key[0] != 'h':
                    if get_next_column(key[0]) + key[1] in board.keys():
                        if board[get_next_column(key[0]) + key[1]] == \
                                {'type': 'P', 'color': 'black'}:
                            if get_next_column(key[0]) + key[1] \
                                    not in last_board.keys():
                                if get_next_column(key[0]) \
                                        + get_next_row(key[1]) \
                                        not in last_board.keys():
                                    return [get_next_column(key[0]) +
                                            get_next_row(key[1])]
        else:
            if key[1] != '4':
                return []
            else:
                last_board = copy.copy(game[str(max_key - 1)])
                if key[0] != 'a':
                    if get_previous_column(key[0]) + key[1] in board.keys():
                        if board[get_previous_column(key[0]) + key[1]] == \
                                {'type': 'P', 'color': 'white'}:
                            if get_previous_column(key[0]) + key[1] \
                                    not in last_board.keys():
                                if get_previous_column(key[0]) \
                                        + get_previous_row(key[1]) \
                                        not in last_board.keys():
                                    return [
                                        get_previous_column(key[0]) +
                                        get_previous_row(key[1])]
                if key[0] != 'h':
                    if get_next_column(key[0]) + key[1] in board.keys():
                        if board[get_next_column(key[0]) + key[1]] == \
                                {'type': 'P', 'color': 'white'}:
                            if get_next_column(key[0]) + key[1] \
                                    not in last_board.keys():
                                if get_next_column(key[0]) \
                                        + get_previous_row(key[1]) \
                                        not in last_board.keys():
                                    return [
                                        get_next_column(key[0])
                                        + get_previous_row(key[1])]
        return []
