#Sets, Tuples, Dictionaries
"""providing a restriction on your code, do not allow duplicotes to be stored inside of them, unique feature is that
they are not indexible, have to call them"""

my_set = {1} # place a value inside of it, python would thibnk it is a dictionary
two = "2"
three = 3
four = "four"
i ="i"
declare = "declare"
a = "a"
thumb = "thumb"
war = "war"

my_set.add(two)
my_set.add(three)
my_set.add(four)
my_set.add(i)
my_set.add(declare)
my_set.add(a)
my_set.add(thumb)
my_set.add(war)

print(my_set)

my_ordered_set = {1}
my_ordered_set.add(2)
my_ordered_set.add(3)
my_ordered_set.add(4)
my_ordered_set.add(5)
my_ordered_set.add(6)

print(my_ordered_set)

# no access to index positions, one way is to use the pop method
#print(my_set[0])

# Randomizing using pop_method
#print(my_set.pop())
#print(my_set)

for element in my_set:
    if element == "four":
       print("I found what I wanted to get specifically")


#Discard removes a set



my_set.remove(four)
my_set.discard(four)

"""  Adding information - use Update method to transfer daa from one iterable collectionto your set."""

rest_of_phrase = [5, 6, 7, 8, "try to keep your thumb straight"]

my_set.update(rest_of_phrase)
print(my_set)

# Tuples can not be changed once set. You can access their positions and duplicates

my_tuple = ("this", "is", "it")

print(my_tuple.count("is"))
print(my_tuple.index("this"))
print(my_tuple[2])

#my_list = [2, 5, 7, 3, 1, 3, 6, 8, 9, 9, ]
#ennumerated_list = enummerate(my_list)
#print(ennumerated_list)
#print(list(ennumerated_list))

#adjusted_ennumerated_list = enummerate(my_list, 10)
#print(list(adjusted_ennumerated_list))

#dictionaries- collection of key value pairs to amke it easy to access

my_dictionary = {
    "key":"value",
    1:"this value is associated with key 1",
    key_function(): "this value is associated with my key_function()",
    True:key_function()
}

print(my_dictionary["key"])

print(my_dictionary[1])
print(my_dictionary[key_function()])
print(my_dictionary["This function is going to act as my key"])
print(my_dictionary[True])

number_dictionary = {
    "one":1,
    "two":2,
    "three":3
}

duplicate_key = {
    "one" : 1,
    "one" : 2,
}

print(duplicate_key["one"])

#make or reassigne anew key pair and place the key inside of square brackets and then use the assignment operator

duplicate_key["two"] = 2

duplicate_key["two"]= "2"

print(duplicate_key.items())  # returns the value pairs inside tuples
print(duplicate_key.keys())  # this returns the keys inside a list
print(duplicate_key.values())  # this returns the values inside a list

for key in duplicate_key.keys():
    print(key)

for key, value in duplicate_key.items():
    print(key, value)

    #delete a key

    del duplicate_key["two"]
    print(duplicate_key.items())

    #set default method

    print duplicate_key.items()
    print(duplicate_key.setdefault(("two, "i want this to be the value"")))
    print(duplicate_key["one"]) #I will get a key error with this
    print duplicate_key.setdefault("one", "This did not exist before")
    print(duplicate_key.items())


