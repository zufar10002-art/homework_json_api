from unittest.mock import patch, Mock
from src.external_api import convert_to_ruble


def test_convert_rub():
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"code": "RUB"}
        }
    }
    assert convert_to_ruble(transaction) == 100.50


@patch('src.external_api.requests.get')
@patch('src.external_api.API_KEY', 'fake_key')
def test_convert_usd_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 75.5}}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "10.00",
            "currency": {"code": "USD"}
        }
    }
    result = convert_to_ruble(transaction)
    assert result == 755.00
    mock_get.assert_called_once()


@patch('src.external_api.requests.get')
@patch('src.external_api.API_KEY', 'fake_key')
def test_convert_usd_api_error(mock_get):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "10.00",
            "currency": {"code": "USD"}
        }
    }
    result = convert_to_ruble(transaction)
    assert result == 0.0


def test_convert_no_api_key():
    with patch('src.external_api.API_KEY', None):
        transaction = {
            "operationAmount": {
                "amount": "10.00",
                "currency": {"code": "USD"}
            }
        }
        result = convert_to_ruble(transaction)
        assert result == 0.0


def test_convert_invalid_transaction():
    transaction = {}
    result = convert_to_ruble(transaction)
    assert result == 0.0


def test_convert_unsupported_currency():
    transaction = {
        "operationAmount": {
            "amount": "10.00",
            "currency": {"code": "GBP"}
        }
    }
    result = convert_to_ruble(transaction)
    assert result == 0.0
