import json

from flask import render_template, request

from app import app
from chess.main import chess_next_move

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/next_move', methods=['POST'])
def next_move():
    data = request.form.to_dict()
    return chess_next_move(json.loads(data['game']), data['start'], data['end'])