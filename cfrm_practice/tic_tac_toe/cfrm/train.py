# class Node:
#     def __init__(self):
#         self.infoSet = ""
#         self.regretSum = np.zeros(NUM_ACTIONS)
#         self.strategy = np.zeros(NUM_ACTIONS)
#         self.strategySum = np.zeros(NUM_ACTIONS)
#
#     def get_strategy(self, realizationWeight, grid):
#         actions = get_available_actions(grid)
#         num_actions = len(actions)
#         normalizingSum = 0
#         for a in actions:
#             self.strategy[a] = self.regretSum[a] if self.regretSum[a] > 0 else 0
#             normalizingSum += self.strategy[a]
#
#         for a in actions:
#             if normalizingSum > 0:
#                 self.strategy[a] /= normalizingSum
#             else:
#                 self.strategy[a] = 1.0 / num_actions
#             self.strategySum[a] += realizationWeight * self.strategy[a]
#         return self.strategy
#
#         # Get average information set mixed strategy across all training iterations i
#
#     def get_average_strategy(self):
#         avgStrategy = np.zeros(NUM_ACTIONS)
#         normalizingSum = 0
#         for a in range(NUM_ACTIONS):
#             normalizingSum += self.strategySum[a]
#         for a in range(NUM_ACTIONS):
#             if normalizingSum > 0:
#                 avgStrategy[a] = round(self.strategySum[a] / normalizingSum, 2)
#             else:
#                 avgStrategy[a] = round(1.0 / NUM_ACTIONS)
#         return avgStrategy
#
#     def __str__(self):
#         return (
#             self.infoSet + ": " + str(self.get_average_strategy())
#         )  # + "; regret = " + str(self.regretSum)
#
#
# # Train TIC TAC TOE
# def train(iterations):
#     grid = np.zeros(NUM_ACTIONS)
#     util = 0
#     for i in range(iterations):
#         util += cfr(grid, "", 1, 1)
#
#
# # Counterfactual regret minimization iteration
# def cfr(grid, history, p0, p1):
#     plays = len(history)
#     player = plays % 2
#     # Return payoff for terminal states
#     if plays > 3:
#         winner = is_player_winner(player, grid)
#         if winner != 0:
#             return winner
#         if is_full(grid):
#             return 0
#
#     # identify the infoset (or node)
#     player_symbol = "x" if player == 0 else "o"
#     infoSet = player_symbol + ":" + get_grid_hash(grid)
#
#     # Get the node or create it, if it does not exist
#     node_exists = infoSet in nodeMap
#     node = None
#     if not node_exists:
#         node = Node()
#         node.infoSet = infoSet
#         nodeMap[infoSet] = node
#     else:
#         node = nodeMap[infoSet]
#
#     # For each action, recursively call cfr with additional history and probability
#     param = p0 if player == 0 else p1
#     strategy = node.get_strategy(param, grid)
#     actions = get_available_actions(grid)
#     util = np.zeros(NUM_ACTIONS)
#
#     nodeUtil = 0
#     for a in actions:
#         newgrid = np.copy(grid)
#         newgrid[a] = 1 if player == 0 else -1
#         nextHistory = history + player_symbol
#         # the sign of the util received is the opposite of the one computed one layer below
#         # because what is positive for one player, is neagtive for the other
#         # if player == 0 is making the call, the reach probability of the node below depends on the strategy of player 0
#         # so we pass reach probability = p0 * strategy[a], likewise if this is player == 1 then reach probability = p1 * strategy[a]
#         util[a] = (
#             -cfr(newgrid, nextHistory, p0 * strategy[a], p1)
#             if player == 0
#             else -cfr(newgrid, nextHistory, p0, p1 * strategy[a])
#         )
#         nodeUtil += strategy[a] * util[a]
#
#     # For each action, compute and accumulate counterfactual regret
#     for a in actions:
#         regret = util[a] - nodeUtil
#         # for the regret of player 0 is multilied by the reach p1 of player 1
#         # because it is the action of player 1 at the layer above that made the current node reachable
#         # conversly if this player 1, then the reach p0 is used.
#         node.regretSum[a] += (p1 if player == 0 else p0) * regret
#
#     return nodeUtil
#
#
# if __name__ == "__main__":
#     # number of iterations
#     # 1 iteration approx 30sec
#     # 10 iterations approx 5min
#     # 100 iterations approx 30min
#     # 1000 iterations approx 4h30min
#     iterations = 10
#     print("iterations =", iterations)
#     train(iterations)
