import unittest

from classes.game import *
from utils.moves import move
from utils.utils import previous_column


class ChessTest(unittest.TestCase):

    def test_scandinavian(self):
        game = Game()
        mv = {
            "type": "normal",
            "start": "E2",
            "end": "E4"
        }
        move(game.board.get_square('E2'), mv, game)
        mv = {
            "type": "normal",
            "start": "D7",
            "end": "D5"
        }
        move(game.board.get_square('D7'), mv, game)

        self.assertEqual(len(legal_moves(game.board.get_square('E4'), game)), 2)

        mv = {
            "type": "normal",
            "start": "E4",
            "end": "D5"
        }
        move(game.board.get_square('E4'), mv, game)

        self.assertEqual(len(game.board.get_black_pieces()), 15)

    
    def test_checkmate_1(self):
        game = Game()
        mv = {
            "type": "normal",
            "start": "G1",
            "end": "F3"
        }
        move(game.board.get_square('G1'), mv, game)
        mv = {
            "type": "normal",
            "start": "A7",
            "end": "A6"
        }
        move(game.board.get_square('A7'), mv, game)
        mv = {
            "type": "normal",
            "start": "D1",
            "end": "H5"
        }
        move(game.board.get_square('D1'), mv, game)
        mv = {
            "type": "normal",
            "start": "A6",
            "end": "A5"
        }
        move(game.board.get_square('A6'), mv, game)
        mv = {
            "type": "normal",
            "start": "F1",
            "end": "C4"
        }
        move(game.board.get_square('F1'), mv, game)
        mv = {
            "type": "normal",
            "start": "A5",
            "end": "A4"
        }
        move(game.board.get_square('A5'), mv, game)
        mv = {
            "type": "normal",
            "start": "H5",
            "end": "F7"
        }
        move(game.board.get_square('H5'), mv, game)

        self.assertEqual(game.is_black_checkmated(), True)


    def test_checkmate_2(self):
        game = Game()
        mv = {
            "type": "normal",
            "start": "F2",
            "end": "F3"
        }
        move(game.board.get_square('F2'), mv, game)
        mv = {
            "type": "normal",
            "start": "E7",
            "end": "E5"
        }
        move(game.board.get_square('E7'), mv, game)
        mv = {
            "type": "normal",
            "start": "G2",
            "end": "G4"
        }
        move(game.board.get_square('G2'), mv, game)
        mv = {
            "type": "normal",
            "start": "D8",
            "end": "H4"
        }
        move(game.board.get_square('D8'), mv, game)

        self.assertEqual(game.is_white_checkmated(), True)

    
    def test_castle_king_white(self):
        game = Game()
        mv = {
            "type": "normal",
            "start": "G1",
            "end": "F3"
        }
        move(game.board.get_square('G1'), mv, game)
        mv = {
            "type": "normal",
            "start": "A7",
            "end": "A5"
        }
        move(game.board.get_square('A7'), mv, game)
        mv = {
            "type": "normal",
            "start": "E2",
            "end": "E4"
        }
        move(game.board.get_square('E2'), mv, game)
        mv = {
            "type": "normal",
            "start": "D7",
            "end": "D5"
        }
        move(game.board.get_square('D7'), mv, game)
        mv = {
            "type": "normal",
            "start": "F1",
            "end": "C4"
        }
        move(game.board.get_square('F1'), mv, game)
        mv = {
            "type": "normal",
            "start": "H7",
            "end": "H6"
        }
        move(game.board.get_square('H7'), mv, game)

        self.assertEqual(len([mv for mv in legal_moves(game.board.get_square('E1'), game) if mv["type"] == 'castle']), 1)

        mv = {
            "type": "castle",
            "start": "E1",
            "end": "G1"
        }
        move(game.board.get_square('E1'), mv, game)

        self.assertEqual(game.board.get_square('E1'), 'empty')
        self.assertEqual(game.board.get_square('H1'), 'empty')
        self.assertEqual(game.board.get_square('G1').type, 'king')
        self.assertEqual(game.board.get_square('F1').type, 'rook')


    def test_castle_queen_white(self):
        game = Game()
        mv = {
            "type": "normal",
            "start": "B1",
            "end": "C3"
        }
        move(game.board.get_square('B1'), mv, game)
        mv = {
            "type": "normal",
            "start": "E7",
            "end": "E5"
        }
        move(game.board.get_square('E7'), mv, game)
        mv = {
            "type": "normal",
            "start": "D2",
            "end": "D3"
        }
        move(game.board.get_square('D2'), mv, game)
        mv = {
            "type": "normal",
            "start": "G8",
            "end": "F6"
        }
        move(game.board.get_square('G8'), mv, game)
        mv = {
            "type": "normal",
            "start": "C1",
            "end": "G5"
        }
        move(game.board.get_square('C1'), mv, game)
        mv = {
            "type": "normal",
            "start": "B8",
            "end": "A6"
        }
        move(game.board.get_square('B8'), mv, game)
        mv = {
            "type": "normal",
            "start": "D1",
            "end": "D2"
        }
        move(game.board.get_square('D1'), mv, game)
        mv = {
            "type": "normal",
            "start": "B7",
            "end": "B6"
        }
        move(game.board.get_square('B7'), mv, game)

        self.assertEqual(len([mv for mv in legal_moves(game.board.get_square('E1'), game) if mv["type"] == 'castle']), 1)

        mv = {
            "type": "castle",
            "start": "E1",
            "end": "C1"
        }
        move(game.board.get_square('E1'), mv, game)

        self.assertEqual(game.board.get_square('E1'), 'empty')
        self.assertEqual(game.board.get_square('A1'), 'empty')
        self.assertEqual(game.board.get_square('C1').type, 'king')
        self.assertEqual(game.board.get_square('D1').type, 'rook')


    def test_castle_king_black(self):
        game = Game()
        mv = {
            "type": "normal",
            "start": "C2",
            "end": "C4"
        }
        move(game.board.get_square('C2'), mv, game)
        mv = {
            "type": "normal",
            "start": "G8",
            "end": "F6"
        }
        move(game.board.get_square('G8'), mv, game)
        mv = {
            "type": "normal",
            "start": "D2",
            "end": "D4"
        }
        move(game.board.get_square('D2'), mv, game)
        mv = {
            "type": "normal",
            "start": "G7",
            "end": "G6"
        }
        move(game.board.get_square('G7'), mv, game)
        mv = {
            "type": "normal",
            "start": "G2",
            "end": "G3"
        }
        move(game.board.get_square('G2'), mv, game)
        mv = {
            "type": "normal",
            "start": "F8",
            "end": "G7"
        }
        move(game.board.get_square('F8'), mv, game)
        mv = {
            "type": "normal",
            "start": "F1",
            "end": "G2"
        }
        move(game.board.get_square('F1'), mv, game)

        self.assertEqual(len([mv for mv in legal_moves(game.board.get_square('E8'), game) if mv["type"] == 'castle']), 1)

        mv = {
            "type": "castle",
            "start": "E8",
            "end": "G8"
        }
        move(game.board.get_square('E8'), mv, game)

        self.assertEqual(game.board.get_square('E8'), 'empty')
        self.assertEqual(game.board.get_square('H8'), 'empty')
        self.assertEqual(game.board.get_square('G8').type, 'king')
        self.assertEqual(game.board.get_square('F8').type, 'rook')


    def test_castle_queen_black(self):
        game = Game()
        mv = {
            "type": "normal",
            "start": "E2",
            "end": "E4"
        }
        move(game.board.get_square('E2'), mv, game)
        mv = {
            "type": "normal",
            "start": "D7",
            "end": "D6"
        }
        move(game.board.get_square('D7'), mv, game)
        mv = {
            "type": "normal",
            "start": "H2",
            "end": "H3"
        }
        move(game.board.get_square('H2'), mv, game)
        mv = {
            "type": "normal",
            "start": "C8",
            "end": "G4"
        }
        move(game.board.get_square('C8'), mv, game)
        mv = {
            "type": "normal",
            "start": "E4",
            "end": "E5"
        }
        move(game.board.get_square('E4'), mv, game)
        mv = {
            "type": "normal",
            "start": "B8",
            "end": "C6"
        }
        move(game.board.get_square('B8'), mv, game)
        mv = {
            "type": "normal",
            "start": "A2",
            "end": "A4"
        }
        move(game.board.get_square('A2'), mv, game)
        mv = {
            "type": "normal",
            "start": "D8",
            "end": "D7"
        }
        move(game.board.get_square('D8'), mv, game)
        mv = {
            "type": "normal",
            "start": "B1",
            "end": "C3"
        }
        move(game.board.get_square('B1'), mv, game)

        self.assertEqual(len([mv for mv in legal_moves(game.board.get_square('E8'), game) if mv["type"] == 'castle']), 1)

        mv = {
            "type": "castle",
            "start": "E8",
            "end": "C8"
        }
        move(game.board.get_square('E8'), mv, game)

        self.assertEqual(game.board.get_square('E8'), 'empty')
        self.assertEqual(game.board.get_square('A8'), 'empty')
        self.assertEqual(game.board.get_square('C8').type, 'king')
        self.assertEqual(game.board.get_square('D8').type, 'rook')

    
    def test_en_passant_white(self):
        game = Game()
        mv = {
            "type": "normal",
            "start": "E2",
            "end": "E4"
        }
        move(game.board.get_square('E2'), mv, game)
        mv = {
            "type": "normal",
            "start": "A7",
            "end": "A5"
        }
        move(game.board.get_square('A7'), mv, game)
        mv = {
            "type": "normal",
            "start": "E4",
            "end": "E5"
        }
        move(game.board.get_square('E4'), mv, game)
        mv = {
            "type": "normal",
            "start": "D7",
            "end": "D5"
        }
        move(game.board.get_square('D7'), mv, game)

        self.assertEqual(len([mv for mv in legal_moves(game.board.get_square('E5'), game) if mv["type"] == 'en_passant']), 1)

        mv = {
            "type": "en_passant",
            "start": "E5",
            "end": "D6"
        }
        move(game.board.get_square('E5'), mv, game)

        self.assertEqual(game.board.get_square('E5'), 'empty')
        self.assertEqual(game.board.get_square('D5'), 'empty')
        self.assertEqual(game.board.get_square('D6').type, 'pawn')
        self.assertEqual(game.board.get_square('D6').color, 'white')
        self.assertEqual(len(game.board.get_black_pawns()), 7)
    
    def test_en_passant_black(self):
        game = Game()
        mv = {
            "type": "normal",
            "start": "G1",
            "end": "F3"
        }
        move(game.board.get_square('G1'), mv, game)
        mv = {
            "type": "normal",
            "start": "E7",
            "end": "E5"
        }
        move(game.board.get_square('E7'), mv, game)
        mv = {
            "type": "normal",
            "start": "B2",
            "end": "B3"
        }
        move(game.board.get_square('B2'), mv, game)
        mv = {
            "type": "normal",
            "start": "E5",
            "end": "E4"
        }
        move(game.board.get_square('E5'), mv, game)
        mv = {
            "type": "normal",
            "start": "D2",
            "end": "D4"
        }
        move(game.board.get_square('D2'), mv, game)

        previous_square = game.board.get_square(previous_column(game.board.get_square('E4').column) + '4')

        self.assertEqual(len([mv for mv in legal_moves(game.board.get_square('E4'), game) if mv["type"] == 'en_passant']), 1)

        mv = {
            "type": "en_passant",
            "start": "E4",
            "end": "D3"
        }
        move(game.board.get_square('E4'), mv, game)

        self.assertEqual(game.board.get_square('E4'), 'empty')
        self.assertEqual(game.board.get_square('D4'), 'empty')
        self.assertEqual(game.board.get_square('D3').type, 'pawn')
        self.assertEqual(game.board.get_square('D3').color, 'black')
        self.assertEqual(len(game.board.get_white_pawns()), 7)

    def test_castle_king_moved(self):
        game = Game()
        mv = {
            "type": "normal",
            "start": "G1",
            "end": "F3"
        }
        move(game.board.get_square('G1'), mv, game)
        mv = {
            "type": "normal",
            "start": "A7",
            "end": "A5"
        }
        move(game.board.get_square('A7'), mv, game)
        mv = {
            "type": "normal",
            "start": "E2",
            "end": "E4"
        }
        move(game.board.get_square('E2'), mv, game)
        mv = {
            "type": "normal",
            "start": "D7",
            "end": "D5"
        }
        move(game.board.get_square('D7'), mv, game)
        mv = {
            "type": "normal",
            "start": "F1",
            "end": "C4"
        }
        move(game.board.get_square('F1'), mv, game)
        mv = {
            "type": "normal",
            "start": "H7",
            "end": "H6"
        }
        move(game.board.get_square('H7'), mv, game)

        mv = {
            "type": "normal",
            "start": "E1",
            "end": "E2"
        }
        move(game.board.get_square('E1'), mv, game)

        mv = {
            "type": "normal",
            "start": "C7",
            "end": "C6"
        }
        move(game.board.get_square('C7'), mv, game)

        mv = {
            "type": "normal",
            "start": "E2",
            "end": "E1"
        }
        move(game.board.get_square('E2'), mv, game)

        mv = {
            "type": "normal",
            "start": "B7",
            "end": "B6"
        }
        move(game.board.get_square('B7'), mv, game)

        self.assertEqual(len([mv for mv in legal_moves(game.board.get_square('E1'), game) if mv["type"] == 'castle']), 0)

    def test_castle_rook_moved(self):
        game = Game()
        mv = {
            "type": "normal",
            "start": "G1",
            "end": "F3"
        }
        move(game.board.get_square('G1'), mv, game)
        mv = {
            "type": "normal",
            "start": "A7",
            "end": "A5"
        }
        move(game.board.get_square('A7'), mv, game)
        mv = {
            "type": "normal",
            "start": "E2",
            "end": "E4"
        }
        move(game.board.get_square('E2'), mv, game)
        mv = {
            "type": "normal",
            "start": "D7",
            "end": "D5"
        }
        move(game.board.get_square('D7'), mv, game)
        mv = {
            "type": "normal",
            "start": "F1",
            "end": "C4"
        }
        move(game.board.get_square('F1'), mv, game)
        mv = {
            "type": "normal",
            "start": "H7",
            "end": "H6"
        }
        move(game.board.get_square('H7'), mv, game)

        mv = {
            "type": "normal",
            "start": "H1",
            "end": "G1"
        }
        move(game.board.get_square('H1'), mv, game)

        mv = {
            "type": "normal",
            "start": "C7",
            "end": "C6"
        }
        move(game.board.get_square('C7'), mv, game)

        mv = {
            "type": "normal",
            "start": "G1",
            "end": "H1"
        }
        move(game.board.get_square('G1'), mv, game)

        mv = {
            "type": "normal",
            "start": "B7",
            "end": "B6"
        }
        move(game.board.get_square('B7'), mv, game)

        self.assertEqual(len([mv for mv in legal_moves(game.board.get_square('E1'), game) if mv["type"] == 'castle']), 0)
        
    def test_castle_king_attacked(self):
        game= Game()
        mv = {
            "type": "normal",
            "start": "E2",
            "end": "E3"
        }
        move(game.board.get_square('E2'), mv, game)
        mv = {
            "type": "normal",
            "start": "E7",
            "end": "E6"
        }
        move(game.board.get_square('E7'), mv, game)
        mv = {
            "type": "normal",
            "start": "G1",
            "end": "F3"
        }
        move(game.board.get_square('G1'), mv, game)
        mv = {
            "type": "normal",
            "start": "G8",
            "end": "F6"
        }
        move(game.board.get_square('G8'), mv, game)
        mv = {
            "type": "normal",
            "start": "D2",
            "end": "D4"
        }
        move(game.board.get_square('D2'), mv, game)
        mv = {
            "type": "normal",
            "start": "B8",
            "end": "C6"
        }
        move(game.board.get_square('B8'), mv, game)
        mv = {
            "type": "normal",
            "start": "F1",
            "end": "D3"
        }
        move(game.board.get_square('F1'), mv, game)
        mv = {
            "type": "normal",
            "start": "F8",
            "end": "B4"
        }
        move(game.board.get_square('F8'), mv, game)

        self.assertEqual(len([mv for mv in legal_moves(game.board.get_square('E1'), game) if mv["type"] == 'castle']), 0)

    def test_promote_white_pawn(self):
        game = Game()
        mv = {
            "type": "normal",
            "start": "H2",
            "end": "H4"
        }
        move(game.board.get_square('H2'), mv, game)
        mv = {
            "type": "normal",
            "start": "E7",
            "end": "E5"
        }
        move(game.board.get_square('E7'), mv, game)
        mv = {
            "type": "normal",
            "start": "H4",
            "end": "H5"
        }
        move(game.board.get_square('H4'), mv, game)
        mv = {
            "type": "normal",
            "start": "D7",
            "end": "D5"
        }
        move(game.board.get_square('D7'), mv, game)
        mv = {
            "type": "normal",
            "start": "H5",
            "end": "H6"
        }
        move(game.board.get_square('H5'), mv, game)
        mv = {
            "type": "normal",
            "start": "B8",
            "end": "C6"
        }
        move(game.board.get_square('B8'), mv, game)
        mv = {
            "type": "normal",
            "start": "H6",
            "end": "G7"
        }
        move(game.board.get_square('H6'), mv, game)
        mv = {
            "type": "normal",
            "start": "B7",
            "end": "B6"
        }
        move(game.board.get_square('B7'), mv, game)
        mv = {
            "type": "normal",
            "start": "G7",
            "end": "H8"
        }
        move(game.board.get_square('G7'), mv, game)

        self.assertEqual(game.board.get_square('H8').type, 'queen')
        self.assertEqual(len(game.board.get_white_queens()), 2)
        self.assertEqual(len(game.board.get_white_pawns()), 7)

        
    def test_promote_black_pawn(self):
        game = Game()
        mv = {
            "type": "normal",
            "start": "G1",
            "end": "F3"
        }
        move(game.board.get_square('G1'), mv, game)
        mv = {
            "type": "normal",
            "start": "A7",
            "end": "A5"
        }
        move(game.board.get_square('A7'), mv, game)
        mv = {
            "type": "normal",
            "start": "E2",
            "end": "E4"
        }
        move(game.board.get_square('E2'), mv, game)
        mv = {
            "type": "normal",
            "start": "A5",
            "end": "A4"
        }
        move(game.board.get_square('A5'), mv, game)
        mv = {
            "type": "normal",
            "start": "D2",
            "end": "D4"
        }
        move(game.board.get_square('D2'), mv, game)
        mv = {
            "type": "normal",
            "start": "A4",
            "end": "A3"
        }
        move(game.board.get_square('A4'), mv, game)
        mv = {
            "type": "normal",
            "start": "A3",
            "end": "B2"
        }
        move(game.board.get_square('A3'), mv, game)
        mv = {
            "type": "normal",
            "start": "D1",
            "end": "D2"
        }
        move(game.board.get_square('D1'), mv, game)
        mv = {
            "type": "normal",
            "start": "B2",
            "end": "A1"
        }
        move(game.board.get_square('B2'), mv, game)
    
        self.assertEqual(game.board.get_square('A1').type, 'queen')
        self.assertEqual(len(game.board.get_black_queens()), 2)
        self.assertEqual(len(game.board.get_black_pawns()), 7)
        

if __name__ == '__main__':
    unittest.main()