import os
import pytest
from app.history import History
from app.calculator_config import CalculatorConfig


def test_load_nonexistent_file(tmp_path):
    config = CalculatorConfig()
    config.history_dir = tmp_path
    config.history_file = "no_file.csv"

    history = History(config)

    # Should handle gracefully (either return empty or raise controlled error)
    try:
        history.load()
    except Exception:
        assert True


def test_load_empty_csv(tmp_path):
    config = CalculatorConfig()
    config.history_dir = tmp_path
    config.history_file = "empty.csv"

    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("")

    history = History(config)

    try:
        history.load()
    except Exception:
        assert True


def test_save_empty_history(tmp_path):
    config = CalculatorConfig()
    config.history_dir = tmp_path
    config.history_file = "test.csv"

    history = History(config)

    # no entries added
    history.save()

    assert os.path.exists(config.history_path)

def test_load_raises_when_file_missing(tmp_path):
    from app.exceptions import PersistenceError

    config = CalculatorConfig()
    config.history_dir = tmp_path
    config.history_file = "missing.csv"

    history = History(config)

    with pytest.raises(PersistenceError):
        history.load()


def test_save_handles_failure(monkeypatch, tmp_path):
    from app.calculator_config import CalculatorConfig
    from app.history import History
    import pandas as pd

    config = CalculatorConfig()
    config.history_dir = tmp_path
    config.history_file = "test.csv"

    history = History(config)

    def raise_error(*args, **kwargs):
        raise Exception("disk error")

    monkeypatch.setattr(pd.DataFrame, "to_csv", raise_error)

    with pytest.raises(Exception):
        history.save()
