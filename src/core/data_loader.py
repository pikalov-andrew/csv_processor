import csv
from typing import List, Dict


def load_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Загружает CSV-файл и возвращает данные в виде списка словарей.

    :param file_path: Путь к CSV-файлу
    :return: Список строк в виде словарей
    """
    try:
        with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except FileNotFoundError:
        raise SystemExit(f"Файл {file_path} не найден.")
    except csv.Error as e:
        raise SystemExit(f"Ошибка чтения CSV: {e}")
