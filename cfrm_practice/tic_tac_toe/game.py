import numpy as np
from typing import Tuple, Union


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
