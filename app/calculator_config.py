"""
Configuration management for the calculator application.
Loads environment variables and provides default values.
"""

import os
from dotenv import load_dotenv


class CalculatorConfig:
    """Loads and validates configuration from environment variables."""

    def __init__(self):
        load_dotenv()

        # Directories
        self.log_dir = os.getenv("CALCULATOR_LOG_DIR", "logs")
        self.history_dir = os.getenv("CALCULATOR_HISTORY_DIR", "history")

        # History settings
        self.max_history_size = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 50))
        self.auto_save = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"

        # Calculation settings
        self.precision = int(os.getenv("CALCULATOR_PRECISION", 4))
        self.max_input_value = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1_000_000))
        self.default_encoding = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")

        # Files
        self.log_file = os.getenv("CALCULATOR_LOG_FILE", "calculator.log")
        self.history_file = os.getenv("CALCULATOR_HISTORY_FILE", "history.csv")

        self._create_directories()

    def _create_directories(self):
        """Ensure required directories exist."""
        os.makedirs(self.log_dir, exist_ok=True)
        os.makedirs(self.history_dir, exist_ok=True)

    @property
    def log_path(self):
        return os.path.join(self.log_dir, self.log_file)

    @property
    def history_path(self):
        return os.path.join(self.history_dir, self.history_file)
