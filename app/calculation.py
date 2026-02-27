"""
Represents a single calculator operation result.
"""

from datetime import datetime


class Calculation:
    """Stores details of a single calculation."""

    def __init__(self, operation, operand1, operand2, result):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result
        self.timestamp = datetime.now()

    def to_dict(self):
        """Convert calculation to dictionary for CSV saving."""
        return {
            "operation": self.operation,
            "operand1": self.operand1,
            "operand2": self.operand2,
            "result": self.result,
            "timestamp": self.timestamp.isoformat()
        }

    @staticmethod
    def from_dict(data):
        """Recreate Calculation from dictionary (CSV load)."""
        calc = Calculation(
            data["operation"],
            float(data["operand1"]),
            float(data["operand2"]),
            float(data["result"])
        )
        calc.timestamp = datetime.fromisoformat(data["timestamp"])
        return calc
