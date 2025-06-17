from typing import List, Dict, Tuple

from .base import CommandHandler


class OrderingCommand(CommandHandler):
    def handle(self, data: List[Dict[str, str]], args: str) -> List[Dict[str, str]]:
        """
        Обрабатывает сортировку по условию.
        """
        column, direction = self._parse_ordering(args)

        if direction not in ["desc", "asc"]:
            raise ValueError(f"Неизвестная функция сортировки: {direction}. Доступные функции: 'desc' и 'asc'.")
        if column not in data[0]:
            raise ValueError(f"Колонка '{column}' не найдена.")

        try:
            reverse = direction == "desc"
            return sorted(data, key=lambda x: self._sort_key(x, column), reverse=reverse)
        except ValueError:
            raise ValueError("Невозможно выполнить фильтрацию по заданной колонке.")

    @staticmethod
    def _parse_ordering(aggregation: str) -> Tuple[str, str]:
        """
        Парсит строку сортировки на колонку и функцию.
        """
        if "=" not in aggregation:
            raise ValueError("Неправильный формат условия. Используйте шаблон 'column=value'.")
        column, _, direction = aggregation.partition("=")
        return column, direction

    @staticmethod
    def _sort_key(item, column: str) -> float | str:
        """
        Сортирует значения в зависимости от типа.
        """
        value = item.get(column, "")
        try:
            return float(value)
        except ValueError:
            return value
