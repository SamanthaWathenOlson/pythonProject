"""functions and Methods"""
"""functions and methods  are a reusable piece of code"""

print("I can do this without having to create and object") #This is a FUNCTION

my_string_object = "     This string has many attached methods"

print(my_string_object.strip()) # This down here is a METHOD

""" Creating a custom function
def function: def function_name(parameters):"""

def my_custom_function(number_one, number_two, number_three):
    #to make my function work, you need to assing the value of this addition to a new variable
    sum = number_one + number_two + number_three
    # now to get this value back, need to use return keyour to get it out of my function
    return sum
# by itself it does not do anything for my code need to do something with it
my_custom_function(1,2,3)

#I can assign it to a variable
result = my_custom_function(1,2,3)
print(result)

"""functions all have a return value even if unassigned"""

def my_no_return_value():
    print("I don't have a return value, or do it?")

my_not_return_value_function()
print(my_no_return_value_function())

def fuction_that_controls_code_flow(argument):
    if arguement == "this is a string":
        return "I was given a string!"
    elif argument == 10:
        return "I was given a number!"
    else:
        print("i was not given the string or the number 10")

def my_program_in_action(argument, my_function):
    result = my_function(argument)
    if result is None:
        print("This will only will print if the result returned by the mu_function is None")
    else:
        print(result)

my_program_in_action("This is a string", function_that_controls_code_flow)

def is_this_math_or_concatination(input_one, input_two):
    return input_one + input_two

print(is_this_math_or_concatination(5,5))
print(is_this_math_or_concatination("Hello", " world"))

"""get around ambiguity f your meaning when it comes to creating your function. it allows type annotation. 
Type annotation are great for reminding the dev what data types they are expecting to work with, but it actually has no
 effect upon your code at runtime."""

def this_fuction_is_meant_for_math(input_one: int, input_two: int) -> int:
    return input_one + input_two

print(this_fuction_is_meant_for_math("Hello" , "World"))

print(this_fuction_is_meant_for_math(10.1, 11.2))

""" Don't know how much data use the variable argument parameter to handle this arbitrary amount of input"""

def this_function_has_a_var_arg_parameters(*args):
    for element in args:
        print(element)

this_function_has_a_var_arg_parameters(1, 2, 3, 4, 5)
this_function_has_a_var_arg_parameters("Hello", " " "world:, "!")
this_function_has_a_var_arg_parameters((1, "Hello", 2, "world")

# Does not matter what type of how many objects you place inside your variable argument there are all accessible.
#funtions in python can also have what is called kwargs, or key word arguments. These are accessed via their keywords.

def show_username_sand_password(**kwargs):
    print(kwargs["username"])
    print(kwargs["passwords"])

show_username_and_password(password="Silly", username"pickle")

# you can mix and match different ways of creating your functions

def over_the_top_function_using_all_input_options(my_number: int, my_string: str, *everything_else, **,ykwargs):
    print(my_number)
    print(my_strings)
    for element in everything_else:
        print(element)
    print(kwargs["my_key"])

over_the_top_fuction_using_all_input_options(1, My String:, 1, 2, 3, 4, 5, 6, "A string", 7, 8, my_key=True)
