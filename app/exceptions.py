"""
Custom exception classes for the calculator application.
"""


class CalculatorError(Exception):
    """Base class for calculator-related errors."""
    pass


class ValidationError(CalculatorError):
    """Raised when user input validation fails."""
    pass


class OperationError(CalculatorError):
    """Raised when an operation cannot be performed."""
    pass


class HistoryError(CalculatorError):
    """Raised when there is an issue with history operations."""
    pass


class PersistenceError(CalculatorError):
    """Raised when saving or loading history fails."""
    pass
