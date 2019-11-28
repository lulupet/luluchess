import copy
from random import randint

from utils.en_passant import en_passant
from utils.castle import castle_moves
from utils.utils import *


def moves_on_board(piece, board):
    possible_moves = piece.get_possible_moves()
    filtered_moves = []
    for move in possible_moves:
        square = board.get_square(move)
        if square == 'empty' or square.color != piece.color:
            if piece.type == 'bishop':
                if move in available_diagonal(piece.column, piece.row, board):
                    filtered_moves.append({"type" : "normal", "start" : piece.column + piece.row, "end" : move})
            elif piece.type == 'rook':
                if move in available_line(piece.column, piece.row, board):
                    filtered_moves.append({"type" : "normal", "start" : piece.column + piece.row, "end" : move})
            elif piece.type == 'queen':
                if move in available_line(piece.column, piece.row, board):
                    filtered_moves.append({"type" : "normal", "start" : piece.column + piece.row, "end" : move})
                if move in available_diagonal(piece.column, piece.row, board):
                    filtered_moves.append({"type" : "normal", "start" : piece.column + piece.row, "end" : move})
            elif piece.type == 'knight':
                filtered_moves.append({"type" : "normal", "start" : piece.column + piece.row, "end" : move})
            elif piece.type == 'king':
                filtered_moves.append({"type" : "normal", "start" : piece.column + piece.row, "end" : move})
        if piece.type == 'pawn':                  
            if move[0] != piece.column and square != 'empty' and square.color != piece.color:
                filtered_moves.append({"type" : "normal", "start" : piece.column + piece.row, "end" : move})
            if piece.color == 'white':
                if move[1] == '4' and piece.row == '2':
                    if board.get_square(piece.column + '3') == 'empty' and square == 'empty':
                        filtered_moves.append({"type" : "normal", "start" : piece.column + piece.row, "end" : move})
                else:
                    if move[0] == piece.column and square == 'empty':
                        filtered_moves.append({"type" : "normal", "start" : piece.column + piece.row, "end" : move})
            else:
                if move[1] == '5' and piece.row == '7':
                    if board.get_square(piece.column + '6') == 'empty' and square == 'empty':
                        filtered_moves.append({"type" : "normal", "start" : piece.column + piece.row, "end" : move})
                else:
                    if move[0] == piece.column and square == 'empty':
                        filtered_moves.append({"type" : "normal", "start" : piece.column + piece.row, "end" : move})
    
    return filtered_moves

def all_moves_on_board(piece, game):
    return moves_on_board(piece, game.board) + en_passant(piece, game) + castle_moves(piece, game)


def move(piece, move, game):
    if move["type"] == "normal":
        square = game.board.get_square(move["end"])
        if square != 'empty':
            game.board.erase(square)
        if piece.type == 'pawn' and move["end"][1] in ['1', '8']:
            game.board.erase(game.board.get_square(move["start"]))
            game.board.promote(move["end"], piece.color)
        else:
            piece.column = move["end"][0]
            piece.row = move["end"][1]
    elif move["type"] == "en_passant":
        if piece.color == 'white':
            game.board.erase(game.board.get_square(move["end"][0] + previous_row(move["end"][1])))
        else:
            game.board.erase(game.board.get_square(move["end"][0] + next_row(move["end"][1])))
        piece.column = move["end"][0]
        piece.row = move["end"][1]
    else:
        if move["end"] == 'G1':
            rook = game.board.get_square('H1')
            rook.column = 'F'
            rook.row = '1'
        elif move["end"] == 'C1':
            rook = game.board.get_square('A1')
            rook.column = 'D'
            rook.row = '1'
        elif move["end"] == 'G8':
            rook = game.board.get_square('H8')
            rook.column = 'F'
            rook.row = '8'
        else:
            rook = game.board.get_square('A8')
            rook.column = 'D'
            rook.row = '8'
        piece.column = move["end"][0]
        piece.row = move["end"][1]
    
    step = copy.deepcopy(game.board)
    game.historic.append(step)


def legal_moves(piece, game):
    legal_moves = []
    for movement in all_moves_on_board(piece, game):
        game_temp = copy.deepcopy(game)
        move(game_temp.board.get_square(piece.column + piece.row), movement, game_temp)
        if piece.color == 'white':
            if not game_temp.board.is_white_checked():
                legal_moves.append(movement)
        else:
            if not game_temp.board.is_black_checked():
                legal_moves.append(movement)
    
    return legal_moves


def get_all_moves(game, color): ##CHANGE MOVE TYPE
    all_moves = []
    if color == 'black':
        for piece in game.board.get_black_pieces():
            all_moves += legal_moves(piece, game)
    else:
        for piece in game.board.get_black_pieces():
            all_moves += legal_moves(piece, game)
    return all_moves


def get_next_move(game, color):
    all_moves = get_all_moves(game, color)
    index = randint(0, len(all_moves) - 1)
    return all_moves[index]