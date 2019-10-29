from flask import request
from flask_api import FlaskAPI
from utils import get_next_move

app = FlaskAPI(__name__)

@app.route('/get/', methods=['GET', 'POST'])
def get():
    board = request.data.get('board')
    piece = request.data.get('piece')
    move = get_next_move(piece, board)
    return move