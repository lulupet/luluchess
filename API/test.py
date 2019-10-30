from classes import *
from utils import *

def lionMate():
    board = Board()
    board.pawns[5].move('F3')
    board.pawns[12].move('E5')
    board.pawns[6].move('G4')
    board.black_queens[0].move('H4')
    print(board.is_white_checkmated())

if __name__ == '__main__':
    lionMate()