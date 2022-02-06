from tic_tac_toe.client import GameClient
from tic_tac_toe.strategies.strategy_trivial import RandomStrategy


def main():
    gc = GameClient(RandomStrategy, RandomStrategy)
    gc.start()


if __name__ == "__main__":
    main()
