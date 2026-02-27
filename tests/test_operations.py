import pytest
from app.operations import OperationFactory
from app.exceptions import OperationError


@pytest.mark.parametrize("operation,a,b,expected", [
    ("add", 2, 3, 5),
    ("subtract", 5, 3, 2),
    ("multiply", 4, 3, 12),
    ("divide", 10, 2, 5),
    ("power", 2, 3, 8),
    ("root", 27, 3, 3),
    ("modulus", 10, 3, 1),
    ("int_divide", 10, 3, 3),
    ("percent", 20, 200, 10),
    ("abs_diff", 10, 3, 7),
])
def test_operations(operation, a, b, expected):
    op = OperationFactory.create(operation)
    result = op.execute(a, b)
    assert pytest.approx(result) == expected


def test_divide_by_zero():
    op = OperationFactory.create("divide")
    with pytest.raises(OperationError):
        op.execute(10, 0)


def test_invalid_operation():
    with pytest.raises(OperationError):
        OperationFactory.create("unknown")
