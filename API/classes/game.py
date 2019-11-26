from classes.board import Board
from utils.moves import legal_moves

class Game:

    def __init__(self):
        self.board = Board()
        self.historic = [self.board]

    
    def is_white_checkmated(self):
        for piece in self.board.get_white_pieces():
            if len(legal_moves(piece, self)) >= 1:
                return False
        return True


    def is_black_checkmated(self):
        for piece in self.board.get_black_pieces():
            if len(legal_moves(piece, self)) >= 1:
                return False
        return True
    

    def king_not_moved(self, color):
        if color == 'black':
            for move in range(len(self.historic)):
                if self.historic[move].get_black_king().row != '8' or self.historic[move].get_black_king().column != 'E':
                    return False
            return True
        else:
            for move in range(len(self.historic)):
                if self.historic[move].get_white_king().row != '1' or self.historic[move].get_white_king().column != 'E':
                    return False
            return True


    def rooks_not_moved(self, color):
        rooks = []
        if color == 'black':
            move = 0
            left_black_rook_not_moved = True
            while left_black_rook_not_moved and move < len(self.historic):
                if self.historic[move].get_square('A8') == 'empty':
                    left_black_rook_not_moved = False
                else:
                    if self.historic[move].get_square('A8').type != 'rook':
                        left_black_rook_not_moved = False
                move += 1
            if left_black_rook_not_moved:
                rooks.append(self.board.get_square('A8'))
            move = 0
            right_black_rook_not_moved = True
            while right_black_rook_not_moved and move < len(self.historic):
                if self.historic[move].get_square('H8') == 'empty':
                    right_black_rook_not_moved = False
                else:
                    if self.historic[move].get_square('H8').type != 'rook':
                        right_black_rook_not_moved = False
                move += 1
            if right_black_rook_not_moved:
                rooks.append(self.board.get_square('H8'))
        else:
            move = 0
            left_white_rook_not_moved = True
            while left_white_rook_not_moved and move < len(self.historic):
                if self.historic[move].get_square('A1') == 'empty':
                    left_white_rook_not_moved = False
                else:
                    if self.historic[move].get_square('A1').type != 'rook':
                        left_white_rook_not_moved = False
                move += 1
            if left_white_rook_not_moved:
                rooks.append(self.board.get_square('A1'))
            move = 0
            right_white_rook_not_moved = True
            while right_white_rook_not_moved and move < len(self.historic):
                if self.historic[move].get_square('H1') == 'empty':
                    right_white_rook_not_moved = False
                else:
                    if self.historic[move].get_square('H1').type != 'rook':
                        right_white_rook_not_moved = False
                move += 1
            if right_white_rook_not_moved:
                rooks.append(self.board.get_square('H1'))

        return rooks
    
