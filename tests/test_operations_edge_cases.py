import pytest
from app.operations import OperationFactory
from app.exceptions import OperationError


def test_divide_by_zero():
    op = OperationFactory.create("divide")
    with pytest.raises(Exception):
        op.execute(10, 0)


def test_modulus_by_zero():
    op = OperationFactory.create("modulus")
    with pytest.raises(Exception):
        op.execute(10, 0)


def test_percent_by_zero():
    op = OperationFactory.create("percent")
    with pytest.raises(Exception):
        op.execute(10, 0)

def test_unknown_operation():
    with pytest.raises(Exception):
        OperationFactory.create("unknown_op")

def test_int_divide_by_zero():
    from app.operations import OperationFactory
    op = OperationFactory.create("int_divide")
    import pytest
    with pytest.raises(Exception):
        op.execute(10, 0)


def test_abs_diff_executes():
    from app.operations import OperationFactory
    op = OperationFactory.create("abs_diff")
    result = op.execute(10, 4)
    assert result == 6


def test_power_executes():
    from app.operations import OperationFactory
    op = OperationFactory.create("power")
    result = op.execute(2, 3)
    assert result == 8

def test_factory_invalid_raises_operation_error():
    from app.operations import OperationFactory
    from app.exceptions import OperationError
    import pytest

    with pytest.raises(OperationError):
        OperationFactory.create("invalid_command_name")


def test_root_zero_degree():
    from app.operations import OperationFactory
    import pytest

    op = OperationFactory.create("root")
    with pytest.raises(Exception):
        op.execute(4, 0)
