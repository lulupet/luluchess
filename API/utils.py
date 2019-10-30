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
            if piece.type in ['bishop', 'queen']:
                if move in available_diagonal(piece.column, piece.row, board):
                    filtered_moves.append(move)
            elif piece.type in ['rook', 'queen']:
                if move in available_line(piece.column, piece.row, board):
                    filtered_moves.append(move)
            elif piece.type == 'pawn':
                if piece.color == 'white':
                    if move[1] == '4' and piece.row == '2':
                        if board.get_square(piece.column + '3') == 'empty':
                            filtered_moves.append(move)
                    else:
                        if move[0] == piece.column and square == 'empty':
                            filtered_moves.append(move)
                else:
                    if move[1] == '5' and piece.row == '7':
                        if board.get_square(piece.column + '6') == 'empty':
                            filtered_moves.append(move)
                    else:
                        filtered_moves.append(move)
            elif piece.type == 'knight':
                filtered_moves.append(move)
            else:
                filtered_moves.append(move)
        if piece.type == 'pawn':                  
            if move[0] != piece.column and square != 'empty' and square.color != piece.color:
                filtered_moves.append(move)
    
    return filtered_moves
            