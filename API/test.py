from classes import *
from utils import *

def lionMate():
    board = Board()
    move(board.pawns[5], 'F3', board)
    move(board.pawns[12], 'E5', board)
    move(board.pawns[6], 'G4', board)
    move(board.black_queens[0], 'H4', board)
    print(board.is_white_checkmated())

def scandinavian():
    board = Board()
    move(board.pawns[4], 'E4', board)
    move(board.pawns[11], 'D5', board)
    print(board.get_square('C4')) 
    print(filter_check(board.pawns[11], board))
    move(board.pawns[4], 'D5', board)
    print(board.get_square('D5').color) 

if __name__ == '__main__':
    #lionMate()
    scandinavian()