import os
from app.calculator import Calculator, AutoSaveObserver
from app.history import History
from app.calculator_config import CalculatorConfig
from app.calculation import Calculation


def test_history_max_size_trim(tmp_path):
    config = CalculatorConfig()
    config.history_dir = tmp_path
    config.history_file = "h.csv"
    config.max_history_size = 2

    history = History(config)

    history.add(Calculation("add", 1, 1, 2))
    history.add(Calculation("add", 2, 2, 4))
    history.add(Calculation("add", 3, 3, 6))

    items = history.get_all()

    assert len(items) == 2
    assert items[0].operand1 == 2  # first one should be trimmed


def test_autosave_observer_creates_file(tmp_path):
    config = CalculatorConfig()
    config.history_dir = tmp_path
    config.history_file = "autosave.csv"
    config.auto_save = True

    history = History(config)
    calculator = Calculator(config, history)

    calculator.add_observer(AutoSaveObserver(config))

    calculator.calculate("add", 2, 3)

    assert os.path.exists(config.history_path)
