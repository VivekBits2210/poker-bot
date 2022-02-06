from abc import ABC, abstractmethod
from typing import Sequence, Tuple

from ..game import Game


class Strategy(ABC):
    @abstractmethod
    def get_move(
        self, game: Game, candidate_moves: Sequence[Tuple[int, int]]
    ) -> Tuple[int, int]:
        pass
