""" Three different ways in creating a string."""

string_one = "This a string"
string_two = 'This is a string'
string_three = """This is string""" #comments in code

# if you need quotations for sentence use single quotes to close code.

trying_to_quote_someone = 'And he said, "Wait that is my burger!"'

"""manipulation of strings: string concatonation  taking multiple strings and combining them together"""

name = "Samantha"

greeting = "Hello "

print(greeting + name)
# string in python are immutable

""" String formation concatination by using f string, add an f to the start of it and you add curly braces
as the value inside the string"""

greeting_as_f_string =f"Hello {name}" #lets the interpreter  know it is working with a formatted string
print(greeting_as_f_string)


"""Format Method (dynamically set strings) Add it onto the end of the string declaration and it lets you add in unique
 values that do not need to be hard-coded in"""

another_name = "Sam"

greeting_using_format_method = "Hello {} and {}".format { another_name, name}

print(greeting_using_format_method)

"""String splicing :subsets of strings. Reasons : checking usernames, no symbols used. We can check substrings by
 using string splicing"""

string_to_slice = "Hello Samantha"
print(string_to_slice [0:5]) # Here we want to get just the substring "Hello"

"""
0 = H
1 = e
2 = l
3 = l
4 = o
etc
"""

for letter in string_to_slice:
    print(letter)

for letter in string_to_slice[::-1]: # reverse a string in this fashion, add an extra colon for starting and up to
    print(letter)

"""useful methods to be aware of: strip and split. Strip removes access. split has you break it down into parts
Strip allows us to strip away and characters and whites space from a string"""

print(string_to_slice)
print(string_to_slice.strip()) # remove any opening and trialing whitespace
print(string_to_slice.strip (cH ))

very_long_string = "This is my very long string. I have losts of words in here:" \
print(very_long_string)
print(very_long_string.split) # by default this separates all substrings by whitespace
print(very_long_string.split("i"))
print(very_long_string.split("iI"))

my_python_variable = "This_is_my_variable"
for word in my_python_variable.split("_"):
    for character in word:
        if character is "a":
            print("this is a bad name for a python variable!")

