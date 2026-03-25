"""
Модуль для маскировки номеров карт и счетов.
"""

import logging
import os

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создаем папку logs, если её нет
os.makedirs("logs", exist_ok=True)

# Создаем file handler
file_handler = logging.FileHandler(
    "logs/masks.log", mode='w', encoding='utf-8'
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


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.

    Формат: XXXX XX** **** XXXX

    Args:
        card_number: Номер карты (16 цифр).

    Returns:
        Замаскированный номер карты.
    """
    logger.debug(
        f"Попытка маскировки номера карты: "
        f"{card_number[:4] if card_number else ''}..."
    )

    if not card_number or len(card_number) < 16:
        logger.error(f"Неверный формат номера карты: {card_number}")
        return "Неверный номер карты"

    # Убираем пробелы, если они есть
    cleaned = card_number.replace(" ", "")
    if len(cleaned) != 16 or not cleaned.isdigit():
        logger.error(f"Некорректные символы в номере карты: {card_number}")
        return "Неверный номер карты"

    # Маскируем: первые 6 цифр, потом 4 звездочки, потом последние 4 цифры
    masked = f"{cleaned[:4]} {cleaned[4:6]}** **** {cleaned[-4:]}"
    logger.info(f"Карта успешно замаскирована: {masked}")
    return masked


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета.

    Формат: **XXXX (показываются только последние 4 цифры)

    Args:
        account_number: Номер счета.

    Returns:
        Замаскированный номер счета.
    """
    logger.debug(f"Попытка маскировки номера счета: {account_number}")

    if not account_number or len(account_number) < 4:
        logger.error(f"Неверный формат номера счета: {account_number}")
        return "Неверный номер счета"

    # Убираем пробелы
    cleaned = account_number.replace(" ", "")
    if not cleaned.isdigit():
        logger.error(f"Некорректные символы в номере счета: {account_number}")
        return "Неверный номер счета"

    # Показываем только последние 4 цифры
    masked = f"**{cleaned[-4:]}"
    logger.info(f"Счет успешно замаскирован: {masked}")
    return masked
