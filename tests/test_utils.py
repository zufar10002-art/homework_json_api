import json
from unittest.mock import mock_open, patch

from src.utils import load_operations


def test_load_operations_success():
    mock_data = [{"id": 1}, {"id": 2}]
    mock_file = mock_open(read_data=json.dumps(mock_data))

    with patch("builtins.open", mock_file):
        result = load_operations("any_path.json")

    assert result == mock_data


def test_load_operations_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_operations("non_existent.json")

    assert result == []


def test_load_operations_invalid_json():
    mock_file = mock_open(read_data="not json")

    with patch("builtins.open", mock_file):
        result = load_operations("any_path.json")

    assert result == []


def test_load_operations_not_a_list():
    mock_data = {"key": "value"}
    mock_file = mock_open(read_data=json.dumps(mock_data))

    with patch("builtins.open", mock_file):
        result = load_operations("any_path.json")

    assert result == []
