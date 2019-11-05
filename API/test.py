import unittest

from classes.board import *
from classes.pieces import *
from utils import *

class ChessTest(unittest.TestCase):

    def test_scandinavian(self):
        board = Board()
        self.assertEqual(len(get_all_moves(board, 'white')), 20)
        move(board.get_square('E2'), 'E4', board)
        move(board.get_square('D7'), 'D5', board)
        self.assertEqual(len(filter_check(board.get_square('E4'), board)), 2)
        move(board.get_square('E4'), 'D5', board)
        self.assertEqual(len(board.get_black_pieces()), 15)
    
    def test_checkmate_1(self):
        board = Board()
        move(board.get_square('G1'), 'F3', board)
        move(board.get_square('A7'), 'A6', board)
        move(board.get_square('D1'), 'H5', board)
        move(board.get_square('A6'), 'A5', board)
        move(board.get_square('F1'), 'C4', board)
        move(board.get_square('A5'), 'A4', board)
        move(board.get_square('H5'), 'F7', board)
        self.assertEqual(board.is_black_checkmated(), True)

    def test_checkmate_2(self):
        board = Board()
        move(board.get_square('F2'), 'F3', board)
        move(board.get_square('E7'), 'E5', board)
        move(board.get_square('G2'), 'G4', board)
        move(board.get_square('D8'), 'H4', board)
        self.assertEqual(board.is_white_checkmated(), True)    


if __name__ == '__main__':
    unittest.main()