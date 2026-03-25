"""
Модуль для работы с JSON-файлами.
"""

import json
import logging
import os
from typing import Any, Dict, List

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создаем папку logs, если её нет
os.makedirs("logs", exist_ok=True)

# Создаем file handler
file_handler = logging.FileHandler(
    "logs/utils.log", mode='w', encoding='utf-8'
)
file_handler.setLevel(logging.DEBUG)

# Создаем formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(formatter)

# Добавляем handler к логгеру
logger.addHandler(file_handler)


def load_operations(json_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные о финансовых операциях из JSON-файла.

    Args:
        json_path: Путь к JSON-файлу.

    Returns:
        Список словарей с данными об операциях.
        Возвращает пустой список, если файл не найден,
        пуст, содержит не список или поврежден.
    """
    logger.debug(f"Попытка открыть файл: {json_path}")

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            logger.debug(f"Файл успешно открыт и прочитан: {json_path}")

            if isinstance(data, list):
                logger.info(
                    f"Загружено {len(data)} операций из файла {json_path}"
                )
                return data
            else:
                logger.error(
                    f"Файл {json_path} содержит не список, а "
                    f"{type(data).__name__}"
                )
                return []

    except FileNotFoundError:
        logger.error(f"Файл не найден: {json_path}")
        return []
    except json.JSONDecodeError as e:
        logger.error(
            f"Ошибка декодирования JSON в файле {json_path}: {e}"
        )
        return []
