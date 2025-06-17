from typing import List, Dict

from .base import AggregationStrategy


class AvgAggregation(AggregationStrategy):
    def apply(self, data: List[Dict], column: str) -> float:
        values = [float(row[column]) for row in data]
        return sum(values) / len(values)
