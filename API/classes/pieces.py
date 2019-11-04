from utils import ROWS, COLUMNS, previous_column, next_column, previous_row, next_row, diagonals, filter_moves

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