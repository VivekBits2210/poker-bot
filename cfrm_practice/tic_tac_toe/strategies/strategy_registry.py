from typing import Callable
from enum import Enum

from .strategy_abstract import Strategy
from .strategy_trivial import (
    CockBlockStrategy,
    OrdinalStrategy,
    HumanStrategy,
    RandomStrategy,
)
from .strategy_cfrm import CFRMStrategy


class StrategyEnum(Enum):
    RANDOM = "RANDOM"
    HUMAN = "HUMAN"
    ORDINAL = "ORDINAL"
    COCK_BLOCK = "COCK_BLOCK"
    CFRM = "CFRM"

    def strategy(
        self,
    ) -> Callable[..., Strategy]:
        mapping = {
            StrategyEnum.RANDOM: RandomStrategy,
            StrategyEnum.HUMAN: HumanStrategy,
            StrategyEnum.ORDINAL: OrdinalStrategy,
            StrategyEnum.COCK_BLOCK: CockBlockStrategy,
            StrategyEnum.CFRM: CFRMStrategy,
        }
        return mapping[self]
