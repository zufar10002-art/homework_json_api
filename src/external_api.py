import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = "http://api.apilayer.com/exchangerates_data/latest"


def convert_to_ruble(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли, если валюта USD или EUR.

    Args:
        transaction: Словарь с данными транзакции.
            Ожидается структура с ключом 'operationAmount',
            содержащим 'amount' и 'currency' с 'code'.

    Returns:
        float: Сумма в рублях. Для RUB возвращает исходную сумму.
               При ошибках или отсутствии API-ключа возвращает 0.0.
    """
    try:
        amount = float(transaction['operationAmount']['amount'])
        currency_code = transaction['operationAmount']['currency']['code']

        if currency_code == 'RUB':
            return amount
        elif currency_code in ('USD', 'EUR'):
            if not API_KEY:
                print("Ошибка: Не найден API ключ")
                return 0.0

            params = {
                'base': currency_code,
                'symbols': 'RUB'
            }
            headers = {
                'apikey': API_KEY
            }
            response = requests.get(BASE_URL, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                rate = data['rates']['RUB']
                return round(amount * rate, 2)
            else:
                print(f"Ошибка API: {response.status_code}")
                return 0.0
        else:
            return 0.0
    except (KeyError, ValueError, TypeError):
        return 0.0
