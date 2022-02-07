import os
import copy
import pickle
from typing import Sequence, Tuple

import numpy as np

from cfrm_practice.tic_tac_toe.game import Game

ACTION_SPACE_SIZE = 9
node_map = {}


class Node:
    def __init__(self) -> None:
        self.infoSet = ""

        self.regret_sum = np.zeros(ACTION_SPACE_SIZE)
        self.strategy = np.zeros(ACTION_SPACE_SIZE)
        self.strategy_sum = np.zeros(ACTION_SPACE_SIZE)

    def get_strategy(
        self, realization_weight: int, candidates: Sequence[Tuple[int, int]]
    ) -> np.ndarray:
        num_actions = len(candidates)
        normalizingSum = 0
        for a in candidates:
            one_dim_index = a[0] * 3 + a[1]
            self.strategy[one_dim_index] = (
                self.regret_sum[one_dim_index]
                if self.regret_sum[one_dim_index] > 0
                else 0
            )
            normalizingSum += self.strategy[one_dim_index]

        for a in candidates:
            one_dim_index = a[0] * 3 + a[1]
            if normalizingSum > 0:
                self.strategy[one_dim_index] /= normalizingSum
            else:
                self.strategy[one_dim_index] = 1.0 / num_actions
            self.strategy_sum[one_dim_index] += (
                realization_weight * self.strategy[one_dim_index]
            )
        return self.strategy


# Train TIC TAC TOE
def train(game_iterations: int) -> None:
    game = Game()
    util = 0
    for i in range(game_iterations):
        print(f"Iteration: {i}, util = {util}")
        print(f"Node map size: {len(node_map)}")
        util += cfr(game, 1, 1)
        print(f"Completed iteration!")


# Counterfactual regret minimization iteration
def cfr(game: Game, p0: int, p1: int) -> int:
    player = game.player
    game_state = game.has_won()
    if game_state is not None:
        return game_state

    # identify the infoset (or node)
    player_symbol = "x" if player == 1 else "o"
    infoSet = player_symbol + ":" + game.get_hash()

    # Get the node or create it, if it does not exist
    node_exists = infoSet in node_map
    if not node_exists:
        node = Node()
        node.infoSet = infoSet
        node_map[infoSet] = node
    else:
        node = node_map[infoSet]

    param = p0 if player == 1 else p1
    strategy = node.get_strategy(param, game.candidate_moves)
    util = np.zeros(ACTION_SPACE_SIZE)

    node_util = 0
    for a in game.candidate_moves:
        new_game = copy.deepcopy(game)
        one_dim_index = a[0] * 3 + a[1]
        new_game.play(a, subdue=True)
        util[one_dim_index] = (
            -cfr(new_game, p0 * strategy[one_dim_index], p1)
            if player == 1
            else -cfr(new_game, p0, p1 * strategy[one_dim_index])
        )
        node_util += strategy[one_dim_index] * util[one_dim_index]

    # For each action, compute and accumulate counterfactual regret
    for a in game.candidate_moves:
        one_dim_index = a[0] * 3 + a[1]
        regret = util[one_dim_index] - node_util
        node.regret_sum[one_dim_index] += (p1 if player == 1 else p0) * regret

    return node_util


# number of iterations
# 1 iteration approx 30sec
# 10 iterations approx 5min
# 100 iterations approx 30min
# 1000 iterations approx 4h30min
def create_model() -> dict:
    iterations = 200
    print("iterations =", iterations)
    train(iterations)
    with open(
        os.path.join(os.path.dirname(__file__), "models", "cfrm_model.pkl"),
        "wb",
    ) as f:
        pickle.dump(node_map, f)
    return node_map
