from classes.board import *
from classes.pieces import *
from utils import *

def lionMate():
    board = Board()
    move(board.pawns[5], 'F3', board)
    move(board.pawns[12], 'E5', board)
    move(board.pawns[6], 'G4', board)
    move(board.get_black_queens()[0], 'H4', board)
    print(board.is_white_checkmated())

def scandinavian():
    board = Board()
    move(board.pawns[4], 'E4', board)
    move(board.pawns[11], 'D5', board)
    print(board.get_square('C4')) 
    print(filter_check(board.pawns[11], board))
    move(board.pawns[4], 'D5', board)
    print(board.get_square('D5').color)

def game():
    board = Board()
    while not board.is_white_checkmated() and not board.is_black_checkmated():
        start = input('Your start : \n')
        end = input('Your move : \n')
        move(board.get_square(start), end, board)
        if board.is_black_checkmated():
            print('White won')
            break
        else:
            movement = get_next_move(board, 'black')
            print(movement['start'] + '  -->  ' + movement['end'])
            move(board.get_square(movement['start']), movement['end'], board)
            if board.is_white_checkmated():
                print('Black won')
                break


if __name__ == '__main__':
    #lionMate()
    #scandinavian()
    game()