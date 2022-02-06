from abc import ABC, abstractmethod
from typing import Callable, Sequence, Tuple, Union
import random
import numpy as np


class Strategy(ABC):
    @abstractmethod
    def get_move(
        self, board: Sequence[Sequence[int]], candidate_moves: Sequence[Tuple[int, int]]
    ) -> Tuple[int, int]:
        pass


class Game:
    def __init__(self) -> None:
        self.board = [[0] * 3 for _ in range(3)]
        self.player = 1  # 1 is X, -1 is O
        self.move_history = []

    def play(self, move: Tuple[int, int]) -> bool:
        print("Move: {} Player: {}".format(len(self.move_history), self.player))
        row, col = move
        if self.board[row][col] != 0:
            return False
        self.board[row][col] = self.player
        self.player = -self.player
        self.move_history.append((row, col))
        return True

    def has_won(self) -> Union[int, None]:
        # Check rows
        for row in self.board:
            if row[0] != 0 and row[0] == row[1] == row[2]:
                return row[0]

        # Check columns
        for col in range(3):
            if (
                self.board[0][col] != 0
                and self.board[0][col] == self.board[1][col] == self.board[2][col]
            ):
                return self.board[0][col]

        # Check diagonals
        if (
            self.board[0][0] != 0
            and self.board[0][0] == self.board[1][1] == self.board[2][2]
        ):
            return self.board[0][0]
        if (
            self.board[0][2] != 0
            and self.board[0][2] == self.board[1][1] == self.board[2][0]
        ):
            return self.board[0][2]

        # Check if game is a draw
        if len(self.move_history) == 9:
            return 0

        # No winner yet
        return None

    def pretty_print_board(self) -> None:
        print(np.matrix(self.board))


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


class GameClient:
    def __init__(self, strategy1: Callable, strategy2: Callable) -> None:
        self.game = Game()
        self.strategy1 = strategy1()
        self.strategy2 = strategy2()
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


class OrdinalStrategy(Strategy):
    def get_move(
        self, board: Sequence[Sequence[int]], candidate_moves: Sequence[Tuple[int, int]]
    ) -> Tuple[int, int]:
        return candidate_moves[0]


class RandomStrategy(Strategy):
    def get_move(
        self, board: Sequence[Sequence[int]], candidate_moves: Sequence[Tuple[int, int]]
    ) -> Tuple[int, int]:
        return random.choice(candidate_moves)


class CockBlockStrategy(Strategy):
    def get_move(
        self, board: Sequence[Sequence[int]], candidate_moves: Sequence[Tuple[int, int]]
    ) -> Tuple[int, int]:
        pass  # TODO: Fill this in


class UserStrategy(Strategy):
    def get_move(
        self, board: Sequence[Sequence[int]], candidate_moves: Sequence[Tuple[int, int]]
    ) -> Tuple[int, int]:
        while True:
            row, column = tuple(input("Enter a move: ").split(""))
            move = int(row), int(column)
            if move not in candidate_moves:
                print(f"Invalid move, pick from candidates: {candidate_moves}")
            else:
                break
        return move


def main():
    gc = GameClient(RandomStrategy, RandomStrategy)
    gc.start()


if __name__ == "__main__":
    main()
