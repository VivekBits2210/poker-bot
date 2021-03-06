import argparse

from strategies.strategy_registry import StrategyEnum


class CommandLineParser:
    @staticmethod
    def parse() -> argparse.Namespace:
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
        parser.add_argument(
            "-i",
            "--iterations",
            type=int,
            help="Number of iterations",
            default=1,
        )
        return parser.parse_args()
