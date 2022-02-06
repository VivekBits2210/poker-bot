import sys
import os

from .client import GameClient
from .commandlineparser import CommandLineParser


def main():
    old_stdout = sys.stdout  # backup current stdout
    arguments = CommandLineParser.parse()
    if arguments.iterations > 1:
        sys.stdout = open(os.devnull, "w")

    state_count = {}
    for iteration in range(arguments.iterations):
        gc = GameClient(arguments.player1, arguments.player2)
        gc.start()

        if gc.state not in state_count:
            state_count[gc.state] = 1
        else:
            state_count[gc.state] += 1

    sys.stdout = old_stdout  # restore stdout    print("GAME STATS:")
    print(f"Games: {arguments.iterations}")
    for game_state in sorted(
        state_count.keys(), key=lambda x: 2 * abs(x) + x, reverse=True
    ):
        if game_state == 0:
            print(
                f"Tie: {state_count[game_state]}, {'%.2f' % (state_count[game_state] / arguments.iterations * 100)}%"
            )
        else:
            print(
                f"Player {game_state}: {state_count[game_state]}, {'%.2f' % (state_count[game_state] / arguments.iterations * 100)}%"
            )


if __name__ == "__main__":
    main()
