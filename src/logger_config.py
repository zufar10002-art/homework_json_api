"""
Модуль для настройки логирования в проекте.
"""

import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(name: str, log_file: str,
                 level=logging.DEBUG) -> logging.Logger:
    """
    Настраивает и возвращает логгер для указанного модуля.

    Args:
        name: Имя логгера (обычно __name__).
        log_file: Имя файла для записи логов.
        level: Уровень логирования (по умолчанию DEBUG).

    Returns:
        Настроенный логгер.
    """
    # Создаем папку logs, если её нет
    os.makedirs("logs", exist_ok=True)

    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Удаляем старые обработчики, если есть
    if logger.handlers:
        logger.handlers.clear()

    # Создаем file handler
    file_path = os.path.join("logs", log_file)
    file_handler = RotatingFileHandler(
        file_path, mode='w', encoding='utf-8',
        maxBytes=5*1024*1024, backupCount=3
    )

    # Создаем formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Привязываем formatter к handler
    file_handler.setFormatter(formatter)

    # Добавляем handler к логгеру
    logger.addHandler(file_handler)

    return logger
