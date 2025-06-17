from typing import List, Dict, Tuple, Any

from src.aggregations import AGGREGATIONS
from .base import CommandHandler


class AggregateCommand(CommandHandler):
    def handle(self, data: List[Dict[str, str]], args: str) -> List[Dict[str, Any]]:
        """
        Выполняет агрегацию по указанной колонке.
        """
        column, func = self._parse_aggregation(args)

        if func not in AGGREGATIONS:
            raise ValueError(f"Неизвестная функция агрегации: {func}. Доступные функции: '{", ".join(AGGREGATIONS)}'.")
        if column not in data[0]:
            raise ValueError(f"Колонка '{column}' не найдена.")

        try:
            result = AGGREGATIONS[func].apply(data, column)
            return [{func: result}]
        except ValueError:
            raise ValueError("Невозможно выполнить агрегацию по заданной колонке.")

    @staticmethod
    def _parse_aggregation(aggregation: str) -> Tuple[str, str]:
        """
        Парсит строку агрегации на колонку и функцию.
        """
        if "=" not in aggregation:
            raise ValueError("Неправильный формат условия. Используйте шаблон 'column=value'.")
        column, _, func = aggregation.partition("=")
        return column.strip(), func.strip()
