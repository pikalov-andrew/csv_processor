from typing import List, Dict

from .base import AggregationStrategy


class MinAggregation(AggregationStrategy):
    def apply(self, data: List[Dict], column: str) -> float:
        values = [float(row[column]) for row in data]
        return min(values)
