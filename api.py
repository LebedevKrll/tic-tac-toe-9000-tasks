from game_app.app import TicTacToeApp
from game_engine.tic_tac_toe_common_lib import TicTacToeGameInfo, TicTacToeTurn
from game_engine.tic_tac_toe_game import TicTacToeGame
from flask import Flask, request

app = Flask(__name__)

@app.route('/home/do_turn', methods=["GET"])
def do_turn():
    game_id = request.args["game_id"]
    turn = request.args["turn"]
    return TicTacToeApp.do_turn({turn}, {game_id})

@app.route('/home/get_game_by_id')
def get_game_by_id():
    game_id = request.args["game_id"]
    return TicTacToeApp.get_game_by_id({game_id})

@app.route('/home/start_game')
def start_game():
    second_player_id = request.args["second_player_id"]
    first_player_id = request.args["first_player_id"]
    return TicTacToeApp.start_game({first_player_id}, {second_player_id})
