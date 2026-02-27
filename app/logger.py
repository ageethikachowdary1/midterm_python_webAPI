"""
Logger configuration for the calculator application.
"""

import logging
from app.calculator_config import CalculatorConfig


def setup_logger():
    """Set up and return a configured logger instance."""
    config = CalculatorConfig()

    logger = logging.getLogger("CalculatorLogger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(config.log_path, encoding=config.default_encoding)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
