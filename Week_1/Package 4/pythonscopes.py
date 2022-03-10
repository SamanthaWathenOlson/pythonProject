import abc import ABC

name = "Samantha"  # global scope, anything without any tabbing, not enclose inside ()

# Name space - enclosed name space- code written inside a method or function
def showing_local_scope():
    y = 11  # this technically local scope, only within the scope of this function, y not define in global scope
    print("I just set y to 11")

# enclosed scope
def outer_function():
    y = 11
    #  inner and outer function have access to y variable
    def inner_function():   # technically enclosed scope - function defined inside another function
        return y
    return inner_function()

#Trick - global key word

global_variable = 5
def add_five():
    print(input + 5)

add_five(global_variable)

def add_five_global_keyword():
    global global_variable
    print(global_variable + 5)

add_five_global_keyword()

class MYAbstractExample(abc.ABC):
    pass






