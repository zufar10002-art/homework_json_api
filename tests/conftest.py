import logging
from unittest.mock import MagicMock

import pytest


@pytest.fixture(autouse=True)
def mock_loggers(monkeypatch):
    """Автоматически мокает все логгеры в тестах"""
    mock_logger = MagicMock()

    # Создаем функцию, которая возвращает один и тот же мок
    def mock_get_logger(name=None):
        return mock_logger

    monkeypatch.setattr(logging, "getLogger", mock_get_logger)
    return mock_logger
