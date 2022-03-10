class Divider:
    def division(self, num):
        return num / 2

class Calculator:
    def __init__(self, divider_obj):
        self.divider_object: Divider = divider_obj

    def even_odd_check(self, num):
        if self.divider_object.division(num) % 2 == 0
            return "Even"
        else:
            return "Odd"

    divider = Divider()
    calculater = Calculater(divider)

    def test_get_even(self):
        result = calculater.even_odd_check(0)
            assert result == "Even"


    def test_get_odd(self):
        result = calculater.even_odd_check(11)
        assert result == "Odd"


def test_get_even_stubbing():
    calculater.divider_object. division = MagicMock(return value =2)
    result = calcultor.even_even_odd_check(11)
    assert result == "Even"

def test_get_odd_stubbing():
        calculator.divider_object.division = MagicMock(return_value=5)
        result = calculater.even_odd_check(423048)
        assert result == "Odd"



