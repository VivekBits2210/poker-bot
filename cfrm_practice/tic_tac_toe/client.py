from typing import Callable

from .bot import Bot
from .game import Game
from .strategies.strategy_registry import StrategyEnum


class GameClient:
    def __init__(self, strategy1: str, strategy2: str) -> None:
        self.game = Game()
        self.strategy1 = StrategyEnum[strategy1].strategy()
        self.strategy2 = StrategyEnum[strategy2].strategy()
        self.player1 = Bot(self.game, self.strategy1)
        self.player2 = Bot(self.game, self.strategy2)
        self.player_object_map = {1: self.player1, -1: self.player2}

    def start(self) -> None:
        while True:
            self.game.pretty_print_board()
            winner = self.game.has_won()
            if winner is not None:
                if winner != 0:
                    print(f"Game over! Player {winner} wins!")
                else:
                    print("Game over! It's a draw!")
                break

            player_object = self.player_object_map[self.game.player]
            move = player_object.play()
            validity = self.game.play(move)
            if validity is False:
                print(
                    f"Invalid move by player {self.game.player}, move {move}, "
                    f"strategy {str(type(self.player_object_map[self.game.player].strategy)).split('.')[-1]}!"
                )
                input("Press enter to continue...")
