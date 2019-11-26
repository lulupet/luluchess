from utils.utils import previous_column, next_column

def en_passant(piece, game):
    list_en_passant = []
    if piece.type == 'pawn':
        if len(game.historic) >= 2:
            if piece.color == 'white':
                if piece.row == '5':
                    if piece.column != 'A':
                        previous_square = game.board.get_square(previous_column(piece.column) + '5')
                        if previous_square != 'empty':
                            if previous_square.type == 'pawn':
                                if previous_square.color == 'black':
                                    if game.historic[-2].get_square(previous_column(piece.column) + '7') != 'empty' and game.historic[-2].get_square(previous_column(piece.column) + '5') == 'empty' and game.board.get_square(previous_column(piece.column) + '7') == 'empty':
                                        list_en_passant.append({"type" : "en_passant", "start" : piece.column + piece.row, "end" : previous_column(piece.column) + '6'})
                    if piece.column != 'H':
                        next_square = game.board.get_square(next_column(piece.column) + '5')
                        if next_square != 'empty':
                            if next_square.type == 'pawn':
                                if next_square.color == 'black':
                                    if game.historic[-2].get_square(next_column(piece.column) + '7') != 'empty' and game.historic[-2].get_square(next_column(piece.column) + '5') == 'empty' and game.board.get_square(next_column(piece.column) + '7') == 'empty':
                                        list_en_passant.append({"type" : "en_passant", "start" : piece.column + piece.row, "end" : next_column(piece.column) + '6'})
            else:
                if piece.row == '4':
                    if piece.column != 'A':
                        previous_square = game.board.get_square(previous_column(piece.column) + '4')
                        if previous_square != 'empty':
                            if previous_square.type == 'pawn':
                                if previous_square.color == 'white':
                                    if game.historic[-2].get_square(previous_column(piece.column) + '2') != 'empty' and game.historic[-2].get_square(previous_column(piece.column) + '4') == 'empty' and game.board.get_square(previous_column(piece.column) + '2') == 'empty':
                                        list_en_passant.append({"type" : "en_passant", "start" : piece.column + piece.row, "end" : previous_column(piece.column) + '3'})
                    if piece.column != 'H':
                        next_square = game.board.get_square(next_column(piece.column) + '4')
                        if next_square != 'empty':
                            if next_square.type == 'pawn':
                                if next_square.color == 'white':
                                    if game.historic[-2].get_square(next_column(piece.column) + '2') != 'empty' and game.historic[-2].get_square(next_column(piece.column) + '4') == 'empty' and game.board.get_square(next_column(piece.column) + '2') == 'empty':
                                        list_en_passant.append({"type" : "en_passant", "start" : piece.column + piece.row, "end" : next_column(piece.column) + '3'})
    
    return list_en_passant