import copy

from .attacks import get_attacked_squares
from .check import is_white_checked, is_black_checked


def piece_moved(key, game):
    original_piece = game['0'][key]
    for k in game.keys():
        if game[k][key] != original_piece:
            return True
    return False


def is_square_attacked(key, board, color):
    for k in board.keys():
        if board[k]['color'] != color:
            if key in get_attacked_squares(board, k):
                return True
    return False


def get_white_king_castle_king_side(key, game):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    if 'h1' in board.keys():
        if board['h1'] == {'type': 'R', 'color': 'white'}:
            if 'f1' not in board.keys() and 'g1' not in board.keys():
                if not is_white_checked(game):
                    if not piece_moved('e1', game) \
                            and not piece_moved('h1', game):
                        if not is_square_attacked('f1', board, 'white') \
                                and not is_square_attacked(
                                    'g1', board, 'white'):
                            return ['g1']
    return []


def get_white_king_castle_queen_side(key, game):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    if 'a1' in board.keys():
        if board['a1'] == {'type': 'R', 'color': 'white'}:
            if 'b1' not in board.keys() and 'c1' not in board.keys() \
                    and 'd1' not in board.keys():
                if not is_white_checked(game):
                    if not piece_moved('a1', game) \
                            and not piece_moved('e1', game):
                        if not is_square_attacked('c1', board, 'white') \
                                and not is_square_attacked(
                                    'd1', board, 'white'):
                            return ['c1']
    return []


def get_black_king_castle_king_side(key, game):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    if 'h8' in board.keys():
        if board['h8'] == {'type': 'R', 'color': 'black'}:
            if 'f8' not in board.keys() and 'g8' not in board.keys():
                if not is_black_checked(game):
                    if not piece_moved('h8', game) \
                            and not piece_moved('e8', game):
                        if not is_square_attacked('f8', board, 'black') \
                                and not is_square_attacked(
                                    'g8', board, 'black'):
                            return ['g8']
    return []


def get_black_king_castle_queen_side(key, game):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    if 'a8' in board.keys():
        if board['a8'] == {'type': 'R', 'color': 'black'}:
            if 'b8' not in board.keys() and 'c8' not in board.keys() \
                    and 'd8' not in board.keys():
                if not is_black_checked(game):
                    if not piece_moved('a8', game) \
                            and not piece_moved('e8', game):
                        if not is_square_attacked('c8', board, 'black') \
                                and not is_square_attacked(
                                    'd8', board, 'black'):
                            return ['c8']
    return []


def get_castle_moves(key, game):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    if board[key]['type'] != 'K':
        return []
    else:
        if board[key]['color'] == 'white':
            if key != 'e1':
                return []
            else:
                return get_white_king_castle_king_side(key, game) \
                    + get_white_king_castle_queen_side(key, game)
        else:
            if key != 'e8':
                return []
            else:
                return get_black_king_castle_king_side(key, game) \
                    + get_black_king_castle_queen_side(key, game)
