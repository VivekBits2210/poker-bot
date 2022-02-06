import pickle
from typing import Tuple, Sequence

from .strategy_abstract import Strategy
from ..game import Game


class CFRM(Strategy):
    def __init__(self):
        self.game = None
        with open("./models/cfrm_model.pkl", "rb") as f:
            node_map = pickle.load(f)
        self.node_map = node_map

    def get_hash(self) -> str:
        game_hash = ""
        for row in self.game.board:
            for col in range(3):
                cell = self.game.board[row][col]
                game_hash += (
                    "x"
                    if cell == self.game.player
                    else ("o" if cell == -self.game.player else "-")
                )
        return game_hash

    def get_move(
        self, game: Game, candidate_moves: Sequence[Tuple[int, int]]
    ) -> Tuple[int, int]:
        self.game = game
        hash = self.get_hash()
        node = self.nodeMap["o:" + hash]
        return node.strategy.argmax()
