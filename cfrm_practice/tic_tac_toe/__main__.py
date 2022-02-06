from .client import GameClient
from .commandlineparser import CommandLineParser


def main():
    arguments = CommandLineParser.parse()
    gc = GameClient(arguments.player1, arguments.player2)
    gc.start()


if __name__ == "__main__":
    main()
