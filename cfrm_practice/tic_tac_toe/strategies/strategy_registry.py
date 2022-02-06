from enum import Enum

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

    def strategy(self):
        mapping = {
            StrategyEnum.RANDOM: RandomStrategy(),
            StrategyEnum.HUMAN: HumanStrategy(),
            StrategyEnum.ORDINAL: OrdinalStrategy(),
            StrategyEnum.COCK_BLOCK: CockBlockStrategy(),
            StrategyEnum.CFRM: CFRMStrategy(),
        }
        return mapping[self]

    @staticmethod
    def get_strategy_name(strategy):
        if strategy == StrategyEnum.RANDOM:
            return "RANDOM"
        elif strategy == StrategyEnum.HUMAN:
            return "HUMAN"
        elif strategy == StrategyEnum.ORDINAL:
            return "ORDINAL"
        elif strategy == StrategyEnum.COCK_BLOCK:
            return "COCK_BLOCK"
        elif strategy == StrategyEnum.CFRM:
            return "CFRM"
        else:
            return None
