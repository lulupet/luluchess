from utils import ROWS, COLUMNS, previous_column, next_column, previous_row, next_row, diagonals

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

class Piece:
    def __init__(self, color, row, column):
        self.color = color
        self.row = row
        self.column = column
        self.possible_moves = []

class Knight(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
    
    def get_possible_moves(self):
        if self.row != '1':
            if self.column not in ['G', 'H']:
                self.possible_moves.append(next_column(next_column(self.column)) + previous_row(self.row))
            if self.column not in ['A', 'B']:
                self.possible_moves.append(previous_column(previous_column(self.column)) + previous_row(self.row))
        if self.row != '2':
            if self.column != 'H':
                self.possible_moves.append(next_column(self.column) + previous_row(previous_row(self.row)))
            if self.column != 'A':
                self.possible_moves.append(previous_column(self.column) + previous_row(previous_row(self.row)))
        if self.row != '7':
            if self.column != 'H':
                self.possible_moves.append(next_column(self.column) + next_row(next_row(self.row)))
            if self.column != 'A':
                self.possible_moves.append(previous_column(self.column) + next_row(next_row(self.row)))
        if self.row != '8':
            if self.column not in ['G', 'H']:
                self.possible_moves.append(next_column(next_column(self.column)) + next_row(self.row))
            if self.column not in ['A', 'B']:
                self.possible_moves.append(previous_column(previous_column(self.column)) + next_row(self.row))
        
        return self.possible_moves


class Bishop(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
    
    def get_possible_moves(self):
        self.possible_moves = [square for square in diagonals(self.column, self.row) if square != self.column + self.row]

        return self.possible_moves


class Rook(Piece):
    def __init__(self, color, row, column):
        super().__init__(color, row, column)
    
    def get_possible_moves(self):
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
    
    def get_possible_moves(self):
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
    
    def get_possible_moves(self):
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
    
    def get_possible_moves(self):
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