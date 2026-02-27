import pytest
from app.calculator import Calculator
from app.history import History
from app.calculator_config import CalculatorConfig
from app.exceptions import OperationError


def test_redo_without_undo(tmp_path):
    config = CalculatorConfig()
    config.history_dir = tmp_path
    config.history_file = "h.csv"

    history = History(config)
    calc = Calculator(config, history)

    with pytest.raises(OperationError):
        calc.redo()
