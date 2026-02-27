from app.calculation import Calculation


def test_calculation_to_dict_and_from_dict():
    calc = Calculation("add", 2, 3, 5)
    data = calc.to_dict()

    new_calc = Calculation.from_dict(data)

    assert new_calc.operation == "add"
    assert new_calc.operand1 == 2
    assert new_calc.operand2 == 3
    assert new_calc.result == 5
