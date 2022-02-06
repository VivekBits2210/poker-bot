#TODO: Add Typing
import random
import numpy as np

class Game:
    def __init__(self):
        self.board = [[0] * 3 for _ in range(3)]
        self.player = 1 # 1 is X, -1 is O
        self.move_history = []

    def play(self, move):
        row, col = move
        if self.board[row][col] != 0:
            return False
        self.board[row][col] = self.player
        self.player = - self.player
        self.move_history.append((row, col))
        return True

    def has_won(self):
        # Check rows
        for row in self.board:
            if row[0] != 0 and row[0] == row[1] == row[2]:
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] != 0 and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] != 0 and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] != 0 and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        # Check if game is a draw
        if len(self.move_history) == 9:
            return 0

        # No winner yet
        return None

    def pretty_print_board(self):
        return np.matrix(self.board)

class Bot:
    def __init__(self, game, strategy):
        self.game = game
        self.strategy = strategy
        self.candidate_moves = []
        self.initalize_candidate_moves()

    def initalize_candidate_moves(self):
        for row in range(3):
            for col in range(3):
                if self.game.board[row][col] == 0:
                    self.candidate_moves.append((row, col))

    def update_candidate_moves(self):
        if len(self.game.move_history) > 0:
            self.candidate_moves.remove(self.game.move_history[-1])

    def play(self):
        self.update_candidate_moves()
        move = self.strategy.get_move(self.candidate_moves)
        return move

class GameClient:
    def __init__(self, strategy1, strategy2):
        self.game = Game()
        self.strategy1 = strategy1()
        self.strategy2 = strategy2()
        self.player1 = Bot(self.game, self.strategy1)
        self.player2 = Bot(self.game, self.strategy2)
        self.player_object_map = {1: self.player1, -1: self.player2}

    def start(self):
        while True:
            self.game.pretty_print_board()
            winner = self.game.has_won()
            if winner:
                if winner!=0:
                    print(f"Game over! Player {winner} wins!")
                else:
                    print("Game over! It's a draw!")
                break

            player_object = self.player_object_map[self.game.player]
            move = player_object.play()
            validity = self.game.play(self, move)
            if not validity:
                print(f"Invalid move by player {self.game.player}, "
                      f"strategy {type(self.player_object_map[self.game.player].strategy)}!")
                input("Press enter to continue...")


class OrdinalStrategy:
    def get_move(self, board, candidate_moves):
        return candidate_moves[0]

class RandomStrategy:
    def get_move(self, candidate_moves, board):
        return random.choice(candidate_moves)

class CockBlockStrategy:
    def get_move(self, board, candidate_moves):
        pass #TODO: Fill this in

class UserStrategy:
    def get_move(self, board, candidate_moves):
        while True:
            row, column = tuple(input("Enter a move: ").split(''))
            move = int(row), int(column)
            if move not in candidate_moves:
                print(f"Invalid move, pick from candidates: {candidate_moves}")
            else:
                break
        return move



def main():
    game = Game()


if __name__ == '__main__':
    main()
