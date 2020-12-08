import copy

from .attacks import get_attacked_squares


def get_white_king_square(board):
    for key in board.keys():
        if board[key]['type'] == 'K' and board[key]['color'] == 'white':
            return key


def get_black_king_square(board):
    for key in board.keys():
        if board[key]['type'] == 'K' and board[key]['color'] == 'black':
            return key


def is_white_checked(game):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    white_king_square = get_white_king_square(board)
    for key in board.keys():
        if board[key]['color'] == 'black':
            if white_king_square in get_attacked_squares(board, key):
                return True
    return False


def is_black_checked(game):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    black_king_square = get_black_king_square(board)
    for key in board.keys():
        if board[key]['color'] == 'white':
            if black_king_square in get_attacked_squares(board, key):
                return True
    return False
