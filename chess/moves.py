import copy
from random import randint

from .castle import get_castle_moves
from .check import is_white_checked, is_black_checked
from .en_passant import (
    en_passant_eaten_pawn,
    get_en_passant_moves,
    is_en_passant
)
from .king import get_king_moves
from .knight import get_knight_moves
from .pawn import get_pawn_moves
from .utils import (
    get_lines,
    get_available_lines,
    get_diagonals,
    get_available_diagonals
)


def make_move(game, start, end):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    if board[start]['type'] == 'K':
        if start == 'e1' and end == 'g1':
            del board['e1']
            board['g1'] = {
                'type': 'K',
                'color': 'white'
            }
            del board['h1']
            board['f1'] = {
                'type': 'R',
                'color': 'white'
            }
            game[str(max_key + 1)] = board
            return game
        elif start == 'e1' and end == 'c1':
            del board['e1']
            board['c1'] = {
                'type': 'K',
                'color': 'white'
            }
            del board['a1']
            board['d1'] = {
                'type': 'R',
                'color': 'white'
            }
            game[str(max_key + 1)] = board
            return game
        elif start == 'e8' and end == 'g8':
            del board['e8']
            board['g8'] = {
                'type': 'K',
                'color': 'black'
            }
            del board['h8']
            board['f8'] = {
                'type': 'R',
                'color': 'black'
            }
            game[str(max_key + 1)] = board
            return game
        elif start == 'e8' and end == 'c8':
            del board['e8']
            board['c8'] = {
                'type': 'K',
                'color': 'black'
            }
            del board['a8']
            board['d8'] = {
                'type': 'R',
                'color': 'black'
            }
            game[str(max_key + 1)] = board
            return game
    if board[start]['type'] == 'P':
        if end[1] == '8':
            del board[start]
            board[end] = {
                'type': 'Q',
                'color': 'white'
            }
            game[str(max_key + 1)] = board
            return game
        elif end[1] == '1':
            del board[start]
            board[end] = {
                'type': 'Q',
                'color': 'black'
            }
            game[str(max_key + 1)] = board
            return game
        if is_en_passant(game, start, end):
            eaten_pawn = en_passant_eaten_pawn(start, end)
            del board[eaten_pawn]
            board[end] = {
                'type': 'P',
                'color': board[start]['color']
            }
            del board[start]
            game[str(max_key + 1)] = board
            return game
    if end in board.keys():
        del board[end]
    board[end] = {
        'type': board[start]['type'],
        'color': board[start]['color']
    }
    del board[start]
    game[str(max_key + 1)] = board
    return game


def get_moves_on_empty_board(key, game):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    moves = []
    if board[key]['type'] == 'B':
        for square in get_diagonals(key):
            moves.append(square)
    if board[key]['type'] == 'R':
        for square in get_lines(key):
            moves.append(square)
    if board[key]['type'] == 'Q':
        for square in get_lines(key):
            moves.append(square)
        for square in get_diagonals(key):
            moves.append(square)
    if board[key]['type'] == 'C':
        for square in get_knight_moves(key):
            moves.append(square)
    if board[key]['type'] == 'K':
        for square in get_king_moves(key):
            moves.append(square)
    if board[key]['type'] == 'P':
        for square in get_pawn_moves(key, board[key]['color']):
            moves.append(square)
    return moves


def get_normal_moves(key, game):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    possible_moves = get_moves_on_empty_board(key, game)
    filtered_moves = []
    for move in possible_moves:
        if move in board.keys():
            end_square_available = board[move]['color'] != board[key]['color']
        else:
            end_square_available = True
        if end_square_available:
            if board[key]['type'] == 'B':
                if move in get_available_diagonals(key, board):
                    filtered_moves.append(move)
            elif board[key]['type'] == 'R':
                if move in get_available_lines(key, board):
                    filtered_moves.append(move)
            elif board[key]['type'] == 'Q':
                if move in get_available_diagonals(key, board):
                    filtered_moves.append(move)
                if move in get_available_lines(key, board):
                    filtered_moves.append(move)
            elif board[key]['type'] == 'C':
                if move in board.keys():
                    if board[move]['color'] != board[key]['color']:
                        filtered_moves.append(move)
                else:
                    filtered_moves.append(move)
            elif board[key]['type'] == 'K':
                if move in board.keys():
                    if board[move]['color'] != board[key]['color']:
                        filtered_moves.append(move)
                else:
                    filtered_moves.append(move)
            elif board[key]['type'] == 'P':
                if move[0] != key[0]:
                    if move in board.keys():
                        if board[move]['color'] != board[key]['color']:
                            filtered_moves.append(move)
                else:
                    if move not in board.keys():
                        if move[1] == '4' and key[1] == '2':
                            if key[0] + '3' not in board.keys():
                                filtered_moves.append(move)
                        elif move[1] == '5' and key[1] == '7':
                            if key[0] + '6' not in board.keys():
                                filtered_moves.append(move)
                        else:
                            filtered_moves.append(move)
    return filtered_moves


def get_all_moves_on_board(key, game):
    return get_normal_moves(key, game) \
        + get_en_passant_moves(key, game) + get_castle_moves(key, game)


def get_legal_moves(key, game):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    legal_moves = []
    for move in get_all_moves_on_board(key, game):
        temp_game = copy.copy(game)
        temp_game = make_move(temp_game, key, move)
        if board[key]['color'] == 'white':
            if not is_white_checked(temp_game):
                legal_moves.append(move)
        else:
            if not is_black_checked(temp_game):
                legal_moves.append(move)
    return legal_moves


def get_white_moves(game):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    white_moves = []
    for key in board.keys():
        if board[key]['color'] == 'white':
            legal_moves = [
                {'start': key, 'end': move}
                for move in get_legal_moves(key, game)
            ]
            white_moves += legal_moves
    return white_moves


def is_legal(game, start, end):
    return {'start': start, 'end': end} in get_white_moves(game)


def get_black_moves(game):
    max_key = max([int(k) for k in game.keys()])
    board = copy.copy(game[str(max_key)])
    black_moves = []
    for key in board.keys():
        if board[key]['color'] == 'black':
            legal_moves = [
                {'start': key, 'end': move}
                for move in get_legal_moves(key, game)
            ]
            black_moves += legal_moves
    return black_moves


def get_next_move(game):
    black_moves = get_black_moves(game)
    index = randint(0, len(black_moves) - 1)
    return black_moves[index]
