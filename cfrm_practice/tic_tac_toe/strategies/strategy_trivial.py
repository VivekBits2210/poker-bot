import random
from copy import deepcopy
from typing import Tuple, Sequence

from .strategy_abstract import Strategy
from ..game import Game


class OrdinalStrategy(Strategy):
    def get_move(
        self, game: Game, candidate_moves: Sequence[Tuple[int, int]]
    ) -> Tuple[int, int]:
        return candidate_moves[0]


class RandomStrategy(Strategy):
    def get_move(
        self, game: Game, candidate_moves: Sequence[Tuple[int, int]]
    ) -> Tuple[int, int]:
        return random.choice(candidate_moves)


class CockBlockStrategy(Strategy):
    def get_move(
        self, game: Game, candidate_moves: Sequence[Tuple[int, int]]
    ) -> Tuple[int, int]:
        for move in candidate_moves:
            # Return winning move
            game_copy = deepcopy(game)
            game_copy.board[move[0]][move[1]] = game.player
            if game_copy.has_won() == game.player:
                return move

            # Return cock blocking move
            game_copy.board[move[0]][move[1]] = -game.player
            if game_copy.has_won() == -game.player:
                return move

        # Otherwise randomize
        return random.choice(candidate_moves)


class HumanStrategy(Strategy):
    def get_move(
        self, game: Game, candidate_moves: Sequence[Tuple[int, int]]
    ) -> Tuple[int, int]:
        while True:
            row, column = tuple(input("Enter a move: ").split(" "))
            move = int(row), int(column)
            if move not in candidate_moves:
                print(f"Invalid move, pick from candidates: {candidate_moves}")
            else:
                break
        return move
