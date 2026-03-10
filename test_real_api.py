from src.external_api import convert_to_ruble

# Тестовая транзакция в долларах
test_transaction = {
    "operationAmount": {
        "amount": "100.00",
        "currency": {"code": "USD"}
    }
}

result = convert_to_ruble(test_transaction)
print(f"100 USD = {result} RUB")
