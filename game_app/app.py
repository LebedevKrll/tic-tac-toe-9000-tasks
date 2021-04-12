from typing import Dict
import uuid
from game_engine.tic_tac_toe_common_lib import TicTacToeGameInfo, TicTacToeTurn
from game_engine.tic_tac_toe_game import TicTacToeGame


class TicTacToeApp:
    def __init__(self):
        """пока не знаю, мб что-то ещё тут будет :)
        в обоих случаях айдишник - ключ, значение - угадайте, что)"""
        self._games: Dict[str, TicTacToeGame] = {}

    def start_game(self, first_player_id: str, second_player_id: str) -> TicTacToeGameInfo:
        gi = str(uuid.uuid4())
        self._games[gi] = TicTacToeGame(game_id=gi, first_player_id=first_player_id, second_player_id=second_player_id)
        return TicTacToeGame(game_id=gi, first_player_id=first_player_id, second_player_id=second_player_id).get_game_info()

    def get_game_by_id(self, game_id: str) -> TicTacToeGameInfo:
        dict_elem = self._games.get(game_id)
        if (dict_elem == None):
            raise Exception("ID doesn't exist")
        return dict_elem.get_game_info()

    def do_turn(self, turn: TicTacToeTurn, game_id: str) -> TicTacToeGameInfo:
        return self._games.get(game_id).do_turn(turn)
