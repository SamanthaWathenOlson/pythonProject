print("I want this to print 5 times")
# for statement and range method for basic loop to happen
# logical statement determines if the boolean is true or not.
# statement is incorrect then boolean is false
for loop in range(5):
    print("I want this to print 5 times")

""" for keyword is used whe you what Python to know tha you are going ot loook FOR a set interval
Loop this is a variable I declare that will reprstne what ever thing we are looking thoufhr.for
in this keyword lets pytho kno that our loop is being facilitated by whatever entity comes next
range() this methods  easy way to control how many times your code is going to loop> The most basic
 way of using it is to enter in a number that represents youw many times you want your code to loop
 
"""
for loop in range(5):
    print(loop)  # when we run this the numbers 0 - 4 will print

for loop in range(1, 5):  # here we start at the number 1 and loop up to the number 5, but don't include it
    print(loop)
"""Sometimes we don't want to look by iterations of one, sometime swe ned to go two or three interations at once, 
we can control this with the third input of range function
"""
for loop in range(0, 11, 2):
    print(loop)
"""We can count backwards"""

for loop in range(10, 4, -1):
    print(loop)

# range(range number, up to endpoint, increment endpoint):

for loop in range(10, -1, -1):
    print(loop)

# using While keyword, does not automatically assuem you arelooping through data
# ctrl +C - kill program

#while X <= 10: #infinite loop
#    print(x)

x = 5
while x <= 10:
    print(X)
    x += 1
    # x = x + 1

# if you need to loop through a set of data use for loops
# when you need to find and/or do something with data inside of a data collection.

# while loops are useful in just about any other situation not covered by the for loop
# they are useful when you need to loop your code arbitrarily number of times
