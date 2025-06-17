from typing import List, Dict

from tabulate import tabulate


def format_result(data: List[Dict[str, str]]) -> None:
    """
    Форматирует результат и выводит в консоль.
    """
    if not data:
        print("Результат пуст.")
        return
    print(tabulate(data, headers="keys", tablefmt="psql"))
