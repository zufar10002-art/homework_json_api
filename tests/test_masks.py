from src.masks import mask_account_number, mask_card_number


def test_mask_card_number_valid():
    result = mask_card_number("1234567812345678")
    assert result == "1234 56** **** 5678"


def test_mask_card_number_with_spaces():
    result = mask_card_number("1234 5678 1234 5678")
    assert result == "1234 56** **** 5678"


def test_mask_card_number_too_short():
    result = mask_card_number("1234")
    assert result == "Неверный номер карты"


def test_mask_card_number_invalid_chars():
    result = mask_card_number("1234abcd12345678")
    assert result == "Неверный номер карты"


def test_mask_card_number_empty():
    result = mask_card_number("")
    assert result == "Неверный номер карты"


def test_mask_account_number_valid():
    result = mask_account_number("12345678")
    assert result == "**5678"


def test_mask_account_number_with_spaces():
    result = mask_account_number("1234 5678")
    assert result == "**5678"


def test_mask_account_number_too_short():
    result = mask_account_number("123")
    assert result == "Неверный номер счета"


def test_mask_account_number_invalid_chars():
    result = mask_account_number("1234abcd")
    assert result == "Неверный номер счета"


def test_mask_account_number_empty():
    result = mask_account_number("")
    assert result == "Неверный номер счета"
