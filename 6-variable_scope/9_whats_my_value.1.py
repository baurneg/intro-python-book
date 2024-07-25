# What will the following code do and why? 
# Don't run it until you have tried to answer.

a = 7

def my_function(b):
    b += 10
    print(b)

my_function(a)
print(a)


# the output is 7
# when my_function(a) is called it takes the value of a as b for the function
# if print(my_function(a)) is called it would print None, however if print is included
# inside the function it would print 17
# print(a) remains at 7, it's immutable and does not change