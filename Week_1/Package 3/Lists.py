my_ordered_list = [1, 3, 5, 4, 6, 7, 8, 9, 10]
print(my_ordered_list)
my_ordered_list.sort()
print(my_ordered_list)

my_ordered_list = ["banana", "carrot", "apple"]
my_ordered_list.sort()
print(my_ordered_list)

my_ordered_list = [[1, "c"], [3, "a"], [2, "b"]]


def my_key(element):
    return element[0]


my_ordered_list.sort(key=my_key)

print(my_ordered_list)


def my_string_key(element):
    return element[1]


my_ordered_list.sort(key=my_string_key)
#Unique ids - mystring_key(element)
#       return element[specific id]
print(my_ordered_list)
# same types of data for comparisons
# look into the method to find the answer

#Reverse a list

my_ordered_list.sort(reverse=True)
print(my_ordered_list)

#copy method
