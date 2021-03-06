from game import Game
from strategies.strategy_registry import StrategyEnum


class GameClient:
    def __init__(self, strategy1: str, strategy2: str) -> None:
        self.game = Game()
        self.strategy1 = StrategyEnum[strategy1].strategy()()
        self.strategy2 = StrategyEnum[strategy2].strategy()()
        self.player_object_map = {1: self.strategy1, -1: self.strategy2}
        self.state = None

    def start(self) -> None:
        while True:
            self.game.pretty_print_board()
            self.state = self.game.has_won()
            if self.state is not None:
                if self.state != 0:
                    print(f"Game over! Player {self.state} wins!")
                else:
                    print("Game over! It's a draw!")
                break

            player_object = self.player_object_map[self.game.player]
            move = player_object.get_move(self.game)
            validity = self.game.play(move)
            if validity is False:
                print(
                    f"Invalid move by player {self.game.player}, move {move}, "
                    f"strategy {str(type(player_object))}!"
                )
                input("Press enter to continue...")
