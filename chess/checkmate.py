from .check import is_white_checked, is_black_checked
from .moves import get_white_moves, get_black_moves


def is_white_checkmated(game):
    return is_white_checked(game) and len(get_white_moves(game)) == 0


def is_black_checkmated(game):
    return is_black_checked(game) and len(get_black_moves(game)) == 0
