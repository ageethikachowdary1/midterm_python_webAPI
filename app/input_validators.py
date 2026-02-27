"""
Input validation helpers.
"""

from app.exceptions import ValidationError


def parse_two_numbers(args, max_value):
    if len(args) != 2:
        raise ValidationError("Please provide exactly two numbers.")

    try:
        a = float(args[0])
        b = float(args[1])
    except ValueError as e:
        raise ValidationError("Inputs must be numeric.") from e

    if abs(a) > max_value or abs(b) > max_value:
        raise ValidationError(f"Input values must be within +/- {max_value}")

    return a, b
