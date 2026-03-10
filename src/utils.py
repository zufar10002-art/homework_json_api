import json
from typing import Any, Dict, List


def load_operations(json_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные о финансовых операциях из JSON-файла.

    Args:
        json_path (str): Путь к JSON-файлу.

    Returns:
        List[Dict[str, Any]]: Список словарей с данными об операциях.
                               Возвращает пустой список, если файл не найден,
                               пуст, содержит не список или поврежден.
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
