import os
import pytest
from app.calculator_config import CalculatorConfig
from app.history import History
from app.calculation import Calculation
from app.exceptions import PersistenceError


def test_history_add_and_clear(tmp_path):
    config = CalculatorConfig()
    config.history_dir = tmp_path
    config.history_file = "test.csv"

    history = History(config)

    calc = Calculation("add", 2, 3, 5)
    history.add(calc)

    assert len(history.get_all()) == 1

    history.clear()
    assert len(history.get_all()) == 0


def test_history_save_and_load(tmp_path):
    config = CalculatorConfig()
    config.history_dir = tmp_path
    config.history_file = "test.csv"

    history = History(config)

    calc = Calculation("add", 2, 3, 5)
    history.add(calc)

    history.save()

    new_history = History(config)
    new_history.load()

    assert len(new_history.get_all()) == 1


def test_history_load_missing_file(tmp_path):
    config = CalculatorConfig()
    config.history_dir = tmp_path
    config.history_file = "missing.csv"

    history = History(config)

    with pytest.raises(PersistenceError):
        history.load()

from app.calculator import Calculator
from app.history import History
from app.calculator_config import CalculatorConfig


def test_undo_and_redo(tmp_path):
    config = CalculatorConfig()
    config.history_dir = tmp_path
    config.history_file = "test.csv"

    history = History(config)
    calculator = Calculator(config, history)

    calculator.calculate("add", 2, 3)
    calculator.calculate("multiply", 2, 4)

    assert len(history.get_all()) == 2

    calculator.undo()
    assert len(history.get_all()) == 1

    calculator.redo()
    assert len(history.get_all()) == 2


def test_undo_when_empty(tmp_path):
    config = CalculatorConfig()
    history = History(config)
    calculator = Calculator(config, history)

    import pytest
    from app.exceptions import OperationError

    with pytest.raises(OperationError):
        calculator.undo()
