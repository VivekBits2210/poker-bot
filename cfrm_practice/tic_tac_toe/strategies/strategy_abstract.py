from abc import ABC, abstractmethod
from typing import Tuple

from cfrm_practice.tic_tac_toe.game import Game


class Strategy(ABC):
    @abstractmethod
    def get_move(self, game: Game) -> Tuple[int, int]:
        pass
