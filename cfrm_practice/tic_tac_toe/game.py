import numpy as np
from typing import Tuple, Union


class Game:
    def __init__(self) -> None:
        self.board = [[0] * 3 for _ in range(3)]
        self.player = 1  # 1 is X, -1 is O
        self.move_history = []
        self.candidate_moves = []
        self.initialize_candidate_moves()

    def initialize_candidate_moves(self) -> None:
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    self.candidate_moves.append((row, col))

    def update_candidate_moves(self) -> None:
        self.candidate_moves.remove(self.move_history[-1])

    def play(self, move: Tuple[int, int], *, subdue: bool = False) -> bool:
        if not subdue:
            print("Move: {} Player: {}".format(len(self.move_history), self.player))
        row, col = move
        if self.board[row][col] != 0:
            return False
        self.board[row][col] = self.player
        self.player = -self.player
        self.move_history.append((row, col))
        self.update_candidate_moves()
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

    def get_hash(self, board=None) -> str:
        if board is None:
            board = self.board

        game_hash = ""
        for row in board:
            for col in range(3):
                cell = row[col]
                game_hash += "x" if cell == 1 else ("o" if cell == -1 else "-")
        return game_hash
