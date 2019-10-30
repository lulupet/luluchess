import copy
from random import randint

ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']
COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def next_column(column):
    return COLUMNS[COLUMNS.index(column) + 1]

def previous_column(column):
    return COLUMNS[COLUMNS.index(column) - 1]

def next_row(row):
    return ROWS[ROWS.index(row) + 1]

def previous_row(row):
    return ROWS[ROWS.index(row) - 1]

def diagonals(column, row):
    diag = []
    i = column
    j = row
    while i != 'H' and j != '8':
        i = next_column(i)
        j = next_row(j)
        diag.append(i + j)
    i = column
    j = row
    while i != 'H' and j != '1':
        i = next_column(i)
        j = previous_row(j)
        diag.append(i + j)
    i = column
    j = row
    while i != 'A' and j != '8':
        i = previous_column(i)
        j = next_row(j)
        diag.append(i + j)
    i = column
    j = row
    while i != 'A' and j != '1':
        i = previous_column(i)
        j = previous_row(j)
        diag.append(i + j)
    return diag

def available_diagonal(column, row, board):
    available_diag = []
    i = column
    j = row
    found_obstacle = False
    while i != 'H' and j != '8' and not found_obstacle:
        i = next_column(i)
        j = next_row(j)
        if board.get_square(i + j) == 'empty':
            available_diag.append(i + j)
        else:
            found_obstacle = True
    i = column
    j = row
    found_obstacle = False
    while i != 'H' and j != '1' and not found_obstacle:
        i = next_column(i)
        j = previous_row(j)
        if board.get_square(i + j) == 'empty':
            available_diag.append(i + j)
        else:
            found_obstacle = True
    i = column
    j = row
    found_obstacle = False
    while i != 'A' and j != '8' and not found_obstacle:
        i = previous_column(i)
        j = next_row(j)
        if board.get_square(i + j) == 'empty':
            available_diag.append(i + j)
        else:
            found_obstacle = True
    i = column
    j = row
    found_obstacle = False
    while i != 'A' and j != '1' and not found_obstacle:
        i = previous_column(i)
        j = previous_row(j)
        if board.get_square(i + j) == 'empty':
            available_diag.append(i + j)
        else:
            found_obstacle = True
    return available_diag


def available_line(column, row, board):
    available = []
    i = column
    j = row
    found_obstacle = False
    while i != 'A' and not found_obstacle:
        i = previous_column(i)
        if board.get_square(i + j) == 'empty':
            available.append(i + j)
        else:
            found_obstacle = True
    i = column
    found_obstacle = False
    while i != 'H' and not found_obstacle:
        i = next_column(i)
        if board.get_square(i + j) == 'empty':
            available.append(i + j)
        else:
            found_obstacle = True
    i = column
    found_obstacle = False
    while j != '1' and not found_obstacle:
        j = previous_row(j)
        if board.get_square(i + j) == 'empty':
            available.append(i + j)
        else:
            found_obstacle = True
    j = row
    found_obstacle = False
    while j != '8' and not found_obstacle:
        j = next_row(j)
        if board.get_square(i + j) == 'empty':
            available.append(i + j)
        else:
            found_obstacle = True
    
    return available


def filter_moves(piece, board):
    possible_moves = piece.get_possible_moves()
    filtered_moves = []
    for move in possible_moves:
        square = board.get_square(move)
        if square == 'empty' or square.color != piece.color:
            if piece.type == 'bishop':
                if move in available_diagonal(piece.column, piece.row, board):
                    filtered_moves.append(move)
            elif piece.type == 'rook':
                if move in available_line(piece.column, piece.row, board):
                    filtered_moves.append(move)
            elif piece.type == 'queen':
                if move in available_line(piece.column, piece.row, board):
                    filtered_moves.append(move)
                if move in available_diagonal(piece.column, piece.row, board):
                    filtered_moves.append(move)
            elif piece.type == 'knight':
                filtered_moves.append(move)
            elif piece.type == 'king':
                filtered_moves.append(move)
        if piece.type == 'pawn':                  
            if move[0] != piece.column and square != 'empty' and square.color != piece.color:
                filtered_moves.append(move)
            if piece.color == 'white':
                if move[1] == '4' and piece.row == '2':
                    if board.get_square(piece.column + '3') == 'empty' and square == 'empty':
                        filtered_moves.append(move)
                else:
                    if move[0] == piece.column and square == 'empty':
                        filtered_moves.append(move)
            else:
                if move[1] == '5' and piece.row == '7':
                    if board.get_square(piece.column + '6') == 'empty' and square == 'empty':
                        filtered_moves.append(move)
                else:
                    if move[0] == piece.column and square == 'empty':
                        filtered_moves.append(move)
    
    return filtered_moves



def get_attacked_diagonal(piece, board):
    attacked_diag = []
    i = piece.column
    j = piece.row
    found_attacked = False
    while i != 'H' and j != '8' and not found_attacked:
        i = next_column(i)
        j = next_row(j)
        square = board.get_square(i + j)
        if square != 'empty':
            if square.color != piece.color:
                attacked_diag.append(i + j)
                found_attacked = True
    i = piece.column
    j = piece.row
    found_attacked = False
    while i != 'H' and j != '1' and not found_attacked:
        i = next_column(i)
        j = previous_row(j)
        square = board.get_square(i + j)
        if square != 'empty':
            if square.color != piece.color:
                attacked_diag.append(i + j)
                found_attacked = True
    i = piece.column
    j = piece.row
    found_attacked = False
    while i != 'A' and j != '8' and not found_attacked:
        i = previous_column(i)
        j = next_row(j)
        square = board.get_square(i + j)
        if square != 'empty':
            if square.color != piece.color:
                attacked_diag.append(i + j)
                found_attacked = True
    i = piece.column
    j = piece.row
    found_attacked = False
    while i != 'A' and j != '1' and not found_attacked:
        i = previous_column(i)
        j = previous_row(j)
        square = board.get_square(i + j)
        if square != 'empty':
            if square.color != piece.color:
                attacked_diag.append(i + j)
                found_attacked = True
    return attacked_diag


def get_attacked_line(piece, board):
    attacked_line = []
    i = piece.column
    j = piece.row
    found_attacked = False
    while i != 'A' and not found_attacked:
        i = previous_column(i)
        square = board.get_square(i + j)
        if square != 'empty':
            if square.color != piece.color:
                attacked_line.append(i + j)
                found_attacked = True
    i = piece.column
    found_attacked = False
    while i != 'H' and not found_attacked:
        i = next_column(i)
        square = board.get_square(i + j)
        if square != 'empty':
            if square.color != piece.color:
                attacked_line.append(i + j)
                found_attacked = True
    i = piece.column
    found_attacked = False
    while j != '1' and not found_attacked:
        j = previous_row(j)
        square = board.get_square(i + j)
        if square != 'empty':
            if square.color != piece.color:
                attacked_line.append(i + j)
                found_attacked = True
    j = piece.row
    found_attacked = False
    while j != '8' and not found_attacked:
        j = next_row(j)
        square = board.get_square(i + j)
        if square != 'empty':
            if square.color != piece.color:
                attacked_line.append(i + j)
                found_attacked = True
    
    return attacked_line


def attacked_pieces(piece, board):
    attacked = []
    if piece.type == 'bishop':
        attacked += get_attacked_diagonal(piece, board)
    elif piece.type == 'rook':
        attacked += get_attacked_line(piece, board)
    elif piece.type == 'queen':
        attacked += get_attacked_line(piece, board)
        attacked += get_attacked_diagonal(piece, board)
    elif piece.type == 'knight':
        for move in piece.get_possible_moves():
            square = board.get_square(move)
            if square != 'empty':
                if square.color != piece.color:
                    attacked.append(move)
    elif piece.type == 'king':
        for move in piece.get_possible_moves():
            square = board.get_square(move)
            if square != 'empty':
                if square.color != piece.color:
                    attacked.append(move)
    else:
        for move in piece.get_possible_moves():
            if move[0] != piece.column:
                square = board.get_square(move)
                if square != 'empty':
                    if square.color != piece.color:
                        attacked.append(move)
    
    return attacked


def filter_check(piece, board):
    filtered_check = []
    for movement in filter_moves(piece, board):
        board_temp = copy.deepcopy(board)
        move(board_temp.get_square(piece.column + piece.row), movement, board_temp)
        if piece.color == 'white':
            if not board_temp.is_white_checked():
                filtered_check.append(movement)
        else:
            if not board_temp.is_black_checked():
                filtered_check.append(movement)
    
    return filtered_check

def move(piece, move, board):
    square = board.get_square(move[0] + move[1])
    if square != 'empty':
        board.erase(square)
    if piece.type == 'pawn' and move[1] in ['1', '8']:
        board.erase(board.get_square(piece.column + piece.row))
        board.promote(move[0] + move[1], piece.color)
    else:
        piece.column = move[0]
        piece.row = move[1]


def get_next_move(board, color):
    if color == 'black':
        all_moves = []
        for piece in board.get_black_pieces():
            for move in filter_check(piece, board):
                all_moves.append({
                    'start': piece.column + piece.row,
                    'end': move
                })
    else:
        all_moves = []
        for piece in board.get_white_pieces():
            for move in filter_check(piece, board):
                all_moves.append({
                    'start': piece.column + piece.row,
                    'end': move
                })
    index = randint(0, len(all_moves) - 1)
    return all_moves[index]
    