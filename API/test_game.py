from classes.board import *
from classes.pieces import *
from utils import *


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
    game()