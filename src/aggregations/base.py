from abc import ABC, abstractmethod
from typing import List, Dict


class AggregationStrategy(ABC):
    @abstractmethod
    def apply(self, data: List[Dict], column: str) -> float:
        pass
