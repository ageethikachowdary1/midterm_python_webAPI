import pytest
from app import App


def test_repl_basic_flow(monkeypatch, capsys, tmp_path):
    # Feed a full REPL session
    inputs = iter([
        "help",
        "add 2 3",
        "history",
        "undo",
        "redo",
        "save",
        "clear",
        "history",
        "exit"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app = App()

    # make history file go into a safe temp directory
    app.config.history_dir = tmp_path
    app.config.history_file = "history.csv"

    app.run()

    out = capsys.readouterr().out
    assert "Available commands" in out
    assert "Result: 5.0" in out
    assert "Undo successful" in out
    assert "Redo successful" in out
    assert "History cleared" in out


def test_repl_invalid_command(monkeypatch, capsys):
    inputs = iter(["unknown_cmd 1 2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app = App()
    app.run()

    out = capsys.readouterr().out
    assert "Error:" in out

def test_help_prints_commands(capsys):
    import app
    application = app.App()
    application.print_help()
    output = capsys.readouterr().out
    assert "add <num1> <num2>" in output
