"""
Core calculator class:
- Uses Factory Pattern to create operations
- Stores history
- Supports undo/redo using Memento Pattern
- Notifies observers using Observer Pattern
"""

from app.operations import OperationFactory
from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento
from app.exceptions import OperationError


class Calculator:
    def __init__(self, config, history):
        self.config = config
        self.history = history

        self._undo_stack = []
        self._redo_stack = []
        self._observers = []

    # ---------- Observer Pattern ----------
    def add_observer(self, observer):
        self._observers.append(observer)

    def _notify_observers(self, calculation):
        for obs in self._observers:
            obs.update(calculation, self.history)

    # ---------- Memento Pattern ----------
    def _save_state(self):
        self._undo_stack.append(CalculatorMemento(self.history.get_all()))
        self._redo_stack.clear()

    def undo(self):
        if not self._undo_stack:
            raise OperationError("Nothing to undo.")
        self._redo_stack.append(CalculatorMemento(self.history.get_all()))
        prev_state = self._undo_stack.pop().get_state()
        self.history._history = prev_state  # internal restore

    def redo(self):
        if not self._redo_stack:
            raise OperationError("Nothing to redo.")
        self._undo_stack.append(CalculatorMemento(self.history.get_all()))
        next_state = self._redo_stack.pop().get_state()
        self.history._history = next_state  # internal restore

    # ---------- Calculation ----------
    def calculate(self, operation_name, a, b):
        self._save_state()

        op = OperationFactory.create(operation_name)
        result = op.execute(a, b)

        if isinstance(result, float):
            result = round(result, self.config.precision)

        calc = Calculation(operation_name, a, b, result)
        self.history.add(calc)

        self._notify_observers(calc)
        return result
