from .check import is_white_checked, is_black_checked
from .moves import get_white_moves, get_black_moves


def is_pat(game, color):
    if color == 'white':
        if not is_white_checked(game):
            if len(get_white_moves(game)) == 0:
                return True
    if color == 'black':
        if not is_black_checked(game):
            if len(get_black_moves(game)) == 0:
                return True
    return False
