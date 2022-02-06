import pickle
from typing import Tuple

from .strategy_abstract import Strategy
from .train import create_model
from cfrm_practice.tic_tac_toe.game import Game


class CFRMStrategy(Strategy):
    def __init__(self) -> None:
        self.game = None
        try:
            with open("./models/cfrm_model.pkl", "rb") as f:
                node_map = pickle.load(f)
            self.node_map = node_map
        except (pickle.PickleError, FileNotFoundError) as e:
            print(f"{repr(e)} occurred while loading model.")
            self.node_map = create_model()

    def get_move(self, game: Game) -> Tuple[int, int]:
        game_hash = game.get_hash()
        player_symbol = "x" if game.player == 1 else "o"
        node = self.node_map[f"{player_symbol}:{game_hash}"]
        return node.strategy.argmax()
