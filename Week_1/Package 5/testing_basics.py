calculator = CalculatorImpleamentation()

def test_addition_success():
    result - calculator.addition(5,5)
result
    asser result ==10
raised

#more tests go here....

def test_division_success():
    result = Calculator.divisions(10,5)
    assert result == 

def test_division_catch_float_first_input(calculator=None):
    result = calculator.division(10.5,5)
    assert result == "Bad input: please only enter whole positive numbers"

def test_division_catch_float_second_input():
    result = calculator.division(10,5.5)
    assert result == "Bad input: please only enter whole positive numbers"

def test_division_divide_by_zero():
    result = calculator.division(10,0)
    assert result =="You can't divide by zero"

def test_division_catch_non_positive_first_input():
    result = calculator.division(-10,5)
    assert result ==" bad input please only enter whole positive numbers"

def test_division_catch_non_positive_second_input():
    result = calculator.division(10,-5)
    assert result =="bad input please only enter whole positive numbers"

def test_division_catch_non_positive_all_input():
    result = calculator.division()
    assert result =="something"

def test_round_success():
    result = calculator.round(1.)
    assert result ==1

def test_round_catch_negative_input():
    result = calculator.round(-1,1)
    assert result =="bad input:please only enter mixed positive numbers"

def test_round_catch_non_non_numeric_input():
    result = calculator.round("5.5")
    assert result =="bad input:please only enter mixed positive numbers"







