from flask import jsonify

from .checkmate import is_black_checkmated, is_white_checkmated
from .moves import get_next_move, is_legal, make_move
from .pat import is_pat


def chess_next_move(game, start, end):
    if is_legal(game, start, end):
        game = make_move(game, start, end)
        if is_black_checkmated(game):
            return jsonify(message='black_checkmated', game=game), 200
        else:
            if is_pat(game, 'black'):
                return jsonify(message='pat', game=game), 200
            else:
                next_move = get_next_move(game)
                game = make_move(game, next_move['start'], next_move['end'])
                if is_white_checkmated(game):
                    return jsonify(message='white_checkmated', game=game), 200
                else:
                    if is_pat(game, 'white'):
                        return jsonify(message='pat', game=game), 200
                    else:
                        return jsonify(message='normal', game=game), 200
    else:
        return jsonify(message='illegal'), 500
