"""
Defines calculator operations and OperationFactory (Factory Pattern).
"""

from abc import ABC, abstractmethod
from app.exceptions import OperationError


class Operation(ABC):
    """Abstract base class for all operations."""

    @abstractmethod
    def execute(self, a, b):
        pass


# Basic Operations

class Add(Operation):
    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    def execute(self, a, b):
        return a * b


class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Division by zero is not allowed.")
        return a / b


# Mandatory Midterm Operations

class Power(Operation):
    def execute(self, a, b):
        return a ** b


class Root(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Root degree cannot be zero.")
        return a ** (1 / b)


class Modulus(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Modulus by zero is not allowed.")
        return a % b


class IntegerDivide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Integer division by zero is not allowed.")
        return a // b


class Percent(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Percentage calculation with zero denominator is not allowed.")
        return (a / b) * 100


class AbsoluteDifference(Operation):
    def execute(self, a, b):
        return abs(a - b)


# Factory Pattern

class OperationFactory:
    """Creates operation instances based on command name."""

    _operations = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
        "power": Power,
        "root": Root,
        "modulus": Modulus,
        "int_divide": IntegerDivide,
        "percent": Percent,
        "abs_diff": AbsoluteDifference,
    }

    @classmethod
    def create(cls, operation_name):
        operation_class = cls._operations.get(operation_name.lower())
        if not operation_class:
            raise OperationError(f"Invalid operation: {operation_name}")
        return operation_class()
