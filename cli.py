import argparse
from typing import Dict, Any


def parse_commands() -> Dict[str, Any]:
    """
    Парсит аргументы командной строки и возвращает словарь с переданными командами.
    """
    parser = argparse.ArgumentParser(description="CSV Processor — обработка данных с фильтрацией и агрегацией")

    parser.add_argument("-f", "--file", required=True, help="Путь к входному CSV-файлу")

    parser.add_argument("-w", "--where", help="Условие фильтрации колонки")
    parser.add_argument("-a", "--aggregate", help="Агрегация по колонке")
    parser.add_argument("-o", "--order_by", help="Сортировка по колонке")

    args = parser.parse_args()
    commands = {}

    if args.aggregate and args.order_by:
        raise SystemExit(f"Ошибка: --aggregate и --order_by не могут использоваться вместе.")

    if args.where:
        commands["where"] = args.where
    if args.aggregate:
        commands["aggregate"] = args.aggregate
    if args.order_by:
        commands["order_by"] = args.order_by

    return {
        "file_path": args.file,
        "commands": commands
    }
