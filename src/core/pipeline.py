from typing import List, Dict

from src.commands import COMMAND_HANDLERS


def run_pipeline(data: List[Dict[str, str]], commands: Dict[str, str]) -> List[Dict[str, str]]:
    """
    Последовательно применяет команды к данным.

    :param data: Исходные данные
    :param commands: Словарь команд
    :return: Обработанные данные
    """
    for cmd_name, cmd_args in commands.items():
        if cmd_name in COMMAND_HANDLERS:
            try:
                if data:
                    data = COMMAND_HANDLERS[cmd_name].handle(data, cmd_args)
                else:
                    return []
            except Exception as e:
                raise SystemExit(f"Ошибка при выполнении команды '{cmd_name}': {e}")
    return data
