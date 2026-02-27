"""
Implements Memento Pattern for undo/redo functionality.
"""

import copy


class CalculatorMemento:
    """Stores a snapshot of calculator history state."""

    def __init__(self, history_state):
        self._state = copy.deepcopy(history_state)

    def get_state(self):
        return copy.deepcopy(self._state)
