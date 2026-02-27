"""
Manages calculator history and CSV persistence.
"""

import pandas as pd
from app.calculation import Calculation
from app.exceptions import PersistenceError


class History:
    """Stores and manages calculation history."""

    def __init__(self, config):
        self._history = []
        self.config = config

    def add(self, calculation):
        """Add a calculation to history with max size enforcement."""
        self._history.append(calculation)

        if len(self._history) > self.config.max_history_size:
            self._history.pop(0)

    def clear(self):
        """Clear history."""
        self._history.clear()

    def get_all(self):
        """Return all history items."""
        return list(self._history)

    def save(self):
        """Save history to CSV using pandas."""
        try:
            data = [calc.to_dict() for calc in self._history]
            df = pd.DataFrame(data)
            df.to_csv(self.config.history_path, index=False)
        except Exception as e:
            raise PersistenceError(f"Failed to save history: {e}")

    def load(self):
        """Load history from CSV using pandas."""
        try:
            df = pd.read_csv(self.config.history_path)
            self._history = [
                Calculation.from_dict(row)
                for _, row in df.iterrows()
            ]
        except FileNotFoundError:
            raise PersistenceError("History file not found.")
        except Exception as e:
            raise PersistenceError(f"Failed to load history: {e}")
