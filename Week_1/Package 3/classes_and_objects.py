from abc import ABC, abstractmethod

class_MyFirstClass:

#I want a string and variable added to it
# You can only have one defined at a time
def __init__(self, my_string_variable: str, my_integer_variable: int):
        #you don't have to name them the same, but it decreases confusion
        self.my_string_variable = my_string_variable
        self.my_integer_variable = my_integer_variable


my_first_object = MyFirstClass("My first object string:, 10)"
my_second_object = MyFirstClass("My second object string", 20)

print(my_first_object.my_string_variable)
print(my_second_object.my_string_variable)

class MyAbstractClass(ABC): #Need to create new classes that are able to inherit
    @abstractmethod
    def my_abstract_method(self):

class ClassOne(MyAbstractClass):
    def my_abstract_method(self, input_one, input_two):
            return input_one / input_two

class ClassTwo(MyAbstractClass):
    def my_abstract_method(self, input_one, input_two):
        return (str)input_one + (str)input_two


object_one = ClassOne()#
object_two = ClassTwo()

print(object_one.my_abstract_method(10,5))
print(object_two.my_abstract_method(10,5))

class ParentClass:
    def __init__(self, parent_variable):
        self.parent_variable = parent_variable
        print("")

class ChildClass(ParentClass:)

    def __init__(self, child_variable, parent_variable):
        super().__init__(parent_variable)
        self.child_variable + child_variable
        print("this method comes from parent class")
my_child_object =  ChildClass("Belongs to child" "Belongs to parent method")

my_child_object.parent_method()

class UsingClassFields:
    class_count = 0

    def __init__(self):
        UsingClassFields.class_count += 1
        print(f"The class count is not{UsingClassFields.class_count}")
    @classmethod
    def  get_class_count(cls): #self, cls are options for this bracket
        return cls.class_count
#interpreter understood, and completed the action
checking_class__variable_object_one = UsingClassFields()
checking_class__variable_object_two = UsingClassFields()

print (UsingClassFields.get_class_count())

#static method - attach functionallity to objecxts but you dont want it to interact with any properties of class and object

class UsingStaticMethod:
    def __init__(self, my_fields):
        self.my_field - my_field

    @staticmethod
    def this_is_my_static_method():
        print("this is my static method")

my_static_example = UsingStaticMethod("This is a string")

my_static_example.this_is_my_static_method()
#with class and with object
UsingStaticMethod.this_is_my_static_method()





