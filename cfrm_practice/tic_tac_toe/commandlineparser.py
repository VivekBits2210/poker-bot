import argparse

from .strategies.strategy_registry import StrategyEnum


class CommandLineParser:
    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(description="Tic Tac Toe")
        parser.add_argument(
            "-p1",
            "--player1",
            type=str,
            help="Player 1 strategy",
            choices=[e.name for e in StrategyEnum],
            default="RANDOM",
        )
        parser.add_argument(
            "-p2",
            "--player2",
            type=str,
            help="Player 1 strategy",
            choices=[e.name for e in StrategyEnum],
            default="RANDOM",
        )
        return parser.parse_args()
