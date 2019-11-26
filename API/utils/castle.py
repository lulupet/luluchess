from utils.utils import attacked_pieces

def line_king_rook(king, rook):
    if rook.column == 'A':
        if king.color == 'black':
            return ['C8', 'D8', 'E8']
        else:
            return ['C1', 'D1', 'E1']
    else:
        if king.color == 'black':
            return ['E8', 'F8', 'G8']
        else:
            return ['E1', 'F1', 'G1']

def clear_path(king, rook, board):
    for i in range(1, len(line_king_rook(king, rook)) - 1):
        if board.get_square(line_king_rook(king, rook)[i]) != 'empty':
            return False
    if king.color == 'black':
        for piece in board.get_white_pieces():
            for attacked_piece in attacked_pieces(piece, board):
                if attacked_piece in line_king_rook(king, rook):
                    return False
        return True
    else:
        for piece in board.get_black_pieces():
            for attacked_piece in attacked_pieces(piece, board):
                if attacked_piece in line_king_rook(king, rook):
                    return False
        return True


def castle_moves(piece, game):
    castle_moves = []
    if piece.type == 'king':
        rooks_not_moved = game.rooks_not_moved(piece.color)
        if game.king_not_moved(piece.color) and len(rooks_not_moved) >= 1:
            for rook in rooks_not_moved:
                if clear_path(piece, rook, game.board):
                    if rook.column == 'A':
                        if piece.color == 'white':
                            if not game.board.is_white_checked():
                                castle_moves.append({"type" : "castle", "start" : "E1", "end" : "C1"})
                        else:
                            if not game.board.is_black_checked():
                                castle_moves.append({"type" : "castle", "start" : "E8", "end" : "C8"})
                    else:
                        if piece.color == 'white':
                            if not game.board.is_white_checked():
                                castle_moves.append({"type" : "castle", "start" : "E1", "end": "G1"})
                        else:
                            if not game.board.is_black_checked():
                                castle_moves.append({"type" : "castle", "start" : "E8", "end": "G8"})
    
    return castle_moves
