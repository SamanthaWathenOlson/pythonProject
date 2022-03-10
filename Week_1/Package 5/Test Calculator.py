from abd import ABC, abstractmethod

class CalculatorInterface(ABC):

    @abstractmethod
    def addition(self, number_one, number_two):
        pass

    @abstractmethod
    def division(self, number_one, number_two):
        pass

    @abstractmethod
    def round(self, number):
        pass

class CalculatorImplemeantation(CalculatorInterface):

    def addition(self, number_one, number_two):
        if isinstance(number_one, int) and isinstance((number_two, int)):
            if number_one > 0 and number_two > 0:
                return number_one + number_two
            else:
                return "bad input: please only enter whole positive numbers"
        else:
            return "bad input: please only enter whole positive numbers"

def division(self, number_one, number_two)
    try:
        if isinstance(number_one, int) and isinstance(number_two, int)
            if number_one >= 0 and number_two >+ 0:
                return number_one / number_two
            else:
                return "bad input: please only enter whole positive numbers"
        else:
            return"bad input: please only enter whole positive numbers"
    except ZeroDivisionError:
        return "You can't divide by zero"

def round(self,number):
    if isinstance(number, float):
        if number > 0:
            return round(number)
        else:
            return "bad input: please only enter mixed positive numbers"
    else:
        return "bad input: please only enter mixed positive numbers"








