try:
    print(10/0)
except ZeroDivisionError as e:
    print("Whoops you tried to divide by zero.")
    print(str(e))
    #print(e.with_traceback())

#create your own nexceptions to handle unique situations.

class UsernameTooLongError(Exception):
    pass

try:
    username_desired = "MySpecialUsernameINeedToUse"
    if len(username_desired) > 10: #  use and, or to create a more complex code
        raise UsernameTooLongError("Your username is too long!")
    else:
        print("Username Created!")
except UsernameTooLongError as e:
    print(e)

finally:
    print("This will also print, whether the exception is thrown or not")

number = 10
my_dictionary = {
    "ten":number
}
try:
    print(my_dictionary["one"]/0)
except ZeroDivisionError as e:
    print(e)
except KeyError as e:
    print(e)
except Exception as e: # doing this is bad practice. put at end of exception change
    print(e)




