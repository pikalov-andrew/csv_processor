from typing import List, Dict

from .base import CommandHandler


class ConditionCommand(CommandHandler):
    def handle(self, data: List[Dict[str, str]], args: str) -> List[Dict[str, str]]:
        """
        Обрабатывает фильтрацию по условию.
        """
        column, operator, value = self._parse_condition(args)

        if column not in data[0]:
            raise ValueError(f"Колонка '{column}' не найдена.")

        filtered = []
        for row in data:
            cell_value = row[column]
            if self._compare(cell_value, operator, value):
                filtered.append(row)
        return filtered

    @staticmethod
    def _parse_condition(condition: str) -> tuple[str, str, str]:
        """
        Парсит строку условия на колонку, оператор и значение.
        """
        possible_operators = [">", "<", "="]
        for op in possible_operators:
            if op in condition:
                parts = condition.split(op)
                if len(parts) != 2:
                    raise ValueError(
                        "Неправильный формат условия. Используйте шаблон 'column>value', 'column<value' или 'column=value'.")
                return parts[0].strip(), op, parts[1].strip()
        raise ValueError(f"Неизвестный оператор. Поддерживаемые операторы: '{", ".join(possible_operators)}'.")

    @staticmethod
    def _compare(cell_value: str, operator: str, value: str) -> bool | None:
        """
        Сравнивает значение ячейки с заданным условием.
        """
        try:
            cell_num = float(cell_value)
            val_num = float(value)
            if operator == ">":
                return cell_num > val_num
            elif operator == "<":
                return cell_num < val_num
            elif operator == "=":
                return cell_num == val_num
            return None
        except ValueError:
            if operator == "=":
                return cell_value == value
            else:
                raise ValueError(f"К строковым значениям можно применять только операцию равенства.")
