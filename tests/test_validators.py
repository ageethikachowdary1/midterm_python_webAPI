import pytest
from app.input_validators import parse_two_numbers
from app.exceptions import ValidationError


def test_parse_two_numbers_ok():
    a, b = parse_two_numbers(["2", "3"], max_value=1000)
    assert a == 2.0
    assert b == 3.0


def test_parse_two_numbers_requires_two_args():
    with pytest.raises(ValidationError):
        parse_two_numbers(["1"], max_value=1000)


def test_parse_two_numbers_numeric_only():
    with pytest.raises(ValidationError):
        parse_two_numbers(["1", "abc"], max_value=1000)


def test_parse_two_numbers_max_value():
    with pytest.raises(ValidationError):
        parse_two_numbers(["9999", "1"], max_value=1000)
