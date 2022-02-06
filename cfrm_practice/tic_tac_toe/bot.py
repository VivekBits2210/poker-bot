from typing import Tuple

from .game import Game
from .strategies.strategy_abstract import Strategy


class Bot:
    def __init__(self, game: Game, strategy: Strategy) -> None:
        self.game = game
        self.strategy = strategy
        self.candidate_moves = []
        self.initialize_candidate_moves()

    def initialize_candidate_moves(self) -> None:
        for row in range(3):
            for col in range(3):
                if self.game.board[row][col] == 0:
                    self.candidate_moves.append((row, col))

    def update_candidate_moves(self) -> None:
        try:
            self.candidate_moves.remove(self.game.move_history[-1])
            self.candidate_moves.remove(self.game.move_history[-2])
        except IndexError:
            pass

    def play(self) -> Tuple[int, int]:
        self.update_candidate_moves()
        move = self.strategy.get_move(self.game.board, self.candidate_moves)
        return move
