from utils import ROWS, COLUMNS, previous_column, next_column, previous_row, next_row, diagonals, filter_moves, attacked_pieces, filter_check

class Board:

    def __init__(self):
        self.knights = [
            Knight('white', '1', 'B'),
            Knight('white', '1', 'G'),
            Knight('black', '8', 'B'),
            Knight('black', '8', 'G')
        ]
        self.bishops = [
            Bishop('white', '1', 'C'),
            Bishop('white', '1', 'F'),
            Bishop('black', '8', 'C'),
            Bishop('black', '8', 'F')
        ]
        self.rooks = [
            Rook('white', '1', 'A'),
            Rook('white', '1', 'H'),
            Rook('black', '8', 'A'),
            Rook('black', '8', 'H')
        ]
        self.queens = [
            Queen('white', '1', 'D'),
            Queen('black', '8', 'D')
        ]
        self.kings = [
            King('white', '1', 'E'),
            King('black', '8', 'E')
        ]
        self.pawns = [
            Pawn('white', '2', 'A'),
            Pawn('white', '2', 'B'),
            Pawn('white', '2', 'C'),
            Pawn('white', '2', 'D'),
            Pawn('white', '2', 'E'),
            Pawn('white', '2', 'F'),
            Pawn('white', '2', 'G'),
            Pawn('white', '2', 'H'),
            Pawn('black', '7', 'A'),
            Pawn('black', '7', 'B'),
            Pawn('black', '7', 'C'),
            Pawn('black', '7', 'D'),
            Pawn('black', '7', 'E'),
            Pawn('black', '7', 'F'),
            Pawn('black', '7', 'G'),
            Pawn('black', '7', 'H'),
        ]

    def get_white_pawns(self):
        return [pawn for pawn in self.pawns if pawn.color == 'white']

    def get_white_bishops(self):
        return [bishop for bishop in self.bishops if bishop.color == 'white']
    
    def get_white_knights(self):
        return [knight for knight in self.knights if knight.color == 'white']
    
    def get_white_rooks(self):
        return [rook for rook in self.rooks if rook.color == 'white']
    
    def get_white_queens(self):
        return [queen for queen in self.queens if queen.color == 'white']
    
    def get_white_king(self):
        return self.kings[0] if self.kings[0].color == 'white' else self.kings[1]
    
    def get_white_pieces(self):
        return self.get_white_pawns() + self.get_white_bishops() + self.get_white_knights() + self.get_white_rooks() + self.get_white_queens() + [self.get_white_king()]

    def get_black_pawns(self):
        return [pawn for pawn in self.pawns if pawn.color == 'black']

    def get_black_bishops(self):
        return [bishop for bishop in self.bishops if bishop.color == 'black']
    
    def get_black_knights(self):
        return [knight for knight in self.knights if knight.color == 'black']
    
    def get_black_rooks(self):
        return [rook for rook in self.rooks if rook.color == 'black']
    
    def get_black_queens(self):
        return [queen for queen in self.queens if queen.color == 'black']
    
    def get_black_king(self):
        return self.kings[0] if self.kings[0].color == 'black' else self.kings[1]
    
    def get_black_pieces(self):
        return self.get_black_pawns() + self.get_black_bishops() + self.get_black_knights() + self.get_black_rooks() + self.get_black_queens() + [self.get_black_king()]

    def is_white_checked(self):
        for bishop in self.get_black_bishops():
            if self.get_white_king().column + self.get_white_king().row in attacked_pieces(bishop, self):
                return True
        for knight in self.get_black_knights():
            if self.get_white_king().column + self.get_white_king().row in attacked_pieces(knight, self):
                return True
        for rook in self.get_black_rooks():
            if self.get_white_king().column + self.get_white_king().row in attacked_pieces(bishop, self):
                return True
        for queen in self.get_black_queens():
            if self.get_white_king().column + self.get_white_king().row in attacked_pieces(queen, self):
                return True
        for pawn in self.get_black_pawns():
            if self.get_white_king().column + self.get_white_king().row in attacked_pieces(pawn, self):
                return True

        return False

    def is_black_checked(self):
        for bishop in self.get_white_bishops():
            if self.get_black_king().column + self.get_black_king().row in attacked_pieces(bishop, self):
                return True
        for knight in self.get_white_knights():
            if self.get_black_king().column + self.get_black_king().row in attacked_pieces(knight, self):
                return True
        for rook in self.get_white_rooks():
            if self.get_black_king().column + self.get_black_king().row in attacked_pieces(bishop, self):
                return True
        for queen in self.get_white_queens():
            if self.get_black_king().column + self.get_black_king().row in attacked_pieces(queen, self):
                return True
        for pawn in self.get_white_pawns():
            if self.get_black_king().column + self.get_black_king().row in attacked_pieces(pawn, self):
                return True
    
        return False
            
    def is_white_checkmated(self):
        for piece in self.get_white_pieces():
            if len(filter_check(piece, self)) >= 1:
                return False
        return True

    def is_black_checkmated(self):
        for piece in self.get_black_pieces():
            if len(filter_check(piece, self)) >= 1:
                return False
        return True

    def get_square(self, square):
        for pawn in self.pawns:
            if pawn.column + pawn.row == square:
                return pawn
        for knight in self.knights:
            if knight.column + knight.row == square:
                return knight
        for bishop in self.bishops:
            if bishop.column + bishop.row == square:
                return bishop
        for rook in self.rooks:
            if rook.column + rook.row == square:
                return rook
        for queen in self.queens:
            if queen.column + queen.row == square:
                return queen
        for king in self.kings:
            if king.column + king.row == square:
                return king
        
        return 'empty'

    def erase(self, square):
        if square.type == 'bishop':
            self.bishops.remove(square)
        elif square.type == 'knight':
            self.knights.remove(square)
        elif square.type == 'rook':
            self.rooks.remove(square)
        elif square.type == 'queen':
            self.queens.remove(square)
        elif square.type == 'pawn':
            self.pawns.remove(square)
    
    def promote(self, square, color):
        queen = (color, square[1], square[0])
        self.queens.append(queen)


class Piece:
    def __init__(self, color, row, column):
        self.color = color
        self.row = row
        self.column = column
        self.possible_moves = []


class Knight(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
        self.type = 'knight'
    
    def get_possible_moves(self):
        self.possible_moves = []
        if self.row != '1':
            if self.column not in ['G', 'H']:
                self.possible_moves.append(next_column(next_column(self.column)) + previous_row(self.row))
            if self.column not in ['A', 'B']:
                self.possible_moves.append(previous_column(previous_column(self.column)) + previous_row(self.row))
        if self.row not in ['1', '2']:
            if self.column != 'H':
                self.possible_moves.append(next_column(self.column) + previous_row(previous_row(self.row)))
            if self.column != 'A':
                self.possible_moves.append(previous_column(self.column) + previous_row(previous_row(self.row)))
        if self.row != '8':
            if self.column != 'H':
                self.possible_moves.append(next_column(self.column) + next_row(next_row(self.row)))
            if self.column != 'A':
                self.possible_moves.append(previous_column(self.column) + next_row(next_row(self.row)))
        if self.row not in ['7', '8']:
            if self.column not in ['G', 'H']:
                self.possible_moves.append(next_column(next_column(self.column)) + next_row(self.row))
            if self.column not in ['A', 'B']:
                self.possible_moves.append(previous_column(previous_column(self.column)) + next_row(self.row))
        
        return self.possible_moves



class Bishop(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
        self.type = 'bishop'
    
    def get_possible_moves(self):
        self.possible_moves = []
        self.possible_moves = [square for square in diagonals(self.column, self.row) if square != self.column + self.row]

        return self.possible_moves


class Rook(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
        self.type = 'rook'
    
    def get_possible_moves(self):
        self.possible_moves = []
        for col in COLUMNS:
            if col != self.column:
                self.possible_moves.append(col + self.row)
        for row in ROWS:
            if row != self.row:
                self.possible_moves.append(self.column + row)
        
        return self.possible_moves


class Queen(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
        self.type = 'queen'
    
    def get_possible_moves(self):
        self.possible_moves = []
        for col in COLUMNS:
            if col != self.column:
                self.possible_moves.append(col + self.row)
        for row in ROWS:
            if row != self.row:
                self.possible_moves.append(self.column + row)
        
        return self.possible_moves
        

class King(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
        self.type = 'king'
    
    def get_possible_moves(self):
        self.possible_moves = []
        if self.row != '1':
            self.possible_moves.append(self.column + previous_row(self.row))
            if self.column != 'A':
                self.possible_moves.append(previous_column(self.column) + previous_row(self.row))
            if self.column != 'H':
                self.possible_moves.append(next_column(self.column) + previous_row(self.row))
        if self.row != '8':
            self.possible_moves.append(self.column + next_row(self.row))
            if self.column != 'A':
                self.possible_moves.append(previous_column(self.column) + next_row(self.row))
            if self.column != 'A':
                self.possible_moves.append(next_column(self.column) + next_row(self.row))
        if self.column != 'A':
            self.possible_moves.append(next_column(self.column) + self.row)
        if self.column != 'H':
            self.possible_moves.append(previous_column(self.column) + self.row)
        
        return self.possible_moves


class Pawn(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
        self.type = 'pawn'
    
    def get_possible_moves(self):
        self.possible_moves = []
        if self.color == 'white':
            self.possible_moves.append(self.column + next_row(self.row))
            if self.column != 'A':
                self.possible_moves.append(previous_column(self.column) + next_row(self.row))
            if self.column != 'H':
                self.possible_moves.append(next_column(self.column) + next_row(self.row))
            if self.row == '2':
                self.possible_moves.append(self.column + next_row(next_row(self.row)))
        else:
            self.possible_moves.append(self.column + previous_row(self.row))
            if self.column != 'A':
                self.possible_moves.append(previous_column(self.column) + previous_row(self.row))
            if self.column != 'H':
                self.possible_moves.append(next_column(self.column) + previous_row(self.row))
            if self.row == '7':
                self.possible_moves.append(self.column + previous_row(previous_row(self.row)))
  
        return self.possible_moves